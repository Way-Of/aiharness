---
description: Fixes Bump — Bump version across project files
---
# /fixes bump — Bump Version Across Project Files

Bump the version across all project files using the fixes-manager skill.

## Usage
`/fixes bump --project=<project> --version=<version>`

## Steps
1. Validate arguments: `--project` (required), `--version` (required)
2. Load the fixes-manager skill
3. Read `assets/<project>/version-config.json` for version files, types, and bump order
4. Update each version file in order (types: json/yaml/regex/markdown)
5. If version-config.json has per_tool_versions: also update per-tool version fields, then recompile if post_bump_hooks present
6. Confirm the result with the user

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
