# 输出格式约定

## 这是什么 / 何时加载

本文件定义了仓库中"金版剧本产物"（golden screenplay artifacts）的最低 Markdown 交付格式约定。

这不是某种"唯一正确的剧本格式"声明，而是仓库层面的交接规则——确保示例、路径、评审和回归检查都指向同一套结构标准。

**Agent 应在以下时机加载本文件：**

- **生成产物之前**——确认待生成的输出类型有哪些必填章节、标签和结构要求。本文列出的五种输出类型（`beat_sheet`、`commercial_script`、`interactive_branch_map`、`scene_draft`、`screenplay_draft`）均由 [`output-format-contracts.json`](./output-format-contracts.json) 进行机器检查。
- **完成产物、准备返回给用户之前**——对照本文件逐项检查产物结构是否完整，确保格式合规后再交付。

配合以下参考一起使用：
- [`references/supported-outputs.md`](./supported-outputs.md) —— 了解每种输出的用途和适用场景；
- `examples/golden/*/route.json` 中的 `output` 字段 —— 查看各路径选择了哪个格式约定；
- [`references/output-format-contracts.json`](./output-format-contracts.json) —— 机器执行格式检查的规则文件。

## 机器检查的格式约定

### `beat_sheet`

- H1 标题必须包含 `Beat Sheet`。
- 必填 H2 章节：
  - `Story Engine`（故事引擎）
  - `Beat List`（节拍列表）
- 每个必填章节必须以列表条目呈现，不能只有松散段落。
- 机器检查要求：`Story Engine` 最少 3 条，`Beat List` 最少 4 条。

### `commercial_script`

- H1 标题必须包含 `Commercial Script`。
- 必填 H2 章节：
  - `Core Message`（核心信息）
  - `Shot Flow`（镜头流）
  - `CTA`（行动号召）
- 文档必须让核心信息、执行流程、行动呼声三部分各自独立可识别，不能互相淹没。
- 机器检查要求：`Core Message` 最少 3 条，`Shot Flow` 最少 4 条，`CTA` 最少 1 条。

### `interactive_branch_map`

- H1 标题必须包含 `Interactive Branch Map`。
- 必填 H2 章节：
  - `Player Goal`（玩家目标）
  - `State Variables`（状态变量）
  - `Branches`（分支）
  - `Convergence Plan`（收束计划）
- 文档必须暴露：玩家目标、被追踪的状态变量、各分支的差异，以及结构如何收束。
- 机器检查要求：`Player Goal` 最少 1 条，`State Variables` 最少 2 条，`Branches` 最少 3 条，`Convergence Plan` 最少 1 条。

### `scene_draft`

- H1 标题必须包含 `Scene Draft`。
- 必填 H2 章节：
  - `Scene Objective`（场景目标）
  - `Script Blocks`（剧本块）
- `Script Blocks` 章节将由机器作为"带标签的剧本流"（labeled screenplay stream）进行检查。
- 每个场景必须声明 `Scene`（场景编号/标题）、`Purpose`（目的）和至少一个 `Action`（动作）。
- 对话节拍不能是裸对话（bare dialogue）。每一段对话必须携带内联的 `Performance:` 或 `Action:` 表演指导，或前面紧邻一行 `Action:` 动作描述。
- `VFX` / `SFX` / `BGM` 为可选项，但如果使用，必须以固定标签形式出现，不能写成自由文字描述。
- 机器检查要求：`Scene Objective` 最少 3 条，`Script Blocks` 最少 6 条；至少包含 1 个场景和 2 个对话节拍；每个场景必须有 `Scene`、`Purpose`、`Action` 标签。

### `screenplay_draft`

- H1 标题必须包含 `Screenplay Draft`。
- 必填 H2 章节：
  - `Story Engine`（故事引擎）
  - `Script Blocks`（剧本块）
- `Script Blocks` 章节将由机器作为"多场景带标签剧本流"（multi-scene labeled screenplay stream）进行检查。
- 产物必须包含至少两个场景，以及足够证明其可读、可演级别的对话节拍数。
- 每个场景必须声明 `Scene`（场景编号/标题）、`Purpose`（目的）和至少一个 `Action`（动作）。
- 对话节拍不能是裸对话。每一段对话必须携带内联的 `Performance:` 或 `Action:` 表演指导，或前面紧邻一行 `Action:` 动作描述。
- `VFX` / `SFX` / `BGM` 为可选项，但如果使用，必须以固定标签形式出现，不能写成自由文字描述。
- 机器检查要求：`Story Engine` 最少 3 条，`Script Blocks` 最少 12 条；至少包含 2 个场景和 4 个对话节拍；每个场景必须有 `Scene`、`Purpose`、`Action` 标签。

## 范围说明

当前格式约定覆盖仓库的金版示例产出。后续可以扩展到更多输出类型，但新增格式规则应保持最小化和"约定优先"原则：

- 暴露产物的决策面（decision surface）；
- 避免把一个好的样本变成教条；
- 优先选择小而稳定的结构，而非冗长的模板。
