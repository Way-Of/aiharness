---
name: ticket-executor
description: Execute approved plans in phases, validating telemetry and committing changes after each phase completes successfully
allowed-tools:
  - read
  - write
  - grep
  - glob
  - web
  - search
---

# Ticket Executor skill

Executes approved plans in phases, with validation and telemetry tracking after each phase.

## Workflow

```
Ticket → /create_plan → /validate_plan → /implement_plan → /validate_implementation → /validate_telemetry → /commit
```

## Commands

- `/implement_plan <ticket-id>` - Execute approved plan phase-by-phase
- `/execute_phase <ticket-id> <phase>` - Execute specific phase
- `/skip_phase <ticket-id> <phase>` - Skip phase with reason

## Telemetry

- Capture execution time
- Track error rates
- Compare against plan expectations

## Audit Utility

A ticket audit script is bundled at `assets/audit-tickets.js`. Run it after executing plan phases to verify ticket frontmatter integrity:

```bash
deno run -A assets/audit-tickets.js
```

## CTO Dashboard UI Integration

The CTO Dashboard status dropdown affects execution workflow:

- **Status Sync**: When `/implement_plan` runs, it reads the current ticket status from the dashboard/UI
- **Auto-transition**: Moving a ticket to "In Progress" in the UI signals the executor to begin work
- **Review Flow**: "In Review" and "Approved" statuses map to the validation phases
- **Completion**: Setting status to "Done" in UI marks ticket complete (or "Submitted for Review" if review required)

Agents should respect the UI status as the current state. Use `update_ticket` tool to programmatically change status:
- `update_ticket` with `status: "In Progress"` when starting work
- `update_ticket` with `status: "In Review"` when submitting for review
- `update_ticket` with `status: "Done"` when work is complete

## Notification Integration

When completing ticket phases or implementing plans, mark related CTO Dashboard notifications as Read via the notification API:

```bash
# Mark review notification as read after phase completion
curl -X POST http://localhost:6969/api/notifications \
  -H "Content-Type: application/json" \
  -d '{"action": "mark-read", "notificationId": "review-<TICKET_ID>"}'

# Mark update notification as read after phase completion
curl -X POST http://localhost:6969/api/notifications \
  -H "Content-Type: application/json" \
  -d '{"action": "mark-read", "notificationId": "update-<TICKET_ID>"}'
```

The notification IDs follow the format:
- `review-<TICKET_ID>` — for tickets in review queue
- `update-<TICKET_ID>` — for ticket status updates

This ensures the CTO Dashboard bell badge reflects only genuinely unread notifications.

## WayOfTeams MCP Integration (Optional)

If WayOfTeams MCP is available, use it for status updates:

### MCP Status Updates
When MCP is available, update ticket status via WayOfTeams:
- `tickets_update` with `status: "In Progress"` when starting
- `tickets_update` with `status: "Done"` when complete
- `team_notifications` for notification management

### MCP + File Hybrid
1. Try MCP first: `tickets_update` via WayOfTeams
2. Also update local ticket file as backup
3. If MCP fails, fall back to file-only

**Always keep file-based operations as fallback.**

## Done Lifecycle

When all phases are complete, move the ticket to `done/`:

### Moving to Done
```bash
# Find and move ticket
TICKET_FILE=$(find thoughts/ -name "<TICKET-ID>*.md" -type f)
mv "$TICKET_FILE" thoughts/<project>/shared/tickets/done/
```

### Plan Done Lifecycle
When implementing a plan, move it to `done/` after completion:
```bash
mv thoughts/<project>/shared/plans/<plan-name>.md \
   thoughts/<project>/shared/plans/done/
```

## Code Traceability

When executing plan phases, ensure all code changes have ticket references:

### Before Committing
1. Check all modified files for `[PREFIX-NNN]` references
2. If missing, add them before the changed lines
3. Verify with: `grep -r "<TICKET-ID>" --include="*.ts" --include="*.py"`

### Reference Format
```typescript
// [AIH-192] Phase 1: Add MCP skill
const skill = new WayOfTeamsMCP();
```

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
