---
name: rules_manager
description: Manage project and global coding rules. List, view, edit, add, and check rules across all projects.
allowed-tools: Read Grep Glob Bash Write Edit
---

# Rules Manager Skill

You are the Rules Manager. Your job is to manage coding rules for projects, ensuring consistent standards and compliance.

## Rules Overview

Rules define coding standards, conventions, and guidelines that agents, skills, and commands reference during planning, implementation, and validation.

### Rules Locations

| Location | Purpose | Precedence |
|----------|---------|------------|
| `thoughts/<project>/rules/` | Project-specific rules | Highest (overrides global) |
| `thoughts/global/rules/` | Global rules (all projects) | Medium (default fallback) |

### Available Rule Categories

| Category | File | Purpose |
|----------|------|---------|
| coding-standards | `coding-standards.md` | Code style, formatting, linting rules |
| naming-conventions | `naming-conventions.md` | File, function, variable naming patterns |
| testing-requirements | `testing-requirements.md` | Test coverage, test structure rules |
| security-guidelines | `security-guidelines.md` | Security best practices |
| deployment-rules | `deployment-rules.md` | Deployment and release rules |

## Core Commands

### `/rules`
Interactive rules management menu. Prompts user for action:
- List all rules (global + project-specific)
- View specific rule content
- Edit rule files
- Add new rules from templates
- Check code against rules

### `list_rules`
List all available rules for a project.

**Parameters:**
- `project` (optional): Project slug (defaults to current project)
- `scope` (optional): "global", "project", or "all" (defaults to "all")

**Returns:** List of rule files with their locations

### `view_rule`
View the content of a specific rule file.

**Parameters:**
- `rule_name` (required): Name of the rule (e.g., "coding-standards")
- `scope` (optional): "global" or "project" (defaults to project, falls back to global)

**Returns:** Full content of the rule file

### `edit_rule`
Edit a rule file.

**Parameters:**
- `rule_name` (required): Name of the rule to edit
- `scope` (optional): "global" or "project" (defaults to project)

**Process:**
1. Read current rule content
2. Present content to user for editing
3. Write updated content back to file
4. Validate rule format

### `add_rule`
Create a new rule from a template.

**Parameters:**
- `rule_name` (required): Name for the new rule
- `template` (optional): Template to use (defaults to coding-standards)
- `scope` (optional): "global" or "project" (defaults to project)

**Process:**
1. Read template from `thoughts/global/rules/`
2. Copy to target location
3. Prompt user for customization
4. Write customized rule

### `check_rules`
Check code against project rules.

**Parameters:**
- `path` (optional): Path to check (defaults to current directory)
- `rules` (optional): Specific rules to check (defaults to all)

**Process:**
1. Load applicable rules (project + global)
2. Analyze code for compliance
3. Report violations with severity levels
4. Suggest fixes for violations

## Rules Precedence

Rules are applied in this order (highest to lowest priority):

1. **Project-specific rules** (`thoughts/<project>/rules/`)
2. **Global rules** (`thoughts/global/rules/`)
3. **Default standards** (built into the skill)

When rules conflict, the higher-priority rule wins.

## Rules Format

Each rule file follows this structure:

```markdown
# Rule Name

## Overview
[Description of what this rule covers]

## Rules
[Specific rules and guidelines]

## File Paths
[Relevant file paths - use dynamic resolution, NEVER hardcoded]

## Compliance Checklist
[Checklist for verifying compliance]

## References
[Links to external standards or documentation]
```

## Production Rules

### CRITICAL: No Hardcoded Paths

Code must NEVER contain hardcoded file paths. Use dynamic path resolution:

```typescript
// BAD: Hardcoded path
const configPath = '/home/user/.config/app/settings.json';

// GOOD: Dynamic path resolution
const configPath = path.join(os.homedir(), '.config', 'app', 'settings.json');
```

### CRITICAL: No Hardcoded Secrets

Code must NEVER contain hardcoded secrets, passwords, or API keys:

```typescript
// BAD: Hardcoded secret
const API_KEY = 'sk-1234567890abcdef';

// GOOD: Environment variable
const API_KEY = process.env.API_KEY;
```

## Agent Integration

### How Agents Use Rules

1. **Before implementing**: Read project rules to understand standards
2. **During implementation**: Follow rules for code style, naming, etc.
3. **After implementation**: Verify compliance with rules

### Agent Workflow

```
1. Locate rules: thoughts/<project>/rules/ + thoughts/global/rules/
2. Read applicable rules
3. Apply rules during work
4. Verify compliance before completion
```

## Skill Integration

### create-plan
- Reads rules before generating plans
- Includes rules compliance section in plan template
- Ensures plans respect project standards

### validate-plan
- Checks implementation against rules
- Reports violations in validation report
- Flags critical violations as blockers

### ticket-manager
- References rules when creating tickets
- Ensures acceptance criteria align with rules
