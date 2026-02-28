---
name: 读
description: 文件读取与网页抓取
version: 1.0.0
category: water_knowledge
disable-model-invocation: false
---

# 读 (Skill)

**Description:** 文件读取与网页抓取

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
