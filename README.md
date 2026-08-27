# AI Engineering Harness

[![CI](https://github.com/Way-Of/aiharness/actions/workflows/ci.yml/badge.svg)](https://github.com/Way-Of/aiharness/actions/workflows/ci.yml)

The AI Engineering Harness provides 51 battle-tested skills, 12 agents, and workflows across 7 AI coding tools. Install once, use everywhere.

## About This

This repo provides a cross-tool AI engineering harness — 51+ skills, 12 agents, and workflows that work across 6 AI coding tools. Install once, use everywhere.

## Prerequisites

The primary installer requires [Deno](https://deno.com). Install it first:

**macOS / Linux:**
```bash
curl -fsSL https://deno.land/install.sh | sh
```

**Windows (PowerShell):**
```powershell
irm https://deno.land/install.ps1 | iex
```

**Via npm (any platform):**
```bash
npm install -g deno
```

> **Windows users:** If you prefer to skip Deno, use the PowerShell installer directly — see [Installation](#installation).

### Updating

To pull the latest skills, agents, and installer updates from the remote repository:

**All platforms (requires Deno):**

```bash
deno run --reload -A https://raw.githubusercontent.com/Way-Of/aiharness/main/install.ts --install-cli
```

The `--reload` flag forces a re-fetch of all dependencies and the script itself, ensuring you always get the latest version.

**Windows (PowerShell, no Deno):**

```powershell
irm https://raw.githubusercontent.com/Way-Of/aiharness/main/install.ps1 | iex
```

**Using the CLI (all platforms):**

```bash
ai-harness --update
```

## Quick Start

```bash
# Install CLI
deno run -A https://raw.githubusercontent.com/Way-Of/aiharness/main/install.ts --install-cli

# Install all tools (safe — prompts before overwriting configs)
ai-harness --tool=all

# Install all tools (destructive — overwrites ALL configs without prompting)
ai-harness --tool=all --yes

# Install all tools (merge — safe for existing setups, never deletes)
ai-harness --tool=all --merge

# Install specific tool
ai-harness --tool=claude
ai-harness --tool=opencode
```

> **⚠️ `--yes` flag destroys custom configs.** See [Installation Safety](#installation-safety) before using it.
> **✅ `--merge` flag preserves user files.** See [Merge Install](#merge-install-safe-for-existing-setups) for details.

## Supported Tools

| Tool | Config Dir (Linux) | Config Dir (macOS) | Config Dir (Windows) | Skill Naming |
|------|-------------------|-------------------|---------------------|--------------|
| **Claude Code** | `~/.claude/` | `~/.claude/` | `%USERPROFILE%\.claude\` | snake_case |
| **OpenCode** | `~/.config/opencode/` | `~/.config/opencode/` | `%APPDATA%\opencode\` | kebab-case |
| **Pi** | `~/.pi/agent/` | `~/.pi/agent/` | `%USERPROFILE%\.pi\agent\` | kebab-case |
| **Wo Coder** | `~/.wocode/agent/` | `~/.wocode/agent/` | `%USERPROFILE%\.wocode\agent\` | kebab-case |
| **Antigravity** | `~/.antigravity/` | `~/.antigravity/` | `%USERPROFILE%\.antigravity\` | snake_case |
| **Codex CLI** | `~/.codex/` | `~/.codex/` | `%USERPROFILE%\.codex\` | snake_case |
| **Gemini CLI** | `~/.gemini/` | `~/.gemini/` | `%USERPROFILE%\.gemini\` | snake_case |

## Installation

### One-liner (Recommended)

```bash
deno run -A https://raw.githubusercontent.com/Way-Of/aiharness/main/install.ts --install-cli
```

### Per-Tool Install

```bash
ai-harness --tool=claude          # Claude Code (safe — prompts on conflict)
ai-harness --tool=opencode        # OpenCode
ai-harness --tool=pi              # Pi
ai-harness --tool=wocode          # Wo Coder
ai-harness --tool=antigravity     # Antigravity
ai-harness --tool=codex           # Codex CLI
ai-harness --tool=all             # All tools (safe — prompts on conflict)
ai-harness --tool=all --yes       # All tools (DESTRUCTIVE — no prompts)
```

### Update

```bash
ai-harness --update
```

### GNU Stow (Alternative)

```bash
git clone https://github.com/Way-Of/aiharness.git ~/.ai-engineering-harness
cd ~/.ai-engineering-harness
./setup.sh claude    # Claude Code
./setup.sh all       # All tools
```

## Installation Safety

### `--yes` flag behavior

| Flag | Behavior | Use when |
|------|----------|----------|
| *(no flag)* | Prompts before overwriting any config file that differs from the harness default | **First install** or when you have custom configs |
| `--yes` | Skips ALL prompts, overwrites every file silently | CI/CD, fresh machines, or you want a clean slate |
| `--merge` | Preserves user files: skips stale removal, skips settings, only updates manifest files | **Existing setups** — adds harness on top of your custom config |

### What `--merge` preserves

| Behavior | `--merge` | Default | `--yes` |
|----------|-----------|---------|---------|
| User's existing skills/agents | ✅ Kept | ✅ Kept | ❌ Deleted if not in manifest |
| Custom config files | ✅ Kept | Prompts | ❌ Overwritten |
| Settings component | ✅ Skipped | Prompts | ✅ Skipped |
| New manifest files | ✅ Installed | ✅ Installed | ✅ Installed |
| Updated manifest files | ✅ Updated | Prompts | ✅ Updated |

### Safe install (recommended)

```bash
# First install — reviews each config conflict
ai-harness --tool=opencode

# Update — reviews changes before applying
ai-harness --update
```

### Merge install (safe for existing setups)

```bash
# Add harness on top of your existing setup — never deletes or overwrites
ai-harness --tool=all --merge

# Just OpenCode, preserve everything else
ai-harness --tool=opencode --merge
```

### Clean wipe (destructive)

```bash
# Nuclear option — overwrites everything, no prompts
ai-harness --tool=all --yes

# Preview what would be overwritten first
ai-harness --tool=all --dry-run
```

### Backup behavior

The installer **always** creates a timestamped backup before overwriting any config file — whether you use `--yes` or not:

```
~/.config/opencode/opencode.json.bak.1723401234567
```

To restore a previous config:
```bash
cp ~/.config/opencode/opencode.json.bak.1723401234567 ~/.config/opencode/opencode.json
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
ai-harness --tool=<name>          # Install tool config
ai-harness --tool=all --yes       # Install all tools (destructive)
ai-harness --tool=all --merge     # Install all tools (safe for existing setups)
ai-harness --update               # Full sync
ai-harness --install-cli          # Install/update CLI
ai-harness --help                 # Full usage
ai-harness --report-skills        # Report to CTO Dashboard
ai-harness --sync-docs --check    # Check docs sync
ai-harness --compliance           # Run compliance check
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
