# AI Engineering Harness

[![CI](https://github.com/Way-Of/aiharness/actions/workflows/ci.yml/badge.svg)](https://github.com/Way-Of/aiharness/actions/workflows/ci.yml)

The AI Engineering Harness provides 51 battle-tested skills, 12 agents, and workflows across 7 AI coding tools. Install once, use everywhere.

## About This

This repo provides a cross-tool AI engineering harness — 51+ skills, 12 agents, and workflows that work across 7 AI coding tools. Install once, use everywhere.

### Updating

To pull the latest skills, agents, and installer updates from the remote repository:

**macOS / Linux:**

```bash
deno run --reload -A https://raw.githubusercontent.com/Way-Of/aiharness/main/install.ts --install-cli
```

**Windows (PowerShell):**

```powershell
irm https://raw.githubusercontent.com/Way-Of/aiharness/main/install.ps1 | iex
```

The `--reload` flag (Deno) forces a re-fetch of all dependencies and the script itself, ensuring you always get the latest version. On Windows, `irm` (Invoke-RestMethod) fetches and pipes the script directly to `iex` (Invoke-Expression).

**Using the CLI (all platforms):**

```bash
way-of --update
```

**Windows (PowerShell) with explicit flags:**

```powershell
way-of.exe --update
```

## Quick Start

```bash
# Install CLI
deno run -A https://raw.githubusercontent.com/Way-Of/aiharness/main/install.ts --install-cli

# Install all tools
way-of --tool=all --yes

# Install specific tool
way-of --tool=claude
way-of --tool=opencode
```

## Supported Tools

| Tool | Config Dir | Skill Naming |
|------|------------|--------------|
| **Claude Code** | `~/.claude/` | snake_case |
| **OpenCode** | `~/.config/opencode/` | kebab-case |
| **Pi** | `~/.pi/agent/` | kebab-case |
| **Wo Coder** | `~/.wocode/` | kebab-case |
| **Antigravity** | `~/.antigravity/` | snake_case |
| **Codex CLI** | `~/.codex/` | snake_case |
| **Gemini CLI** | `~/.gemini/` | snake_case |

## Installation

### One-liner (Recommended)

```bash
deno run -A https://raw.githubusercontent.com/Way-Of/aiharness/main/install.ts --install-cli
```

### Per-Tool Install

```bash
way-of --tool=claude          # Claude Code
way-of --tool=opencode        # OpenCode
way-of --tool=pi              # Pi
way-of --tool=wocode          # Wo Coder
way-of --tool=antigravity     # Antigravity
way-of --tool=codex           # Codex CLI
way-of --tool=all --yes       # All tools
```

### Update

```bash
way-of --update
```

### GNU Stow (Alternative)

```bash
git clone https://github.com/Way-Of/aiharness.git ~/.ai-engineering-harness
cd ~/.ai-engineering-harness
./setup.sh claude    # Claude Code
./setup.sh all       # All tools
```

## Skills (52)

### Core Workflow
- `ticket-manager` — Full ticket lifecycle management
- `ticket-executor` — Phase-by-phase implementation
- `ticket-organization` — Proactive ticket organization (audit, archive, naming, orphans, TODO regeneration)
- `backlog-groomer` — Ticket creation and maintenance
- `create-plan` — Implementation plan generation
- `validate-plan` — Verify implementation against plan
- `commit` — Structured git commits
- `debug` — Issue investigation

### Code Quality
- `git-commit-helper` — Well-structured commits
- `pr-description-generator` — PR descriptions
- `tdd` — Test-driven development

### Documentation
- `document-generation` — Generate documents
- `fixes-manager` — Cross-project fix notes
- `fixes-bump` — Version bumping
- `fixes-create` — Fix note creation

### GitHub Integration
- `github-branch` — Feature branch management
- `github-issue` — Issue management
- `github-pr` — Pull request workflow
- `github-release` — Release management
- `github-review` — PR review
- `github-sync` — Branch synchronization

### Analysis & Research
- `research-codebase` — Codebase research
- `improve-codebase-architecture` — Architecture improvements
- `self-documentation` — Self-help system

### WayOfMono-Specific
- `womono-practices-guide` — Development best practices
- `womono-practices-audit` — Compliance verification
- `womono-practices-backlog` — Ticket creation
- `womono-version-updater` — Version management
- `womono-validate-manifest` — Manifest validation

### Build Tools
- `build-tool` — Universal component builder
- `build-tool-skill` — Skill builder for all tools
- `build-tool-agent` — Agent builder
- `build-tool-config` — Configuration builder
- `build-tool-extension` — Extension builder

### Observability
- `otel-instrument` — OpenTelemetry orchestrator
- `otel-collector` — Collector configuration
- `otel-instrumentation` — SDK setup
- `observability-driven-development` — ODD workflow

## Agents

| Agent | Purpose |
|-------|---------|
| `codebase_analyzer` | Analyze implementation details |
| `codebase_locator` | Find files and components |
| `codebase_pattern_finder` | Find similar implementations |
| `coder` | Implementation and code generation |
| `explore` | Fast codebase exploration |
| `general` | General-purpose tasks |
| `planner` | Architecture planning |
| `reviewer` | Code review |
| `scout` | Fast codebase recon |
| `thoughts_analyzer` | Research document analysis |
| `thoughts_locator` | Document discovery |
| `web_search_researcher` | Web research |

## Commands

```bash
way-of --tool=<name>          # Install tool config
way-of --tool=all --yes       # Install all tools
way-of --update               # Full sync
way-of --install-cli          # Install/update CLI
way-of --help                 # Full usage
way-of --report-skills        # Report to CTO Dashboard
way-of --sync-docs --check    # Check docs sync
way-of --compliance           # Run compliance check
```

## Repository Structure

```
aiharness/
├── install.ts          # Main installer (Deno)
├── install.ps1         # Windows PowerShell installer
├── setup.sh            # GNU Stow installer
├── manifest.json       # Skills/agents manifest
├── skills/             # 52 skill definitions
├── opencode/           # OpenCode configs
├── claude/             # Claude Code configs
├── pi/                 # Pi configs
├── wocode/             # Wo Coder configs
├── antigravity/        # Antigravity configs
├── codex/              # Codex CLI configs
├── gemini/             # Gemini CLI configs
├── scripts/            # Validation scripts
├── config-manifest/    # Per-tool YAML configs
├── docs/               # Documentation
└── .github/workflows/  # CI/CD
```

## Manifest

The `manifest.json` defines all skills, agents, and commands with their source and destination paths for each tool. Validation:

```bash
deno run -A scripts/validate-manifest.ts
```

## CI/CD

- **CI**: Deno check, format, manifest validation, skill compliance, docs sync
- **Release**: Semantic versioning via `go-semantic-release`

## Related Projects

- [WayOfMono](https://github.com/Way-Of/wayofmono) — Monorepo with `@wayofmono/*` npm packages
- [CTO Dashboard](https://github.com/Way-Of/wayofmono/tree/main/ui) — Telemetry, tickets, reviews
- [f-rr-d](https://github.com/Way-Of/f-rr-d) — Centralized thoughts storage

## License

MIT
