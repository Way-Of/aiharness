---
name: teams
description: Connect to WayOfTeams for team context — team members, roles, assignments, GitHub activity, workspace info. Works with or without MCP.
allowed-tools: read, write, edit, bash, grep, glob, websearch
---

# teams — WayOfTeams Team Context

Get team awareness for your AI coding agent. Know who's on the team, what they're working on, and what the team's context is.

## When to Use This Skill

- You need to know who's available to work on something
- You need to understand team structure and roles
- You need to see what the team is currently working on
- You need GitHub activity context (commits, PRs, branches)
- You need workspace context (current project, members, settings)

## Prerequisites

- WayOfTeams account with active subscription
- GitHub login (provides JWT token for MCP auth)
- AI tool with MCP support

## Team Structure

```
Company
  └── Department
       └── Team
            └── Developer
```

Each developer has:
- **Role**: CTO, Lead, Senior, Developer
- **Skills**: Installed harness skills
- **Assignments**: Current tickets and tasks
- **Activity**: Recent commits, standups, reviews

## Available Actions

### 1. `teams_status` — Current workspace status
Shows: connection status, current workspace, team members, recent activity.

```
WayOfTeams Status:
  MCP: Connected (https://teamsapp.zerwiz.org/mcp)
  Workspace: Way-Of
  Team: 5 members
  Tickets: 42 total, 5 in progress
  Standups: 3 today
```

### 2. `teams_tickets` — List team tickets
Query tickets from WayOfTeams via MCP.

```
teams_tickets --status=in_progress --assignee=me
  → Returns: list of tickets assigned to current user
```

### 3. `teams_standups` — Get team standups
Pull standups from WayOfTeams.

```
teams_standups --date=today
  → Returns: today's standup entries from all team members
```

### 4. `teams_skills` — List available skills
Show what skills the team has installed.

```
teams_skills
  → Returns: list of installed harness skills and their status
```

### 5. `teams_github` — GitHub activity
Show recent GitHub activity (commits, PRs, issues).

```
teams_github --repo=myproject --limit=10
  → Returns: recent commits, open PRs, recent issues
```

### 6. `teams_thoughts` — Read project context
Read from the `thoughts/` directory via MCP.

```
teams_thoughts --path=docs/architecture
  → Returns: content of thoughts/docs/architecture files
```

## MCP Detection

Before attempting MCP connection, check if WayOfTeams is available:

```bash
# Check if MCP endpoint is reachable
curl -s -o /dev/null -w "%{http_code}" https://teamsapp.zerwiz.org/mcp

# Check if config has wayofteams entry
grep -l "wayofteams" ~/.config/opencode/opencode.json ~/.claude/.mcp.json 2>/dev/null
```

## Config Examples

### OpenCode (`~/.config/opencode/opencode.json`)
```json
{
  "mcp": {
    "wayofteams": {
      "type": "remote",
      "url": "https://teamsapp.zerwiz.org/mcp",
      "enabled": false,
      "headers": { "Authorization": "{env:WAYOFTEAMS_MCP_TOKEN}" },
      "timeout": 30000
    }
  }
}
```

## Authentication

1. Sign in to [Way of Teams](https://teamsapp.zerwiz.org) via GitHub
2. Go to Settings → API Tokens → Generate MCP Token
3. Set env var: `export WAYOFTEAMS_MCP_TOKEN="your-token"`

## Fallback Behavior

When MCP is not available, fall back to local operations:
- **Team members**: Read from `thoughts/<project>/AGENTS.md`
- **Tickets**: Read from `thoughts/<project>/shared/tickets/`
- **Standups**: Generate from git log
- **GitHub**: Use `gh` CLI directly
- **Knowledge**: Search local `thoughts/` directory

**Always check MCP availability before attempting connection.**

## Code Traceability

When using team context, maintain ticket references:

### Ticket References
Every code change must include a ticket reference:
```typescript
// [PROJ-001] Add team member to project
const member = await mcp.teams_status();
```

### Fetching Context from Tickets
Use team context to understand what tickets are being worked on:
```
teams_tickets(status="in_progress")
  → Returns: list of active tickets
  → Use this to understand team context
```

### Linking Code to Tickets
After implementing, add reference to all changed files:
```bash
grep -r "PROJ-001" --include="*.ts" --include="*.py"
```
