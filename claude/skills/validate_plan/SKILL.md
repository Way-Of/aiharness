---
name: validate_plan
description: Validate an implementation plan before coding begins — checks completeness, feasibility, paths, and rules compliance.
allowed-tools: Read, Bash, Grep, Glob, Task
disable-model-invocation: true
---

# Validate Plan

Validate that an implementation plan is complete, feasible, and ready for implementation.

## When to Use

- After `/create_plan` finishes and before `/implement_plan` starts
- When reviewing a plan created by someone else
- Before starting work on any plan

## Validation Checklist

### 1. Plan Completeness
- [ ] All phases have clear scope
- [ ] All files to modify are listed with paths
- [ ] Success criteria are defined per phase
- [ ] No open questions remain
- [ ] "What We're NOT Doing" section exists

### 2. Path Verification
- [ ] All referenced files exist (use `ls`/`find`)
- [ ] All directories exist or will be created
- [ ] No hardcoded paths that should be dynamic

### 3. Rules Compliance
- [ ] Read applicable rules from `thoughts/<project>/rules/` and `thoughts/global/rules/`
- [ ] Plan respects coding standards
- [ ] Plan respects naming conventions
- [ ] Plan respects security guidelines

### 4. Feasibility Check
- [ ] Changes are possible with current codebase patterns
- [ ] No circular dependencies introduced
- [ ] No breaking changes without migration plan
- [ ] Dependencies are available

### 5. Risk Assessment
- [ ] Risks are identified and documented
- [ ] Mitigation strategies exist for high-risk items
- [ ] Rollback plan exists if needed

## Output Format

```markdown
## Plan Validation Report: [Plan Name]

### Verdict: ✅ APPROVED / ⚠️ CONDITIONS / ❌ REJECTED

### Completeness: ✅/⚠️/❌
- [Status of each check]

### Path Verification: ✅/⚠️/❌
- [Files found/missing]

### Rules Compliance: ✅/⚠️/❌
- [Rules checked, any violations]

### Feasibility: ✅/⚠️/❌
- [Assessment]

### Risks: ✅/⚠️/❌
- [Risk summary]

### Conditions (if applicable):
- [What must be resolved before implementation]

### Recommendation:
- [Go / Fix first / Reconsider approach]
```

## Relationship to Other Commands

Recommended workflow:
1. `/create_plan` - Create implementation plan
2. **`/validate_plan`** - Validate plan before implementation (THIS COMMAND)
3. `/implement_plan` - Execute the implementation
4. `/validate_implementation` - Verify implementation correctness
5. `/commit` - Create atomic commits

## Rules

- **Read-Only**: Never modify files, only read and analyze
- **Block on Critical Issues**: If plan has critical flaws, block implementation
- **Allow Minor Issues**: Note minor issues but don't block
- **Be Specific**: Reference exact file paths and line numbers
- End with `[PLAN_VALIDATION_COMPLETE]`

## Context Reference

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
- **Knowledge**: `thoughts/global/knowledge/` — stored knowledge base, searchable via `knowledge` skill
