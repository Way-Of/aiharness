#!/usr/bin/env python3
"""Validate context consistency across all tools — skills, prompts, and commands."""

import os
import sys
import hashlib

TOOLS = {
    'opencode': {'skills': 'opencode/skills', 'commands': 'opencode/commands', 'agents': 'opencode/agents'},
    'claude': {'skills': 'claude/skills', 'commands': 'claude/commands', 'agents': 'claude/agents'},
    'pi': {'skills': 'pi/agent/skills', 'prompts': 'pi/agent/prompts', 'agents': 'pi/agent/agents'},
    'wocode': {'skills': 'wocode/agent/skills', 'prompts': 'wocode/agent/prompts', 'agents': 'wocode/agent/agents'},
    'antigravity': {'skills': 'antigravity/skills', 'commands': 'antigravity/commands', 'agents': 'antigravity/agents'},
    'codex': {'skills': 'codex/skills', 'commands': 'codex/commands', 'agents': 'codex/agents'},
}

SNAKE_SKILL_TOOLS = ['claude', 'antigravity', 'codex']

def normalize_skill(name):
    return name.replace('_', '-')

def normalize_content(content):
    """Normalize content for comparison (ignore expected per-tool differences)."""
    lines = content.split('\n')
    normalized = []
    in_frontmatter = False
    
    for line in lines:
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            normalized.append(line)
            continue
        
        if in_frontmatter:
            if line.startswith('name:'):
                name = line.split(':', 1)[1].strip().replace('_', '-')
                normalized.append(f'name: {name}')
                continue
            if line.startswith('allowed-tools:'):
                tools_str = line.split(':', 1)[1].strip()
                normalized = [l for l in normalized]
                normalized.append(f'allowed-tools: {",".join(t.strip().lower() for t in tools_str.replace(" ", ",").split(","))}')
                continue
        
        normalized.append(line)
    
    return '\n'.join(normalized)

def get_hash(path):
    with open(path, 'r') as f:
        return hashlib.md5(normalize_content(f.read()).encode()).hexdigest()

def check_skills():
    """Check all skills are identical across tools."""
    errors = []
    
    canonical_dir = 'skills'
    canonical = {}
    for skill in os.listdir(canonical_dir):
        path = os.path.join(canonical_dir, skill, 'SKILL.md')
        if os.path.isfile(path):
            canonical[skill] = get_hash(path)
    
    print(f"Canonical skills: {len(canonical)}")
    
    for tool, config in TOOLS.items():
        if 'skills' not in config:
            continue
        base = config['skills']
        if not os.path.exists(base):
            continue
        
        tool_skills = {}
        for d in os.listdir(base):
            path = os.path.join(base, d, 'SKILL.md')
            if os.path.isfile(path):
                tool_skills[normalize_skill(d)] = get_hash(path)
        
        missing = set(canonical.keys()) - set(tool_skills.keys())
        mismatched = []
        for skill in set(canonical.keys()) & set(tool_skills.keys()):
            if canonical[skill] != tool_skills[skill]:
                mismatched.append(skill)
        
        status = "OK" if not missing and not mismatched else "ISSUES"
        print(f"  {tool}: {len(tool_skills)} skills — {status}")
        
        if missing:
            for s in sorted(missing):
                errors.append(f"{tool}: MISSING skill {s}")
        if mismatched:
            for s in sorted(mismatched):
                errors.append(f"{tool}: MISMATCHED skill {s}")
    
    return errors

def check_commands_prompts():
    """Check commands/prompts are identical across tools."""
    errors = []
    
    # Collect all commands from opencode (reference)
    ref_commands = {}
    ref_dir = 'opencode/commands'
    if os.path.exists(ref_dir):
        for f in os.listdir(ref_dir):
            if f.endswith('.md') and f != 'README.md':
                name = f.replace('.md', '')
                ref_commands[name] = get_hash(os.path.join(ref_dir, f))
    
    print(f"\nReference commands (opencode): {len(ref_commands)}")
    
    # Check each tool's commands/prompts
    for tool, config in TOOLS.items():
        items = {}
        
        if 'commands' in config and os.path.exists(config['commands']):
            for f in os.listdir(config['commands']):
                if f.endswith('.md') and f != 'README.md':
                    name = f.replace('.md', '')
                    items[name] = get_hash(os.path.join(config['commands'], f))
                elif f.endswith('.toml'):
                    name = f.replace('.toml', '').replace('run-', '')
                    items[name] = get_hash(os.path.join(config['commands'], f))
        
        if 'prompts' in config and os.path.exists(config['prompts']):
            for f in os.listdir(config['prompts']):
                if f.endswith('.md') and f != 'README.md':
                    name = f.replace('.md', '')
                    items[name] = get_hash(os.path.join(config['prompts'], f))
        
        missing = set(ref_commands.keys()) - set(items.keys())
        mismatched = []
        for cmd in set(ref_commands.keys()) & set(items.keys()):
            if ref_commands[cmd] != items[cmd]:
                mismatched.append(cmd)
        
        status = "OK" if not missing and not mismatched else "ISSUES"
        print(f"  {tool}: {len(items)} commands/prompts — {status}")
        
        if missing:
            for c in sorted(missing):
                errors.append(f"{tool}: MISSING command/prompt {c}")
        if mismatched:
            for c in sorted(mismatched):
                errors.append(f"{tool}: MISMATCHED command/prompt {c}")
    
    return errors

def check_agents():
    """Check agents are identical across tools."""
    errors = []
    
    ref_agents = {}
    ref_dir = 'opencode/agents'
    if os.path.exists(ref_dir):
        for f in os.listdir(ref_dir):
            if f.endswith('.md') and f != 'README.md':
                ref_agents[f] = get_hash(os.path.join(ref_dir, f))
    
    print(f"\nReference agents (opencode): {len(ref_agents)}")
    
    for tool, config in TOOLS.items():
        if 'agents' not in config:
            continue
        base = config['agents']
        if not os.path.exists(base):
            continue
        
        tool_agents = {}
        for f in os.listdir(base):
            if f.endswith('.md') and f != 'README.md':
                tool_agents[f] = get_hash(os.path.join(base, f))
        
        missing = set(ref_agents.keys()) - set(tool_agents.keys())
        mismatched = []
        for agent in set(ref_agents.keys()) & set(tool_agents.keys()):
            if ref_agents[agent] != tool_agents[agent]:
                mismatched.append(agent)
        
        status = "OK" if not missing and not mismatched else "ISSUES"
        print(f"  {tool}: {len(tool_agents)} agents — {status}")
        
        if missing:
            for a in sorted(missing):
                errors.append(f"{tool}: MISSING agent {a}")
        if mismatched:
            for a in sorted(mismatched):
                errors.append(f"{tool}: MISMATCHED agent {a}")
    
    return errors

def main():
    print("=" * 60)
    print("CONTEXT VALIDATION — Skills, Commands, Prompts, Agents")
    print("=" * 60)
    
    all_errors = []
    
    print("\n--- Skills ---")
    all_errors.extend(check_skills())
    
    print("\n--- Commands & Prompts ---")
    all_errors.extend(check_commands_prompts())
    
    print("\n--- Agents ---")
    all_errors.extend(check_agents())
    
    print("\n" + "=" * 60)
    if all_errors:
        print(f"ERRORS: {len(all_errors)}")
        for e in all_errors:
            print(f"  ✗ {e}")
        return 1
    else:
        print("ALL TOOLS CONSISTENT ✓")
        return 0

if __name__ == '__main__':
    sys.exit(main())
