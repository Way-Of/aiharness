#!/usr/bin/env python3
"""Validate that all tools have identical skill content (modulo naming conventions)."""

import os
import sys
import hashlib

TOOLS = {
    'opencode': 'opencode/skills',
    'claude': 'claude/skills',
    'pi': 'pi/agent/skills',
    'wocode': 'wocode/agent/skills',
    'antigravity': 'antigravity/skills',
    'codex': 'codex/skills',
}

SNAKE_TOOLS = ['claude', 'antigravity', 'codex']

def normalize(name):
    """Normalize skill name to kebab-case for comparison."""
    return name.replace('_', '-')

def get_skill_content(path):
    """Read skill file and normalize for comparison (ignore expected per-tool differences)."""
    with open(path, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    normalized_lines = []
    in_frontmatter = False
    
    for line in lines:
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            normalized_lines.append(line)
            continue
        
        if in_frontmatter:
            # Normalize name field to kebab-case
            if line.startswith('name:'):
                name = line.split(':', 1)[1].strip().replace('_', '-')
                normalized_lines.append(f'name: {name}')
                continue
            
            # Normalize allowed-tools to lowercase (Claude uses PascalCase)
            if line.startswith('allowed-tools:'):
                tools_str = line.split(':', 1)[1].strip()
                # Convert PascalCase to lowercase for comparison
                normalized = ','.join(t.strip().lower() for t in tools_str.replace(' ', ',').split(','))
                normalized_lines.append(f'allowed-tools: {normalized}')
                continue
        
        normalized_lines.append(line)
    
    return '\n'.join(normalized_lines)

def main():
    errors = []
    warnings = []
    
    # Get all canonical skills
    canonical_dir = 'skills'
    canonical_skills = {}
    for skill in os.listdir(canonical_dir):
        skill_path = os.path.join(canonical_dir, skill, 'SKILL.md')
        if os.path.isfile(skill_path):
            canonical_skills[skill] = get_skill_content(skill_path)
    
    print(f"Canonical skills: {len(canonical_skills)}")
    
    # Check each tool
    for tool, base_path in TOOLS.items():
        if not os.path.exists(base_path):
            errors.append(f"{tool}: directory not found")
            continue
        
        tool_skills = {}
        for skill_dir in os.listdir(base_path):
            skill_path = os.path.join(base_path, skill_dir, 'SKILL.md')
            if os.path.isfile(skill_path):
                tool_skills[normalize(skill_dir)] = get_skill_content(skill_path)
        
        # Check missing skills
        missing = set(canonical_skills.keys()) - set(tool_skills.keys())
        for skill in sorted(missing):
            errors.append(f"{tool}: MISSING skill {skill}")
        
        # Check content mismatches
        for skill in sorted(set(canonical_skills.keys()) & set(tool_skills.keys())):
            canonical_hash = hashlib.md5(canonical_skills[skill].encode()).hexdigest()
            tool_hash = hashlib.md5(tool_skills[skill].encode()).hexdigest()
            if canonical_hash != tool_hash:
                warnings.append(f"{tool}: content differs for {skill} (may be naming difference)")
        
        # Check extra skills (not in canonical)
        extras = set(tool_skills.keys()) - set(canonical_skills.keys())
        if extras:
            warnings.append(f"{tool}: has {len(extras)} extra skills not in canonical: {sorted(extras)}")
        
        print(f"{tool}: {len(tool_skills)} skills")
    
    # Check agent consistency
    print("\n=== Agent Consistency ===")
    agent_files = ['coder.md', 'reviewer.md', 'planner.md', 'scout.md', 'debugger.md', 'github.md']
    for agent_file in agent_files:
        agent_name = agent_file.replace('.md', '')
        agent_status = {}
        for tool, base_path in TOOLS.items():
            agent_path = os.path.join(base_path.replace('/skills', '/agents'), agent_file)
            if os.path.isfile(agent_path):
                with open(agent_path, 'r') as f:
                    content = f.read()
                agent_status[tool] = 'Code Traceability' in content
        
        if agent_status:
            tools_with = [t for t, v in agent_status.items() if v]
            tools_without = [t for t, v in agent_status.items() if not v]
            if tools_without and tools_with:
                errors.append(f"agent/{agent_name}: traceability in {tools_with} but MISSING in {tools_without}")
            elif tools_without and not tools_with:
                warnings.append(f"agent/{agent_name}: no traceability in any tool")
    
    # Check skill content consistency (compare canonical to each tool)
    print("\n=== Skill Content Consistency ===")
    for skill in sorted(canonical_skills.keys()):
        canonical_hash = hashlib.md5(canonical_skills[skill].encode()).hexdigest()
        for tool, base_path in TOOLS.items():
            if tool in SNAKE_TOOLS:
                dir_name = skill.replace('-', '_')
            else:
                dir_name = skill
            skill_path = os.path.join(base_path, dir_name, 'SKILL.md')
            if os.path.isfile(skill_path):
                tool_hash = hashlib.md5(get_skill_content(skill_path).encode()).hexdigest()
                if canonical_hash != tool_hash:
                    errors.append(f"{tool}/{skill}: content does NOT match canonical")
    
    # Summary
    print(f"\n{'='*50}")
    if errors:
        print(f"ERRORS: {len(errors)}")
        for e in errors:
            print(f"  ✗ {e}")
    if warnings:
        print(f"WARNINGS: {len(warnings)}")
        for w in warnings:
            print(f"  ⚠ {w}")
    if not errors and not warnings:
        print("ALL TOOLS IDENTICAL ✓")
    
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
