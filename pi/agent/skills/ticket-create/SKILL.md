---
name: ticket-create
description: Interactive ticket creation wizard. Delegates to the ticket-manager skill.
allowed-tools:
  - read
  - write
  - bash
  - grep
  - glob
---

# /ticket-create — Interactive ticket creation wizard

Activates the [ticket-manager](skills/ticket-manager/SKILL.md) skill to perform this operation.

## Context Reference

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
- **Knowledge**: `thoughts/global/knowledge/` — stored knowledge base, searchable via `knowledge` skill
