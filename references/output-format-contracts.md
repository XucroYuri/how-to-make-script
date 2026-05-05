# 输出格式约定

## 这是什么 / 何时加载

本文件定义了仓库中"金版剧本产物"（golden screenplay artifacts）的最低 Markdown 交付格式约定。

它是格式合约——定义每个输出类型的交付标准与结构要求。

**Agent 应在以下时机加载本文件：**

- **生成产物之前**——确认待生成的输出类型有哪些必填章节、标签和结构要求。本文列出的十二种输出类型均由 [`output-format-contracts.json`](./output-format-contracts.json) 进行机器检查。
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

### `branded_film_script`

- H1 标题必须包含 `Branded Film Script`。
- 必填 H2 章节：
  - `Narrative Arc`（叙事弧线）
  - `Key Sequences`（关键序列）
  - `Brand Integration Points`（品牌融合点）
- 品牌价值必须进入角色冲突或叙事情境，而非后贴标签。允许更强的情感与美学，但保持品牌方向。
- 机器检查要求：`Narrative Arc` 最少 3 条，`Key Sequences` 最少 4 条，`Brand Integration Points` 最少 2 条。

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

### `quality_gate_report`

- H1 标题必须包含 `Quality Gate Report`。
- 必填 H2 章节：
  - `Target Contract & Scope`（目标合同与范围）
  - `Selected Lenses & Rationale`（选用镜头与理由）
  - `Hard Fails`（硬性不合格项）
  - `Weighted Weaknesses`（加权弱点）
  - `Correction Ladder`（修正阶梯）
  - `Recheck Plan`（复查计划）
- 文档必须先把审什么、审多宽说清楚，再按 lens 分层给出独立诊断，最后用修正阶梯告诉团队下一步该怎么动。
- 硬性不合格项必须与加权弱点明确分离，不能揉成一个笼统评价。
- 机器检查要求：`Target Contract & Scope` 最少 2 条，`Selected Lenses & Rationale` 最少 3 条，`Hard Fails` 最少 1 条，`Weighted Weaknesses` 最少 1 条，`Correction Ladder` 最少 2 条，`Recheck Plan` 最少 1 条。

### `rewrite_report`

- H1 标题必须包含 `Rewrite Report`。
- 必填 H2 章节：
  - `Failure Layer`（失败层级）
  - `Root Symptoms`（根本症状）
  - `Prioritized Actions`（优先动作）
  - `Classification`（分类）
- 必须先判定主要问题发生在概念、结构、场景还是对白层，不能跳过层级诊断直接给建议。
- 分类必须区分 `must-restructure`（必须重构）、`suggested`（建议改进）和 `observable-risk`（可观察风险）。
- 机器检查要求：`Failure Layer` 最少 1 条，`Root Symptoms` 最少 2 条，`Prioritized Actions` 最少 2 条，`Classification` 最少 2 条。

### `audience_proxy_report`

- H1 标题必须包含 `Audience Proxy Report`。
- 必填 H2 章节：
  - `Proxy State Snapshots`（代理状态快照）
  - `Consensus Concerns`（共识关切）
  - `High-Value Scenes`（高价值场景）
  - `Dropout Risks`（断流风险）
  - `Modification Priorities`（修改优先级）
- 每个代理状态快照必须包含 patience、trust、hooked、concerns 摘要。
- 共识关切必须标注哪些代理共同持有。
- 修改优先级最多 3 条，每条必须映射到具体场景位置和具体动作。
- 机器检查要求：`Proxy State Snapshots` 最少 2 条，`Consensus Concerns` 最少 1 条，`High-Value Scenes` 最少 1 条，`Dropout Risks` 最少 1 条，`Modification Priorities` 最少 1 条。

### `voice_style_guide`

- H1 标题必须包含 `Voice Style Guide`。
- 必填 H2 章节：
  - `Voice Anchors`（声音锚点）
  - `Lived Pressure`（处境压力）
  - `Register Envelope`（语域包络）
  - `Continuity Anchors`（连续性锚点）
  - `Creative Range`（创意区间）
- Voice Anchors 必须写出世界观倾向、关系策略、羞耻点和常见回避方式，不能只是风格形容词。
- Lived Pressure 必须把身体压力、社会风险和时间成本转进语言机制。
- Register Envelope 必须写清允许的词汇层级、修辞密度和明确禁行区。
- 如果涉及 IP、系列角色或品牌人格，必须有 Continuity Anchors 和漂移警报。
- 机器检查要求：`Voice Anchors` 最少 2 条，`Lived Pressure` 最少 2 条，`Register Envelope` 最少 2 条，`Continuity Anchors` 最少 1 条，`Creative Range` 最少 1 条。

