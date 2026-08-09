export function formatSeconds(s) {
    const h = Math.floor(s / 3600);
    const m = Math.floor((s % 3600) / 60);
    const sec = s % 60;
    if (h > 0)
        return `${h}:${String(m).padStart(2, "0")}:${String(sec).padStart(2, "0")}`;
    return `${m}:${String(sec).padStart(2, "0")}`;
}
export function readExecError(err) {
    if (!err || typeof err !== "object") {
        return { stderr: "", message: String(err) };
    }
    const code = err.code;
    const message = err.message ?? "";
    const stderrRaw = err.stderr;
    const stderr = Buffer.isBuffer(stderrRaw)
        ? stderrRaw.toString("utf-8")
        : typeof stderrRaw === "string"
            ? stderrRaw
            : "";
    return { code, stderr, message };
}
export function isTimeoutError(err) {
    if (!err || typeof err !== "object")
        return false;
    if (err.killed)
        return true;
    const name = err.name;
    const code = err.code;
    const message = err.message ?? "";
    return name === "AbortError" || code === "ETIMEDOUT" || message.toLowerCase().includes("timed out");
}
export function trimErrorText(text) {
    return text.replace(/\s+/g, " ").trim().slice(0, 200);
}
export function mapFfmpegError(err) {
    const { code, stderr, message } = readExecError(err);
    if (code === "ENOENT")
        return "ffmpeg is not installed. Install with: brew install ffmpeg";
    if (isTimeoutError(err))
        return "ffmpeg timed out extracting frame";
    if (stderr.includes("403"))
        return "Stream URL returned 403 — may have expired, try again";
    const snippet = trimErrorText(stderr || message);
    return snippet ? `ffmpeg failed: ${snippet}` : "ffmpeg failed";
}
//# sourceMappingURL=utils.js.map