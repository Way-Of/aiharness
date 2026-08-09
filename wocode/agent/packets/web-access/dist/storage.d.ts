import type { ExtensionContext } from "@mariozechner/pi-coding-agent";
import type { ExtractedContent } from "./extract.js";
import type { SearchResult } from "./perplexity.js";
export interface QueryResultData {
    query: string;
    answer: string;
    results: SearchResult[];
    error: string | null;
    provider?: string;
}
export interface StoredSearchData {
    id: string;
    type: "search" | "fetch";
    timestamp: number;
    queries?: QueryResultData[];
    urls?: ExtractedContent[];
}
export declare function generateId(): string;
export declare function storeResult(id: string, data: StoredSearchData): void;
export declare function getResult(id: string): StoredSearchData | null;
export declare function getAllResults(): StoredSearchData[];
export declare function deleteResult(id: string): boolean;
export declare function clearResults(): void;
export declare function restoreFromSession(ctx: ExtensionContext): void;
//# sourceMappingURL=storage.d.ts.map