### `visual_language_pack`

- H1 标题必须包含 `Visual Language Pack`。
- 必填 H2 章节：
  - `Task Scope`（任务范围）
  - `Selected Terms`（选用术语）
  - `Cultural Notes`（文化注释）
  - `Misread Alerts`（误读警报）
- Selected Terms 必须只包含会改变当前镜头和表达决策的术语，不能退化成全类目词典。
- Cultural Notes 必须把抽象文化概念落到镜头、构图、灯光、节奏或动作层面的具体约束。
- Misread Alerts 必须写明 hybrid 使用方式、误读风险和禁忌点。
- 机器检查要求：`Task Scope` 最少 2 条，`Selected Terms` 最少 3 条，`Cultural Notes` 最少 1 条，`Misread Alerts` 最少 1 条。

### `screen_to_video_brief`

- H1 标题必须包含 `Screen To Video Brief`。
- 必填 H2 章节：
  - `Source Spans`（来源段）
  - `Clip Chain`（片段链）
  - `Invariants/Avoid Rules`（不变量与避免规则）
  - `Duration Boundaries`（时长边界）
  - `Source Traceability`（来源可追溯）
- 每个 clip 必须只有明确的主动作和主镜头逻辑，不能一个 clip 承载多个互相竞争的镜头逻辑。
- 必须区分可见人物、画外音人物、可见道具和仅在语义层存在的信息。
- 关键桥接判断必须能回指上游文本证据（source span 或证据锚点）。
- 机器检查要求：`Source Spans` 最少 1 条，`Clip Chain` 最少 1 条，`Invariants/Avoid Rules` 最少 2 条，`Duration Boundaries` 最少 1 条，`Source Traceability` 最少 1 条。

### `research_background_map`

- H1 标题必须包含 `Research Background Map`。
- 必填 H2 章节：
  - `Research Lenses`（研究镜头）
  - `Stability Classification`（稳定性分类）
  - `Callable Resources`（可调用资源）
  - `Loading Boundaries`（加载边界）
- Research Lenses 必须把宽问题拆成 3-6 个有判断力的研究镜头，避免套用单一方法。
- Stability Classification 必须区分稳定发现、局部经验、历史条件和开放争议，不把局部经验包装成普适结论。
- Callable Resources 必须列出可调用的 atom、source map 和后续 route，不能只做阅读摘要。
- 机器检查要求：`Research Lenses` 最少 3 条，`Stability Classification` 最少 2 条，`Callable Resources` 最少 2 条，`Loading Boundaries` 最少 1 条。

### `dialogue_polish`

- H1 标题必须包含 `Dialogue Polish`。
- 必填 H2 章节：
  - `Target Lines`（目标台词）
  - `Subtext Benchmarks`（潜台词基准）
  - `Voice Adjustments`（声音调整）
  - `Rhythm Notes`（节奏注释）
- 文档必须暴露每句台词的表面意思与实际意思的差异，以及声音分离是否可追踪。
- 机器检查要求：`Target Lines` 最少 3 条，`Subtext Benchmarks` 最少 2 条，`Voice Adjustments` 最少 2 条，`Rhythm Notes` 最少 1 条。

### `premise`

- H1 标题必须包含 `Premise`。
- 必填 H2 章节：
  - `Core Concept`（核心概念）
  - `Audience Promise`（观众承诺）
  - `Tone Pledge`（调性承诺）
- 文档必须说清"给谁看"和"调性承诺"，比一句话梗概（`logline`）多氛围感和观众指向。
- 机器检查要求：`Core Concept` 最少 1 条，`Audience Promise` 最少 2 条，`Tone Pledge` 最少 2 条。

### `logline`

- H1 标题必须包含 `Logline`。
- 必填 H2 章节：
  - `Story Engine`（故事引擎）
  - `Stakes Statement`（利害陈述）
- 文档必须在一句话内暴露主角、目标、障碍与利害关系。
- 机器检查要求：`Story Engine` 最少 1 条，`Stakes Statement` 最少 1 条。

### `outline`

- H1 标题必须包含 `Outline`。
- 必填 H2 章节：
  - `Scene Sequence`（场景序列）
  - `Emotional Arc`（情感弧线）
- 文档必须按时间顺序列出每个场景的目的与内容要点。
- 机器检查要求：`Scene Sequence` 最少 6 条，`Emotional Arc` 最少 2 条。

## 范围说明

当前格式约定覆盖仓库的金版示例产出。后续可以扩展到更多输出类型，但新增格式规则应保持最小化和"约定优先"原则：

- 暴露产物的决策面（decision surface）；
- 避免把一个好的样本变成教条；
- 优先选择小而稳定的结构，而非冗长的模板。
