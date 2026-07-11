---
name: build-auto-ticket-creator
description: Monitor codebase, dependencies, and external sources to auto-create tickets for agent updates, skill updates, dep updates, security advisories
allowed-tools: read, write, grep, glob, web, search
---

# Build Auto-Ticket Creation skill

Autonomously monitors the codebase, dependencies, and external sources for updates, and automatically creates tickets.

## Templates & Rules

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/templates/rules/` — coding standards, naming, security, testing, deployment rules
