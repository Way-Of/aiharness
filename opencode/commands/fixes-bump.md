# Fixes Bump

Bump the version across all project files using the fixes-manager skill.

## Usage
`/fixes bump --project=<project> --version=<version>`

### Arguments
- `--project` (required) — Project namespace (any project with `assets/<project>/version-config.json`)
- `--version` (required) — Target version string (e.g. `1.8.0`)

## Process:

### 1. Validate Arguments
- Project must be a valid namespace from `skills/fixes-manager/assets/`

### 2. Load Version Config
- Read `skills/fixes-manager/assets/<project>/version-config.json`
- This defines ALL version files for that project, their types (json/yaml/regex/markdown), and bump order
- **Each project has its own config** — check the project's `version-config.json` for the full list of version files

### 3. Bump Each Version File in Order
For each file in `version-config.json.version_files`, sorted by `bump_order`:

| type | How to update |
|------|--------------|
| `json` | Update the specified `fields` in the JSON file |
| `yaml` | Update the specified `fields` in the YAML file |
| `regex` | Replace the regex `pattern` match with the new version |
| `markdown` | Insert a new version header entry (CHANGELOG) or find/replace old version strings (README) |

### 4. Project-Specific Steps
Some projects have additional version files beyond the base config. Check `version-config.json` for:
- `per_tool_versions` — If present, update per-tool version fields after the base manifest
- `post_bump_hooks` — If present, run the specified commands (e.g., recompile manifests)

### 5. CHANGELOG Entry
Insert after `# Changelog` line:

```markdown
## [<version>] - YYYY-MM-DD

### Harness (AI Engineering Harness v<version>)
- <summary of changes>
```

### 6. Confirm
Show the user a summary of what was changed and ask for confirmation before committing.

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
