# 社区分诊机制

这份 playbook 面向需要把社区输入转成仓库改动的维护者和 agent，同时避免把有效分歧压平成单一结论。

它默认假设：剧本指导是启发式的、有边界的、可争论的，并且受历史条件影响。因此，triage 的目标不是过早逼近唯一真理，而是在多条有效路径仍然成立时把它们保留下来。

## 分诊状态

- `new`：议题尚未分类。
- `needs-evidence`：这个 claim 看起来合理，但还没有足够依据。
- `reproducing`：正在验证 route、失败模式或 counterexample。
- `routed`：这条反馈已经映射到某种资产类型。
- `encoded`：仓库已经完成更新。
- `deferred`：问题成立，但当前受 scope、证据或时机阻塞。
- `rejected`：问题不可执行、缺乏支撑，或超出范围。

## 分类问题

1. 这是 route failure、theory rebuttal、field report、missing case，还是 governance 问题？
2. 这条反馈改变的是 route、contract、rubric，还是 taxonomy 条目？
3. 它能否通过 example、fixture 或 source reference 复现？
4. 正确修复方式是增加新资产、拆分资产，还是更新 policy？
5. 它暴露的是稳定缺口，还是一次性的偏好冲突？
6. 它是否本质上是在提醒 false universal，因此应该削弱 claim，而不是用另一条绝对结论替换？
7. 它是否需要做 scope correction？原 claim 中又有哪些部分仍然成立？
8. 仓库是不是过早收敛，压掉了仍然有效的多条路径？
9. 如果存在不止一条可行 route，仓库是否应保留这种 plurality，而不是直接塌缩？

## 维护者响应规则

- 直接承认分歧的存在。
- 在争论抽象理论前，先要求具体例子。
- 如果问题成立，即使仓库暂时不改，也要保留这条批评。
- 如果问题过大，就把它收窄成最小可编码资产。
- 如果问题重复，合并线程，但保留有价值的 counterexample 并回链。
- 如果问题暂时受阻，就明确说明还缺什么证据。

## 表面转换规则

- 当变更目标仍然宽泛、比较性强或带探索性时，把 issue 转成 discussion。
- 当目标资产、route、rubric 或 governance rule 已经清晰时，把 discussion 转成 issue。
- Q&A 保持公开；当某个澄清足够稳定时，及时标记 answer，方便后续贡献者检索。
- 当贡献者带来了真实 field note，但还没形成可落地的仓库变更时，先保留在 `Show and tell`，直到稳定经验出现。

## 标签建议

默认标签与流转应保持可预期：

- 用 `type:*` 标记这是什么类型的信号；
- 用 `status:*` 标记维护者正在做什么；
- 当真实模式是 counterexample、scope correction、boundary mismatch 或 premature convergence 时，用 `kind:*`；
- 当讨论还太开放，不适合 issue 范围时，用 `discussion-first`；
- 当还缺下一步证据时，用 `needs-practitioner-input`、`needs-counterexample`、`needs-route-reproduction` 或 `needs-second-field-report`。

完整标签注册表见 [`../references/community-label-taxonomy.json`](../references/community-label-taxonomy.json)。

## 响应节奏

- 72 小时内：完成分类，或把线程移动到更合适的表面。
- 7 天内：补上相关 `status:*` 标签，或明确提出缺失证据。
- 每周：检查停滞线程，决定它们应被转换、编码、延期，还是带说明关闭。
- 每月：回看反复出现的异议模式，判断是否应转化为 fixture、文档或治理更新。

## 把反馈转成资产

- `knowledge_atom`：社区发现缺失的是决策规则或概念边界。
- `workflow_protocol`：社区发现缺失的是 handoff、fallback 或 stop condition。
- `evaluation_rubric`：社区发现缺失的是模糊或失准的质量门槛。
- `example_fixture`：社区发现 route 回归或输入歧义模式。
- `docs`：社区发现解释或 onboarding 缺口。
- `governance`：社区发现贡献政策、安全边界或 review 规范的空洞。
- `boundary map`：当问题表明一个二元答案应该拆成 hard-no、soft-risk、bold-safe 和 defer-to-review 等区域。
- `scope correction`：当问题说明某条规则应该收窄，而不是简单删除或强行捍卫。

## 分诊输出

每个被分诊的问题最终都应落到以下结果之一：

- `convert`：创建或更新资产。
- `split`：把一个想法拆成多个资产。
- `scope-correct`：保留仍然成立的核心，同时收窄规则并编码失败上下文。
- `monitor`：保留打开状态，等待更多证据。
- `close-with-note`：确认问题存在，但当前不可执行。
- `escalate`：需要维护者判断或 policy review。

## 好的维护者回复长什么样

- “这是一个有效的 route failure。请补一个 fixture。”
- “这个反驳有价值，但我们需要一个 counterexample 才能编码。”
- “你说得对，这条 rubric 漏掉了这个失败模式。我们会拆分规则。”
- “这是平台特定场景，所以它应成为独立 protocol。”
- “这条反馈是真实的，但我们还需要再收一份 field report 才能改治理。”
- “这不是对原规则的彻底否定，而是一次 scope correction。”
- “当前指导收敛得太早了，这里应保留多条 path option。”

## 相关文档

- [社区反馈回路](./community-feedback-loop-zh.md)
- [Community Feedback Loop](./community-feedback-loop.md)
- [社区运营策略](./community-operations-zh.md)
- [认识论姿态](./epistemic-stance-zh.md)
- [探索与审查分离](./exploration-vs-review.md)
- [内容模型](./content-model-zh.md)
- [仓库卫生](./repository-hygiene.md)
