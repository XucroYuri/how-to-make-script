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

- 仓库现在已经有 runtime-oriented metadata，但还不能把这些 metadata 真正消费成 live runtime planner。
- 仓库现在已经有 loading budget check 和自然语言路由 benchmark，但 benchmark 覆盖面和 bundle-planner 执行力仍然不足。
- 仓库现在已经有第一批 end-to-end journey 和 failure archive，但样本量还远远不够支撑多阶段创作可靠性。
- route 覆盖面已经很广，但 route-priority 规则和相邻输出的 adversarial fixture 仍然偏薄。
- 知识面已经大了，但 genre、medium、dialogue、character、case study 的深度仍然和仓库 ambition 不匹配。
- 社区入口已经有了，但 objections / failures 转成 fixtures、rubrics、case files 仍然太靠人工。
- 双语入口改善明显，但 parity 和 glossary 级别的语义纪律仍然不够。

## 同步后 Top 20 TODO

1. `P01` 扩展叙事类 end-to-end journey，覆盖 `premise -> character -> outline -> scene -> dialogue`。原因：当前 e2e 只证明到 scene，line-level creative continuity 还没被稳定证明。Phase：`Phase 5`。
2. `P02` 扩展 episodic、short-drama、interactive、branded 的 end-to-end journey。原因：当前 journey 还只覆盖仓库媒介面的很小一部分。Phase：`Phase 5`。
3. `P03` 扩充 failure archive，优先补 `handoff_loss`、`false_structure`、`context_overload`、`audience_mismatch`。原因：当前 failure archive 已经有价值，但规模还不足以形成稳定回归压力。Phase：`Phase 9`。
4. `P04` 增加 premise ↔ outline ↔ scene ↔ dialogue 的跨工件一致性检查。原因：很多创作失败发生在 handoff 漂移，而不是单一工件写坏。Phase：`Phase 5`。
5. `P05` 给 `premise`、`outline`、`scene_draft`、`dialogue_polish`、`commercial_script` 增加 output-specific quality preset。原因：仓库需要更强的创作核心工件默认审查配置。Phase：`Phase 5`。
6. `P06` 给高价值创作输出补自然语言路由 benchmark，优先覆盖 `beat_sheet`、`logline`、`synopsis`、`treatment`、`scene_card`、`scene_draft`。原因：新的 routing benchmark 还没覆盖大量核心写作输出。Phase：`Phase 7`。
7. `P07` 给 `research_background_map`、`story_memory_checkpoint`、`screen_to_video_brief` 补 benchmark 和 creative handoff coverage。原因：这些较新的输出现在已有 runtime metadata，但 route 和 handoff 证明还不够。Phase：`Phase 7`。
8. `P08` 深化 dialogue-stage atoms：subtext、信息差、节奏、去解释化、角色化说话。原因：对白层的知识细粒度仍然落后于结构层与路由层。Phase：`Phase 6`。
9. `P09` 深化 character-stage atoms：sympathy design、矛盾、关系压力、转变追踪。原因：角色层仍然缺少足够细的决策支撑。Phase：`Phase 6`。
10. `P10` 优先扩 genre packs：thriller、mystery、horror、comedy、romance。原因：这些问题簇覆盖了大量真实剧本场景，也最适合建立对照式样本。Phase：`Phase 6`。
11. `P11` 增加 stage-specific reference packs：weak opening、flat reveal、limp midpoint、collapsed ending、generic dialogue。原因：reference power 应该绑定具体问题族，而不是只停留在宽 craft。Phase：`Phase 6`。
12. `P12` 把 success/failure case study 做成显式对照样本，而不只是成功范式。原因：仓库需要教会 Agent 区分，而不是只展示“成功长什么样”。Phase：`Phase 6`。
13. `P13` 增加 screenplay-to-video 的创作保真示例，强调 screenplay logic 在 bridge 后仍然成立。原因：bridge layer 已经有了，但还需要更强的创作可信度。Phase：`Phase 6`。
14. `P14` 增加 checkpoint-aware creative handoff 样本，尤其是 dialogue resume / rewrite resume。原因：checkpoint layer 需要真实恢复路径，而不只需要静态路由。Phase：`Phase 5`。
15. `P15` 增加相邻输出的 route-priority register 和 adversarial fixtures。原因：runtime metadata 上线后，路由歧义会带来更高的执行成本。Phase：`Phase 7`。
16. `P16` 把 loading budget / adjunct bundles / loading modes 真正接成 bundle-planner 规则。原因：仓库现在已经记录了这些 metadata，但还没有把它们执行化。Phase：`Phase 7`。
17. `P17` 增加 craft term 语义漂移治理：`premise`、`beat`、`voice`、`canon`、`continuity`。原因：这些词已经跨写作、审查、失败归档和双语表面频繁出现，必须先稳住。Phase：`Phase 10`。
18. `P18` 基于新 runtime metadata 定义 live runtime planner contract。原因：metadata 层已经具备，缺的是消费它的 planner。Phase：`Phase 8`。
19. `P19` 增加 machine-checkable handoff packet schema 和 resumable runtime ledger。原因：没有 packet / ledger 契约，就无法把 live execution 做得可靠。Phase：`Phase 8`。
20. `P20` 把 community 里的 creative objections / failures 更稳定地转成 fixtures、rubrics、case files。原因：仓库的社区入口已经不错，但转资产回路还不够稳定。Phase：`Phase 9`。

