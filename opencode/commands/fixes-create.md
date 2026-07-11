# Fixes Create

Create a new fix note entry for any Way-Of project using the fixes-manager skill.

## Usage
`/fixes create --project=<project> [--component=<component>] [--version=<version>]`

### Arguments
- `--project` (required) — Project namespace (any project with `assets/<project>/components.json`)
- `--component` (optional) — Component name (from `assets/<project>/components.json`). Prompts interactively if omitted.
- `--version` (optional) — Version string (e.g. `1.8.0`). Prompts interactively if omitted.

## Process:
1. Validate the provided arguments
2. Activate the fixes-manager skill
3. Load `assets/<project>/` for version fields and component list
4. Read existing fix notes from `thoughts/<project>/docs/fixes/`
5. Append new version entry with standardized format
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
