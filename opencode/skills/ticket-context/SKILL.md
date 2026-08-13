---
name: ticket-context
description: Associates work with a specific ticket ID across all WoM projects (WOMONO, WOW, OPT). Use when initiating new work to ensure compliance and production-ready standards.
---

# Ticket Context Guide

## Overview

This skill ensures all work is linked to an approved ticket from the correct namespace, following WoM naming conventions and production-ready standards.

## Ticket Namespaces

| Prefix | Project | Storage |
|--------|---------|---------|
| WOMONO-XXX | WayOfMono | `thoughts/wayofmono/shared/tickets/` |
| WOW-XXX | WayOfWork | `thoughts/wow/shared/tickets/` |
| OPT-XXX | Opticat | `thoughts/opticat/shared/tickets/` |

## Ticket Resolution

When looking up a ticket, search in this order:

1. `thoughts/<project>/shared/tickets/<PREFIX>-<NNN>-*.md` (active)
2. `thoughts/<project>/shared/tickets/done/<PREFIX>-<NNN>-*.md` (completed)
3. `thoughts/<project>/shared/tickets/deprecated/<PREFIX>-<NNN>-*.md` (deprecated)
4. `thoughts/<project>/<developer>/<PREFIX>-<NNN>-*.md` (personal copy)

If found in `done/` or `deprecated/`, inform the user:
- "This ticket is completed/deprecated. Do you want to reopen it?"
- If yes: Move back to shared/tickets/ root, set status to "In Progress"

## Domain Awareness

Every ticket has a `domain` field. When loading ticket context:
- Display the domain and primary team member for that domain
- If work crosses domains, note the cross-domain impact
- Suggest consulting the domain primary if the work is outside the agent's expertise

## Workflow

1. **Activation**: Activate when starting any new task, feature, or bug fix.
2. **Ticket ID Prompt**: Ask for ticket ID in `<PREFIX>-<NNN>` format.
3. **Load Context**: Read ticket from resolved location.
4. **Production-Ready Standard**: AC must include no mock data, error handling, observability, security, edge cases, tests. Flag if missing.
5. **Compliance Reminder**: All work must align with ticket AC and WoM best practices.

## Rules

- All code changes **must** be associated with an existing ticket.
- Tickets follow naming convention in `thoughts/global/templates/ticket-template.md`.
- Never work on a deprecated ticket without user confirmation.
- The `ticket_manager` skill handles full lifecycle. This skill ensures process adherence.

## CTO Dashboard UI Integration

- **Status Dropdown**: Both list and detail views have status Select
- **Available Statuses**: Backlog, In Progress, In Review, Done, Blocked, Deprecated
- **Source of Truth**: UI status is authoritative; agents sync to it


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
