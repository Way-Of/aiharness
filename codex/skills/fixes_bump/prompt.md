> **Platform**: Codex | **Skill**: fixes_bump | **Version**: 1.0.0
>
> _Auto-generated from canonical format. Do not edit directly._

Bump the version across all project files using the fixes-manager skill.

## Usage
`/fixes bump --project=<project> --version=<version>`

### Arguments
- `--project` (required) — Project namespace (any project with `assets/<project>/version-config.json`)
- `--version` (required) — Target version string (e.g. `1.8.0`)

## Process
1. Validate the provided arguments
2. Activate the fixes-manager skill
3. Load `assets/<project>/version-config.json` for version fields and file list
4. Update each file's version field in the defined order
5. Update fix notes and CHANGELOG
6. Confirm the result with the user

## Templates & Rules

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
