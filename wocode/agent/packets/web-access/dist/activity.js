export class ActivityMonitor {
    entries = [];
    maxEntries = 10;
    listeners = new Set();
    rateLimitInfo = { used: 0, max: 10, oldestTimestamp: null, windowMs: 60000 };
    nextId = 1;
    logStart(partial) {
        const id = `act-${this.nextId++}`;
        const entry = {
            ...partial,
            id,
            startTime: Date.now(),
            status: null,
        };
        this.entries.push(entry);
        if (this.entries.length > this.maxEntries) {
            this.entries.shift();
        }
        this.notify();
        return id;
    }
    logComplete(id, status) {
        const entry = this.entries.find((e) => e.id === id);
        if (entry) {
            entry.endTime = Date.now();
            entry.status = status;
            this.notify();
        }
    }
    logError(id, error) {
        const entry = this.entries.find((e) => e.id === id);
        if (entry) {
            entry.endTime = Date.now();
            entry.error = error;
            this.notify();
        }
    }
    getEntries() {
        return this.entries;
    }
    getRateLimitInfo() {
        return this.rateLimitInfo;
    }
    updateRateLimit(info) {
        this.rateLimitInfo = info;
        this.notify();
    }
    onUpdate(callback) {
        this.listeners.add(callback);
        return () => this.listeners.delete(callback);
    }
    clear() {
        this.entries = [];
        this.rateLimitInfo = { used: 0, max: 10, oldestTimestamp: null, windowMs: 60000 };
        this.notify();
    }
    notify() {
        for (const cb of this.listeners) {
            try {
                cb();
            }
            catch {
            }
        }
    }
}
export const activityMonitor = new ActivityMonitor();
//# sourceMappingURL=activity.js.map