import { type ExtractedContent, type ExtractOptions, type FrameResult } from "./extract.js";
interface VideoFileInfo {
    absolutePath: string;
    mimeType: string;
    sizeBytes: number;
}
export declare function isVideoFile(input: string): VideoFileInfo | null;
export declare function extractVideo(info: VideoFileInfo, signal?: AbortSignal, options?: ExtractOptions): Promise<ExtractedContent | null>;
export declare function extractVideoFrame(filePath: string, seconds?: number): Promise<FrameResult>;
export declare function getLocalVideoDuration(filePath: string): Promise<number | {
    error: string;
}>;
export {};
//# sourceMappingURL=video-extract.d.ts.map