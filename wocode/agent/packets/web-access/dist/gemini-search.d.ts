import { type SearchResponse, type SearchOptions } from "./perplexity.js";
export type SearchProvider = "auto" | "perplexity" | "gemini" | "exa";
export type ResolvedSearchProvider = Exclude<SearchProvider, "auto">;
export interface AttributedSearchResponse extends SearchResponse {
    provider: ResolvedSearchProvider;
}
export interface FullSearchOptions extends SearchOptions {
    provider?: SearchProvider;
    includeContent?: boolean;
}
export declare function search(query: string, options?: FullSearchOptions): Promise<AttributedSearchResponse>;
//# sourceMappingURL=gemini-search.d.ts.map