# AI Engineering Harness

> **For AI Agents**: This document provides structured reference data for AI coding assistants. For human-readable documentation, see [README.md](README.md).

## Quick Reference

**Purpose**: Configuration harness for AI coding agents with reusable prompts, agents, and workflows.

**Supported Tools**: OpenCode, Claude Code, Pi, Wo Coder, Antigravity, Codex

**Installation**: `./setup.sh <tool>` (macOS/Linux) or `.\install.ps1 -Tool all` (Windows/PowerShell)

## Repository Structure

```
ai-engineering-harness/
├── skills/             # CANONICAL SKILLS (single source of truth)
│   ├── skill-registry.json   # Registry of all available skills
│   ├── ticket-manager/       # Ticket Manager (PROJ-013)
│   ├── team-setup/           # Team Setup (PROJ-018)
│   ├── skill-auto-update/    # Skill Auto-Update (PROJ-014)
│   ├── auto-ticket-creator/  # Auto-Ticket Creation (PROJ-017)
│   ├── docs-sync-updater/    # Docs Sync Updater (PROJ-022)
│   ├── cto-dashboard/        # CTO Dashboard (PROJ-019)
│   ├── skill-adapter/        # Skill Adapter (PROJ-020)
│   └── help-command/         # /help Command (PROJ-024)
├── agents/             # CORE AGENTS registry + definitions
│   ├── agent-registry.json   # Registry of all core agents
│   ├── codebase_analyzer.md
│   ├── codebase_locator.md
│   ├── codebase_pattern_finder.md
│   ├── thoughts_analyzer.md
│   ├── thoughts_locator.md
│   └── web_search_researcher.md
├── opencode/           → ~/.config/opencode/
│   ├── agents/         # 6 agents (snake_case)
│   ├── commands/       # 11 slash commands
│   ├── skills/         # 25+ skills (auto-triggered)
│   └── opencode.json   # MCP configuration
├── claude/             → ~/.claude/
│   ├── agents/         # 6 agents (snake_case)
│   ├── skills/         # 35+ skills (13 manual + 22+ auto)
│   ├── .mcp.json       # MCP configuration
│   └── settings.json   # Settings schema
│   ├── agents/         # 6 agents (snake_case)
│   ├── commands/       # 14 commands (TOML format)
│   └── skills/         # 33+ skills (auto-triggered)
├── pi/                 → ~/.pi/agent/
│   ├── agents/         # 6 agents (kebab-case)
│   ├── prompts/        # 11 prompt templates (Pi's commands)
│   ├── skills/         # 31+ skills (auto-triggered)
│   └── extensions/     # subagent extension (multi-agent workflows)
├── wocode/            → ~/.wocode/agent/
│   ├── agents/         # 13 agents (kebab-case, incl. subagent agents)
│   ├── extensions/     # subagent, open-editor, theme-cycler
│   ├── packets/        # web-access extension code
│   ├── prompts/        # 24 prompt templates (kebab-case)
│   ├── skills/         # 79 skills (kebab-case)
│   ├── themes/         # 12 themes (kebab-case)
│   ├── README.md       # Tool docs
│   └── wocode.json    # MCP configuration
├── codex/              → ~/.codex/
│   ├── agents/         # 7 agents (snake_case)
│   ├── skills/         # 50+ skills (auto-triggered)
│   └── README.md       # Platform notes
└── thoughts/           # Context engineering artifacts
    ├── shared/tickets/ # Work items (organized by category)
    ├── shared/plans/   # Implementation plans
    ├── shared/research/# Research documents
    └── global/         # Cross-repo concerns
```

## Commands & Skills

