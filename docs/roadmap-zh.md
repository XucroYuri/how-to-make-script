# Roadmap

## 当前所处位置

这个仓库已经过了“搭骨架”的阶段。它现在已经具备：

- 根 skill、显式路由和 bounded-loading 规则；
- 多层知识资产模型；
- narrative / commercial / interactive 的基础覆盖；
- review、research、continuity、team orchestration 等非纯写作类产物；
- 针对 route、registry、semantic consistency、community surface 和本地工具泄漏的 CI 校验；
- 面向编剧与 Agent builder 的双语入口。

## 当前最关键的不足

- 仓库已经能描述多智能体 / writers' room 协作，但还不能把 blueprint 真正落成 live runtime planner。
- bounded loading 已经写成规则，但 bundle 选择和扩展停止条件还没有充分机器化。
- registry 校验强度不均衡：有的已经有 schema/checker，有的还主要依赖人工约束。
- route 覆盖面已经很广，但相邻输出之间的 adversarial fixture 深度还不够。
- 知识面已经大了，但很多 genre、medium、case study、dialogue / character 研究切片仍然偏浅。
- 社区入口已经有了，但 discussion → triage → asset / fixture / rubric 的转化链仍然太靠人工。
- 双语入口改善明显，但深层文档 parity 还不完整。

## 下一阶段路线

### Phase 5：Runtime 执行层

- [ ] 定义 runtime planner 契约，把 `team_workflow_blueprint`、`expert_subagent_cast`、`subagent_dispatch_plan` 变成可执行 lane。
- [ ] 增加机器可校验的 handoff packet schema，覆盖 writer handoff、review handoff、research handoff、adaptation handoff。
- [ ] 定义可恢复 runtime ledger，让长流程任务可以安全暂停、恢复和分支。
- [ ] 给 runtime planning 加显式 context-budget accounting，让每一步扩容都有理由和 stop condition。
- [ ] 增加 dry-run mode，在真正执行多智能体流程前先模拟 lane sequencing 和 handoff 顺序。
- [ ] 增加 human-gate 插入点，覆盖审批、质疑、scope correction 和 final sign-off。
- [ ] 增加 runtime failure policy，处理 route 死路、handoff 丢失、矛盾暴露、context 超预算等问题。
- [ ] 至少增加一个 feature pod、一个 showrunner room、一个 branded-content flow 的端到端执行 fixture。

### Phase 6：Router 与 Retrieval 治理加固

- [ ] 增加 route-priority register，明确多个输出都可能命中同一请求时谁优先。
- [ ] 为 `path_options`、`boundary_map`、`scope_correction`、`pattern_reference_pack`、`quality_gate_report` 增加对抗性 fixture。
- [ ] 把 `route_kernel`、`focus_pack`、`compare_pack`、`teaching_pack`、`survey_pack` 进一步做成机器可校验的 bundle-planner 规则。
- [ ] 给更多 registry 增加 schema/checker，优先覆盖 scenario taxonomy、check-lens matrix、expression-lens trigger、context-loading-mode 等表面。
- [ ] 增加 contradiction lint，检查 atoms / protocols / rubrics / reference packs 在相近概念上的语义冲突。
- [ ] 增加受控词表 / alias registry，治理 craft、生产、审查、agent 设计语境里的语义漂移。
- [ ] 增加 coverage report，按 medium、stage、output、route family 展示 fixture 密度。
- [ ] 增加测试，防止新增 route 在没更新 docs 或 fixtures 的情况下悄悄扩大加载范围。

### Phase 7：知识深度与参考能力

