---
name: commit
description: "Create structured git commits. Delegates to the git-commit-helper skill."
allowed-tools:
  - read
  - bash
  - glob
  - grep
disable-model-invocation: true
---

# /commit — Create structured git commits

Activates the [git-commit-helper](skills/git_commit_helper/SKILL.md) skill to perform this operation.

## Usage
```
/commit
```

## Process
1. This command activates the `git-commit-helper` skill
2. Follow that skill's workflow to complete the operation
3. Report results to the user

## Context Reference

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
- **Knowledge**: `thoughts/global/knowledge/` — stored knowledge base, searchable via `knowledge` skill


## Critical: Update Tickets and Plans When Done

When implementation is complete, ALWAYS update the ticket and plan:

### Ticket Updates
- Set `status: "Done"` in frontmatter
- Set `completed: "YYYY-MM-DD"` in frontmatter
- ADD work log entry (never delete old entries)
- ADD any new findings or decisions
- Move ticket to `done/` subdirectory if applicable

### Plan Updates
- Check off completed phases in the plan file
- ADD any deviations from the original plan
- ADD notes about what was actually implemented vs planned
- Move plan to `done/` subdirectory if fully implemented

### Why This Matters
- Future developers need to know what was done and why
- Audit trails require complete history
- Debugging needs context from implementation
- Ticket status must reflect reality
