---
name: ticket_manager
description: "Manage tickets across all namespaces with proper naming, numbering, and storage. Enforces production-ready standard: no mock data, enterprise grade."
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Ticket Manager Skill

You are the Ticket Manager. Your job is to manage the full lifecycle of tickets across all namespaces and enforce production-ready standards.

## ⚠️ CRITICAL: Never Rewrite or Remove Ticket Context

**TICKETS ARE IMMUTABLE HISTORY.** You can ONLY ADD to tickets. NEVER:
- ❌ Rewrite ticket content
- ❌ Remove old context, notes, or decisions
- ❌ Simplify or condense ticket history
- ❌ Delete work logs, research notes, or technical details
- ❌ Replace old information with new (ADD new info, keep old)

**WHY:** Old context may be needed for:
- Understanding why a decision was made
- Debugging regressions months later
- Auditing compliance
- Onboarding new team members
- Legal/contractual requirements

**WHAT TO DO INSTEAD:**
- ADD new sections at the bottom
- ADD work log entries
- ADD updated status in frontmatter
- ADD new research findings
- NEVER touch existing content below the frontmatter

**Example:**
```markdown
---
status: "Done"
updated: "2026-08-13"
---

# Original content here — NEVER DELETE THIS

## Old research notes — KEEP THESE

## Work Log
| Date | Status | Notes |
|------|--------|-------|
| 2026-08-12 | Created | Initial ticket |
| 2026-08-13 | Done | Completed implementation |

## Additional Context (added later)
[New findings, decisions, etc.]
```

## Ticket Namespaces

| Prefix | Namespace | Project Folder | Description |
|--------|-----------|----------------|-------------|
| `<PREFIX>-XXX` | `<namespace>` | `thoughts/<project>/` | Project-specific namespace |

## Ticket Status Flow

```
Backlog → Planned → Ready → In Progress → Submitted for Review → In Review → Approved → Done
                                           ↘ Changes Requested → In Progress
                                           ↘ Reject → Blocked
```

| Status | Color | Description |
|--------|-------|-------------|
| **Backlog** | Gray | Initial state, not yet planned |
| **Planned** | Blue-gray | Planned for upcoming sprint |
| **Ready** | Light blue | Ready to be picked up |
| **In Progress** | Blue | Currently being worked on |
| **Submitted for Review** | Yellow | Awaiting CTO/Lead review |
| **In Review** | Yellow | Under active review |
| **Approved** | Green | Review passed, ready for done |
| **Done** | Green | Completed and merged |
| **Blocked** | Red | Blocked by dependency/issue |
| **Changes Requested** | Orange | Review requested changes, back to work |

## Ticket Naming Convention

### File Name

```
<NAMESPACE>-<NNN>-<UPPERCASE-DESCRIPTION-WITH-DASHES>.md
```

Examples:
- `PROJ-044-IDEAS-PRIORITIZATION-BOARD.md`
- `PROJ-049-SELF-UPDATING-INSTALLER.md`
- `TEAM-001-SOME-FEATURE.md`
- `SYS-001-SOME-FEATURE.md`

### Finding the Next Number

```Bash
ls thoughts/<project-slug>/shared/tickets/<PREFIX>-*.md
```

Take the highest number, increment by 1. If no tickets exist, start at `001`.

### Storage Location

- Shared tickets (active): `thoughts/<project-slug>/shared/tickets/<category>/<ID>-<description>.md`
- Shared tickets (done): `thoughts/<project-slug>/shared/tickets/done/<ID>-<description>.md`
- Personal tickets: `thoughts/<project-slug>/<dev>/tickets/<DEV>-<XXX>-<description>.md`

**Category subdirectories**: `frontend/`, `backend/`, `infrastructure/`, `devops/`, `security/`, `architecture/`, `docs/`, `testing/`, `ai-tools/`

### Frontmatter

```yaml
---
title: "[<PREFIX>-<NNN>] <Descriptive Title>"
type: "Feature" | "Bug" | "TechDebt" | "Epic" | "Improvement"
priority: "Critical" | "High" | "Medium" | "Low"
status: "Backlog" | "Planned" | "Ready" | "In Progress" | "Submitted for Review" | "In Review" | "Approved" | "Done" | "Blocked" | "Changes Requested"
assignee: ""
reporter: "@username"
project: "<PROJECT>"
namespace: "<namespace>"
category: "feature" | "bug" | "infrastructure" | "compliance" | "system"
parent_ticket: ""
shared_tickets: "[]"
pr_url: ""
github_issue: ""
---
```

### Template

Use `thoughts/shared/tickets/ticket-template.md`.

## Audit Utility

A ticket audit script is bundled at `assets/audit-tickets.js`. Run it to validate all tickets across namespaces for frontmatter compliance:

