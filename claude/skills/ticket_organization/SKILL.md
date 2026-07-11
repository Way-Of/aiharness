---
name: ticket_organization
description: Proactively organize tickets across all namespaces — auto-audit, archive management, naming enforcement, orphan detection, cross-project consistency, TODO.md regeneration
allowed-tools: Read Grep Glob Bash Write Edit
---

# Ticket Organization Skill

You are an automated ticket organization agent. Your task is to keep tickets organized across all namespaces by auditing frontmatter compliance, archiving completed/deprecated tickets, enforcing naming conventions, detecting orphan files, and regenerating TODO.md.

## Design Principles

- **Pure agent-native**: All operations use Read/Grep/Glob/Bash/Write/Edit — no runtime deps
- **Dry-run safe**: Every operation checks `--dry-run` flag before modifying
- **Idempotent**: Running twice produces same result as running once
- **Composable**: Each tool works standalone; `organize_all` runs them in sequence

## Pre-Session Audit (Automatic)

Before any ticket-manager or ticket-executor operation, run a light audit:
1. Use Glob to find 5 random tickets across active namespaces
2. Read each ticket's frontmatter and validate required fields (title, type, priority, status, project, created)
3. Alert the user if issues are found and offer to run full `organize_all`
4. Do NOT auto-fix without user consent during pre-session

## Ticket Namespaces & Locations

| Namespace | Project Folder | Prefix | Ticket Dir |
|-----------|---------------|--------|------------|
| `<NAMESPACE>` | `thoughts/<project>/` | `<PREFIX>-` | `shared/tickets/` |

## Validation Rules

The following rules apply to ALL tools below. They are ported from the existing `audit-tickets.js` script.

### 1. Frontmatter Presence
File must start with `---` (YAML frontmatter delimiter).

### 2. Required Fields
Each ticket MUST have these frontmatter fields with non-empty values:
- `title` — Ticket title, typically `[<PREFIX>-<NNN>] <Description>`
- `type` — One of: Feature, Bug, TechDebt, Epic, Improvement, Compliance, Task
- `priority` — One of: Critical, High, Medium, Low
- `status` — One of: Backlog, Planned, Ready, In Progress, Submitted for Review, In Review, Approved, Done, Blocked, Changes Requested, Deprecated
- `project` — One of: Project-specific values
- `created` — Date in YYYY-MM-DD format

### 3. Enum Validation
- **Status**: Backlog, Planned, Ready, In Progress, Submitted for Review, In Review, Approved, Done, Blocked, Changes Requested, Deprecated
- **Priority**: Critical, High, Medium, Low
- **Type**: Feature, Bug, TechDebt, Epic, Improvement, Compliance, Task
- **Project**: Project-specific values
- **Namespace**: Project-specific values
- **Category**: feature, bug, infrastructure, compliance, system

### 4. Pipe-Syntax Detection
Flag any field containing ` | ` (space-pipe-space) — these are template placeholders that should be resolved.

### 5. Date Format Validation
Date fields (created, updated, reviewed_at, completed) must match `YYYY-MM-DD`.

### 6. Cross-Project Consistency
- Tickets must reside in their project's `shared/tickets/` directory

### 7. Deprecated Ticket Rules
Deprecated tickets must have:
- `deprecated: true`
- `deprecated_reason`: Non-empty string explaining why
- `deprecated_date`: YYYY-MM-DD
- `replaced_by`: Ticket ID of replacement (or empty if not replaced)

## Auto-Fix Rules

When `--auto-fix` is enabled, apply these repairs:

1. **Missing required fields** → Set to defaults:
   - title: Derive from filename (replace hyphens/underscores with spaces)
   - type: "Task"
   - priority: "Medium"
   - status: "Backlog"
   - project: Infer from filename prefix
   - namespace: Infer from filename prefix
   - created: Today's date
2. **Invalid status "Open"** → "Backlog", **"Closed"** → "Done"
3. **Pipe-syntax values** → Use first value (e.g., `"Feature | Bug"` → `"Feature"`)
4. **Missing title** → Extract from first `# Heading` in body, or derive from filename
5. **Outdated updated date** → Set to today

## Available Tools

### `audit_tickets`

Scan all namespaces for frontmatter compliance.

Parameters:
- `namespace` (optional): Limit scan to one namespace
- `--dry-run` (optional): Preview issues without modifying anything
- `--auto-fix` (optional): Auto-repair fixable issues

Execution steps:
1. Determine namespaces to scan (all 4 if not specified, or the requested one)
2. For each namespace, use Glob to find `thoughts/<project>/shared/tickets/*.md`
3. For each file found:
   a. Read the file with Read tool
   b. Extract YAML frontmatter (between first `---` and second `---`)
   c. Validate each field against the Validation Rules above
   d. Collect errors (hard violations) and warnings (soft issues like pipe-syntax)
   e. If `--auto-fix`: compute fixed values and track what changed
4. Generate a structured report (see Report Format below)
5. If `--auto-fix`: apply fixes by writing corrected frontmatter to each file

### `archive_tickets`

Move done/deprecated tickets to archive directories.

Parameters:
- `namespace` (optional): Limit to one namespace
- `--dry-run` (optional): Preview moves without executing

Archive tiers:
1. **`shared/tickets/done/`** — status is "Done", or status is "Deprecated" with a completed date
2. **`shared/tickets/deprecated/`** — deprecated=true but no replacement ticket specified
3. **`shared/tickets/legacy/`** — Old-format tickets pre-dating the standard frontmatter convention (no valid frontmatter found)

