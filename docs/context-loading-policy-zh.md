# 上下文加载策略

定义路由选定后上下文加载的扩展规则、停止条件与回退策略。需控制"加载多少"非"走哪条路"时读本文。位于路由之后、生成之前。

## 当前定位

Agent Skill 设计已有优点：
- 路由先行，先定 intent / medium / stage / output / constraints。
- 场景图谱、参考范式、边界工具、范围修正已分层。
- content model 倾向小粒度，不一气塞大 prompt。

真风险非知识不够，是加载过量。请求一复杂就拉附近全文档，模型复述仓库非使用仓库。三后果：
- 上下文腐化，键信号被噪音淹。
- 推理变慢，创意推进被冗余拖住。
- 输出变钝，看"全"不"准"。

本策略目标：在准确与广度间保可控平衡。

## 基本原则

1. 先路由，再加载。
2. 先加最小能改判断的上下文包。
3. 一次只扩一层，不从一 route 直跳全知识仓。
4. 优先对照型参考，非批量相似材料。
5. 新上下文不改路由、输出契约或自检时停。

## 加载模式

详见 [`docs/context-loading-policy.md`](./context-loading-policy.md)。

简化：
- `route_kernel`：最小可路由包。
- `focus_pack`：单任务、单路由、单 rubric 执行包。
- `compare_pack`：备选方案、为何不这样写、边界判断。
- `teaching_pack`：解释、示例、学习。
- `survey_pack`：仅用户明要全景梳理时用，且先定明确 background bundle。

## 扩展触发

仅"新一层上下文真改答案"时扩：
- 任务混合，单路由不够。
- 用户明要 alternatives、counterexample、为何更好。
- 草稿已露路由错配、失败环节或边界混。
- 任务涉受众适配、委制适配、学习路径、现实约束。
- 任务明需风格校准、语域控制、IP 角色声延续或更强活人感。
- 任务明需 team mode 选、handoff 设计或 review gate 设计。
- 用户明要教学、比较或广综述。
- 任务本宽问题理论撑，需声明 research/background bundle 防乱扩。

## 停止条件

任一即停：
- 路由稳，输出契约定。
- 新材料只复已有结论。
- 再一层只增细节，不改判断。
- 当前包已含「路由锚点 + 撑参考 + 反例/对照」。

任务窄，首包停，不凑"更全"。任务宽，停"讲清 tradeoff 最小包"。

## 失效信号

以下示加载过或欠：
- 模型复述文档非解题。
- 多源冲突但输出未消。
- 覆面太广致输出空泛。
- 仅一样本无对照致输出脆。
- 模型把参考片段当模板非参考路径。

## 平衡规则

- 始终保留主 route pack。
- 除非用户明要更广 survey，至多加一邻比较包。
- 写作优先"一强例 + 一弱对照"，不堆似例。
- 边界问题优先 `boundary_map` 或 `scope_correction`，不先拉大量通用 craft。
- 场景问题优先 [`docs/scenario-atlas-zh.md`](../docs/scenario-atlas-zh.md) 与 [`references/scenario-taxonomy.json`](../references/scenario-taxonomy.json)，再定是否加样。
- 宽理论/背景支持优先从 [`references/background-bundles.json`](../references/background-bundles.json) 选背景包，再定是否扩邻文档。
- 暂停续写、room handoff、长连续保护优先 `story_memory_checkpoint`，不同批材料越拉越宽。
- 受众/策略优先加载现实 lens，再虑扩更广 craft。
- 角色声音/语言风格优先最小表达校准包，不直上大包参考。
- 协作机制优先最小 team-mode bundle，不直塞多智能体框架对比。

## 回退规则

加载太宽：
- 退 route kernel。
- 只重载主 protocol、主 rubric 与一支撑参考。
- route 仍不清，直问一最小澄清问题。

加载太窄：
- 补缺决策层。
- 加一对照参考或边界说明。
- 不"加载全仓库"补不足。

## 一句话

最好上下文包，让模型把路由说清、判断讲明、答案写对的最小包。
