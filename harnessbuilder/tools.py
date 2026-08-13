"""Per-tool naming rules and configuration."""

REPO_ROOT = None  # Set by sync-everything.py

TOOLS = {
    'opencode': {
        'skills_dir': 'opencode/skills',
        'agents_dir': 'opencode/agents',
        'commands_dir': 'opencode/commands',
        'skill_case': 'kebab',
        'agent_case': 'snake',
        'cmd_format': 'md',
        'allowed_tools_case': 'lower',
        'allowed_tools_format': 'comma',
    },
    'claude': {
        'skills_dir': 'claude/skills',
        'agents_dir': 'claude/agents',
        'commands_dir': 'claude/commands',
        'skill_case': 'snake',
        'agent_case': 'snake',
        'cmd_format': 'md',
        'allowed_tools_case': 'pascal',
        'allowed_tools_format': 'space',
    },
    'pi': {
        'skills_dir': 'pi/agent/skills',
        'agents_dir': 'pi/agent/agents',
        'commands_dir': 'pi/agent/prompts',
        'skill_case': 'kebab',
        'agent_case': 'snake',
        'cmd_format': 'md',
        'allowed_tools_case': 'lower',
        'allowed_tools_format': 'yaml',
    },
    'wocode': {
        'skills_dir': 'wocode/agent/skills',
        'agents_dir': 'wocode/agent/agents',
        'commands_dir': 'wocode/agent/prompts',
        'skill_case': 'kebab',
        'agent_case': 'snake',
        'cmd_format': 'md',
        'allowed_tools_case': 'lower',
        'allowed_tools_format': 'comma',
    },
    'antigravity': {
        'skills_dir': 'antigravity/skills',
        'agents_dir': 'antigravity/agents',
        'commands_dir': 'antigravity/commands',
        'skill_case': 'snake',
        'agent_case': 'snake',
        'cmd_format': 'toml',
        'allowed_tools_case': 'lower',
        'allowed_tools_format': 'comma',
    },
    'codex': {
        'skills_dir': 'codex/skills',
        'agents_dir': 'codex/agents',
        'commands_dir': 'codex/commands',
        'skill_case': 'snake',
        'agent_case': 'snake',
        'cmd_format': 'md',
        'allowed_tools_case': 'lower',
        'allowed_tools_format': 'yaml',
    },
}

def to_kebab(name):
    return name.replace('_', '-')

def to_snake(name):
    return name.replace('-', '_')

def adapt_name(name, target_case):
    if target_case == 'kebab':
        return to_kebab(name)
    else:
        return to_snake(name)

def adapt_frontmatter(content, target_tool):
    """Adapt frontmatter to match target tool's conventions."""
    tool = TOOLS[target_tool]
    lines = content.split('\n')
    result = []
    in_frontmatter = False
    
    for line in lines:
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            result.append(line)
            continue
        
        if in_frontmatter:
            # Adapt name field
            if line.startswith('name:'):
                old_name = line.split(':', 1)[1].strip()
                new_name = adapt_name(old_name, tool['skill_case'])
                result.append(f'name: {new_name}')
                continue
            
            # Adapt allowed-tools
            if line.startswith('allowed-tools:'):
                tools_str = line.split(':', 1)[1].strip()
                tools_list = [t.strip() for t in tools_str.replace(',', ' ').split()]
                
                if tool['allowed_tools_case'] == 'pascal':
                    adapted = [t.capitalize() for t in tools_list]
                else:
                    adapted = [t.lower() for t in tools_list]
                
                if tool['allowed_tools_format'] == 'yaml':
                    result.append('allowed-tools:')
                    for t in adapted:
                        result.append(f'  - {t}')
                elif tool['allowed_tools_format'] == 'space':
                    result.append(f'allowed-tools: {" ".join(adapted)}')
                else:  # comma
                    result.append(f'allowed-tools: {",".join(adapted)}')
                continue
        
        result.append(line)
    
    return '\n'.join(result)
