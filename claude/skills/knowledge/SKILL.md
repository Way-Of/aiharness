---
name: knowledge
description: Store, fetch, search, and manage learned knowledge in a structured, growing database.
allowed-tools: Read Write Grep Glob
---

# Knowledge Database

Store, fetch, search, and manage learned knowledge in a structured, growing database.

## What This Skill Does

1. **Store** — Capture knowledge from sessions, research, debugging into structured entries
2. **Fetch** — Read specific entries, all entries in a topic, or the entire database
3. **Search** — Full-text search across all knowledge entries
4. **List** — Browse entries by topic or view all topics
5. **Stats** — See database growth, entry counts, topic breakdown

Knowledge lives at `thoughts/global/knowledge/` — a cross-project resource shared across all namespaces.

## Database Structure

```
thoughts/global/knowledge/
├── knowledge-registry.json          # All topics, counts, timestamps
├── docker/
│   ├── index.json                   # Topic index (fast lookups)
│   ├── docker-001.md               # Knowledge entry
│   └── docker-002.md
├── postgres/
│   ├── index.json
│   └── postgres-001.md
├── ash/
│   ├── index.json
│   └── ash-001.md
└── ...
```

## Entry Format

```yaml
---
id: docker-001
title: Docker compose volume permissions fix
topic: docker
tags: ["compose", "volumes", "permissions"]
source: debugging
date: 2026-07-06
confidence: high
related: []
deprecated: false
---

# Docker Compose Volume Permissions

When running containers with named volumes...
```

## Commands

### Store Knowledge

```bash
# Interactive — pipe content via stdin
echo "Fix: run chown on the volume mount" | python3 skills/knowledge/scripts/knowledge.py store docker "Volume permission fix"

# With all flags
python3 skills/knowledge/scripts/knowledge.py store postgres "Connection pooling with PgBouncer" \
  --tags "pgbouncer,connection-pool,performance" \
  --source research \
  --confidence high \
  --content "PgBouncer sits between app and Postgres..."

# From a file
cat notes.md | python3 skills/knowledge/scripts/knowledge.py store ash "Ash resource patterns" --tags "resources,policies"
```

### Fetch Knowledge

```bash
# Fetch a specific entry
python3 skills/knowledge/scripts/knowledge.py fetch docker-001

# Fetch all entries in a topic
python3 skills/knowledge/scripts/knowledge.py fetch --topic docker

# Fetch everything
python3 skills/knowledge/scripts/knowledge.py fetch
```

### Search

```bash
# Full-text search across all entries
python3 skills/knowledge/scripts/knowledge.py search "connection pool"

# Search by tag or content
python3 skills/knowledge/scripts/knowledge.py search "chown"
```

### List & Stats

```bash
# List all topics
python3 skills/knowledge/scripts/knowledge.py topics

# List entries in a topic
python3 skills/knowledge/scripts/knowledge.py list docker

# List all entries
python3 skills/knowledge/scripts/knowledge.py list

# Show statistics
python3 skills/knowledge/scripts/knowledge.py stats
```

### Maintenance

```bash
# Rebuild all indexes from actual files
python3 skills/knowledge/scripts/knowledge.py rebuild

# Initialize with seed topics
python3 skills/knowledge/scripts/knowledge.py init
```

## Agent Instructions

When the user says "store this" or "save this knowledge":

1. Run `python3 skills/knowledge/scripts/knowledge.py init` if first time
2. Determine the topic from context (or ask)
3. Generate a short, descriptive title
4. Extract relevant tags from the content
5. Run `knowledge.py store <topic> "<title>" --tags "..." --content "..."`
6. Confirm the entry was stored

When the user says "look up" or "what do we know about":

1. Run `knowledge.py search "<query>"` or `knowledge.py fetch --topic <topic>`
2. Present the results

When the user says "what's in the knowledge base":

1. Run `knowledge.py topics` and `knowledge.py stats`
2. Summarize the state of the KB

## Seed Topics

- `ash` — Ash framework (Elixir)
- `docker` — Docker, compose, containers
- `postgres` — PostgreSQL, SQL, migrations
- `opentelemetry` — OTel, tracing, metrics, collector
- `elixir` — Elixir language, patterns, gotchas
- `deno` — Deno runtime, TypeScript
- `react` — React, Next.js, frontend
- `devops` — CI/CD, deployment, infrastructure
- `ai-tools` — AI coding tools, harness, skills

New topics are auto-created on first entry.

## Rules

- Entries are append-only — never delete, only deprecate via `deprecated: true`
- Entry IDs are auto-incrementing: `<topic>-<NNN>`
- Topics are auto-created when first entry is stored
- Index files are rebuilt on every store operation
- The registry is the single source of truth for topic counts

## Integration with Other Skills

- **Postmortem Manager**: Stores root causes and solutions from incidents in the knowledge base
- **Sales Knowledge**: Provides market data, competitive intel, and customer research for investor-ready-doc-gen
- **Feature Testing Framework**: Template for testing features with knowledge capture built in
- **Ticket System**: Links knowledge entries to tickets via `knowledge_entries` frontmatter field

## Templates & Rules

- **Templates**: `thoughts/global/templates/` — ticket, fix note, knowledge, and other templates
- **Rules**: `thoughts/global/rules/` — coding standards, naming, security, testing, deployment rules
