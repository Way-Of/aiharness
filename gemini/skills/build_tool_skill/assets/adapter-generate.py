#!/usr/bin/env python3
"""
Platform adapter generator for canonical skills.
Migrated from skill-adapter.

Generates per-tool skill directories from the canonical source at
packages/@aiengineeringharness/skills/<skill>/ for each of the 7 AI tools.

Usage:
    python3 adapter-generate.py                          # Generate all skills for all tools
    python3 adapter-generate.py --skill=example-skill     # Single skill
    python3 adapter-generate.py --tool=opencode           # Single tool
    python3 adapter-generate.py --dry-run                 # Preview only
"""

import os
import sys
import shutil
import re

HARNESS_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "..")
HARNESS_ROOT = os.path.abspath(HARNESS_ROOT)
CANONICAL_DIR = os.path.join(HARNESS_ROOT, "skills")

# Per-tool path mapping: (directory_prefix, naming_transform)
TOOL_PATHS = {
    "opencode": ("opencode/skills", lambda n: n),                    # kebab → kebab
    "claude": ("claude/skills", lambda n: n.replace("-", "_")),     # kebab → snake
    "gemini": ("gemini/skills", lambda n: n.replace("-", "_")),     # kebab → snake
    "pi": ("pi/agent/skills", lambda n: n),                          # kebab → kebab
    "wocode": ("wocode/agent/skills", lambda n: n),                          # kebab → kebab
    "codex": ("codex/skills", lambda n: n.replace("-", "_")),       # kebab → snake
    "antigravity": ("antigravity/skills", lambda n: n.replace("-", "_")), # kebab → snake
}

SKIP_SKILLS = {"README.md"}


def generate(tool_filter=None, skill_filter=None, dry_run=False):
    if not os.path.isdir(CANONICAL_DIR):
        print(f"Canonical skills directory not found: {CANONICAL_DIR}")
        sys.exit(1)

    skills = sorted(d for d in os.listdir(CANONICAL_DIR)
                    if os.path.isdir(os.path.join(CANONICAL_DIR, d)) and d not in SKIP_SKILLS)

    if skill_filter:
        skills = [s for s in skills if s == skill_filter]

    tools = list(TOOL_PATHS.keys())
    if tool_filter:
        tools = [t for t in tools if t == tool_filter]

    for skill in skills:
        canonical_skill = os.path.join(CANONICAL_DIR, skill)
        for tool in tools:
            prefix, transform = TOOL_PATHS[tool]
            dir_name = transform(skill)
            target_dir = os.path.join(HARNESS_ROOT, prefix, dir_name)
            target_skill = os.path.join(target_dir, "SKILL.md")

            action = "update" if os.path.exists(target_skill) else "create"
            if dry_run:
                print(f"[{tool}] {action} {prefix}/{dir_name}/SKILL.md")
                continue

            os.makedirs(target_dir, exist_ok=True)
            os.makedirs(os.path.join(target_dir, "assets"), exist_ok=True)
            os.makedirs(os.path.join(target_dir, "platform"), exist_ok=True)

            shutil.copy2(os.path.join(canonical_skill, "SKILL.md"),
                         os.path.join(target_dir, "SKILL.md"))

            # Codex: also generate skill.yaml + prompt.md from SKILL.md
            if tool == "codex":
                skill_md_path = os.path.join(target_dir, "SKILL.md")
                skill_yaml_path = os.path.join(target_dir, "skill.yaml")
                prompt_md_path = os.path.join(target_dir, "prompt.md")
                with open(skill_md_path) as f:
                    content = f.read()
                # Parse frontmatter
                if content.startswith("---"):
                    end = content.find("---", 3)
                    if end != -1:
                        fm_str = content[3:end].strip()
                        body = content[end+3:].strip()
                        # Convert allowed-tools to tools list
                        fm_lines = []
                        for line in fm_str.split("\n"):
                            if line.startswith("allowed-tools:"):
                                tools_str = line.split(":", 1)[1].strip()
                                tool_names = [t.strip().lower() for t in re.split(r"[\s,]+", tools_str) if t.strip()]
                                fm_lines.append("tools:")
                                for t in tool_names:
                                    fm_lines.append(f"  - {t}")
                            elif line.startswith("name:"):
                                fm_lines.append(line.replace("-", "_").replace("name: ", "name: ").rstrip())
                            else:
                                fm_lines.append(line)
                        fm_lines.append("version: 1.0.0")
                        with open(skill_yaml_path, "w") as f:
                            f.write("\n".join(fm_lines) + "\n")
                        with open(prompt_md_path, "w") as f:
                            f.write(f"> **Platform**: Codex | **Skill**: {dir_name} | **Version**: 1.0.0\n")
                            f.write(f">\n")
                            f.write(f"> _Auto-generated from canonical format. Do not edit directly._\n\n")
                            f.write(body + "\n")

            # Copy assets/
            src_assets = os.path.join(canonical_skill, "assets")
            if os.path.isdir(src_assets):
                for f in os.listdir(src_assets):
                    src_file = os.path.join(src_assets, f)
                    if os.path.isfile(src_file):
                        shutil.copy2(src_file,
                                     os.path.join(target_dir, "assets", f))

            print(f"[{tool}] {action} {prefix}/{dir_name}/ ({'updated' if action == 'update' else 'created'})")


def main():
    args = sys.argv[1:]
    tool_filter = None
    skill_filter = None
    dry_run = "--dry-run" in args

    for arg in args:
        if arg.startswith("--tool="):
            tool_filter = arg.split("=", 1)[1]
        elif arg.startswith("--skill="):
            skill_filter = arg.split("=", 1)[1]

    generate(tool_filter, skill_filter, dry_run)


if __name__ == "__main__":
    main()
