import { type ExtractedContent, type FrameResult, type VideoFrame } from "./extract.js";
export declare function isYouTubeURL(url: string): {
    isYouTube: boolean;
    videoId: string | null;
};
export declare function isYouTubeEnabled(): boolean;
export declare function extractYouTube(url: string, signal?: AbortSignal, prompt?: string, model?: string): Promise<ExtractedContent | null>;
type StreamInfo = {
    streamUrl: string;
    duration: number | null;
};
type StreamResult = StreamInfo | {
    error: string;
};
export declare function getYouTubeStreamInfo(videoId: string): Promise<StreamResult>;
export declare function extractYouTubeFrame(videoId: string, seconds: number, streamInfo?: StreamInfo): Promise<FrameResult>;
export declare function extractYouTubeFrames(videoId: string, timestamps: number[], streamInfo?: StreamInfo): Promise<{
    frames: VideoFrame[];
    duration: number | null;
    error: string | null;
}>;
export declare function fetchYouTubeThumbnail(videoId: string): Promise<{
    data: string;
    mimeType: string;
} | null>;
export {};
//# sourceMappingURL=youtube-extract.d.ts.map