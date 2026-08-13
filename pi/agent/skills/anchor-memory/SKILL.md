---
name: anchor-memory
description: Store and retrieve semantic memories via Anchor through WayOfTeams MCP — decisions, patterns, invariants, context injection, PR review context.
allowed-tools:
  - read
  - write
  - edit
  - bash
  - grep
  - glob
  - websearch
---

# anchor-memory — Anchor Semantic Memory Integration

Store decisions, patterns, and context that your AI tools can recall across sessions. Powered by Anchor memory plane via WayOfTeams MCP.

## When to Use This Skill

- You made a decision that should persist across sessions
- You want to search for past decisions or patterns
- You're starting a new session and need relevant context
- You're reviewing a PR and need decision rationale
- You fixed a bug and want to record the invariant

## Memory Types

| Type | Use Case | Example |
|------|----------|---------|
| `decision` | Why a choice was made | "Chose Bandit over Cowboy for performance" |
| `invariant` | Rules that shouldn't change | "Always use Ash Framework for domain logic" |
| `working_state` | Where things stand now | "Currently refactoring the auth module" |
| `raw_trace` | What actually happened | "Explored the PGVector search implementation" |
| `review_pattern` | Recurring patterns | "PR reviews always check for N+1 queries" |

## How It Works

```
Agent makes a decision or observes a pattern
  → Store via WayOfTeams MCP: memory_store
  → Later: memory_search(query="what did we decide about auth?")
  → Anchor returns relevant memories via semantic search
  → Agent uses context to inform current work
```

## Available Tools (via WayOfTeams MCP)

### Core Memory
| Tool | Description | Example |
|------|-------------|---------|
| `memory_store` | Store a memory | "Remember we chose Ash Framework" |
| `memory_search` | Semantic search | "What decisions about auth?" |
| `memory_get` | Get by ID | "Show me memory abc123" |
| `memory_list` | List recent | "What are my recent memories?" |
| `memory_update` | Update content | "Update with new context" |
| `memory_delete` | Delete memory | "Remove memory abc123" |

### Anchors (containers for related memories)
| Tool | Description | Example |
|------|-------------|---------|
| `anchors_list` | List all anchors | "What anchors exist?" |
| `anchors_get` | Get anchor detail | "Show me the project anchor" |
| `anchors_create` | Create anchor | "Create a new project anchor" |
| `anchors_update` | Update anchor | "Update the project anchor" |
| `anchors_destroy` | Delete anchor | "Remove the test anchor" |

### Context & Review
| Tool | Description | Example |
|------|-------------|---------|
| `context_inject` | Token-budgeted context for new sessions | "Load relevant context" |
| `pr_review_context` | Full PR review context | "Review with decisions + patterns" |

## Auto-Store Triggers

Memories can be stored automatically on key events:

| Event | Memory Type | What to Store |
|-------|-------------|---------------|
| Ticket created | `working_state` | Current focus and context |
| Ticket updated | `working_state` | Progress and blockers |
| Ticket done | `decision` | What was built and why |
| Plan created | `decision` | Architecture choices and rationale |
| Plan approved | `decision` | Finalized approach |
| Bug fixed | `invariant` | "This must never happen again" |
| Architecture decision | `decision` | Choice + rationale + trade-offs |
| PR reviewed | `review_pattern` | Common review findings |

## Context Injection

When starting a new session, use `context_inject` to get relevant history:

```
Agent starts new session
  → Call context_inject with current task/project
  → Receive: recent decisions, related patterns, relevant invariants
  → Agent is immediately up to speed without re-explaining
```

## PR Review Context

When reviewing a PR, use `pr_review_context` to get full context:

```
Agent reviewing a PR
  → Call pr_review_context with PR URL/ticket ID
  → Receive: decision rationale, linked tickets, similar past decisions, review patterns
  → Agent can review with full historical context
```

## Memory Search

Semantic search finds related memories by meaning, not just keywords:

```
memory_search("authentication approach")
  → Returns memories about auth decisions, patterns, and context
  → Even if they don't contain the exact word "authentication"
```

## Fallback Behavior

When Anchor/MCP is not available:
- Store decisions in `thoughts/<project>/shared/research/`
- Search via `grep -r "decision" thoughts/`
- Context from local `thoughts/` directory files

**Always check MCP availability before attempting connection.**
