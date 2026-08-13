"""Validate context consistency across all 6 tools."""

import os
import sys
import hashlib

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
                normalized.append(f'allowed-tools: {",".join(t.strip().lower() for t in tools_str.replace(" ", ",").split(","))}')
                continue
        
        normalized.append(line)
    
    return '\n'.join(normalized)

def get_hash(path):
    with open(path, 'r') as f:
        return hashlib.md5(normalize_content(f.read()).encode()).hexdigest()

def check_skills(canonical_dir, tools):
    """Check all skills are identical across tools."""
    errors = []
    
    canonical = {}
    for skill in os.listdir(canonical_dir):
        path = os.path.join(canonical_dir, skill, 'SKILL.md')
        if os.path.isfile(path):
            canonical[skill] = get_hash(path)
    
    print(f"Canonical skills: {len(canonical)}")
    
    for tool_name, config in tools.items():
        base = config['skills_dir']
        if not os.path.exists(base):
            continue
        
        tool_skills = {}
        for d in os.listdir(base):
            path = os.path.join(base, d, 'SKILL.md')
            if os.path.isfile(path):
                # Normalize name to kebab for comparison
                norm_name = d.replace('_', '-')
                tool_skills[norm_name] = get_hash(path)
        
        missing = set(canonical.keys()) - set(tool_skills.keys())
        mismatched = []
        for skill in set(canonical.keys()) & set(tool_skills.keys()):
            if canonical[skill] != tool_skills[skill]:
                mismatched.append(skill)
        
        status = "OK" if not missing and not mismatched else "ISSUES"
        print(f"  {tool_name}: {len(tool_skills)} skills — {status}")
        
        if missing:
            for s in sorted(missing):
                errors.append(f"{tool_name}: MISSING skill {s}")
        if mismatched:
            for s in sorted(mismatched):
                errors.append(f"{tool_name}: MISMATCHED skill {s}")
    
    return errors

def check_agents(canonical_dir, tools):
    """Check all agents are identical across tools."""
    errors = []
    
    canonical = {}
    agents_path = os.path.join(canonical_dir, 'opencode', 'agents')
    if os.path.exists(agents_path):
        for f in os.listdir(agents_path):
            if f.endswith('.md') and f != 'README.md':
                canonical[f] = get_hash(os.path.join(agents_path, f))
    
    print(f"\nCanonical agents: {len(canonical)}")
    
    for tool_name, config in tools.items():
        base = config['agents_dir']
        if not os.path.exists(base):
            continue
        
        tool_agents = {}
        for f in os.listdir(base):
            if f.endswith('.md') and f != 'README.md':
                tool_agents[f] = get_hash(os.path.join(base, f))
        
        missing = set(canonical.keys()) - set(tool_agents.keys())
        mismatched = []
        for agent in set(canonical.keys()) & set(tool_agents.keys()):
            if canonical[agent] != tool_agents[agent]:
                mismatched.append(agent)
        
        status = "OK" if not missing and not mismatched else "ISSUES"
        print(f"  {tool_name}: {len(tool_agents)} agents — {status}")
        
        if missing:
            for a in sorted(missing):
                errors.append(f"{tool_name}: MISSING agent {a}")
        if mismatched:
            for a in sorted(mismatched):
                errors.append(f"{tool_name}: MISMATCHED agent {a}")
    
    return errors

def check_commands(canonical_dir, tools):
    """Check commands/prompts consistency."""
    errors = []
    
    canonical = {}
    cmds_path = os.path.join(canonical_dir, 'opencode', 'commands')
    if os.path.exists(cmds_path):
        for f in os.listdir(cmds_path):
            if f.endswith('.md') and f != 'README.md':
                canonical[f.replace('.md', '')] = get_hash(os.path.join(cmds_path, f))
    
    print(f"\nCanonical commands: {len(canonical)}")
    
    # Antigravity uses .toml format — skip command validation for it
    skip_tools = {'antigravity'}
    
    for tool_name, config in tools.items():
        if tool_name in skip_tools:
            print(f"  {tool_name}: SKIPPED (uses .toml format)")
            continue
        
        items = {}
        
        cmds_dir = config['commands_dir']
        if os.path.exists(cmds_dir):
            for f in os.listdir(cmds_dir):
                if f.endswith('.md') and f != 'README.md':
                    name = f.replace('.md', '')
                    items[name] = get_hash(os.path.join(cmds_dir, f))
        
        missing = set(canonical.keys()) - set(items.keys())
        mismatched = []
        for cmd in set(canonical.keys()) & set(items.keys()):
            if canonical[cmd] != items[cmd]:
                mismatched.append(cmd)
        
        status = "OK" if not missing and not mismatched else "ISSUES"
        print(f"  {tool_name}: {len(items)} commands — {status}")
        
        if missing:
            for c in sorted(missing):
                errors.append(f"{tool_name}: MISSING command {c}")
        if mismatched:
            for c in sorted(mismatched):
                errors.append(f"{tool_name}: MISMATCHED command {c}")
    
    return errors
