export interface VideoFrame {
    data: string;
    mimeType: string;
    timestamp: string;
}
export type FrameData = {
    data: string;
    mimeType: string;
};
export type FrameResult = FrameData | {
    error: string;
};
export interface ExtractedContent {
    url: string;
    title: string;
    content: string;
    error: string | null;
    thumbnail?: {
        data: string;
        mimeType: string;
    };
    frames?: VideoFrame[];
    duration?: number;
}
export interface ExtractOptions {
    timeoutMs?: number;
    forceClone?: boolean;
    prompt?: string;
    timestamp?: string;
    frames?: number;
    model?: string;
}
export declare function extractContent(url: string, signal?: AbortSignal, options?: ExtractOptions): Promise<ExtractedContent>;
export declare function extractHeadingTitle(text: string): string | null;
export declare function fetchAllContent(urls: string[], signal?: AbortSignal, options?: ExtractOptions): Promise<ExtractedContent[]>;
//# sourceMappingURL=extract.d.ts.map