# 自适应质检架构

当前仓库把“剧本自检”从一个单一路径的 checklist，升级成了一个可按场景切换镜头的通用质检层。

## 为什么要这样做

特定定位的 checker workflow 往往在自己的应用场景里很强。真正值得吸收的，不是它固定有几层，而是它背后的方法：
- 不做泛泛点评，而做分层检查；
- 每层检查都尽量保持视角独立；
- 层间只传提炼后的 metrics，不把 findings 全文一路堆下去；
- 硬门槛和软评分分开；
- 修改后有明确复查路径。

但这些方法一旦被直接照搬成“所有剧本场景都跑同一条线性 stage 流程”，就会立刻失效。因为这个仓库要处理的不只是 AI 可执行剧本，还包括：
- narrative / commercial / interactive；
- voice style guide；
- visual language pack；
- screen-to-video brief；
- team workflow / subagent dispatch；
- project surface map。

这些输出物的失败机制根本不同。

## 当前抽象方式

仓库新增了 `quality_gate_report`，把质检逻辑改成：
1. 先锁定 target contract；
2. 先过当前输出物自身的原生 rubric 或最接近的 contract gate；
3. 再从 [`references/check-lens-matrix.json`](../references/check-lens-matrix.json) 里选择最小有效 lens stack；
4. 每个 lens 在 bounded brief 下独立检查；
5. 分离 hard fail 和 weighted weakness；
6. 聚合出 correction ladder；
7. 如果需要，再设计 targeted recheck。

## 当前的通用 lens

- `contract_fit`：题做对没有；
- `mechanics_pressure`：叙事 / 说服 / 互动发动机在不在；
- `continuity_invariants`：状态、不变量、连贯性有没有断；
- `expression_integrity`：声音、语域、角色 / IP / 品牌表达有没有漂；
- `operational_feasibility`：下游到底能不能执行、生成、游玩、落地；
- `delivery_handoff`：人和工具到底接不接得住这份交付；
- `boundary_risk`：硬边界和真实 veto 风险有没有被踩。

不是每次都全开。重点是按场景选，而不是默认全跑。

## 复查模式

为了避免每次修改都重跑整条大流程，当前质检层支持四种 scope：
- `full_audit`
- `lens_targeted`
- `range_limited`
- `recheck`

也就是说，系统会优先做”最小必要复查”，而不是把复查变成另一个沉重的工作流。

## 和 rewrite_report 的边界

`rewrite_report` 仍然保留，它主要解决的是“病灶在哪一层、下一轮先改什么”。

`quality_gate_report` 解决的是另一类问题：
- 这份交付物在当前 contract 下有没有过关；
- 哪些是 hard fail，哪些只是弱项；
- 哪些 lens 必须再审；
- 非故事型输出物是否具备可交接、可落地、可验收性。

它的默认次序是：
- 先跑当前输出物的原生 rubric；
- 再叠加共享 lens matrix。

简化说：
- 要改稿优先级，用 `rewrite_report`；
- 要做自检、预检、复查、验收、跨 artifact 质检，用 `quality_gate_report`。

## 关联文件

- [`wp.quality-gate-report`](../knowledge/20-workflows/wp-quality-gate-report.md)
- [`rb.quality-gate-report`](../knowledge/60-rubrics/rb-quality-gate-report.md)
- [`references/check-lens-matrix.json`](../references/check-lens-matrix.json)
