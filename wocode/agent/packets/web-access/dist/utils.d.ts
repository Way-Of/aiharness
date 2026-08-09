export declare function formatSeconds(s: number): string;
export declare function readExecError(err: unknown): {
    code?: string;
    stderr: string;
    message: string;
};
export declare function isTimeoutError(err: unknown): boolean;
export declare function trimErrorText(text: string): string;
export declare function mapFfmpegError(err: unknown): string;
//# sourceMappingURL=utils.d.ts.map