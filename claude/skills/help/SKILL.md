---
name: help
description: Unified help system for all commands and skills. Delegates to the help-command skill.
allowed-tools: Read Bash Glob Grep
disable-model-invocation: true
---

# /help — Unified help system for all commands and skills

Activates the [help-command](skills/help_command/SKILL.md) skill to perform this operation.

## Usage
```
/help
```

## Process
1. This command activates the `help-command` skill
2. Follow that skill's workflow to complete the operation
3. Report results to the user

## Templates & Rules

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/templates/rules/` — coding standards, naming, security, testing, deployment rules
