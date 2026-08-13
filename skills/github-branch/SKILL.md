---
name: github_branch
description: "Create and manage GitHub feature branches from tickets. Ensures proper branch naming, ticket linking, and base branch selection."
allowed-tools: Read, Write, Edit, Bash, Git
---

# GitHub Branch Skill

Creates and manages feature branches for tickets with proper naming conventions and GitHub integration.

## Branch Naming Convention

```
<namespace>/<ticket-id>-<short-description>
```

Examples:
- `project/PROJ-084-feature-name`
- `service/SVC-001-user-auth`
- `infra/INF-003-pipeline-fix`

## Workflow

### 1. Create Branch from Ticket

```bash
# From ticket ID, auto-detect namespace and create branch
git checkout main
git pull origin main
git checkout -b project/PROJ-084-feature-name
```

### 2. Push Branch to Origin

```bash
git push -u origin project/PROJ-084-feature-name
```

### 3. Create PR (handled by github_pr skill)

Branch is now ready for PR creation.

## Available Tools

### `create_branch_from_ticket`
Create feature branch from ticket ID.
Parameters:
- `ticket_id` (required): Ticket ID (e.g., "PROJ-084")
- `description` (optional): Short description for branch name
- `base_branch` (optional): Base branch (default: "main")

### `push_branch`
Push branch to origin with upstream tracking.
Parameters:
- `branch_name` (required): Branch name
- `force` (optional): Force push (default: false)

### `sync_branch`
Sync feature branch with base branch.
Parameters:
- `branch_name` (required): Branch name
- `base_branch` (optional): Base branch (default: "main")

### `delete_branch`
Delete local and remote branch after merge.
Parameters:
- `branch_name` (required): Branch name
- `remote` (optional): Also delete remote (default: true)

## Integration

- Uses `ticket-manager` to get ticket details
- Branch name includes ticket ID for traceability
- Auto-sets upstream tracking on push
- Respects branch protection rules
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
