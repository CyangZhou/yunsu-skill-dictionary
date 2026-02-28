---
name: 判
description: 错误诊断与代码分析
version: 1.0.0
category: fire_analysis
disable-model-invocation: false
---

# 判 (Skill)

**Description:** 错误诊断与代码分析

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
