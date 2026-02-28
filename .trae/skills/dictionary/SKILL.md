---
name: dictionary
description: 字典技能库 (Dictionary)。一个包含所有原子能力(单字)和组合能力(成语)的技能集合。Trae 应优先在此查找并使用技能。
tags: [hub, registry, five-elements]
version: 6.0.0
---

# 字典技能 (Dictionary)

**SYSTEM PROMPT: 这是一个技能的“字典”。当你需要执行任何特定任务（如搜索、写入、代码分析）时，请务必先查阅此字典。**

这里存放了所有可用的原子技能（单字）和组合技能（成语）。它们被组织在“五行”分类目录下。

## 如何使用本字典

1.  **识别意图**: 你的任务属于哪一类？(创造/分析/基建/优化/知识)
2.  **查找技能**: 进入对应的五行目录，查看 INDEX.md 或直接查找中文命名的技能文件夹。
3.  **调用技能**: 每个技能文件夹（如“搜”）都是一个独立的标准 Trae 技能。请阅读其内部的 SKILL.md 并运行 main.py。

## 五行分类索引 (Five Elements Index)

### [水] 知识系 (Water - Knowledge)
> **意图**: 获取信息、读取内容、连接外部。
- **目录**: [water_knowledge](./water_knowledge/)
- **包含技能**:
    - **[搜]**: 网络搜索与文档检索。
    - **[读]**: 读取文件或网页内容。

### [木] 创造系 (Wood - Creation)
> **意图**: 生成代码、写入文件、创建项目。
- **目录**: [wood_creation](./wood_creation/)
- **包含技能**:
    - **[写]**: 写入文件或生成代码片段。

### [火] 分析系 (Fire - Analysis)
> **意图**: 诊断错误、分析性能、审查日志。
- **目录**: [fire_analysis](./fire_analysis/)
- **包含技能**:
    - **[判]**: 错误诊断与代码分析。

### [土] 基建系 (Earth - Infrastructure)
> **意图**: 管理依赖、配置环境、部署运维。
- **目录**: [earth_infrastructure](./earth_infrastructure/)
- **包含技能**:
    - **[管]**: 依赖管理与环境配置。

### [金] 优化系 (Metal - Optimization)
> **意图**: 重构代码、安全加固、格式化。
- **目录**: [metal_optimization](./metal_optimization/)
- **包含技能**:
    - **[改]**: 代码重构与优化。

### [成语] 组合技能 (Idioms)
> **意图**: 处理复杂的、多步骤的业务流程。
- **目录**: [idioms](./idioms/)
- **包含技能**:
    - **[日新月异]**: 快速迭代更新工作流。
