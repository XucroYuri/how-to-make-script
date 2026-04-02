# 架构说明

## 核心思路

这个仓库把可复用的剧本方法论拆成四层：

1. `knowledge/` 用来存放可长期积累的理论与 craft 片段。
2. `schemas/` 定义结构化内容的机器校验契约。
3. `skills/` 为 agent 提供轻量编排入口。
4. `scripts/` 和 `tests/` 保证仓库可以持续验证。

这个仓库有明确立场：

- 知识层才是 source of truth；
- skill 负责路由与组合，不负责重写理论；
- fixture 和测试用来约束路由稳定性；
- 优先做增量扩展，而不是频繁重组已发布的 ID。

编排层现在还带有一套有边界的现实锚定规则：

- 受众视角；
- 行业与委托视角；
- 平台与发行视角；
- 作者成长视角；
- 历史演化视角。

这些 lens 只在它们会改变路由选择或输出质量时才加载。

编排层包含五个扩展领域的有边界加载规则：

**团队协作。** 普通剧本请求默认仍应保持单路由；只有当团队结构会实质改变下一步决策时，才加载多智能体或混合团队逻辑；专家角色之间应交换有边界的交接包，而不是共享整份上下文。

**Subagent library。** `team_workflow_blueprint` 负责选择协作形态；`expert_subagent_cast` 负责选择受限的专家 roster；`subagent_dispatch_plan` 负责选择实时调度与 review 结构；reference persona 只是有边界的 lens，不应替代 route logic 或 convergence ownership。

**Project surface。** `project_surface_map` 负责定义权威来源放在哪里；runtime mirror、cache、trace 默认都应是派生层；packet assembly 应该可审查，而不是隐藏流程；review surface 和 export surface 应该被明确命名，而不是与可编辑内容混在一起。

**Quality gating。** `quality_gate_report` 选择的是一组 lens stack，而不是一份通用检查清单；hard gate 要和加权弱点拆开；优先做 targeted recheck，而不是自动全量重审；专用 checker 逻辑可以启发设计，但不应直接变成整个仓库的通用规则。

**视觉转译。** multilingual visual-language 资产只应在跨语言镜头/调度沟通确实影响答案质量时加载；screenplay-to-video 转译层资产要保持 vendor-neutral，并且以 clip 为边界；下游模型或工具选择应发生在转译层构建之后，而不是混进 screenplay routing。

仓库还带有明确的 anti-dogma 立场：

- 剧本指导是启发式的，不是绝对法则；
- 在收敛前，可以并存多条有效路径；
- hard boundary 和 soft constraint 不能混为一谈；
- exploration 和 review 是两个阶段，不是一次混合动作；
- 被挑战的 claim 应通过 scope correction 收窄，而不是在两个绝对口号之间摇摆；
- reference pattern 应教会人对照式的成败逻辑，而不是偷偷变成新的 canon。

这意味着 agent 默认不该读取整个仓库。它们应先进入一个 route，再加载一个 protocol、它链接的 atom，以及一个 rubric。

如果任务属于教学、比较或场景诊断，还应把 scenario atlas 当作一个因子分解层，而不是从媒体标签直接跳到样例选择。

在 route selection 和 generation 之间，还应选择一种有边界的 loading mode，这样系统才能扩展参考而不走向 context corrosion。

当任务确实需要多角色协作时，还应明确选择 team mode，这样协作结构就不会退化成不可见的 prompt 习惯。

当任务确实需要长周期项目设计时，还应明确选择 project surface，这样可编辑内容、运行时状态、交接包和交付界面就不会塌缩成一个按文件夹拼凑的模糊结构。

当任务确实需要结构化审查时，还应明确选择 quality gate，这样契约匹配、执行风险、交付准备度和 recheck 范围就不会埋在泛泛的 rewrite 建议里。

## 为什么是 Monorepo

单仓库可以让以下内容同步演进，避免不同仓库之间的版本漂移：

- 共享 taxonomy；
- routing 规则；
- 相互链接的 knowledge atom；
- 跨 skill fixture；
- 验证工具；
- 开源文档。

这也能避免 narrative、commercial 和 interactive 逻辑逐渐分裂成彼此隔离的 prompt silo。
也能避免纯 craft 输出与真实受众需求、生产约束之间越走越远。

## 设计约束

- `research-first`，不是 `UI-first`。
- 优先 human-readable，但必须 machine-validated。
- 维持 stable ID，采用 additive evolution。
- 用明确路由代替临时 prompt 堆叠。
- 一个 route 应能解释成 `intent x medium x stage x output x constraints`。
- constraint 必须支持真实世界参数，例如受众需求状态、委托上下文、商业模式、发行逻辑和作者成熟度。
- 系统必须通过明确表达假设、边界与收敛触发条件，来抵抗 false universal。
- 系统必须通过把 route selection 与有边界的 reference expansion 分离，来抵抗 context corrosion。
- 系统必须通过区分真正的专家 lane、handoff 契约和人工 gate，来抵抗假协作。
- 系统必须通过区分 craft lineage 压力与直接模仿 persona，来抵抗 persona worship。
- 系统必须通过把 screenplay 推理和下游 visual 转译容器分离，来抵抗 prompt-first drift。
- 系统必须通过区分权威来源、runtime state 和交付界面，来抵抗 repo-surface drift。
- 系统必须通过把可复用 audit abstraction 和单一领域 checker pipeline 分离，来抵抗 checker 过度泛化。
- 每一种资产类型都应可以独立 lint。
- 薄 skill 应保持可运行，而理论应集中存放在 `knowledge/`。

## 构建哲学

这个仓库应能通过不断追加以下内容而无限扩展：

- 新 atom；
- 新 protocol；
- 新 rubric；
- 新 fixture；
- 新 skill；
- 新 media 与 genre pack。

同时又不破坏现有使用者。
