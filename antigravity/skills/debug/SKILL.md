---
name: debug
description: Debug issues during manual testing or implementation by examining logs, state, and git history using CLI tools.
allowed-tools: read, bash, grep, glob
---

# Debug

You are tasked with helping debug issues during manual testing or implementation. This command allows you to investigate problems by examining logs, state, and git history without editing files.

## Initial Response

When invoked WITH a context file:
```
I'll help debug issues with [file name]. Let me understand the current state.

What specific problem are you encountering?

* What were you trying to test/implement?
* What went wrong?
* Any error messages?

I'll investigate the logs, state, and git history to help figure out what's happening.
```

When invoked WITHOUT parameters:
```
I'll help debug your current issue.

Please describe what's going wrong:

* What are you working on?
* What specific problem occurred?
* When did it last work?

I can investigate logs, state, and recent changes to help identify the issue.
```

## Process Steps

### Step 1: Understand the Problem

1. **Read provided context** (plan, ticket, or error logs provided by the user).
2. **Quick state check**:
   - Identify the current git branch and recent commit history.
   - Check for uncommitted changes or untracked files (`git status`).

### Step 2: Investigate the Issue

Perform parallel investigation tasks without modifying the environment:

- **Analyze Recent Logs**: Locate relevant runtime or system logs. Focus on the most recent entries, filtering for `ERROR`, `CRITICAL`, or `Exception`.
- **Inspect Application State**: Check environment variables, running processes, or database connectivity if applicable.
- **Examine Git Diffs**: Inspect the exact lines changed in modified files (`git diff`) to pinpoint regressions.

### Step 3: Present Findings

```markdown
## Debug Report

### What's Wrong
[Clear, concise statement of the identified failure point]

### Evidence Found

**From Logs**:
- [Timestamped errors, stack traces, or anomalous entries]

**From Application State**:
- [Environment or state findings]

**From Git/Files**:
- [Specific lines of code recently changed or uncommitted modifications]

### Root Cause
[The most probable explanation of why the failure is occurring]

### Next Steps

1. **Try This First**:
   ```bash
   [Specific command, config adjustment, or diagnostic action]
   ```

2. **If That Doesn't Work**:
   - [Alternative troubleshooting approach]

### Can't Access?

Some context is outside my immediate environment:

* Browser console errors / Frontend UI state
* External third-party API dashboards
* System-level OS permissions

Would you like me to investigate a specific file or log layer further?
```

### Step 4: Save Debug Session to Docs

After presenting findings, save a debug session record to `docs/debug/` using the template at `fixes-templates/debug-template.md`:

```bash
mkdir -p docs/debug
```

Create a file named `docs/debug/YYYY-MM-DD-<short-description>.md` with:

```markdown
# Debug Session — YYYY-MM-DD — <Short Description>

## Problem Description
- **What was being tested/implemented**: <what>
- **What went wrong**: <problem>
- **When did it last work**: <last worked>
- **Error messages**: <errors>

## Evidence Found

**From Logs**:
- <log evidence>

**From Application State**:
- <state evidence>

**From Git/Files**:
- <git evidence>

## Root Cause
<root cause>

## Resolution
- **Fix applied**: <fix>
- **Files changed**: <files>
- **Verification**: <verification>

## Lessons Learned
- <lesson>
```

This creates a searchable debug history for the project. Reference `fixes-templates/debug-template.md` for the full template with placeholders.

## Important Notes

- **Read-Only Operations**: Do not write code or apply fixes. Focus entirely on diagnostic discovery.
- **Prevent Context Flooding**: Read files completely but handle large log streams using targeted filters (`grep`, `tail`) rather than dumping full files.
- **Always Require Context**: If the user's issue description is vague, ask targeted questions before running deep diagnostics.
