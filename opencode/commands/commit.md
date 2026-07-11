# Commit Changes

You are tasked with creating git commits for the changes made during this session.

## Process:

1. **Think about what changed:**
   - Review the conversation history and understand what was accomplished
   - Run `git status` to see current changes
   - Run `git diff` to understand the modifications
   - Consider whether changes should be one commit or multiple logical commits

2. **Plan your commit(s):**
   - Identify which files belong together
   - Draft clear, descriptive commit messages
   - Use imperative mood in commit messages
   - Focus on why the changes were made, not just what

3. **Present your plan to the user:**
   - List the files you plan to add for each commit
   - Show the commit message(s) you'll use
   - Ask: "I plan to create [N] commit(s) with these changes. Shall I proceed?"

4. **Execute upon confirmation:**
   - Use `git add` with specific files (never use `-A` or `.`)
   - Create commits with your planned messages
   - Show the result with `git log --oneline -n [number]`

## Important:
- **NEVER add co-author information or AI attribution**
- Commits should be authored solely by the user
- Do not include any "Generated with Claude" messages
- Do not add "Co-Authored-By" lines
- Write commit messages as if the user wrote them

## Remember:
- You have the full context of what was done in this session
- Group related changes together
- Keep commits focused and atomic when possible
- The user trusts your judgment - they asked you to commit

## Context Reference

### Rules
- **Location**: `thoughts/global/rules/` (global) + `thoughts/<project>/rules/` (project-specific)
- **Precedence**: Project rules override global rules
- **Categories**: coding-standards, naming-conventions, testing-requirements, security-guidelines, deployment-rules

### Templates
- **Location**: `thoughts/global/templates/`
- **Available**: ticket-template.md, knowledge-entry.md, todo-template.md, AGENTS.md.template, fixes/

### Knowledgebase
- **Location**: `thoughts/global/knowledge/`
- **Commands**: Use `knowledge` skill to store, fetch, search, list, stats

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
