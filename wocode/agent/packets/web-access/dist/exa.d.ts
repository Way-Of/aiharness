import type { SearchOptions, SearchResponse } from "./perplexity.js";
export type ExaSearchResult = SearchResponse | {
    exhausted: true;
} | null;
export interface ExaSearchOptions extends SearchOptions {
    includeContent?: boolean;
}
export declare function callExaMcp(toolName: string, args: Record<string, unknown>, signal?: AbortSignal): Promise<string>;
export declare function isExaAvailable(): boolean;
export declare function hasExaApiKey(): boolean;
export declare function searchWithExa(query: string, options?: ExaSearchOptions): Promise<ExaSearchResult>;
//# sourceMappingURL=exa.d.ts.map