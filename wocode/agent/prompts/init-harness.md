---
description: Initialize Harness
---
# Initialize Harness

Initialize the AI Engineering Harness in this repository.

## What This Command Does

1. Runs the built-in `/init` command to generate `AGENTS.md`
2. Creates the `thoughts/` directory structure for context engineering
3. Adds a ticket template for consistent ticket creation
4. Provides guidance on next steps

## Instructions

Load and follow the `init-harness` skill for detailed instructions on how to:

1. Check the current state of the repository
2. Run `/init` to generate AGENTS.md (the built-in codebase analysis command)
3. Create the thoughts/ directory structure
4. Add the ticket template
5. Optionally create a personal thoughts directory
6. Present next steps to the user

**Important**: The `/init` command is OpenCode's built-in command that analyzes the codebase and generates AGENTS.md. This `/init_harness` command wraps that functionality and adds the context engineering setup.

## Quick Reference

After running this command, the repository will have:

```
AGENTS.md                           # Codebase context (from /init)
thoughts/
├── shared/
│   ├── tickets/                    # Feature requests, bugs, tasks
│   │   └── ticket-template.md      # Template for new tickets
│   ├── plans/                      # Implementation plans
│   └── research/                   # Research documents
└── global/                         # Cross-repository concerns
```

## Workflow After Initialization

```
Ticket → /create_plan → /validate_plan → /implement_plan → /validate_implementation → /commit
```

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
