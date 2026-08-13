---
name: work
description: "Start working on a ticket, update status to In Progress. Delegates to the ticket-manager skill."
allowed-tools: read, write, bash, grep, glob
---

# /work — Start working on a ticket, update status to In Progress

Activates the [ticket-manager](skills/ticket-manager/SKILL.md) skill to perform this operation.

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
