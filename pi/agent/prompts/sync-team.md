---
description: Sync-team — Show team ticket dashboard
---
# /sync-team — Show team ticket dashboard

Activates the ticket-manager skill to perform this operation.

## Usage
```
/sync-team
```

## Steps
1. Activate the `ticket-manager` skill
2. Follow that skill's workflow
3. Report results to the user

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
