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

## Agent Reference

### Available Agents
| Agent | Purpose | When to Use |
|-------|---------|-------------|
| `scout` | Fast codebase recon, file finding | Most code investigation tasks |
| `codebase_locator` | Find files by feature/task | Locating specific files |
| `codebase_pattern_finder` | Find similar implementations | Modeling after existing code |
| `planner` | Design implementation plans | Starting new features, refactoring |
| `codebase_analyzer` | Deep complex analysis | Tracing data flow through 5+ files |
| `coder` | Implementation and code generation | Turning plans into code |
| `reviewer` | Code review and quality checks | After implementation |
| `debugger` | Debug issues (read-only) | When something is broken |
| `thoughts_analyzer` | Extract insights from research | Analyzing research documents |
| `thoughts_locator` | Find documents in thoughts/ | Locating tickets, plans, docs |
| `web_search_researcher` | Research from web sources | Current info not in codebase |
| `netlify_troubleshooter` | Netlify CI/CD diagnostics | Build pipeline issues |
| `github` | GitHub operations (safe) | PRs, issues, branches, reviews |