```bash
deno run -A assets/audit-tickets.js
```

This checks every ticket file for required frontmatter fields, correct formatting, and file naming. Use it before submitting tickets for review or after batch operations.

## Production-Ready Standard

Every ticket's acceptance criteria **must** include:

- **No mock data** — all endpoints, queries, and components work against real data. Mocks only in test suites.
- **Error handling** — every external call, DB query, and user input validated and handled.
- **Observability** — structured logging, metrics, or traces for non-trivial operations.
- **Security** — RBAC, Economics Shield, audit logging per `wow_access_control`.
- **Edge cases** — empty states, timeouts, rate limits, malformed input handled.
- **Tests** — failure modes covered, not just happy path.

If a ticket's AC don't cover these, add them.

## Core Commands

### `/work <ticket-id>`
Start working on a ticket. Updates status to "In Progress", creates a work session context.

**Steps:**
1. Find ticket file in `shared/tickets/<category>/` or `shared/tickets/` (fallback)
2. Update frontmatter: `status: "In Progress"`
3. Create work session context
4. Log work start in ticket's Work Log section

### `/complete <ticket-id>`
Mark a ticket as done. **CRITICAL: Moves ticket file to `done/` subdirectory.**

**Steps:**
1. Find ticket file: `thoughts/<project-slug>/shared/tickets/<category>/<ticket-id>*.md` or `thoughts/<project-slug>/shared/tickets/<ticket-id>*.md`
2. Update frontmatter: `status: "Done"`, `completed: "YYYY-MM-DD"`
3. Move file: `git mv <source> thoughts/<project-slug>/shared/tickets/done/<filename>`
4. Create `done/` directory if it doesn't exist
5. If review is required, moves to "Submitted for Review" instead (no file move)
6. Checks off linked TODO checkboxes in `thoughts/<project-slug>/shared/tickets/TODO.md`

**Example:**
```bash
# Before
thoughts/<project>/shared/tickets/backend/TEAM-045-AUTH-FIX.md

# After /complete TEAM-045
thoughts/<project>/shared/tickets/done/TEAM-045-AUTH-FIX.md
```

### `/sync team`
Show team dashboard: all tickets grouped by owner, status, blockers, dependencies.

### `/sync skills`
Sync all available skills to all configured frontends.

### `/ticket create`
Interactive ticket creation wizard. Prompts for:
- Title, type, priority, namespace
- Assignee, project, category
- Context, requirements, technical notes, success criteria

**Ticket creation path:**
```
thoughts/<project-slug>/shared/tickets/<category>/<ID>-<description>.md
```

**Auto-creates category subdirectory** if it doesn't exist (e.g., `backend/`, `frontend/`, `infrastructure/`)

## Available Tools

### `list_tickets`
List tickets with filtering.
Parameters:
- `namespace` (optional): Filter by namespace
- `status` (optional): Filter by status
- `assignee` (optional): Filter by assignee
- `project` (optional): Filter by project
- `category` (optional): Filter by category
- `role` (optional): Filter by required role

### `get_ticket`
Get full ticket metadata.
Parameters:
- `ticket_id` (required): The ticket ID (e.g., "TKT-001")

### `update_ticket`
Update ticket status and metadata.
Parameters:
- `ticket_id` (required): The ticket ID
- `status` (optional): New status
- `assignee` (optional): New assignee
- `blockers` (optional): Array of blocking ticket IDs
- `unblocks` (optional): Array of unblocked ticket IDs
- `pr_url` (optional): Link to GitHub PR

### `link_todo_to_ticket`
Bind a TODO.md section to a ticket ID.
Parameters:
- `ticket_id` (required): The ticket ID
- `section` (required): The section header in TODO.md
- `owner` (required): Developer ID owning the task

### `submit_for_review`
Submit completed work for CTO review.
Parameters:
- `ticket_id` (required): The ticket ID
- `pr_url` (optional): GitHub PR URL

### `cto_review_action`
_review_action
CTO reviews submitted work.
Parameters:
- `ticket_id` (required): The ticket ID
- `action` (required): "approve" | "request-changes" | "reject"
- `comments` (optional): Review comments

### CTO Review Flow (Dashboard Integration)

The WayOfTeams provides a dedicated **Review Queue** view for tickets awaiting CTO review:

1. **Submit for Review**: When developer sets status to "In Review" (or uses `/complete` which auto-submits if review required), ticket appears in Review Queue
2. **CTO Notification**: CTO sees ticket in Review Queue with "Approve", "Request Changes", "Reject" buttons
3. **Review Actions**:
   - **Approve**: Status → "Approved" → Auto-transition to "Done"
   - **Request Changes**: Status → "Changes Requested" → Auto-transition back to "In Progress"
   - **Reject**: Status → "Blocked" with review comments as reason
