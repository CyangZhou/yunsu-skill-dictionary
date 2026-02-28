# 🌏 CloudShu Dictionary Skills: An Open Standard for AI Capabilities
> **云舒字典技能：为 AI 打造的原子能力标准库**

---

## 🚀 摘要 (Executive Summary)

**CloudShu Dictionary** 是一个基于“五行哲学”构建的、高度模块化的 AI 技能生态系统。它打破了传统 AI Agent 复杂的调用链路，通过**“单字即能力”**（Single Character as Capability）的极简设计，让 AI 的每一次行动都像查字典一样精准、高效。

我们正在构建一个**开放的技能标准**，诚邀全球开发者共同参与，丰富这本属于 AI 时代的“新华字典”。

---

## ⚡ 快速开始 (Quick Start)

### 获取字典
```bash
git clone https://github.com/CyangZhou/yunsu-skill-dictionary.git
cd yunsu-skill-dictionary
```

### 使用技能
直接调用 Python 脚本即可，无需安装复杂依赖（仅需 Python 3.x）：
```bash
# 示例：调用【搜】技能
python .trae/skills/dictionary/water_knowledge/搜/scripts/main.py --input '{"query": "Trae IDE"}'
```

---

## ☯️ 核心哲学 (Core Philosophy)

### 1. 单字即能力 (Atomic Design)
我们将复杂的软件工程能力解构为最基本的原子操作，并用单字命名：
- **搜 (Search)**: 信息的获取。
- **读 (Read)**: 知识的摄入。
- **写 (Write)**: 内容的创造。
- **判 (Judge)**: 逻辑的诊断。
- **管 (Manage)**: 系统的治理。
- **改 (Modify)**: 状态的优化。

### 2. 五行分类 (Five Elements Taxonomy)
所有技能遵循五行生克关系进行组织，确保生态的有序演进：
- **💧 水 (Water - Knowledge)**: 滋润万物，对应信息的流动（搜、读）。
- **🌲 木 (Wood - Creation)**: 生机勃勃，对应代码的生成（写、创）。
- **🔥 火 (Fire - Analysis)**: 洞察秋毫，对应问题的诊断（判、测）。
- **🌏 土 (Earth - Infrastructure)**: 厚德载物，对应环境的支撑（管、部）。
- **⚔️ 金 (Metal - Optimization)**: 变革重塑，对应系统的重构（改、优）。

### 3. 原生调用 (Native Execution)
拒绝黑盒。每个技能都是一个独立的、标准的 Python 包，拥有统一的 `scripts/main.py` 入口。AI Agent 甚至无需安装额外依赖，只需“查字典”即可调用。

---

## 📖 技能图谱 (Skill Registry)

| 五行 | 技能 (Skill) | 描述 (Description) | 典型指令 |
| :--- | :--- | :--- | :--- |
| **[水]** | **搜** | 网络搜索与文档检索 | `查一下 Rust 的最新版本特性` |
| **[水]** | **读** | 读取文件或网页内容 | `读取这个页面的核心内容` |
| **[木]** | **写** | 写入文件或生成代码 | `写一个 Python 的 Hello World` |
| **[火]** | **判** | 错误诊断与代码分析 | `分析这个脚本为什么报错` |
| **[土]** | **管** | 依赖管理与环境配置 | `安装 requests 库` |
| **[金]** | **改** | 代码重构与安全加固 | `把这段代码重构得更优雅` |

---

## 🤝 共建计划 (Co-creation Manifesto)

这就好比编纂一部 AI 时代的《康熙字典》，一个人的力量是有限的。我们需要你！

### 如何参与？
1.  **Fork & Clone**: 从 [GitHub](https://github.com/CyangZhou/yunsu-skill-dictionary) 克隆项目。
2.  **提交新字**: 发现了一个缺失的能力？提交一个 PR，创建一个新的“单字”技能。
    *   *例如：添加 [测] (Test) 到火系，用于自动化测试。*
3.  **优化释义**: 现有的技能逻辑不够强？优化 `scripts/main.py`，让它更聪明。
4.  **编纂成语**: 将多个单字组合成“成语”（Workflow），解决复杂场景。
    *   *例如：[日新月异] = 搜(最新库) + 改(升级依赖) + 测(运行测试)*

### 开发者工具
我们提供了 **元技能 (Skill Creator)**，一键生成标准模版：
```bash
python .trae/skills/agent-skill-creator/scripts/generate_skill.py --name "新" --category "wood_creation" --description "创新实验"
```

---

> **Let's define the vocabulary of the future AI.**
> **让我们共同定义未来 AI 的词汇表。**
