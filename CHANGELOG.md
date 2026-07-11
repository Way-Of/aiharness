# Changelog

All notable changes to the AI Engineering Harness will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

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
