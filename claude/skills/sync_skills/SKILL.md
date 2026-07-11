---
name: sync_skills
description: Sync all skills across all frontends. Delegates to the build-tool-skill skill.
allowed-tools: Read Bash Glob Grep
disable-model-invocation: true
---

# /sync-skills — Sync all skills across all frontends

Activates the [build-tool-skill](skills/build_tool_skill/SKILL.md) skill to perform this operation.

## Usage
```
/sync-skills
```

## Process
1. This command activates the `build-tool-skill` skill
2. Follow that skill's workflow to complete the operation
3. Report results to the user

## Context Reference

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
- **Knowledge**: `thoughts/global/knowledge/` — stored knowledge base, searchable via `knowledge` skill
