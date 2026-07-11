---
name: fixes_create
description: Create a fix note entry for any Way-Of project. Delegates to fixes-manager skill.
---

Create a new fix note entry for any Way-Of project using the fixes-manager skill.

## Usage
`/fixes create --project=<project> [--component=<component>] [--version=<version>]`

### Arguments
- `--project` (required) — Project namespace (any project with `assets/<project>/components.json`)
- `--component` (optional) — Component name (from `assets/<project>/components.json`). Prompts interactively if omitted.
- `--version` (optional) — Version string (e.g. `1.8.0`). Prompts interactively if omitted.

## Process
1. Validate the provided arguments
2. Activate the fixes-manager skill
3. Load `assets/<project>/` for version fields and component list
4. Read existing fix notes from `thoughts/<project>/docs/fixes/`
5. Append new version entry with standardized format
6. Confirm the result with the user

## Templates & Rules

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
