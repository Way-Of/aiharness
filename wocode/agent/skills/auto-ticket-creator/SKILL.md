---
name: auto-ticket-creator
description: Monitor codebase, dependencies, and external sources to auto-create tickets for agent updates, skill updates, dep updates, security advisories
allowed-tools: read, write, grep, glob, web, search
---

# Auto-Ticket Creation skill

Autonomously monitors the codebase, dependencies, and external sources for updates, and automatically creates tickets.

## Monitored Sources

- Git commits, tags, branches (`git-adapter`)
- npm registry for package updates (`npm-adapter`)
- Deno/JSR registry for module updates (`deno-adapter`)
- GitHub releases, security advisories (`github-adapter`)
- `ref/skills/` and `ref/agents/` for new content (`ref-adapter`)
- Agent frontend releases (`platform-adapter`)

## Commands

- `ai-harness monitor --once` - Single scan
- `ai-harness monitor --daemon` - Continuous monitoring
- `ai-harness monitor --source=github,npm,ref` - Selective sources

## Change Classification

Detected changes are classified as: `agent-update`, `skill-update`, `dep-update`, `security`, `breaking-change`

Tickets are created with proper namespace and auto-assigned based on change type.

## Templates & Rules

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
