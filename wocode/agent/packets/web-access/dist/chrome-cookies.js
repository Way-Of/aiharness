import { execFile } from "node:child_process";
import { pbkdf2Sync, createDecipheriv } from "node:crypto";
import { copyFileSync, existsSync, mkdtempSync, rmSync } from "node:fs";
import { tmpdir, homedir, platform } from "node:os";
import { join } from "node:path";
const GOOGLE_ORIGINS = [
    "https://gemini.google.com",
    "https://accounts.google.com",
    "https://www.google.com",
];
const ALL_COOKIE_NAMES = new Set([
    "__Secure-1PSID",
    "__Secure-1PSIDTS",
    "__Secure-1PSIDCC",
    "__Secure-1PAPISID",
    "NID",
    "AEC",
    "SOCS",
    "__Secure-BUCKET",
    "__Secure-ENID",
    "SID",
    "HSID",
    "SSID",
    "APISID",
    "SAPISID",
    "__Secure-3PSID",
    "__Secure-3PSIDTS",
    "__Secure-3PAPISID",
    "SIDCC",
]);
const MACOS_BROWSER_CONFIGS = [
    {
        name: "Helium",
        baseDir: "Library/Application Support/net.imput.helium",
        keychainService: "Helium Storage Key",
        keychainAccount: "Helium",
    },
    {
        name: "Chrome",
        baseDir: "Library/Application Support/Google/Chrome",
        keychainService: "Chrome Safe Storage",
        keychainAccount: "Chrome",
    },
    {
        name: "Arc",
        baseDir: "Library/Application Support/Arc/User Data",
        keychainService: "Arc Safe Storage",
        keychainAccount: "Arc",
    },
];
const LINUX_BROWSER_CONFIGS = [
    { name: "Chromium", baseDir: ".config/chromium", secretToolApp: "chromium" },
    { name: "Chrome", baseDir: ".config/google-chrome", secretToolApp: "chrome" },
];
export async function getGoogleCookies(options) {
    const currentPlatform = platform();
    const configs = currentPlatform === "darwin"
        ? MACOS_BROWSER_CONFIGS
        : currentPlatform === "linux"
            ? LINUX_BROWSER_CONFIGS
            : [];
    if (configs.length === 0)
        return null;
    const warnings = [];
    const profile = options?.profile ?? "Default";
    const hosts = GOOGLE_ORIGINS.map((origin) => new URL(origin).hostname);
    for (const config of configs) {
        const cookiesPath = join(homedir(), config.baseDir, profile, "Cookies");
        if (!existsSync(cookiesPath))
            continue;
        const password = await readBrowserPassword(config, currentPlatform);
        if (!password) {
            warnings.push(`Could not read ${config.name} cookie encryption password`);
            continue;
        }
        const key = pbkdf2Sync(password, "saltysalt", currentPlatform === "darwin" ? 1003 : 1, 16, "sha1");
        const tempDir = mkdtempSync(join(tmpdir(), "pi-chrome-cookies-"));
        try {
            const tempDb = join(tempDir, "Cookies");
            copyFileSync(cookiesPath, tempDb);
            copySidecar(cookiesPath, tempDb, "-wal");
            copySidecar(cookiesPath, tempDb, "-shm");
            const metaVersion = await readMetaVersion(tempDb);
            const stripHash = metaVersion >= 24;
            const rows = await queryCookieRows(tempDb, hosts);
            if (!rows) {
                warnings.push(`Failed to query ${config.name} cookie database`);
                continue;
            }
            const cookies = {};
            for (const row of rows) {
                const name = row.name;
                if (!ALL_COOKIE_NAMES.has(name))
                    continue;
                if (cookies[name])
                    continue;
                let value = typeof row.value === "string" && row.value.length > 0 ? row.value : null;
                if (!value) {
                    const encrypted = row.encrypted_value;
                    if (encrypted instanceof Uint8Array) {
                        value = decryptCookieValue(encrypted, key, stripHash);
                    }
                }
                if (value)
                    cookies[name] = value;
            }
            if (options?.requiredCookies?.length && !options.requiredCookies.every((name) => Boolean(cookies[name]))) {
                continue;
            }
            return { cookies, warnings };
        }
        finally {
            rmSync(tempDir, { recursive: true, force: true });
        }
    }
    return null;
}
function decryptCookieValue(encrypted, key, stripHash) {
    const buf = Buffer.from(encrypted);
    if (buf.length < 3)
        return null;
    const prefix = buf.subarray(0, 3).toString("utf8");
    if (!/^v\d\d$/.test(prefix))
        return null;
    const ciphertext = buf.subarray(3);
    if (!ciphertext.length)
        return "";
    try {
        const iv = Buffer.alloc(16, 0x20);
        const decipher = createDecipheriv("aes-128-cbc", key, iv);
        decipher.setAutoPadding(false);
        const plaintext = Buffer.concat([decipher.update(ciphertext), decipher.final()]);
        const unpadded = removePkcs7Padding(plaintext);
        const bytes = stripHash && unpadded.length >= 32 ? unpadded.subarray(32) : unpadded;
        const decoded = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
        let i = 0;
        while (i < decoded.length && decoded.charCodeAt(i) < 0x20)
            i++;
        return decoded.slice(i);
    }
    catch {
        return null;
    }
}
function removePkcs7Padding(buf) {
    if (!buf.length)
        return buf;
    const padding = buf[buf.length - 1];
    if (!padding || padding > 16)
        return buf;
    return buf.subarray(0, buf.length - padding);
}
function readBrowserPassword(config, currentPlatform) {
    if (currentPlatform === "darwin") {
        if (!config.keychainAccount || !config.keychainService)
            return Promise.resolve(null);
        return readKeychainPassword(config.keychainAccount, config.keychainService);
    }
    if (currentPlatform === "linux") {
        return readLinuxPassword(config.secretToolApp);
    }
    return Promise.resolve(null);
}
function readKeychainPassword(account, service) {
    return new Promise((resolve) => {
        execFile("security", ["find-generic-password", "-w", "-a", account, "-s", service], { timeout: 5000 }, (err, stdout) => {
            if (err) {
                resolve(null);
                return;
            }
            resolve(stdout.trim() || null);
        });
    });
}
function readLinuxPassword(secretToolApp) {
    if (!secretToolApp)
        return Promise.resolve("peanuts");
    return new Promise((resolve) => {
        execFile("secret-tool", ["lookup", "application", secretToolApp], { timeout: 5000 }, (err, stdout) => {
            if (err) {
                // KDE Wallet users fall through to peanuts intentionally.
                resolve("peanuts");
                return;
            }
            resolve(stdout.trim() || "peanuts");
        });
    });
}
let sqliteModule = null;
async function importSqlite() {
    if (sqliteModule)
        return sqliteModule;
    const orig = process.emitWarning.bind(process);
    process.emitWarning = ((warning, ...args) => {
        const msg = typeof warning === "string" ? warning : warning?.message ?? "";
        if (msg.includes("SQLite is an experimental feature"))
            return;
        return orig(warning, ...args);
    });
    try {
        sqliteModule = await import("node:sqlite");
        return sqliteModule;
    }
    catch {
        return null;
    }
    finally {
        process.emitWarning = orig;
    }
}
function supportsReadBigInts() {
    const [major, minor] = process.versions.node.split(".").map(Number);
    if (major > 24)
        return true;
    if (major < 24)
        return false;
    return minor >= 4;
}
async function readMetaVersion(dbPath) {
    const sqlite = await importSqlite();
    if (!sqlite)
        return 0;
    const opts = { readOnly: true };
    if (supportsReadBigInts())
        opts.readBigInts = true;
    const db = new sqlite.DatabaseSync(dbPath, opts);
    try {
        const rows = db.prepare("SELECT value FROM meta WHERE key = 'version'").all();
        const val = rows[0]?.value;
        if (typeof val === "number")
            return Math.floor(val);
        if (typeof val === "bigint")
            return Number(val);
        if (typeof val === "string")
            return parseInt(val, 10) || 0;
        return 0;
    }
    catch {
        return 0;
    }
    finally {
        db.close();
    }
}
async function queryCookieRows(dbPath, hosts) {
    const sqlite = await importSqlite();
    if (!sqlite)
        return null;
    const clauses = [];
    for (const host of hosts) {
        for (const candidate of expandHosts(host)) {
            const esc = candidate.replaceAll("'", "''");
            clauses.push(`host_key = '${esc}'`);
            clauses.push(`host_key = '.${esc}'`);
            clauses.push(`host_key LIKE '%.${esc}'`);
        }
    }
    const where = clauses.join(" OR ");
    const opts = { readOnly: true };
    if (supportsReadBigInts())
        opts.readBigInts = true;
    const db = new sqlite.DatabaseSync(dbPath, opts);
    try {
        return db
            .prepare(`SELECT name, value, host_key, encrypted_value FROM cookies WHERE (${where}) ORDER BY expires_utc DESC`)
            .all();
    }
    catch {
        return null;
    }
    finally {
        db.close();
    }
}
function expandHosts(host) {
    const parts = host.split(".").filter(Boolean);
    if (parts.length <= 1)
        return [host];
    const candidates = new Set();
    candidates.add(host);
    for (let i = 1; i <= parts.length - 2; i++) {
        const c = parts.slice(i).join(".");
        if (c)
            candidates.add(c);
    }
    return Array.from(candidates);
}
function copySidecar(srcDb, targetDb, suffix) {
    const sidecar = `${srcDb}${suffix}`;
    if (!existsSync(sidecar))
        return;
    try {
        copyFileSync(sidecar, `${targetDb}${suffix}`);
    }
    catch {
    }
}
//# sourceMappingURL=chrome-cookies.js.map