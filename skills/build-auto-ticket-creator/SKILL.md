---
name: build_auto_ticket_creator
description: Monitor codebase, dependencies, and external sources to auto-create tickets for agent updates, skill updates, dep updates, security advisories
allowed-tools: Read, Write, Grep, Glob, Web, Search
---

# Build Auto-Ticket Creation skill

Autonomously monitors the codebase, dependencies, and external sources for updates, and automatically creates tickets.

## Context Reference

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
- **Knowledge**: `thoughts/global/knowledge/` — stored knowledge base, searchable via `knowledge` skill
