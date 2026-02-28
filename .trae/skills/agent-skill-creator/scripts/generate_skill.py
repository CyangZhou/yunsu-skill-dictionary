import os
import sys
import argparse
import json
import datetime
from pathlib import Path

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def generate_standard_skill_md(name, description, category):
    """Generate SKILL.md adhering to Claude Skill Standard (Clean)"""
    return f"""---
name: {name}
description: {description}
version: 1.0.0
category: {category}
disable-model-invocation: false
---

# {name} (Skill)

**Description:** {description}

## Usage

### Invocation
This skill is invoked by running the Python script in the `scripts/` directory.

```bash
python scripts/main.py --input '{{"key": "value"}}'
```

### Parameters
The input should be a JSON string.
- `input` (JSON string): The input parameters for this skill.

## Output
Returns a JSON object with `status` and `data`.
"""

def generate_standard_main_py(name, description):
    """Generate scripts/main.py for a native skill (Clean)"""
    return f"""import sys
import json
import argparse
import traceback

def execute_logic(params):
    \"\"\"
    Core logic for {name}.
    Replace this with actual implementation.
    \"\"\"
    print(f"Executing {name} with params: {{params}}")
    
    # TODO: Implement {description}
    return {{
        "message": f"Successfully executed {name}",
        "input_received": params
    }}

def main():
    parser = argparse.ArgumentParser(description="{name}: {description}")
    parser.add_argument('--input', help='JSON input parameters', default='{{}}')
    args = parser.parse_args()
    
    try:
        params = json.loads(args.input)
        result = execute_logic(params)
        print(json.dumps({{"status": "success", "data": result}}, ensure_ascii=False, indent=2))
    except Exception as e:
        error_res = {{
            "status": "error",
            "message": str(e),
            "traceback": traceback.format_exc()
        }}
        print(json.dumps(error_res, ensure_ascii=False))
        sys.exit(1)

if __name__ == "__main__":
    main()
"""

def update_index_file(root_dir, category, name, description):
    """Update or create INDEX.md in the category directory (Clean)."""
    index_path = Path(root_dir) / category / "INDEX.md"
    
    # Create header if not exists
    if not index_path.exists():
        index_path.parent.mkdir(parents=True, exist_ok=True)
        content = f"# {category} Index\n\n- Skill: Name of the skill\n- Description: What it does\n- Path: Link to skill directory\n\n"
        index_path.write_text(content, encoding="utf-8")
    
    # Append new entry (List format instead of Table)
    # Using relative path to the skill directory
    entry = f"- **[{name}](./{name}/)**: {description}\n"
    
    # Check for duplicates
    current_content = index_path.read_text(encoding="utf-8")
    if f"- **[{name}](./{name}/)**" not in current_content:
        with open(index_path, "a", encoding="utf-8") as f:
            f.write(entry)

def main():
    parser = argparse.ArgumentParser(description="Agent Skill Creator - Clean Standard v7.0")
    parser.add_argument("--name", required=True, help="Skill Name (Chinese, e.g. 搜)")
    parser.add_argument("--category", required=True, help="Category (e.g. water_knowledge)")
    parser.add_argument("--description", required=True, help="Description")
    parser.add_argument("--output", required=True, help="Output directory root (.trae/skills/dictionary)")
    
    args = parser.parse_args()
    
    print(f"[Creator] Generating Clean Skill: {args.name} in {args.category}...")
    
    # 1. Determine Paths
    root_dir = Path(args.output)
    skill_dir = root_dir / args.category / args.name
    scripts_dir = skill_dir / "scripts"
    
    skill_dir.mkdir(parents=True, exist_ok=True)
    scripts_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. Generate Content
    skill_md = generate_standard_skill_md(args.name, args.description, args.category)
    main_py = generate_standard_main_py(args.name, args.description)
    
    # 3. Write Files
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
    (scripts_dir / "main.py").write_text(main_py, encoding="utf-8")
    (skill_dir / "requirements.txt").touch()
    
    # 4. Update Sub-Index
    update_index_file(root_dir, args.category, args.name, args.description)
    
    print(f"Generated successfully at: {skill_dir}")
    print(f"Index updated: {args.category}/INDEX.md")

if __name__ == "__main__":
    main()
