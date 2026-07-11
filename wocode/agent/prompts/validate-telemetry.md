---
description: Validate Telemetry
---
# Validate Telemetry

Activate the **observability-driven-development** skill and run its
**Validation** section.

## Mode Detection

- If an argument was provided and it resolves to an existing file under
  `thoughts/shared/telemetry/`, run **Mode A — Spec-Driven Validation**.
- Otherwise (no argument, or argument doesn't resolve), run
  **Mode B — Generic Health Check**.

## Pre-Flight

Before running either mode, confirm:

1. The local Aspire dashboard is reachable (`curl -sf http://localhost:18888`
   returns 2xx).
2. The user's service is configured to export to the dashboard
   (`OTEL_EXPORTER_OTLP_ENDPOINT` set).

If either fails, surface a one-line setup hint pointing at
`observability-driven-development/local-setup.md` and stop.

## Output

Per the report format in the ODD skill's Validation section. Don't modify
code or config silently — the report is the output.

## Relationship to Other Commands

```
Ticket → /create_plan → [ODD: write narrative]
       → /implement_plan → /validate_implementation (correctness)
       → /validate_telemetry (telemetry) → /commit
```

## Context Reference

### Rules
- **Location**: `thoughts/global/rules/` (global) + `thoughts/<project>/rules/` (project-specific)
- **Precedence**: Project rules override global rules
- **Categories**: coding-standards, naming-conventions, testing-requirements, security-guidelines, deployment-rules

### Templates
- **Location**: `thoughts/global/templates/`
- **Available**: ticket-template.md, knowledge-entry.md, todo-template.md, AGENTS.md.template, fixes/

### Knowledgebase
- **Location**: `thoughts/global/knowledge/`
- **Commands**: Use `knowledge` skill to store, fetch, search, list, stats

## Agent Reference

### Available Agents
| Agent | Purpose | When to Use |
|-------|---------|-------------|
| `scout` | Fast codebase recon, file finding | Most code investigation tasks |
| `codebase_locator` | Find files by feature/task | Locating specific files |
| `codebase_pattern_finder` | Find similar implementations | Modeling after existing code |
| `planner` | Design implementation plans | Starting new features, refactoring |
| `codebase_analyzer` | Deep complex analysis | Tracing data flow through 5+ files |
| `coder` | Implementation and code generation | Turning plans into code |
| `reviewer` | Code review and quality checks | After implementation |
| `debugger` | Debug issues (read-only) | When something is broken |
| `thoughts_analyzer` | Extract insights from research | Analyzing research documents |
| `thoughts_locator` | Find documents in thoughts/ | Locating tickets, plans, docs |
| `web_search_researcher` | Research from web sources | Current info not in codebase |
| `netlify_troubleshooter` | Netlify CI/CD diagnostics | Build pipeline issues |
| `github` | GitHub operations (safe) | PRs, issues, branches, reviews |
