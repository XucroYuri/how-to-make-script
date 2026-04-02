# 社区运营策略

这个仓库不想把社区做成“有人提 bug，我们被动处理”的模式，而是想把它做成一个高质量质疑和高密度修正不断发生的地方。

目标不是让大家来点赞，而是让大家更容易提出反驳、举反例、贴一线经验、指出理论失效点，并且让这些输入最后真的变成仓库资产。

## 运营目标

- 提高社区输入里“带具体质疑 / 反例 / 现场经验”的比例。
- 让开放式争论先留在 Discussions，不要一上来就把模糊讨论挤进 issue。
- 让重复出现的争议最终积累成 atom、protocol、rubric、fixture 或治理规则。
- 让不写代码的人也能高质量贡献，而不是默认只有提 PR 才算参与。

## 反馈入口分层

不同阶段的问题，应该进不同入口：

1. `Q&A` 讨论：
   还在搞清楚某条说法、某条路由、某个资产到底什么意思时，先来这里。
2. `General` 讨论：
   已经有真实质疑，但还比较开放、比较大、还没收敛成一个 issue 时，先来这里。
3. `Ideas` 讨论：
   你觉得缺了一条路径、少了一类 workflow、社区流程该改，但现在还没缩小到具体改动时，先来这里。
4. `Show and tell` 讨论：
   你有现场经验、项目案例、试错记录、使用反馈，想给仓库补“现实材料”时，来这里。
5. Issue 表单：
   你已经能明确指出具体文件、具体 claim、具体 route、具体 rubric 或具体治理规则时，再开 issue。
6. PR：
   你已经知道该怎么把这条经验编码进仓库时，再提 PR。

这和 GitHub 官方对 Discussions 的定位一致：先用它收集更开放的想法和反馈，等工作边界清楚以后再转成 issue。

## 维护节奏

下面是目标节奏，不是生硬 SLA：

- 72 小时内：
  至少加上 `type:*` 或 `discussion-first`，先把线程归类。
- 7 天内：
  至少补上 `status:*`，或说明缺什么证据，或把线程转到更合适的表面。
- 每周：
  统一看一次 `needs-triage`、`needs-practitioner-input`、`needs-counterexample`。
- 每月：
  发一次简短社区总结，说明最近哪些反驳真正改变了仓库。
- 每季度：
  回看 labels、表单、没人回应的讨论，以及维护压力是不是失衡。

## 维护角色

- `maintainer`：负责最后的范围判断、合并和治理决策。
- `triage steward`：负责分诊、补充问题、避免线程卡死。
- `field-note curator`：负责从一线反馈里找出值得进仓库的判断点。
- `fixture shepherd`：负责把重复失败积累成 fixture。
- `discussion moderator`：负责保持讨论建设性，并把“还太早的 issue”转回 discussion。

GitHub Discussions 支持把长期高质量参与者提升到更高权限。对于那些长期能给出高质量回答、反驳和分诊帮助的人，应该逐步邀请其参与 triage / moderation。

## 默认互动动作

希望维护者和贡献者多做这些动作：

- 先问清楚被挑战的到底是哪条 claim / route / rubric；
- 先要一个具体反例，再讨论抽象理念；
- 如果问题方向是对的，但还没缩小清楚范围，就打 `discussion-first`；
- 一旦变更目标清楚了，就把 discussion 转成 issue；
- 如果一个 issue 本质还在探索，就把它转回 discussion；
- Q&A 里能回答的问题尽量标 answer，方便后来者检索；
- 只有当经验已经被吸收、明确延期、或带理由拒绝后，线程才关闭。

## 社区运营动作

- 常驻一个“反例与一线现场”讨论串。
- 常驻一个“被忽略的路径 / workflow / 类型需求”讨论串。
- 每个 PR 在 review 时都明确追问一次：这次改动最容易在哪种现实场景里坏掉？
- 每次做范围修正时，都回链到逼出这次修正的讨论或 issue。

## 可追踪指标

- discussion 转 issue 的数量；
- issue 最终转成仓库资产的数量；
- 还挂着的 `needs-practitioner-input` 数量；
- 还挂着的 `needs-second-field-report` 数量；
- 维护者首次分类的中位时间；
- 带来源讨论 / 异议来源的合并 PR 数量。

## 相关文件

- [社区反馈回路](./community-feedback-loop-zh.md)
- [社区分诊机制](./community-triage-loop-zh.md)
- [贡献指南](../CONTRIBUTING.md)
- [讨论入口地图](../references/discussion-surface-map.json)
- [社区标签注册表](../references/community-label-taxonomy.json)
