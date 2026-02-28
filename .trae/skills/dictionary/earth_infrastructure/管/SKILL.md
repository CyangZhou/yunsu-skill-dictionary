---
name: 管
description: 依赖管理与环境配置
version: 1.0.0
category: earth_infrastructure
disable-model-invocation: false
---

# 管 (Skill)

**Description:** 依赖管理与环境配置

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
