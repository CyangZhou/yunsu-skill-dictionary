# Dictionary Skill Refactoring Plan (字典技能重构计划 v3.0)

## 1. 核心理念 (Core Philosophy)
- **五行分类 (Five Elements)**: 使用木、火、土、金、水作为顶级分类，构建清晰的技能本体论。
- **辅助工具 (Auxiliary Tool)**: 移除所有 "Autonomous Agent" 自主运行逻辑，回归 IDE 辅助工具定位。
- **中文优先 (Chinese First)**: 技能定义、描述及对外暴露的接口以中文核心含义（单字/成语）为主。
- **Trae 原生集成**: 提供标准化的技能清单接口，让 Trae 能快速索引和调用。

## 2. 新架构设计 (New Architecture)

### 2.1 目录结构 (Directory Structure)
采用英文目录名以保证工程稳定性，但逻辑映射为中文分类。

```text
.trae/skills/dictionary/
├── core/                   # 核心引擎 (极简)
│   ├── skill.py            # BaseSkill 基类
│   ├── skill_loader.py     # 支持五行扫描的加载器
│   └── protocol.py         # 输入输出协议
├── wood_creation/          # [木] 创造系 (Creation)
│   ├── xie/                # [写] 对应 code_generator/writer
│   └── ...
├── fire_analysis/          # [火] 分析系 (Analysis)
│   ├── pan/                # [判] 对应 error_diagnosis
│   └── ...
├── earth_infrastructure/   # [土] 基建系 (Infrastructure)
│   ├── guan/               # [管] 对应 dependency_manager
│   └── ...
├── metal_optimization/     # [金] 优化系 (Optimization)
│   ├── gai/                # [改] 对应 refactor
│   └── ...
├── water_knowledge/        # [水] 知识系 (Knowledge)
│   ├── sou/                # [搜] 对应 doc_retrieval
│   └── ...
├── idioms/                 # [成语] 定制化组合技能
│   ├── ri_xin_yue_yi/      # [日新月异]
│   └── ...
└── main.py                 # 统一入口 (支持 --list)
```

### 2.2 技能定义规范
每个技能目录 (如 `sou/`) 下包含 `__init__.py` 和 `skill.py` (或 `main.py`)。
技能类必须包含元数据：
```python
class SouSkill(BaseSkill):
    name = "搜"
    category = "water_knowledge" # 水-知识系
    description = "网络与文档搜索技能"
    ...
```

## 3. 重构任务清单 (Tasks)

### Phase 1: 架构重塑 (Architecture Reshaping)
- [ ] **1.1 清理旧物**: 删除 `characters/`, `workflow/`, `retrieval/` 及相关残留代码。
- [ ] **1.2 建立五行**: 创建上述 5+1 个顶级目录。
- [ ] **1.3 升级加载器**: 修改 `SkillLoader` 以递归扫描这些特定目录。

### Phase 2: 引擎瘦身 (Engine Simplification)
- [ ] **2.1 移除 Workflow**: 删除 `WorkflowEngine`，不再维护复杂的 Session 状态。
- [ ] **2.2 增强 Main**: `main.py` 增加 `list_skills()` 功能，输出结构化的中文技能清单。

### Phase 3: 核心单字迁移 (Core Characters Migration)
将原计划的技能按五行归位：
- [ ] **3.1 水 - [搜] (sou)**: 原 `characters/sou` -> `water_knowledge/sou`
- [ ] **3.2 水 - [读] (du)**: 原 `characters/du` -> `water_knowledge/du`
- [ ] **3.3 木 - [写] (xie)**: 原 `characters/xie` -> `wood_creation/xie`
- [ ] **3.4 金 - [版] (ban)**: 原 `characters/ban` -> `metal_optimization/ban` (排版优化)

### Phase 4: 成语集成 (Idioms Integration)
- [ ] **4.1 成语 - [日新月异]**: 组合调用上述单字技能。

## 4. 交付物 (Deliverables)
- 一个干净的、分类明确的技能库。
- `python main.py --list` 能打印出漂亮的中文技能树。
