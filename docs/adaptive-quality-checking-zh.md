# 自适应质检架构

定义仓库通用质检层设计思路、lens 选择与复查模式。需理解质量把关如何按场景切镜头非跑固定清单时读本文。

## 缘由

特定 checker workflow 在自己场景里很强。值得吸收的不是固定层数，是背后的方法：
- 不做泛评做分层查。
- 每层视角独立。
- 层间只传提炼 metrics，不全文堆 findings。
- 硬门槛与软评分分。
- 改后有明确复路径。

但这些方法一旦照搬"全场景同条线性 stage 流程"即失效。因仓库处理的不仅是 AI 可执行剧本，还包括：
- narrative / commercial / interactive。
- voice style guide。
- visual language pack。
- screen-to-video brief。
- team workflow / subagent 调度。
- project surface map。

输出物失败机制本不同。

## 当前抽象

`quality_gate_report` 将质检改为：
1. 先锁 target contract。
2. 先过当前输出物原生 rubric 或最近 contract gate。
3. 从 [`references/check-lens-matrix.json`](../references/check-lens-matrix.json) 选最小有效 lens stack。
4. 每 lens 在有界 brief 下独立查。
5. 分离 hard fail 与 weighted weakness。
6. 聚合 correction ladder。
7. 如须再设 targeted recheck。

## 通用 lens

- `contract_fit`：题对否。
- `mechanics_pressure`：叙事/说服/互动发动机在否。
- `continuity_invariants`：状态、不变量、连贯断否。
- `expression_integrity`：声、语域、角色/IP/品牌表达漂否。
- `operational_feasibility`：下游能否执行、生成、游玩、落地。
- `delivery_handoff`：人工具接不接得住。
- `boundary_risk`：硬边界与真实 veto 风险踩否。

非每次全开。按场景选非默认全跑。

## 复查模式

避每次全跑大流程，质检层四 scope：
- `full_audit`
- `lens_targeted`
- `range_limited`
- `recheck`

系统优先最小必要复查，非变另一沉工作流。

## 与 rewrite_report 边界

`rewrite_report` 保留，主解"病灶哪层、下轮先改什么"。

`quality_gate_report` 解另类问题：
- 交付物当前 contract 过关否。
- 哪些 hard fail，哪些弱项。
- 哪些 lens 必再审。
- 非故事型输出物可交接、可落地、可验收否。

默认序：先跑原生 rubric，再叠共享 lens matrix。

简：
- 改稿优先级用 `rewrite_report`。
- 自检、预检、复查、验收、跨 artifact 质检用 `quality_gate_report`。

## 关联文件

- [`wp.quality-gate-report`](../knowledge/20-workflows/wp-quality-gate-report.md)
- [`rb.quality-gate-report`](../knowledge/60-rubrics/rb-quality-gate-report.md)
- [`references/check-lens-matrix.json`](../references/check-lens-matrix.json)
