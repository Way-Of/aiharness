/**
 * RSC Content Extractor
 *
 * Extracts readable content from Next.js React Server Components (RSC) flight payloads.
 * RSC pages embed content as JSON in <script>self.__next_f.push([...])</script> tags.
 */
export interface RSCExtractResult {
    title: string;
    content: string;
}
export declare function extractRSCContent(html: string): RSCExtractResult | null;
//# sourceMappingURL=rsc-extract.d.ts.map