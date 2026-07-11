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
       → /implement_plan → /validate_plan (correctness)
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