4. **Review Comments**: CTO can add comments that are stored in ticket frontmatter (`reviewComments`, `reviewedBy`, `reviewedAt`)

The dashboard store has `updateTicketReview` action that handles this flow.

### `sync_personal_todos`
Regenerate personal TODO.md for all developers from shared ticket assignments.

## Ticket Storage (per project, from harness.json project_slug)

Tickets are stored as markdown files in:
- `thoughts/<project-slug>/shared/tickets/<category>/<ID>-<description>.md` (shared tickets)
- `thoughts/<project-slug>/<dev>/tickets/<DEV>-<XXX>-<description>.md` (personal tickets)

Each ticket follows the template in `thoughts/shared/tickets/ticket-template.md` (cross-project template at f-rr-d root).

## Hierarchical Linking

- Personal tickets reference parent shared ticket via `parent_ticket` frontmatter
- Shared tickets reference personal sub-tasks via `sub_tasks` array
- Personal TODO.md auto-generates from assigned shared tickets

## Done Lifecycle

When a ticket is marked as Done, move it to the `done/` subdirectory:

### Moving Tickets to Done
```bash
# Move shared ticket to done/
mv thoughts/<project>/shared/tickets/<category>/<TICKET-ID>.md \
   thoughts/<project>/shared/tickets/done/

# Move personal ticket to done/
mv thoughts/<project>/<dev>/tickets/<TICKET-ID>.md \
   thoughts/<project>/<dev>/tickets/done/
```

### Creating the done/ Directory
If `done/` doesn't exist, create it:
```bash
mkdir -p thoughts/<project>/shared/tickets/done/
```

### `/done <ticket-id>` Command
1. Find ticket file: `thoughts/<project>/shared/tickets/<category>/<ticket-id>*.md`
2. Update frontmatter: `status: "Done"`, `completed: "YYYY-MM-DD"`
3. Move file to `done/` subdirectory
4. Create `done/` directory if it doesn't exist

### `/done-plan <plan-path>` Command
1. Find plan file
2. Update plan with completion notes
3. Move to `thoughts/<project>/shared/plans/done/` or `thoughts/plans/done/`

## Code Traceability

When creating or updating tickets, add traceability references to code changes:

### Reference Format
```
[<PREFIX>-<NNN>] <brief description>
```

### Placement
- Add BEFORE the changed line in code files
- Every modified file should have at least one reference

### Examples
```typescript
// [AIH-192] Add WayOfTeams MCP integration
const mcpClient = new WayOfTeamsMCP();
```

```python
# [AIH-191] Validate ticket frontmatter on creation
def validate_frontmatter(ticket):
```

### Querying
```bash
# Find all code for a ticket
grep -r "AIH-192" --include="*.ts" --include="*.py"

# Find which tickets touched a file
grep -l "AIH-" install.ts
```

## Notification Integration

When updating ticket status or managing tickets, mark related WayOfTeams notifications as Read via the notification API:

```bash
# Mark review notification as read after review action
curl -X POST http://localhost:6969/api/notifications \
  -H "Content-Type: application/json" \
  -d '{"action": "mark-read", "notificationId": "review-<TICKET_ID>"}'

# Mark update notification as read after status change
curl -X POST http://localhost:6969/api/notifications \
  -H "Content-Type: application/json" \
  -d '{"action": "mark-read", "notificationId": "update-<TICKET_ID>"}'
```

The notification IDs follow the format:
- `review-<TICKET_ID>` — for tickets in review queue
- `update-<TICKET_ID>` — for ticket status updates

This ensures the WayOfTeams bell badge reflects only genuinely unread notifications.

## WayOfTeams MCP Integration (Optional)

If WayOfTeams MCP is available, use it for ticket operations instead of local file manipulation:

### Check MCP Availability
```bash
# Check if WayOfTeams MCP is configured
grep -l "wayofteams" ~/.config/opencode/opencode.json ~/.claude/.mcp.json 2>/dev/null
```

### MCP Ticket Operations
When MCP is available, these operations can use WayOfTeams MCP tools:

| Operation | MCP Tool | Fallback |
|-----------|----------|----------|
| List tickets | `tickets_list` | Read from `thoughts/` |
| Get ticket | `tickets_get` | Read ticket file |
| Create ticket | `tickets_create` | Write to `thoughts/` |
| Update ticket | `tickets_update` | Edit ticket file |
| Notifications | `team_notifications` | curl localhost:6969 |

### MCP + File Hybrid Approach
1. Try MCP first: `tickets_create` via WayOfTeams
2. Also write to local `thoughts/` as backup
3. If MCP fails, fall back to file-only

**Always keep file-based operations as fallback.** MCP is additive, not a replacement.

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
