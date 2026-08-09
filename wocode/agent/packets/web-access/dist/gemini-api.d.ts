export declare const API_BASE = "https://generativelanguage.googleapis.com/v1beta";
export declare const DEFAULT_MODEL = "gemini-3-flash-preview";
export declare function getApiKey(): string | null;
export declare function isGeminiApiAvailable(): boolean;
export interface GeminiApiOptions {
    model?: string;
    mimeType?: string;
    signal?: AbortSignal;
    timeoutMs?: number;
}
export declare function queryGeminiApiWithVideo(prompt: string, videoUri: string, options?: GeminiApiOptions): Promise<string>;
//# sourceMappingURL=gemini-api.d.ts.map