---
name: 写
description: 文件写入与代码生成
version: 1.0.0
category: wood_creation
disable-model-invocation: false
---

# 写 (Skill)

**Description:** 文件写入与代码生成

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
