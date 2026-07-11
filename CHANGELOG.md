# Changelog

All notable changes to the AI Engineering Harness will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

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
