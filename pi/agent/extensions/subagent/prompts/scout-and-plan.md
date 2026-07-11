---
description: Scout gathers context, planner creates implementation plan (no implementation)
---
Use the subagent tool with the chain parameter to execute this workflow:

1. First, use the "scout" agent to find all code relevant to: $@
2. Then, use the "planner" agent to create an implementation plan for "$@" using the context from the previous step (use {previous} placeholder)

Execute this as a chain, passing output between steps via {previous}. Do NOT implement - just return the plan.

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
