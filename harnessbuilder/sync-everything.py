#!/usr/bin/env python3
"""harnessbuilder — Sync canonical sources to all 6 tools.

Usage:
    python3 harnessbuilder/sync-everything.py [--dry-run] [--validate-only]
"""

import os
import sys
import shutil
import subprocess

# Add repo root to path
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from harnessbuilder.tools import TOOLS, adapt_name, adapt_frontmatter, to_kebab, to_snake
from harnessbuilder.validate import check_skills, check_agents, check_commands

def log(msg):
    print(f"  {msg}")

def sync_skills(dry_run=False):
    """Sync canonical skills to all 6 tools."""
    canonical_dir = os.path.join(REPO_ROOT, 'skills')
    count = 0
    
    for skill_name in os.listdir(canonical_dir):
        canonical_path = os.path.join(canonical_dir, skill_name, 'SKILL.md')
        if not os.path.isfile(canonical_path):
            continue
        
        with open(canonical_path, 'r') as f:
            content = f.read()
        
        for tool_name, config in TOOLS.items():
            target_dir = config['skills_dir']
            dir_name = adapt_name(skill_name, config['skill_case'])
            dest_path = os.path.join(REPO_ROOT, target_dir, dir_name, 'SKILL.md')
            
            adapted = adapt_frontmatter(content, tool_name)
            
            if os.path.exists(dest_path):
                with open(dest_path, 'r') as f:
                    existing = f.read()
                if existing == adapted:
                    continue
            
            if not dry_run:
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                with open(dest_path, 'w') as f:
                    f.write(adapted)
            
            count += 1
            log(f"{'WOULD' if dry_run else 'SYNCED'} skill {skill_name} → {tool_name}/{dir_name}")
    
    return count

def sync_agents(dry_run=False):
    """Sync canonical agents to all 6 tools."""
    canonical_dir = os.path.join(REPO_ROOT, 'opencode', 'agents')
    count = 0
    
    for agent_file in os.listdir(canonical_dir):
        if not agent_file.endswith('.md') or agent_file == 'README.md':
            continue
        
        canonical_path = os.path.join(canonical_dir, agent_file)
        with open(canonical_path, 'r') as f:
            content = f.read()
        
        for tool_name, config in TOOLS.items():
            target_dir = config['agents_dir']
            dest_path = os.path.join(REPO_ROOT, target_dir, agent_file)
            
            if os.path.exists(dest_path):
                with open(dest_path, 'r') as f:
                    existing = f.read()
                if existing == content:
                    continue
            
            if not dry_run:
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                with open(dest_path, 'w') as f:
                    f.write(content)
            
            count += 1
            log(f"{'WOULD' if dry_run else 'SYNCED'} agent {agent_file} → {tool_name}")
    
    return count

def sync_commands(dry_run=False):
    """Sync canonical commands to all 6 tools."""
    canonical_dir = os.path.join(REPO_ROOT, 'opencode', 'commands')
    count = 0
    
    for cmd_file in os.listdir(canonical_dir):
        if not cmd_file.endswith('.md') or cmd_file == 'README.md':
            continue
        
        canonical_path = os.path.join(canonical_dir, cmd_file)
        with open(canonical_path, 'r') as f:
            content = f.read()
        
        cmd_name = cmd_file.replace('.md', '')
        
        for tool_name, config in TOOLS.items():
            target_dir = config['commands_dir']
            
            if config['cmd_format'] == 'toml':
                # Antigravity uses .toml with run- prefix and snake_case
                dest_name = f"run-{to_snake(cmd_name)}.toml"
                # Create minimal TOML delegation
                toml_content = f'description = "{cmd_name.replace("-", " ").title()}"\nprompt = "Activate the `{cmd_name}` skill."\n'
                dest_content = toml_content
            else:
                dest_name = cmd_file
                dest_content = content
            
            dest_path = os.path.join(REPO_ROOT, target_dir, dest_name)
            
            # Skip if already exists with different content (antigravity has its own format)
            if os.path.exists(dest_path):
                with open(dest_path, 'r') as f:
                    existing = f.read()
                if existing == dest_content:
                    continue
                # For antigravity .toml files, don't overwrite existing ones
                if config['cmd_format'] == 'toml' and dest_name.endswith('.toml'):
                    continue
            
            if not dry_run:
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                with open(dest_path, 'w') as f:
                    f.write(dest_content)
            
            count += 1
            log(f"{'WOULD' if dry_run else 'SYNCED'} command {cmd_name} → {tool_name}/{dest_name}")
    
    return count

def rebuild_manifest():
    """Rebuild manifest.json from YAMLs."""
    compile_script = os.path.join(REPO_ROOT, 'config-manifest', 'compile.py')
    result = subprocess.run(
        ['python3', compile_script],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"ERROR: compile.py failed:\n{result.stderr}")
        return False
    log("Manifest rebuilt successfully")
    return True

def validate():
    """Validate all 6 tools match canonical."""
    from harnessbuilder.tools import TOOLS as tool_config
    
    errors = []
    errors.extend(check_skills(REPO_ROOT, tool_config))
    errors.extend(check_agents(REPO_ROOT, tool_config))
    errors.extend(check_commands(REPO_ROOT, tool_config))
    
    return errors

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Sync canonical sources to all 6 tools')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be synced')
    parser.add_argument('--validate-only', action='store_true', help='Only validate, don\'t sync')
    args = parser.parse_args()
    
    print("=" * 60)
    print("harnessbuilder — Syncing canonical → all 6 tools")
    print("=" * 60)
    
    if args.validate_only:
        print("\nValidating...")
        errors = validate()
        if errors:
            print(f"\nERRORS: {len(errors)}")
            for e in errors:
                print(f"  ✗ {e}")
            sys.exit(1)
        else:
            print("\nAll tools consistent ✓")
            sys.exit(0)
    
    print("\nSyncing skills...")
    skill_count = sync_skills(dry_run=args.dry_run)
    log(f"Skills synced: {skill_count}")
    
    print("\nSyncing agents...")
    agent_count = sync_agents(dry_run=args.dry_run)
    log(f"Agents synced: {agent_count}")
    
    print("\nSyncing commands...")
    cmd_count = sync_commands(dry_run=args.dry_run)
    log(f"Commands synced: {cmd_count}")
    
    if not args.dry_run:
        print("\nRebuilding manifest...")
        rebuild_manifest()
    
    print("\nValidating...")
    errors = validate()
    
    if errors:
        print(f"\nERRORS: {len(errors)}")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print(f"\nDone. {skill_count + agent_count + cmd_count} files synced, 0 errors ✓")
        sys.exit(0)

if __name__ == '__main__':
    main()
