import { existsSync, readFileSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
const CONFIG_PATH = join(homedir(), ".wocode", "web-search.json");
let cachedConfig = null;
export function normalizeChromeProfile(value) {
    if (typeof value !== "string")
        return undefined;
    const normalized = value.trim();
    return normalized.length > 0 ? normalized : undefined;
}
function loadConfig() {
    if (cachedConfig)
        return cachedConfig;
    if (!existsSync(CONFIG_PATH)) {
        cachedConfig = {};
        return cachedConfig;
    }
    const rawText = readFileSync(CONFIG_PATH, "utf-8");
    let raw;
    try {
        raw = JSON.parse(rawText);
    }
    catch (err) {
        const message = err instanceof Error ? err.message : String(err);
        throw new Error(`Failed to parse ${CONFIG_PATH}: ${message}`);
    }
    cachedConfig = {
        chromeProfile: normalizeChromeProfile(raw.chromeProfile),
        allowBrowserCookies: raw.allowBrowserCookies === true,
    };
    return cachedConfig;
}
export function getChromeProfileFromConfig() {
    return loadConfig().chromeProfile;
}
export function isBrowserCookieAccessAllowed() {
    if (process.env.PI_ALLOW_BROWSER_COOKIES === "1" || process.env.FEYNMAN_ALLOW_BROWSER_COOKIES === "1") {
        return true;
    }
    return loadConfig().allowBrowserCookies === true;
}
//# sourceMappingURL=gemini-web-config.js.map