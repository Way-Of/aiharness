# Changelog

All notable changes to the AI Engineering Harness will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- Debugger agent for all 6 tools + 2 subagent extensions (AIH-186)
- Context Reference section to all 83 agent files (rules, templates, knowledgebase)
- Context Reference section to 108 command and prompt files
- Knowledgebase reference (`thoughts/global/knowledge/`) to all 659 skill boilerplate sections
- Mandatory validation gate to create-plan: plans require explicit user approval before implementation (16 files)
- Knowledge entry ai-tools-001: sed bulk-update pattern for mass path renames

### Changed
- Consolidated duplicate rules directories: removed `thoughts/global/templates/rules/`, kept `thoughts/global/rules/` as single source of truth (AIH-187)
- Updated ~680 skill files to reference `thoughts/global/rules/` instead of `thoughts/global/templates/rules/`
- Simplified rules-manager from 3-tier to 2-tier precedence (project > global)
- Updated init-harness to copy rules from `thoughts/global/rules/` to new projects
- Renamed "Templates & Rules" boilerplate to "Context Reference" across 659 skill files

### Fixed
- Planner agent repositioned from 8th to 4th in agent lists across all tools (AIH-186)
- Planner agent description updated to clearly state when to use it

## [1.7.21] - 2026-07-11

### Fixed
- Skill naming format: all 6 tool validators now pass with 0 issues (AIH-185)
- Wo Code skill conflict warnings eliminated — names match per-tool conventions
- serialize_frontmatter colon-quoting bug fixed in all 6 tool update scripts (wocode, opencode, claude, pi, codex, antigravity)
- Added missing YAML frontmatter to 5 canonical skills (agents-md-manager, init-harness, knowledge, sales, standup)
- Codex dual-file format: validator accepts SKILL.md fallback, generates prompt.md from SKILL.md body, writes pure YAML for skill.yaml
- adapter-generate.py: fixed HARNESS_ROOT path (3 levels not 4), skip directories in assets copy, generate correct dir names per tool
- adapter-generate.py: fixed variable shadowing that broke multi-tool sync
- Cleaned orphan dirs (no SKILL.md) in opencode, claude, antigravity
- Renamed kebab→snake dirs in claude and antigravity to match tool conventions

### Changed
- Repositioned agents: scout is now the default code investigation agent, codebase_analyzer is only for deep complex analysis
- Repositioned planner: moved from 8th to 4th in agent lists, description updated to say when to use it (AIH-186)
- All 25 canonical skills made project-agnostic — removed "AI Engineering Harness", "WOMONO", "WOW", "OPT" references (AIH-185)
- wo-coder.md docs updated: Wo Coder uses kebab-case + Title Case (inherits from Pi, not snake_case)
- Codex skill.yaml files use pure YAML format (no `---` frontmatter delimiters)
- Templates consolidated to `thoughts/global/templates/` — removed scattered `fixes-templates/` and `thoughts/shared/templates/` (AIH-185)
- Debug skill updated with optimized workflow + saves debug sessions to `docs/debug/` (AIH-184)
- init-harness creates `docs/debug/` directory during project setup (AIH-184)
- Fixes commands/prompts added to manifest for deployment across all tools (AIH-184)

## [1.7.20] - 2026-07-11

### Added
- Rules system with global and project-specific rules (AIH-182)
- rules-manager skill with interactive menu
- /rules command for all 7 tools
- Production-ready rules templates (AIH-183)
- init-harness creates rules folder and copies templates
- create-plan loads rules before planning
- validate-plan checks rules compliance
- Cross-platform tool paths in README (Linux/macOS/Windows)
- aiharness version-config.json for fixes-bump support (AIH-184)

### Changed
- Fixes skills (fixes-manager, fixes-bump, fixes-create, fixes-validate) made project-agnostic — no longer hardcoded to womono/wow/opticat (AIH-184)
- fixes-manager uses dynamic project discovery from `assets/<project>/` instead of hardcoded project table
- fixes-bump `--project` accepts any project with `assets/<project>/version-config.json`
- fixes-create `--project` and `--component` arguments are now generic
- Command and prompt files use generic conditional logic instead of project-specific sections
- CTO Dashboard references renamed to WayOfTeams (AIH-179)
- Workflow order updated: validate-plan before implement-plan (AIH-179)
- Ticket-manager uses category subdirectories (AIH-180)
- /complete command moves tickets to done/ subdirectory (AIH-180)
- All .pi references in wocode updated to .wocode (AIH-181)

### Fixed
- Ticket creation now uses correct category subdirectories (AIH-180)
- Tickets moved to done/ subdirectory on completion (AIH-180)
- theme-cycler.ts uses .wocode/themes instead of .pi/themes (AIH-181)
- All .pi path references fixed in wocode/agent (AIH-181)
- Incomplete v1.7.20 bump fixed: base_manifest.yaml, install.ts now at 1.7.20 (AIH-184)

## [Unreleased]

### Fixed
- Fixed theme-cycler.ts to use `.wocode/themes` instead of `.pi/themes` (AIH-181)
- Fixed subagents-index.ts to use `.wocode/agent/agents` instead of `.pi/agent/agents` (AIH-181)
- Fixed all SKILL.md files in wocode to reference correct `.wocode` paths (AIH-181)
- Fixed web-access packets to use `~/.wocode/web-search.json` instead of `~/.pi/web-search.json` (AIH-181)
- Fixed ticket-manager skill to use category subdirectories (AIH-180)
- Fixed `/complete` command to move tickets to `done/` subdirectory (AIH-180)

### Changed
- Renamed CTO Dashboard references to WayOfTeams (AIH-179)
- Updated workflow order: validate-plan before implement-plan (AIH-179)
- Added `/create-ticket` command for all 7 tools (AIH-179)
- Updated README with cross-platform paths for all tools (AIH-176)

## [1.7.19] - 2026-07-10

### Added
- Ticket organization skill (AIH-172)
- Ticket category subdirectory support

### Fixed
- Install URLs pointing to correct aiharness repo (AIH-173)
- Settings component prompt now shows once for all tools
- Stale file detection excludes node_modules
