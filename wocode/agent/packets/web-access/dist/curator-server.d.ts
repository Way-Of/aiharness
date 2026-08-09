import http from "node:http";
import type { SummaryMeta } from "./summary-review.js";
export interface CuratorServerOptions {
    queries: string[];
    sessionToken: string;
    timeout: number;
    availableProviders: {
        perplexity: boolean;
        exa: boolean;
        gemini: boolean;
    };
    defaultProvider: string;
    summaryModels: Array<{
        value: string;
        label: string;
    }>;
    defaultSummaryModel: string | null;
}
export interface CuratorServerCallbacks {
    onSubmit: (payload: {
        selectedQueryIndices: number[];
        summary?: string;
        summaryMeta?: SummaryMeta;
        rawResults?: boolean;
    }) => void;
    onCancel: (reason: "user" | "timeout" | "stale") => void;
    onProviderChange: (provider: string) => void;
    onAddSearch: (query: string, queryIndex: number, provider?: string) => Promise<{
        answer: string;
        results: Array<{
            title: string;
            url: string;
            domain: string;
        }>;
        provider: string;
    }>;
    onSummarize: (selectedQueryIndices: number[], signal: AbortSignal, model?: string, feedback?: string) => Promise<{
        summary: string;
        meta: SummaryMeta;
    }>;
    onRewriteQuery: (query: string, signal: AbortSignal) => Promise<string>;
}
export interface CuratorServerHandle {
    server: http.Server;
    url: string;
    close: () => void;
    pushResult: (queryIndex: number, data: {
        answer: string;
        results: Array<{
            title: string;
            url: string;
            domain: string;
        }>;
        provider: string;
    }) => void;
    pushError: (queryIndex: number, error: string, provider?: string) => void;
    searchesDone: () => void;
}
export declare function startCuratorServer(options: CuratorServerOptions, callbacks: CuratorServerCallbacks): Promise<CuratorServerHandle>;
//# sourceMappingURL=curator-server.d.ts.map