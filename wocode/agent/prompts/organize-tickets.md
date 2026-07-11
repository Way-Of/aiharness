---
description: Organize tickets — audit, archive, check naming, detect orphans, regenerate TODO.md
---
# /organize-tickets — Audit, archive, and organize all tickets

Activates the ticket-organization skill to perform this operation.

## Usage
```
/organize-tickets [--dry-run] [--auto-fix]
```

## Steps
1. Activate the `ticket-organization` skill
2. Run `organize_all` with the provided flags
3. If `--dry-run`, preview changes without modifying anything
4. If `--auto-fix`, auto-repair fixable issues during audit
5. Report results and write report to `thoughts/<project>/shared/research/`

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
