import type { ExtractedContent } from "./extract.js";
import type { GitHubUrlInfo } from "./github-extract.js";
export declare function checkGhAvailable(): Promise<boolean>;
export declare function showGhHint(): void;
export declare function checkRepoSize(owner: string, repo: string): Promise<number | null>;
export declare function fetchViaApi(url: string, owner: string, repo: string, info: GitHubUrlInfo, sizeNote?: string): Promise<ExtractedContent | null>;
//# sourceMappingURL=github-api.d.ts.map