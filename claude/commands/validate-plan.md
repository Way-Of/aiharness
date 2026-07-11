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
- [ ] "What We're NOT DOING" section exists

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
- End with `[PLAN_VALIDATION_COMPLETE]`

## Context Reference

### Rules
- **Location**: `thoughts/global/rules/` (global) + `thoughts/<project>/rules/` (project-specific)
- **Precedence**: Project rules override global rules

### Templates
- **Location**: `thoughts/global/templates/`

### Knowledgebase
- **Location**: `thoughts/global/knowledge/`

## Agent Reference

### Available Agents
| Agent | Purpose | When to Use |
|-------|---------|-------------|
| `scout` | Fast codebase recon, file finding | Most code investigation tasks |
| `codebase_locator` | Find files by feature/task | Locating specific files |
| `codebase_pattern_finder` | Find similar implementations | Modeling after existing code |
| `planner` | Design implementation plans | Starting new features, refactoring |
| `codebase_analyzer` | Deep complex analysis | Tracing data flow through 5+ files |
| `coder` | Implementation and code generation | Turning plans into code |
| `reviewer` | Code review and quality checks | After implementation |
| `debugger` | Debug issues (read-only) | When something is broken |
| `thoughts_analyzer` | Extract insights from research | Analyzing research documents |
| `thoughts_locator` | Find documents in thoughts/ | Locating tickets, plans, docs |
| `web_search_researcher` | Research from web sources | Current info not in codebase |
| `netlify_troubleshooter` | Netlify CI/CD diagnostics | Build pipeline issues |
| `github` | GitHub operations (safe) | PRs, issues, branches, reviews |
