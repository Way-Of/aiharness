---
name: commit
description: Create structured git commits. Delegates to the git-commit-helper skill.
allowed-tools: read, bash, glob, grep
---

# /commit — Create structured git commits

Activates the [git-commit-helper](skills/git_commit_helper/SKILL.md) skill to perform this operation.

## Usage
```
/commit
```

## Process
1. This command activates the `git-commit-helper` skill
2. Follow that skill's workflow to complete the operation
3. Report results to the user

## Templates & Rules

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
