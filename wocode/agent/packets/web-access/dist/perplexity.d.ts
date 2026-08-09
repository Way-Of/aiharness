import type { ExtractedContent } from "./extract.js";
export interface SearchResult {
    title: string;
    url: string;
    snippet: string;
}
export interface SearchResponse {
    answer: string;
    results: SearchResult[];
    inlineContent?: ExtractedContent[];
}
export interface SearchOptions {
    numResults?: number;
    recencyFilter?: "day" | "week" | "month" | "year";
    domainFilter?: string[];
    signal?: AbortSignal;
}
export declare function isPerplexityAvailable(): boolean;
export declare function searchWithPerplexity(query: string, options?: SearchOptions): Promise<SearchResponse>;
//# sourceMappingURL=perplexity.d.ts.map