| Command | OpenCode | Claude | Pi | Wo Code | Antigravity | Codex | Type | Description |
|---------|:--------:|:------:|:------:|:--:|:--------:|:-----------:|:----:|------|-------------|
| `/init_harness` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Initialize harness (creates AGENTS.md/CLAUDE.md + thoughts/) |
| `/create_plan` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Generate implementation plan from ticket |
| `/implement_plan` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Execute approved plan phase-by-phase |
| `/validate_plan` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Verify implementation against plan |
| `/commit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Create well-structured git commits |
| `/debug` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Investigate issues during testing |
| `/debug_k8s` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Debug Kubernetes (prefers MCP, falls back to kubectl) |
| `/research_codebase` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Comprehensive codebase research |
| `/validate_telemetry` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Validate local telemetry against a narrative spec |
| `/work <ticket-id>` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Start working on a ticket (requires ticket-manager) |
| `/complete <ticket-id>` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Complete a ticket, syncs status (requires ticket-manager) |
| `/sync team` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Show team dashboard (requires ticket-manager) |
| `/help` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Unified help system (requires help-command) |
| `/sync skills` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Manual | Sync all skills to all frontends (requires skill-auto-update) |
| `ticket_manager` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Manage tickets across namespaces with full lifecycle |
| `team_setup` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Initialize and manage team configuration |
| `skill_auto_update` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Auto-discover and sync skills across frontends |
| `auto_ticket_creator` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Monitor and auto-create tickets from changes |
| `docs_sync_updater` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Fetch latest docs and auto-update skill configs |
| `cto_dashboard` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | CTO dashboard with review queue and developer progress |
| `skill_adapter` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Platform-specific skill loading and format adapters |
| `help_command` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Unified /help across all platform frontends |
| `observability_driven_development` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Design the trace before the feature; local OTel feedback loop |
| `git_commit_helper` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Triggers on "commit" keywords |
| `pr_description_generator` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Triggers when creating PRs |
| `experimental_pr_workflow` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Formalizes experimental work |
| `interview` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Stress-test plans via relentless user interview |
| `improve_codebase_architecture` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Find architectural friction, propose deep-module refactors |
| `prd_to_issues` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Break a PRD into vertical-slice issue files |
| `tdd` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Red-green-refactor TDD discipline |
| `write_a_prd` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Generate a PRD from a client brief |
| `womono_version_updater` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Bump WoM harness version across all files and tools |
| `build_pi_agent` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Build Pi agent definitions with frontmatter format |
| `pi_cli` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Pi CLI expert — CLI flags, subcommands, output modes |
| `pi_config` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Pi configuration — settings, providers, models, packages |
| `build_pi_extension` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Build Pi extensions — tools, events, commands, providers |
| `pi_keybindings` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Pi keyboard shortcuts — registerShortcut, key IDs |
| `pi_orchestrate` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Orchestrate Pi domain experts to research and build Pi components |
| `pi_prompts` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Pi prompt templates — .md format, arguments, /template |
| `build_pi_skill` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Build Pi skills — SKILL.md format, frontmatter, validation |
| `pi_themes` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Pi themes — JSON, 51 color tokens, vars, hex/256-color |
| `pi_tui` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Auto | Pi TUI — built-in & custom components, keyboard, widgets |

**Naming**: OpenCode, Pi, and Wo Coder use kebab-case; Claude, Codex, and Antigravity use snake_case.

## Agents

All agents are shared across all six tools:

| Agent | OpenCode | Claude | Pi | Wo Coder | Antigravity | Codex | Purpose |
|-------|:--------:|:------:|:------:|:--:|:--------:|:-----------:|:----:|--------|
| `scout` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Find files, understand code, quick analysis — use this for most code investigation tasks |
| `codebase_locator` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Find files/directories by feature or task |
| `codebase_pattern_finder` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Discover similar implementations and patterns |
| `planner` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Design implementation plans before coding — use when starting a new feature, refactoring, or complex change |
| `codebase_analyzer` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Deep analysis of complex systems — trace data flow through 5+ files, understand intricate interactions |
| `thoughts_analyzer` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Extract insights from research documents |
| `thoughts_locator` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Discover documents in thoughts/ directory |
| `web_search_researcher` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Research information from web sources |
| `coder` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Implementation and code generation |
| `reviewer` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Code review and quality checks |
| `debugger` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Debug issues during testing — examines logs, state, git history to find root causes (read-only) |
| `github` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | GitHub operations — creates PRs, branches, issues, reviews. ALWAYS asks before destructive actions |
| `netlify_troubleshooter` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Netlify CI/CD diagnostics and build pipeline |

## Workflow

```
Ticket → /create_plan → /validate_plan → /implement_plan → /validate_implementation → [/validate_telemetry] → /commit
```

1. Create ticket in `thoughts/shared/tickets/` (use ticket-template.md)
2. Run `/create_plan <ticket-path>` to generate plan
3. Run `/implement_plan <plan-path>` to execute
4. Run `/validate_plan` to verify
5. (Optional, telemetry-bearing features only) Run `/validate_telemetry [<spec>]` to verify the trace narrative
6. Run `/commit` to commit changes

## MCP Configuration

| Tool | File | Disable Syntax |
|------|------|----------------|
| OpenCode | `opencode.json` | `"enabled": false` |
| Claude Code | `.mcp.json` | `"disabled": true` |
| Pi | N/A | N/A |
| Wo Coder | `wocode.json` | `"enabled": false` |
| Antigravity | `antigravity.json` | `"enabled": false` |
| Codex | N/A | N/A |

### Available MCP Servers

| Server | Endpoint | Tools | Auth | Status |
|--------|----------|-------|------|--------|
| `kubernetes` | local (npx) | Cluster management | None | Disabled by default |
| `aspire-dashboard` | `http://localhost:18891` | .NET Aspire | None | Disabled by default |
| `wayofteams` | `https://teamsapp.zerwiz.org/mcp` | 41 tools (tickets, standups, knowledge, rules, memory) | Bearer JWT | **Requires paid subscription** |
| `anchor` | `http://localhost:42777/mcp` | 11 tools (memory, context, PR review) | API key | Use via WayOfTeams (direct is STDIO-only) |

