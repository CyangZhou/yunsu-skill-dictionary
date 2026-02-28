---
name: 搜
description: 网络与文档搜索技能
version: 1.0.0
category: water_knowledge
disable-model-invocation: false
---

# 搜 (Skill)

**Description:** 网络与文档搜索技能

## Usage

### Invocation
This skill is invoked by running the Python script in the `scripts/` directory.

```bash
python scripts/main.py --input '{"key": "value"}'
```

### Parameters
The input should be a JSON string.
- `input` (JSON string): The input parameters for this skill.

## Output
Returns a JSON object with `status` and `data`.