- [ ] 把 genre pack 从当前骨干继续扩展到 thriller、mystery、horror、comedy、romance、action、family、speculative-fiction 等问题簇。
- [ ] 增加 feature、episodic、short drama、animation、branded film、shortform video、game narrative 的 medium-specific constraint pack。
- [ ] 深化 dialogue stage 的 atoms，覆盖 subtext pressure、information asymmetry、verbal rhythm、exposition avoidance、角色化说话行为。
- [ ] 深化 character stage 的 atoms，覆盖 sympathy design、contradiction design、relationship pressure、transformation tracking。
- [ ] 把宽 research scope 继续拆成更窄的可调用切片，比如 audience cognition、scene escalation、character inference、dialogue perception、rewrite psychology。
- [ ] 增加 success / failure case studies，不只讲“成功怎么做”，也讲“看起来合理却为什么失败”。
- [ ] 增加 stage-specific reference pack，覆盖 weak opening、flat reveal、limp midpoint turn、collapsed ending、generic dialogue 等问题。
- [ ] 增加更多 screenplay-to-video bridge 示例，但继续避免把仓库滑向供应商专用 prompt 目录。

### Phase 8：质量体系与回归深度

- [ ] 给 premise、outline、scene、dialogue、commercial、branch map、research map、checkpoint 等输出增加 output-specific quality-gate preset。
- [ ] 扩充 golden flow，让每个高价值 output family 至少有一条端到端示例链。
- [ ] 增加“改完再复查”的 targeted recheck fixture，而不只覆盖首轮诊断。
- [ ] 增加跨工件一致性检查，优先覆盖 premise ↔ outline、outline ↔ scene、scene ↔ dialogue、script ↔ bridge。
- [ ] 增加 semantic drift regression fixture，盯住 `premise`、`beat`、`scene function`、`voice`、`continuity`、`canon` 等高频漂移词。
- [ ] 增加分层 review-depth preset，区分教学反馈、development-room feedback、preflight、launch-ready acceptance gate。
- [ ] 增加可 handoff 的 compact evaluation summary，避免 review 结果交接时又要回看整段历史。
- [ ] 增加 background bundle scope 和 checkpoint-vs-reload 决策质量的专项测试。

### Phase 9：Human-in-the-loop 社区运营

- [ ] 把现有 discussion-to-asset workflow 继续运营化，明确 ownership、节奏和 handoff 预期。
- [ ] 把现有 triage 分类进一步压成 maintainer 决策树，明确什么时候缩 claim、什么时候修 route、什么时候补 fixture、什么时候做治理调整。
- [ ] 在当前入口仍然偏自由输入的地方补 contributor 模板，支持 field note、failed route、successful override、professional disagreement report。
- [ ] 增加周期性 backlog review ritual，把高信号讨论转成 roadmap item 或闭环决定。
- [ ] 增加 intake metrics，比如 discussion 变 fixture 的数量、route bug 变测试的数量、反驳导致 claim 缩边界的数量。
- [ ] 增加 moderation playbook，让现有社区 guidance 在规模变大后仍然能稳定执行。
- [ ] 增加 contributor ladder onboarding，让贡献者能从 issue reporter 升级到 triage steward、knowledge curator。
- [ ] 只在确实能减少人工漂移时，才增加 triage / follow-up automation，避免制造新的 meta-work。

### Phase 10：双语与仓库包装成熟度

- [ ] 补齐深层文档的中英 parity，避免 English/Chinese 一边快、一边长期掉队。
- [ ] 增加关键术语 glossary，治理剧作、制作、审查、Agent 设计语境里的跨语言语义偏移。
- [ ] 增加 doc-level parity check，防止核心链接文档只更新一种语言。
- [ ] 增加更清晰的安装 / 调用示例，覆盖 Codex、Claude Code、OpenCode、Gemini CLI、OpenClaw 以及后续兼容 runtime。
- [ ] 增加面向新用户的“如何选 route”快速入口，降低 output vocabulary 的理解成本。
- [ ] 增加面向 Agent 的 quick-reference card，总结 loading mode、route 选择和升级规则。
- [ ] 只有在确实降低 onboarding 成本时，才增加 generated index / overview page，避免复制 source of truth。
- [ ] 保持 README 对外部访客仍然足够短，不把所有执行细节直接堆在 landing page。

## 维护原则

下一阶段的目标应该是提升辨识力、可执行性和抗回归能力。

不应该：

- 把仓库长成一个巨大的 runtime framework；
- 把每个新洞见都升级成一个新 taxonomy axis；
- 把每个成功案例都偷偷变成模板教条；
- 把双语覆盖做成重复灌上下文。
