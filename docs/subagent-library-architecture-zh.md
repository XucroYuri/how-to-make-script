# Subagent 库架构

仓库现在把“多智能体”进一步拆成了一个真正可调度的 subagent 层。

目标不是“多开几个 Agent 看起来更强”，而是让系统能像高水平剧本团队那样：
- 先搞清楚当前到底是什么问题；
- 再决定需要什么 team mode；
- 再决定谁应该进场；
- 最后决定这些 subagent 怎么跑、怎么合并、怎么停。

## 四层顺序

推荐顺序是：

1. `route`
2. `team mode`
3. `expert cast`
4. `dispatch topology`

这四层不能倒着来。否则系统会很容易先沉迷于“组织形式”，再反过来硬找一个任务去匹配。

## 三类 Subagent

### 功能型

它解决的是专业问题。

例如：
- premise scout
- structure / engine architect
- character pressure designer
- dialogue / subtext doctor
- visual story partner
- audience pressure analyst
- state QA architect

### 流程节点型

它解决的是推进问题，而不是创作内容问题。

例如：
- divergence facilitator
- counterexample keeper
- rewrite triage lead
- convergence editor
- table-read synthesizer
- spec reviewer
- quality reviewer

### 参考人物型

它不是“把某位大师本人请进来”，而是把某种可识别的 craft lineage 和 workflow 偏置抽出来，作为一种有边界的镜头。

例如：
- prestige moral collision
- romantic verbal precision
- animation humanist visuality
- high-concept clockwork
- social satire thriller
- luxury restraint brand film
- branching systemic choice

它们的价值在于施加压力，而不是替代协议和路由。

## 参考 Persona 治理

仓库支持三层：

- `inspired_by`
  借用决策风格、工作方式、审美偏置。
- `calibrated_reference`
  允许更强的风格 / workflow 压力，但必须带 loading cap、allowed use 和 blocked use。
- `forbidden_roleplay`
  不允许作为 live persona 出场。包括直接 impersonation、伪装本人发言、精确模仿等。

这套治理的核心，不是要把真实人物赶出系统，而是防止系统把“参考”做成“教条模仿”。

## 调度拓扑层

除了“选谁进场”，仓库还新增了“怎么调度”的机器层。

首批 topology 包括：
- `orchestrator_specialist_ring`
- `writers_room_tree`
- `debate_then_merge_board`
- `dual_track_story_visual`
- `variant_strike_grid`
- `branch_state_triangle`
- `fresh_task_review_loop`

其中 `fresh_task_review_loop` 就是把 `subagent-driven-development` 的核心思想正式编码进仓库：
- implementer 先做；
- spec reviewer 先看有没有做对题；
- quality reviewer 再看做得稳不稳；
- convergence owner 决定是否锁定和收口。

这对仓库自身开发和剧本复杂任务都很重要，因为很多失败不是“不会写”，而是“做错了题却写得很像那么回事”。

## 扩展原则

这个 subagent 库要尽量大，但不能靠“每种情况新造一个独占 agent”来变大。

更稳的扩展方式是：
- 顶层 router 尽量稳定；
- 新增能力优先进入 cast layer；
- 新增调度形状优先进入 topology layer；
- 只有当 output contract 真变了，才新增新 route。

## 一套靠谱系统应该能回答什么

面对复杂剧本任务时，仓库应该能够明确回答：

- 当前最像哪一种 team mode；
- 最小可运行阵容是什么；
- 哪些 persona lens 值得上，哪些不值得；
- 哪种 topology 最合适；
- 谁是 merge owner；
- 数据包怎么传；
- 哪些地方必须 human-in-the-loop；
- 什么时候该扩容，什么时候该收缩。

## 关键文件

- [`references/expert-subagent-library.json`](../references/expert-subagent-library.json)
- [`references/subagent-topology-matrix.json`](../references/subagent-topology-matrix.json)
- [`references/team-mode-matrix.json`](../references/team-mode-matrix.json)
- [`references/agent-team-roles.json`](../references/agent-team-roles.json)
- [`knowledge/20-workflows/wp-expert-subagent-cast.md`](../knowledge/20-workflows/wp-expert-subagent-cast.md)
- [`knowledge/20-workflows/wp-subagent-dispatch-plan.md`](../knowledge/20-workflows/wp-subagent-dispatch-plan.md)
