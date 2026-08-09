export declare function executeCodeSearch(_toolCallId: string, params: {
    query: string;
    maxTokens?: number;
}, signal?: AbortSignal): Promise<{
    content: Array<{
        type: "text";
        text: string;
    }>;
    details: {
        query: string;
        maxTokens: number;
        error?: string;
        mode?: "code-context" | "web-search-fallback";
    };
}>;
//# sourceMappingURL=code-search.d.ts.map