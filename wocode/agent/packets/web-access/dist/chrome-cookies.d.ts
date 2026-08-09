export type CookieMap = Record<string, string>;
export declare function getGoogleCookies(options?: {
    profile?: string;
    requiredCookies?: string[];
}): Promise<{
    cookies: CookieMap;
    warnings: string[];
} | null>;
//# sourceMappingURL=chrome-cookies.d.ts.map