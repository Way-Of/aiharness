export interface ActivityEntry {
    id: string;
    type: "api" | "fetch";
    startTime: number;
    endTime?: number;
    query?: string;
    url?: string;
    status: number | null;
    error?: string;
}
export interface RateLimitInfo {
    used: number;
    max: number;
    oldestTimestamp: number | null;
    windowMs: number;
}
export declare class ActivityMonitor {
    private entries;
    private readonly maxEntries;
    private listeners;
    private rateLimitInfo;
    private nextId;
    logStart(partial: Omit<ActivityEntry, "id" | "startTime" | "status">): string;
    logComplete(id: string, status: number): void;
    logError(id: string, error: string): void;
    getEntries(): readonly ActivityEntry[];
    getRateLimitInfo(): RateLimitInfo;
    updateRateLimit(info: RateLimitInfo): void;
    onUpdate(callback: () => void): () => void;
    clear(): void;
    private notify;
}
export declare const activityMonitor: ActivityMonitor;
//# sourceMappingURL=activity.d.ts.map