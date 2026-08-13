---
name: implement-plan
description: Implement an approved technical plan from thoughts/plans/ with phase-by-phase execution, leveraging CLI tools for file interaction, command execution, and task management.
allowed-tools:
  - read
  - write
  - bash
  - grep
  - glob
  - todowrite
  - task
disable-model-invocation: true
---

# Implement Plan

You are tasked with implementing an approved technical plan from `thoughts/plans/`. These plans contain phases with specific changes and success criteria.

**Directory Structure:**
- `thoughts/tickets/` - Original feature requests and task descriptions
- `thoughts/plans/` - Implementation plans (the files you'll be executing)
- `thoughts/research/` - Supporting research and investigation notes

## Getting Started

When given a plan path:
- Read the plan completely and check for any existing checkmarks (- [x])
- Read the original ticket and all files mentioned in the plan
- **Read files fully** - never use limit/offset parameters
- Use `write_todos` to track your progress
- Start implementing if you understand what needs to be done

If no plan path provided, ask for one.

## Implementation Philosophy

Plans are carefully designed, but reality can be messy. Your job is to:
- Follow the plan's intent while adapting to what you find
- Implement each phase fully before moving to the next
- Verify your work makes sense in the broader codebase context
- Update checkboxes in the plan as you complete sections

If you encounter a mismatch:
- STOP and present the issue clearly:
  ```
  Issue in Phase [N]:
  Expected: [what the plan says]
  Found: [actual situation]
  Why this matters: [explanation]

  How should I proceed?
  ```

## Verification Approach

After implementing a phase:

### 1. Run Success Criteria Checks

Use technology-appropriate commands:

**Node.js/JavaScript**: `npm test`, `npm run lint`, `npm run build`
**Python**: `pytest`, `black --check .`, `mypy .`
**Go**: `go test ./...`, `golangci-lint run`, `go build`
**Rust**: `cargo test`, `cargo clippy`, `cargo build`
**Make-based**: `make test`, `make lint`, `make build`

### 2. Delegate Review to `reviewer`

After success criteria pass, **delegate to `reviewer`** agent to perform a thorough code audit:
- Reviews code against the plan's intent
- Identifies deviations, potential issues, and quality gaps
- Writes audit report for the phase

Address any issues found by `reviewer` before moving to the next phase.

### 3. Fix Issues and Update Progress

- Address any failures before moving to the next phase
- Update checkboxes in the plan file using the Edit tool
- Update your TodoWrite list

## If You Get Stuck

1. **Investigate First** - Read all relevant code completely
2. **Delegate to `scout`** for rapid recon of the code area you're stuck on
3. **Delegate to research agents** (e.g., `codebase_investigator`, `codebase_locator`, `codebase_pattern_finder`) for deeper targeted help
4. **Present Issues Clearly** - Don't guess, ask for clarification

## Resuming Work

If the plan has existing checkmarks:
- Trust that completed work is done correctly
- Pick up from the first unchecked item
- Verify previous work only if something seems off

## Key Principles

1. **Deep Understanding Before Action** - Read files completely
2. **Follow Intent, Not Just Instructions** - Adapt to reality
3. **Maintain Quality** - Run verification commands
4. **Communicate Clearly** - Update checkboxes and todos
5. **Keep Momentum** - Don't get stuck on minor details

## Critical: Code Traceability (MANDATORY)

**Every code change MUST include a ticket reference comment. This is NOT optional.**

### Format
```typescript
// [AIH-192] Add WayOfTeams MCP integration
const mcpClient = new WayOfTeamsMCP();
```

```python
# [AIH-191] Validate ticket frontmatter on creation
def validate_frontmatter(ticket):
```

### Rules
- Format: `[<PREFIX>-<NNN>] <brief description>`
- Place BEFORE the changed line
- Every modified file must have at least one reference
- Use the ticket ID from the ticket you're implementing

### Why This Matters
- Traces what code was supposed to do (read the ticket)
- Verifies code matches acceptance criteria
- Finds all code related to a specific ticket
- Debugging: "why was this changed?" → read the ticket

## Critical: Acceptance Criteria for ALL Components

When implementing, verify acceptance criteria for:

### Skills
- [ ] All 77 canonical skills present in all 6 tools
- [ ] Frontmatter `name:` matches directory name
- [ ] Content identical across tools (modulo naming)

### Agents
- [ ] All 14 canonical agents present in all 6 tools
- [ ] Content identical across tools

### Commands/Prompts
- [ ] All 24 canonical commands present in opencode/claude/pi/wocode/codex
- [ ] Antigravity uses .toml format (skip validation)
- [ ] Content identical across tools (modulo format)

### After Implementation
```bash
# Sync all components to all tools

# Verify consistency
```

## Critical: Never Rewrite Ticket Context

**TICKETS ARE IMMUTABLE HISTORY.** You can ONLY ADD to tickets. NEVER:
- ❌ Rewrite ticket content
- ❌ Remove old context, notes, or decisions
- ❌ Simplify or condense ticket history
- ❌ Delete work logs, research notes, or technical details
- ❌ Replace old information with new (ADD new info, keep old)

**WHY:** Old context may be needed for debugging, auditing, onboarding, or legal requirements.

## Critical: Update Tickets and Plans When Done

**When implementation is complete, ALWAYS update the ticket and plan:**

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

## Critical: Fetch Context from Tickets/Plans

Before implementing, READ the ticket and plan:
- **Ticket**: `thoughts/<project>/shared/tickets/<TICKET-ID>.md` — requirements, acceptance criteria
- **Plan**: `thoughts/<project>/shared/plans/<PLAN-NAME>.md` — implementation phases, file changes
- **Search**: `grep -r "<TICKET-ID>" --include="*.ts"` — find related code

The ticket contains what to build. The plan contains how to build it. Never implement without reading both.

## Context Reference

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
- **Knowledge**: `thoughts/global/knowledge/` — stored knowledge base, searchable via `knowledge` skill
