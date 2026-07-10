# AI Engineering Harness Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- "WAY OF" ASCII art branding in CLI help output
- `way-of` CLI command alias in help display
- About This section in README with update instructions for macOS/Linux and Windows
- AIH-173 ticket for tracking install URL fixes

### Changed
- All install URLs updated from `Way-Of/wayofmono` to `Way-Of/aiharness`
- README command references updated from `ai-harness` to `way-of`
- ASCII art logo updated across all 7 occurrences in install.ts
- Repo made public for raw.githubusercontent.com access

### Fixed
- Install URLs in README pointed to wrong repo (wayofmono instead of aiharness)
- `deno run --reload -A` install command now works from online
- PowerShell install URL corrected

---

## [1.7.19] - 2026-07-09

### Added
- Ticket organization skill (AIH-172)
- Multi-f-rr-d support (WOMONO-169)

### Changed
- Harness extracted from wayofmono monorepo to standalone repo

### Fixed
- Install.ps1 internal URL references
