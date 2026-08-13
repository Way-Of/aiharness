---
name: wayofteams-mcp
description: Connect to WayOfTeams MCP server — 41 tools for tickets, standups, knowledge, rules, memory, and team context. Works with or without MCP connection.
allowed-tools:
  - read
  - write
  - edit
  - bash
  - grep
  - glob
  - websearch
---

# wayofteams-mcp — WayOfTeams MCP Integration

Connect your AI coding agent to WayOfTeams via the Model Context Protocol (MCP). Access tickets, standups, knowledge, rules, and Anchor memory — all from your editor.

## When to Use This Skill

- You need to read or write tickets in WayOfTeams
- You need team context (who's on the team, what they're working on)
- You need to store or search semantic memories via Anchor
- You need to pull standups, knowledge, or rules from WayOfTeams
- You need context injection for new sessions or PR reviews

## Prerequisites

- WayOfTeams account with active subscription
- GitHub login (provides JWT token for MCP auth)
- AI tool with MCP support (OpenCode, Claude Code, etc.)

## MCP Server Details

| Property | Value |
|----------|-------|
| **Endpoint** | `https://teamsapp.zerwiz.org/mcp` |
| **Transport** | Streamable HTTP (MCP spec 2025-06-18) |
| **Auth** | Bearer JWT from GitHub login |
| **Tools** | 41 total (tickets, standups, knowledge, rules, memory, team, skills) |
| **Env var** | `WAYOFTEAMS_MCP_TOKEN` |

## Connection Flow

```
Agent needs data from WayOfTeams
  → Check if MCP is configured (opencode.json, .mcp.json, etc.)
  → If configured: call MCP tool via HTTP
  → If not configured: use local files as fallback
  → Return data to agent
```

## Available Tools (41)

### Ticket Management
| Tool | Description | Example |
|------|-------------|---------|
| `tickets_list` | List/search tickets | "Show me high-priority tickets" |
| `tickets_get` | Get ticket detail | "What's the status of WOTEAMS-100?" |
| `tickets_create` | Create new ticket | "Create a ticket for the auth bug" |
| `tickets_update` | Update ticket | "Move WOTEAMS-100 to done" |

### Team & Standups
| Tool | Description | Example |
|------|-------------|---------|
| `standup_get` | Get standup entries | "What did the team do today?" |
| `standup_create` | Create standup | "Post my standup for today" |
| `team_skills` | Get skill reports | "What skills does the team have?" |
| `team_notifications` | Get notifications | "Any new notifications?" |

### Knowledge & Rules
| Tool | Description | Example |
|------|-------------|---------|
| `knowledge_list` | List knowledge entries | "What knowledge do we have?" |
| `knowledge_search` | Search knowledge base | "Find knowledge about deployment" |
| `knowledge_create` | Create knowledge entry | "Add this as a knowledge entry" |
| `rules_list` | List coding rules | "What coding rules exist?" |
| `rules_get` | Get rule content | "Show me the security rules" |
| `rules_create` | Create new rule | "Add a new naming rule" |

### Templates
| Tool | Description | Example |
|------|-------------|---------|
| `templates_list` | List all templates | "What templates are available?" |
| `templates_get` | Get template content | "Show me the ticket template" |
| `templates_create` | Create new template | "Create a deployment template" |
| `templates_update` | Update template | "Update the fix template" |

### Skills & Agents
| Tool | Description | Example |
|------|-------------|---------|
| `skills_list` | List harness skills | "What skills are available?" |
| `skills_get` | Get skill details | "How does ticket-manager work?" |
| `agents_list` | List specialist agents | "What agents can I use?" |
| `commands_list` | List commands | "What commands are available?" |

### Project Context
| Tool | Description | Example |
|------|-------------|---------|
| `thoughts_read` | Read project context | "Read the architecture docs" |
| `thoughts_search` | Search project docs | "Find tickets about auth" |
| `kanban_boards` | List kanban boards | "Show me the kanban boards" |
| `time_sync` | Get server time | "What time is it?" |

### Memory (Anchor via WayOfTeams)
| Tool | Description | Example |
|------|-------------|---------|
| `memory_store` | Store a memory | "Remember we chose Ash Framework" |
| `memory_search` | Search memories semantically | "What decisions about auth?" |
| `memory_get` | Get memory by ID | "Show me memory abc123" |
| `memory_list` | List recent memories | "What are my recent memories?" |
| `memory_delete` | Delete a memory | "Remove memory abc123" |
| `memory_update` | Update memory content | "Update memory with new context" |
| `anchors_list` | List all anchors | "What anchors exist?" |
| `anchors_get` | Get anchor detail | "Show me the project anchor" |
| `anchors_create` | Create anchor | "Create a new project anchor" |
| `anchors_update` | Update anchor | "Update the project anchor" |
| `anchors_destroy` | Delete anchor | "Remove the test anchor" |
| `context_inject` | Get context for new session | "Load relevant context" |
| `pr_review_context` | PR review with full context | "Review this PR with decisions" |

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

### Claude Code (`~/.claude/.mcp.json`)
```json
{
  "mcpServers": {
    "wayofteams": {
      "type": "http",
      "url": "https://teamsapp.zerwiz.org/mcp",
      "disabled": true,
      "headers": { "Authorization": "{env:WAYOFTEAMS_MCP_TOKEN}" }
    }
  }
}
```

## Authentication

1. Sign in to [Way of Teams](https://teamsapp.zerwiz.org) via GitHub
2. Go to Settings → API Tokens → Generate MCP Token
3. Set env var: `export WAYOFTEAMS_MCP_TOKEN="your-token"`
4. Or add to config: `"headers": {"Authorization": "Bearer YOUR_TOKEN"}`

## Fallback Behavior

When MCP is not available, skills fall back to local file operations:
- Tickets: read from `thoughts/<project>/shared/tickets/`
- Standups: generate from git log
- Knowledge: search local `thoughts/` directory
- Rules: read from `thoughts/global/rules/`

**Always check MCP availability before attempting connection.**

## Code Traceability

When using MCP tools, maintain ticket traceability:

### Ticket References
Every code change must include a ticket reference:
```typescript
// [PROJ-001] Create ticket via MCP
const ticket = await mcp.tickets_create({ title: "..." });
```

### Fetching Context from Tickets
Use MCP to get ticket context for implementation:
```
tickets_get(ticket_id="PROJ-001")
  → Returns: requirements, acceptance criteria, technical notes
  → Use this context to guide implementation
```

### Linking Code to Tickets
After implementing from a ticket, add reference to all changed files:
```bash
grep -r "PROJ-001" --include="*.ts" --include="*.py"
```