### WayOfTeams MCP Integration

WayOfTeams provides 41 MCP tools for team-aware AI agents:
- **Tickets**: `tickets_list`, `tickets_get`, `tickets_create`, `tickets_update`
- **Standups**: `standup_get`, `standup_create`
- **Knowledge**: `knowledge_list/search/get/create`, `rules_list/get/create/update`
- **Memory**: `memory_store/search/get/list/delete`, `memory_update`, `anchors_*`, `context_inject`, `pr_review_context`
- **Team**: `team_skills`, `team_notifications`, `thoughts_read/search`

**Auth**: Bearer JWT from GitHub login. Set `WAYOFTEAMS_MCP_TOKEN` env var.
**Config**: See `skills/wayofteams-mcp/SKILL.md` for per-tool config examples.

### Anchor Memory Integration

Anchor provides persistent semantic memory via WayOfTeams MCP:
- Store decisions, patterns, invariants across sessions
- Context injection for new sessions
- PR review context with decision rationale

**Config**: See `skills/anchor-memory/SKILL.md` for details.

## Code Traceability

Every code change MUST include a ticket reference comment. This enables:
- Tracing what a piece of code was supposed to do (read the ticket)
- Verifying code matches the ticket's acceptance criteria
- Finding all code related to a specific ticket
- Understanding why a change was made (ticket context)

### Reference Format
```
[<PREFIX>-<NNN>] <brief description>
```

### Placement
- Add BEFORE the changed line in code files
- Every modified file must have at least one reference

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

### Fetching Context from Tickets/Plans
- **Ticket**: `thoughts/<project>/shared/tickets/<TICKET-ID>.md` — requirements, acceptance criteria
- **Plan**: `thoughts/<project>/shared/plans/<PLAN-NAME>.md` — implementation phases, file changes
- **Search**: `grep -r "<TICKET-ID>" --include="*.ts"` — find related code

## Tool-Specific Notes

### OpenCode
- Project memory: `AGENTS.md` (generated by `/init`)
- Commands and skills are separate directories
- Agent naming: Uses snake_case convention
- Config location: `~/.config/opencode/`

### Claude Code
- Project memory: `CLAUDE.md` (generated by `/init`)
- Commands implemented as skills with `disable-model-invocation: true`
- Agent naming: Uses snake_case convention
- Config location: `~/.claude/`
- Supports `.claude/rules/` for modular instructions

## Available Skills & Commands

> **Full catalog:** See `thoughts/wayofmono/docs/AI-Engineering-Harness-Skills-Catalog.md` for detailed descriptions of all 49 skills, 12 agents, and 5 commands/prompts.

