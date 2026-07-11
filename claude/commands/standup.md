---
name: standup
description: "Generate daily end-of-day standup entries. Delegates to the standup skill."
---

# /standup — Generate daily standup

Activates the standup skill to capture today's work, blockers, and metrics.
Saves to thoughts/global/standup/<dev>/<YYYY-MM-DD>.md

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
