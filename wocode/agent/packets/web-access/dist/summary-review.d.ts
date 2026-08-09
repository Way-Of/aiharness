import type { ExtensionContext } from "@mariozechner/pi-coding-agent";
import type { QueryResultData } from "./storage.js";
export interface SummaryMeta {
    model: string | null;
    durationMs: number;
    tokenEstimate: number;
    fallbackUsed: boolean;
    fallbackReason?: string;
    edited?: boolean;
}
export type SummaryGenerationContext = Pick<ExtensionContext, "model" | "modelRegistry">;
export declare function buildSummaryPrompt(results: QueryResultData[], feedback?: string): string;
export declare function buildDeterministicSummary(results: QueryResultData[]): {
    summary: string;
    meta: SummaryMeta;
};
export declare function generateSummaryDraft(results: QueryResultData[], ctx: SummaryGenerationContext, signal?: AbortSignal, modelOverride?: string, feedback?: string): Promise<{
    summary: string;
    meta: SummaryMeta;
}>;
//# sourceMappingURL=summary-review.d.ts.map