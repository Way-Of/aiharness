# Fixes Validate

Validate version consistency across all project files using the fixes-manager skill.

## Usage
`/fixes validate --project=<project>`

### Arguments
- `--project` (required) — Project namespace (any project with `assets/<project>/version-config.json`)

## Process
1. Validate the provided arguments
2. Activate the fixes-manager skill
3. Load `assets/<project>/version-config.json` and `validate-rules.json`
4. Read all version fields from their respective files
5. Report any mismatches between versions
6. Present a summary of findings to the user

## Templates & Rules

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
