import { type CookieMap } from "./chrome-cookies.js";
export interface GeminiWebOptions {
    youtubeUrl?: string;
    model?: string;
    files?: string[];
    signal?: AbortSignal;
    timeoutMs?: number;
}
export declare function isGeminiWebAvailable(chromeProfile?: string): Promise<CookieMap | null>;
export declare function getActiveGoogleEmail(cookies: CookieMap): Promise<string | null>;
export declare function queryWithCookies(prompt: string, cookieMap: CookieMap, options?: GeminiWebOptions): Promise<string>;
//# sourceMappingURL=gemini-web.d.ts.map