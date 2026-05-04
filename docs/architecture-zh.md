# 架构说明

定义仓库四层架构、扩展立场与设计约束。需理解仓库"为何这样组织"时读本文。

## 核心思路

仓库拆为四层：

1. `knowledge/` 存放可长期积累理论与 craft 片段。
2. `schemas/` 定义结构化内容机器校验契约。
3. `skills/` 为 agent 提供轻量编排入口。
4. `scripts/` 和 `tests/` 保证仓库可持续验证。

立场：

- 知识层是 source of truth。
- skill 负责路由与组合，不重写理论。
- fixture 和测试约束路由稳定性。
- 优先增量扩展，不频繁重组已发布 ID。

编排层带有边界现实锚定规则：

- 受众视角。
- 行业与委托视角。
- 平台与发行视角。
- 作者成长视角。
- 历史演化视角。

仅当会改变路由选择或输出质量时才加载这些 lens。

编排层五扩展领域有边界加载规则：

**团队协作。** 普通请求默认单路由；仅当团队结构实质改变下一步决策才加载多智能体或混合团队；专家间交换有边界交接包，不共享整份上下文。

**Subagent library。** `team_workflow_blueprint` 选协作形态；`expert_subagent_cast` 选受限专家 roster；reference persona 是有边界 lens，不替代 route logic 或 convergence ownership。内部调度与表面管理在后处理实时编排、review 结构和真源治理。

**Project surface。** 权威来源、runtime mirror、packet assembly 和 review/export surface 由内部治理管理——agent 和用户通过公开合同交互，不触底层管道。

**Quality gating。** `quality_gate_report` 选 lens stack，非通用清单；hard gate 与加权弱项分离；优先 targeted recheck，不自全量重审；专用 checker 逻辑可启发设计，不直变仓库通用规则。

**视觉转译。** multilingual visual-language 资产仅当跨语言镜头/调度沟通实影响答案质量时加载；screenplay-to-video 转译层保持 vendor-neutral，以 clip 为界；下游模型或工具选择在转译层构建之后，不混进 screenplay routing。

Anti-dogma 立场：

- 剧本指导是启发式，非绝对法则。
- 收敛前可并存多条有效路径。
- hard boundary 和 soft constraint 不可混。
- exploration 和 review 是两阶段，非一次混合。
- 被挑战 claim 通过 scope correction 收窄，不摇摆于两绝对口号间。
- reference pattern 教对照式成败逻辑，不偷变新 canon。

所以 agent 默认不读整仓库。先入 route，再加载 protocol、其链接 atom、及 rubric。

教学、比较或场景诊断类任务，还应把 scenario atlas 作因子分解层，不从媒体标签直跳样例选择。

route selection 与 generation 间，选有边界 loading mode，使系统扩展参考时不堕入 context corrosion。

任务需多角色协作时，明确选 team mode，防协作退化不可见 prompt 习惯。

任务需长周期项目设计时，明确选 project surface，防可编辑内容、运行时状态、交接包与交付界面塌为按文件夹拼凑模糊结构。

任务需结构化审查时，明确选 quality gate，防契约匹配、执行风险、交付准备度与 recheck 范围埋于泛泛 rewrite 建议。

## 为什么 Monorepo

单仓库使以下同步演进，避跨库版本漂移：

- 共享 taxonomy。
- routing 规则。
- 相互链接 knowledge atom。
- 跨 skill fixture。
- 验证工具。
- 开源文档。

防 narrative、commercial、interactive 逻辑裂为隔离 prompt silo。防纯 craft 输出与真实受众需求、生产约束渐远。

## 设计约束

- `research-first`，非 `UI-first`。
- 优先 human-readable，但必 machine-validated。
- 维持 stable ID，采用 additive evolution。
- 用明确路由代替临时 prompt 堆叠。
- route 应能解释为 `intent x medium x stage x output x constraints`。
- constraint 须支持真实参数：受众需求状态、委托上下文、商业模式、发行逻辑、作者成熟度。
- 系统须明确表达假设、边界与收敛触发条件，抵 false universal。
- 系统须分离 route selection 与有界 reference expansion，抵 context corrosion。
- 系统须区分真专家 lane、handoff 契约与人工 gate，抵假协作。
- 系统须区分 craft lineage 压力与直模仿 persona，抵 persona worship。
- 系统须分离 screenplay 推理与下游 visual 转译容器，抵 prompt-first drift。
- 系统须区分权威来源、runtime state 与交付界面，抵 repo-surface drift。
- 系统须分离可复用 audit abstraction 与单领域 checker pipeline，抵 checker 泛化。
- 每种资产可独立 lint。
- 薄 skill 保持可运行，理论集存 `knowledge/`。

## 构建哲学

仓库应能不断追加以下内容而无限扩展：

- 新 atom。
- 新 protocol。
- 新 rubric。
- 新 fixture。
- 新 skill。
- 新 media 与 genre pack。

同时不破现有使用者。
