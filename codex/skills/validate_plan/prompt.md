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

## Rules

- **Read-Only**: Never modify files, only read and analyze
- **Block on Critical Issues**: If plan has critical flaws, block implementation
- **Allow Minor Issues**: Note minor issues but don't block
- **Be Specific**: Reference exact file paths and line numbers
- End with `[PLAN_VALIDATION_COMPLETE]`
