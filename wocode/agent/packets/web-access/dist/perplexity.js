import { existsSync, readFileSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
import { activityMonitor } from "./activity.js";
const PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions";
const CONFIG_PATH = join(homedir(), ".wocode", "web-search.json");
const RATE_LIMIT = {
    maxRequests: 10,
    windowMs: 60 * 1000,
};
const requestTimestamps = [];
let cachedConfig = null;
function loadConfig() {
    if (cachedConfig)
        return cachedConfig;
    if (!existsSync(CONFIG_PATH)) {
        cachedConfig = {};
        return cachedConfig;
    }
    const content = readFileSync(CONFIG_PATH, "utf-8");
    try {
        cachedConfig = JSON.parse(content);
        return cachedConfig;
    }
    catch (err) {
        const message = err instanceof Error ? err.message : String(err);
        throw new Error(`Failed to parse ${CONFIG_PATH}: ${message}`);
    }
}
function normalizeApiKey(value) {
    if (typeof value !== "string")
        return null;
    const normalized = value.trim();
    return normalized.length > 0 ? normalized : null;
}
function getApiKey() {
    const config = loadConfig();
    const key = normalizeApiKey(process.env.PERPLEXITY_API_KEY) ?? normalizeApiKey(config.perplexityApiKey);
    if (!key) {
        throw new Error("Perplexity API key not found. Either:\n" +
            `  1. Create ${CONFIG_PATH} with { "perplexityApiKey": "your-key" }\n` +
            "  2. Set PERPLEXITY_API_KEY environment variable\n" +
            "Get a key at https://perplexity.ai/settings/api");
    }
    return key;
}
function checkRateLimit() {
    const now = Date.now();
    const windowStart = now - RATE_LIMIT.windowMs;
    while (requestTimestamps.length > 0 && requestTimestamps[0] < windowStart) {
        requestTimestamps.shift();
    }
    if (requestTimestamps.length >= RATE_LIMIT.maxRequests) {
        const waitMs = requestTimestamps[0] + RATE_LIMIT.windowMs - now;
        throw new Error(`Rate limited. Try again in ${Math.ceil(waitMs / 1000)}s`);
    }
    requestTimestamps.push(now);
}
function validateDomainFilter(domains) {
    return domains.filter((d) => {
        const domain = d.startsWith("-") ? d.slice(1) : d;
        return /^[a-zA-Z0-9][a-zA-Z0-9-_.]*\.[a-zA-Z]{2,}$/.test(domain);
    });
}
export function isPerplexityAvailable() {
    const config = loadConfig();
    return !!(normalizeApiKey(process.env.PERPLEXITY_API_KEY) ?? normalizeApiKey(config.perplexityApiKey));
}
export async function searchWithPerplexity(query, options = {}) {
    checkRateLimit();
    const activityId = activityMonitor.logStart({ type: "api", query });
    activityMonitor.updateRateLimit({
        used: requestTimestamps.length,
        max: RATE_LIMIT.maxRequests,
        oldestTimestamp: requestTimestamps[0] ?? null,
        windowMs: RATE_LIMIT.windowMs,
    });
    const apiKey = getApiKey();
    const numResults = Math.min(options.numResults ?? 5, 20);
    const requestBody = {
        model: "sonar",
        messages: [{ role: "user", content: query }],
        max_tokens: 1024,
        return_related_questions: false,
    };
    if (options.recencyFilter) {
        requestBody.search_recency_filter = options.recencyFilter;
    }
    if (options.domainFilter && options.domainFilter.length > 0) {
        const validated = validateDomainFilter(options.domainFilter);
        if (validated.length > 0) {
            requestBody.search_domain_filter = validated;
        }
    }
    let response;
    try {
        response = await fetch(PERPLEXITY_API_URL, {
            method: "POST",
            headers: {
                Authorization: `Bearer ${apiKey}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestBody),
            signal: options.signal,
        });
    }
    catch (err) {
        const message = err instanceof Error ? err.message : String(err);
        if (message.toLowerCase().includes("abort")) {
            activityMonitor.logComplete(activityId, 0);
        }
        else {
            activityMonitor.logError(activityId, message);
        }
        throw err;
    }
    if (!response.ok) {
        activityMonitor.logComplete(activityId, response.status);
        const errorText = await response.text();
        throw new Error(`Perplexity API error ${response.status}: ${errorText}`);
    }
    let data;
    try {
        data = await response.json();
    }
    catch (err) {
        activityMonitor.logComplete(activityId, response.status);
        const message = err instanceof Error ? err.message : String(err);
        throw new Error(`Perplexity API returned invalid JSON: ${message}`);
    }
    const answer = data.choices?.[0]?.message?.content || "";
    const citations = Array.isArray(data.citations) ? data.citations : [];
    const results = [];
    for (let i = 0; i < Math.min(citations.length, numResults); i++) {
        const citation = citations[i];
        if (typeof citation === "string") {
            results.push({ title: `Source ${i + 1}`, url: citation, snippet: "" });
        }
        else if (citation && typeof citation === "object" && typeof citation.url === "string") {
            results.push({
                title: citation.title || `Source ${i + 1}`,
                url: citation.url,
                snippet: "",
            });
        }
    }
    activityMonitor.logComplete(activityId, response.status);
    return { answer, results };
}
//# sourceMappingURL=perplexity.js.map