Execution steps:
1. List all tickets in `thoughts/<namespace>/shared/tickets/` (not in subdirectories)
2. For each ticket:
   a. Read frontmatter
   b. Determine target archive tier based on rules above
   c. If `--dry-run`: log the planned move
   d. If not dry-run: run `git mv <file> <archive-dir>/` via Bash
3. Update TODO.md after moves (delegate to `regenerate_todo`)

### `check_naming`

Validate all ticket filenames match convention.

Parameters:
- `namespace` (optional): Limit to one namespace
- `--dry-run` (optional): Preview violations without reporting

Convention: `<PREFIX>-<NNN>-<UPPERCASE-DASHED-DESC>.md`
- Prefix: Project-specific uppercase prefix
- NNN: Zero-padded 3+ digit number (e.g., 001, 042, 172)
- Description: UPPERCASE words separated by hyphens

Examples:
- `PROJ-001-LOGIN-FEATURE.md` ✓
- `proj-1-login.md` ✗ (lowercase prefix, no padding, lowercase desc)
- `TEAM-042-API-ENDPOINT.md` ✓
- `SYS-172-TICKET-ORGANIZATION-SKILL.md` ✓

### `detect_orphans`

Find files in personal developer folders with no matching ticket in shared/tickets/.

Parameters:
- `namespace` (optional): Limit to one namespace

Execution steps:
1. For each namespace, use Glob to find `thoughts/<project>/*/**/*.md` (developer folders)
2. Skip `shared/`, `global/`, `docs/`, `enforcement-ticket/` directories
3. For each file found:
   a. Extract ticket prefix+number from filename (e.g., `PROJ-042` from `PROJ-042-NOTE.md`)
   b. If prefix+number found, check if a matching file exists in `thoughts/<project>/shared/tickets/`
   c. If no match found, report as orphan with developer name and file path
4. Generate orphan report

### `regenerate_todo`

Rebuild TODO.md from current ticket state.

Parameters:
- `namespace` (optional): Limit to one namespace

Execution steps:
1. List all non-archived tickets in `thoughts/<project>/shared/tickets/*.md`
2. Group tickets by priority (Critical → High → Medium → Low)
3. Within each priority group, sort by status flow (Backlog → Planned → Ready → In Progress → Submitted for Review)
4. Format as markdown:
   ```markdown
   # TODO — <Project Name>
   
   ## Critical
   - [ ] [PROJ-042] Login Feature (In Progress)
   - [ ] [TEAM-001] Auth System (Backlog)
   
   ## High
   - [ ] [SYS-007] Sensor Calibration (Ready)
   
   ## Medium
   ...
   
   ## Low
   ...
   ```
5. Write to `thoughts/<project>/TODO.md`
6. If a ticket has `status: "Done"`, mark as `[x]` in Done section

### `organize_all`

Run all organization tools in sequence.

Parameters:
- `--dry-run` (optional): Preview all changes without modifying anything
- `--auto-fix` (optional): Auto-repair issues during audit

Execution order:
1. `audit_tickets` (with --auto-fix if specified)
2. `archive_tickets`
3. `check_naming`
4. `detect_orphans`
5. `regenerate_todo`

After completion, write a comprehensive report to `thoughts/<project>/shared/research/`.

## Report Format

After each organization run, write a structured report to:
`thoughts/<project>/shared/research/ticket-organization-<YYYY-MM-DD>.md`

```
# Ticket Organization Report — YYYY-MM-DD HH:MM

## Summary
- Namespaces audited: <list of namespaces>
- Tickets scanned: N
- Issues found: N (Critical: N, Warnings: N)
- Auto-fixed: N
- Archived: N
- Orphans detected: N
- Naming violations: N
- TODO.md regenerated: Y/N

## Issues by Namespace

### <Namespace>
| File | Issue | Severity |
|------|-------|----------|
| PROJ-042-LOGIN.md | Missing required field: assignee | Error |
| PROJ-001-AUTH.md | Pipe syntax in type: "Feature \| Bug" | Warning |

## Auto-fixes Applied
| File | Field | Old Value | New Value |
|------|-------|-----------|-----------|
| PROJ-042-LOGIN.md | status | Open | Backlog |

## Archive Moves
| File | From | To |
|------|------|----|
| PROJ-001-AUTH.md | shared/tickets/ | shared/tickets/done/ |

## Orphans Detected
| Developer | File | Matching Ticket |
|-----------|------|-----------------|
| dev-name | TEAM-099-personal-note.md | Not found in shared/tickets/ |
```

## Dry-Run Mode

All tools support `--dry-run`. When enabled:
- Perform all reads and computations
- Log what would change (file, field, old value → new value)
- Do NOT write any files, move any files, or run any git commands
- Prefix the report title with `[DRY RUN]`

## Auto-Fix Mode

Only `audit_tickets` supports `--auto-fix`. When enabled with that tool:
- Apply auto-fix rules (see Auto-Fix Rules above)
- Write corrected frontmatter to affected files
- Report all changes in the Auto-fixes Applied section
- Update the `updated` frontmatter field to today's date

## Integration Notes

- **Status changes**: Delegate to ticket-manager's `update_ticket` tool
- **Archive moves**: Use `git mv` via Bash (never `cp` + `rm`)
- **TODO.md regeneration**: Follow backlog-groomer patterns
- **Ordering**: Audit runs BEFORE any ticket-manager or ticket-executor operation (see Pre-Session Audit)

## Templates & Rules

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/templates/rules/` — coding standards, naming, security, testing, deployment rules