### Skills (auto-triggered by the AI Engineering Harness)
- agents-md-manager
- alliner-compliance-check
- auto-ticket-creator
- backlog-groomer
- build-auto-ticket-creator
- build-backlog-groomer
- build-tool
- build-tool-agent
- build-tool-cli
- build-tool-config
- build-tool-extension
- build-tool-keybindings
- build-tool-prompts
- build-tool-skill
- build-tool-themes
- build-tool-tui
- commit
- create-plan
- debug
- document-generation
- fixes-bump
- fixes-create
- fixes-manager
- git-commit-helper
- github-branch
- github-issue
- github-pr
- github-release
- github-review
- github-sync
- help-command
- implement-plan
- improve-codebase-architecture
- init-harness
- knowledge
- postmortem-manager
- pr-description-generator
- prd-to-issues
- research-codebase
- runbook-manager
- sales
- self-documentation
- session-export
- standup
- tdd
- ticket-executor
- ticket-manager
- usage-rules
- validate-plan
- validate-podman
- write-a-prd

### Commands (slash commands from the AI Engineering Harness)
- create-plan
- implement-plan
- standup
- ticket-create
- validate-plan

### Agents (available from the AI Engineering Harness)
- scout
- codebase_locator
- codebase_pattern_finder
- planner
- codebase_analyzer
- thoughts_analyzer
- thoughts_locator
- web_search_researcher
- coder
- reviewer
- debugger
- github
- netlify_troubleshooter

## GitHub Skills Agent Directory

Use these skills for all GitHub operations. Never use raw `gh` or `git` commands for operations covered by these skills.

#### Agent: GitHub Branch (github-branch)
- **Identifier:** `github_branch_v1`
- **Primary Runtime:** Platform-native
- **Core Responsibility:** Create and manage feature branches from tickets with proper naming, ticket linking, and base branch selection
- **Inputs:** Ticket ID, branch name, namespace
- **Outputs:** Feature branch created, pushed to origin
- **Constraints:** Never push directly to `main`; always create feature branches; never force-push

#### Agent: GitHub Issue (github-issue)
- **Identifier:** `github_issue_v1`
- **Primary Runtime:** Platform-native
- **Core Responsibility:** Create, manage, and link GitHub Issues with f-rr-d tickets; bi-directional sync
- **Inputs:** Ticket details, namespace, labels
- **Outputs:** GitHub Issue created/updated, synced with f-rr-d
- **Constraints:** Must maintain bi-directional link between GitHub Issue and f-rr-d ticket; never close tickets without verification

#### Agent: GitHub PR (github-pr)
- **Identifier:** `github_pr_v1`
- **Primary Runtime:** Platform-native
- **Core Responsibility:** Create, manage, and review Pull Requests with ticket linking, templates, and review workflow
- **Inputs:** Branch name, ticket reference, PR template
- **Outputs:** PR created, linked to ticket, ready for review
- **Constraints:** Never merge own PRs; always use PR templates; must reference the ticket in the PR body

#### Agent: GitHub Release (github-release)
- **Identifier:** `github_release_v1`
- **Primary Runtime:** Platform-native
- **Core Responsibility:** Create releases with changelog generation, version tagging, and automated publishing
- **Inputs:** Version number, changelog entries, target branch
- **Outputs:** GitHub Release created, tag pushed
- **Constraints:** Must validate version is bumped in all required files; never delete existing releases

#### Agent: GitHub Review (github-review)
- **Identifier:** `github_review_v1`
- **Primary Runtime:** Platform-native
- **Core Responsibility:** Review Pull Requests with structured feedback, approval workflow, and CTO Dashboard integration
- **Inputs:** PR URL, review criteria
- **Outputs:** Review submitted (approve/changes-requested/reject), CTO Dashboard notified
- **Constraints:** Never self-review; must verify against ticket acceptance criteria; only CTO can dismiss reviews

#### Agent: GitHub Sync (github-sync)
- **Identifier:** `github_sync_v1`
- **Primary Runtime:** Platform-native
- **Core Responsibility:** Sync feature branches with base branch, resolve conflicts, and manage branch lifecycle
- **Inputs:** Feature branch name, base branch name
- **Outputs:** Branch synced, conflicts resolved, CI re-triggered
- **Constraints:** Never force-push; always pull --rebase before syncing; must run CI after conflict resolution

## GitHub Workflow

All GitHub operations follow this sequence:
1. `github-branch` — Create a feature branch from a ticket
2. `github-pr` — Create a Pull Request from the branch
3. `github-review` — Request review, address feedback
4. `github-sync` — Keep branch up-to-date with base
5. `github-release` — Tag and release when merged
6. `github-issue` — Link issues to PRs throughout

