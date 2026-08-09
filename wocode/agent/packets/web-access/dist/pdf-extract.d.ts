/**
 * PDF Content Extractor
 *
 * Extracts text from PDF files and saves to markdown.
 * Uses unpdf (pdfjs-dist wrapper) for text extraction.
 */
export interface PDFExtractResult {
    title: string;
    pages: number;
    chars: number;
    outputPath: string;
}
export interface PDFExtractOptions {
    maxPages?: number;
    outputDir?: string;
    filename?: string;
}
/**
 * Extract text from a PDF buffer and save to markdown file
 */
export declare function extractPDFToMarkdown(buffer: ArrayBuffer, url: string, options?: PDFExtractOptions): Promise<PDFExtractResult>;
/**
 * Check if URL or content-type indicates a PDF
 */
export declare function isPDF(url: string, contentType?: string): boolean;
//# sourceMappingURL=pdf-extract.d.ts.map