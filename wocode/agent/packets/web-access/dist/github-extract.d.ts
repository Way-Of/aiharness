import type { ExtractedContent } from "./extract.js";
export interface GitHubUrlInfo {
    owner: string;
    repo: string;
    ref?: string;
    refIsFullSha: boolean;
    path?: string;
    type: "root" | "blob" | "tree";
}
export declare function parseGitHubUrl(url: string): GitHubUrlInfo | null;
export declare function extractGitHub(url: string, signal?: AbortSignal, forceClone?: boolean): Promise<ExtractedContent | null>;
export declare function clearCloneCache(): void;
//# sourceMappingURL=github-extract.d.ts.map