## 同步后提交映射

- `08e9441` `Add runtime execution metadata for skills` -> `P15-P19`
- `c8e03cd` `Add routing benchmarks and budget checks` -> `P06-P07`、`P15-P17`
- `4410ec8` `Add end-to-end journeys and failure examples` -> `P01-P05`、`P11-P14`、`P20`
- `cb190e6` `Align runtime metadata checks with new routes` -> `P07`、`P16`、`P18-P19`

## 下一阶段路线

### Phase 5：创作链路与端到端可靠性

- Scope：`P01`、`P02`、`P04`、`P05`、`P14`
- Goal：让多阶段剧本创作链路在 handoff、resume 和多工件切换中仍然稳定。
- Done when：仓库不只会 route 这些创作链路，还能用 journey 和 consistency 检查证明它们可靠。

### Phase 6：创作知识深度与参考能力

- Scope：`P08`、`P09`、`P10`、`P11`、`P12`、`P13`
- Goal：把仓库对剧本创作质量的直接提升能力补到 dialogue、character、genre、contrastive reference 和 bridge fidelity 这些关键面。
- Done when：仓库能通过更深的知识层和更强的参考层提升创作结果，而不只靠更聪明的路由。

### Phase 7：路由、预算与加载治理

- Scope：`P06`、`P07`、`P15`、`P16`
- Goal：让 route 选择、benchmark 覆盖、loading budget 和 bundle expansion 规则真正达到可执行治理级别。
- Done when：仓库能明确解释为什么某条 route 胜出、允许加载多少上下文、以及何时必须停止扩容。

### Phase 8：Runtime 执行使能

- Scope：`P18`、`P19`
- Goal：把新 metadata 层真正接成 live runtime 的最小可执行契约。
- Done when：实现者可以基于明确的 planner / packet / ledger 契约搭建可恢复 runtime，而不是依赖 repo 默会知识。

### Phase 9：失败驱动的社区闭环

- Scope：`P03`、`P20`
- Goal：让 failure、反驳和实战 objections 能像成功案例一样稳定反哺仓库。
- Done when：社区回路能持续地产出 failure case、fixture、rubric 和 case file，而不是靠零散人工整理。

### Phase 10：双语与仓库包装成熟度

- Scope：`P17`
- Goal：先把高频漂移创作术语稳住，再做更深的双语 parity、glossary 和 onboarding packaging。
- Done when：`premise`、`beat`、`voice`、`canon`、`continuity` 这些词在写作、审查和 Agent 表面之间有清晰且一致的治理基础。

## 维护原则

下一阶段的目标应该是提升辨识力、可执行性和抗回归能力。

不应该：

- 把仓库长成一个巨大的 runtime framework；
- 把每个新洞见都升级成一个新 taxonomy axis；
- 把每个成功案例都偷偷变成模板教条；
- 把双语覆盖做成重复灌上下文。
