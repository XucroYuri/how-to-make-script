# Socratic Question Backlog

## Purpose

This document is the repository-wide question engine for future knowledge expansion.

Use it to do three things:
- discover where the current knowledge model is still shallow;
- identify contradictions, edge cases, and missing standards;
- turn answered questions into new atoms, protocols, rubrics, fixtures, or case studies.

The repository should not grow only by adding conclusions. It should also grow by making its open questions explicit.

## How To Use

1. Pick one section or one file-level TODO block.
2. Answer the question with concrete examples, counterexamples, or routing implications.
3. Decide whether the answer belongs in:
   - a `knowledge_atom`
   - a `workflow_protocol`
   - an `evaluation_rubric`
   - an `example_fixture`
   - a case study or reference note
4. Update the relevant file and remove or narrow the TODO only after the answer has been encoded into the repository structure.

## Repository-Wide To-Dos

### Ontology And Taxonomy
- [ ] 哪些剧本知识现在其实被错误地塞进了同一个 atom，但应该拆成两个甚至三个更小的判断单元？
- [ ] 当前 taxonomy 是否遗漏了“短视频剧情化带货”“综艺化脚本”“实拍 + AI 混合叙事”这类灰区媒介？
- [ ] 哪些概念其实跨 `foundation / craft / medium / rubric` 多层存在，但仓库里还没有统一命名？
- [ ] 现在的 `intent x medium x stage x output x constraints` 路由维度，是否还缺少“production reality”或“distribution channel”这样的硬约束？
- [ ] 哪些知识更适合作为“反模式库”单独存在，而不是埋在主说明里？

### Foundations
- [ ] 什么情况下一个故事没有明确主角目标，依然能成立？这种例外应如何建模？
- [ ] 外部目标和内部目标发生冲突时，哪一种应该优先进入 logline 或 premise？
- [ ] 什么样的“情绪体验型作品”不适合强行套入传统因果驱动模型？
- [ ] 哪些类型或媒介的人物弧光并不依赖显著改变，而更依赖揭示或确认？
- [ ] 主题表达和说教之间的边界，能否形成更可操作的判断标准？

### Workflows
- [ ] 当前哪些协议默认前提过强，导致真实创作现场里并不总能直接套用？
- [ ] 哪些协议之间存在交叠，后续应通过更明确的 stop condition 或 handoff rule 切开？
- [ ] 在“先开发 premise”与“先开发角色/世界”这两种流程中，是否应该建立分支协议而不是只保留一种默认顺序？
- [ ] 商业脚本和互动叙事是否需要各自独立的 ideation 协议，而不是复用同一个 generic 发现流程？
- [ ] 哪些工作流步骤应增加“何时不要继续往下写，而应该回退重构”的明确停止信号？

### Craft
- [ ] 场景功能除了信息、关系、权力、行动条件之外，还需要单列哪些变化类型？
- [ ] 什么情况下“解释性对白”其实是必要的，而不是应被一律压缩？
- [ ] 节奏评价里是否需要为不同观看环境建立不同的密度模型，而不是只写通用原则？
- [ ] 哪些改稿病灶最容易被误诊成对白问题，能否建立更细的误诊清单？
- [ ] 是否需要单独建立“视角管理”“悬念管理”“反转前提管理”等 craft 原子？

### Media
- [ ] 长片、短剧、短视频三者在“开头必须完成什么”这件事上，能否形成更具体的对照表？
- [ ] 哪些品牌片其实更接近 narrative short，而哪些本质上仍是 ad logic？
- [ ] 游戏叙事和 branching interactive 的边界是否需要更清晰的区分规则？
- [ ] 动画项目里哪些信息必须在脚本阶段锁定，哪些可以留给分镜或导演环节再处理？
- [ ] 是否需要把“预算 / 制作复杂度 /拍摄可行性”作为媒介包里的独立判断维度？

### Genre
- [ ] 哪些类型机制目前缺席但在实际项目里高频，例如悬疑、恐怖、犯罪、爽剧、家庭伦理、儿童向？
- [ ] 类型混搭时，主类型和副类型的优先级应如何判断？
- [ ] 哪些类型承诺最容易被“表面元素”伪装出来，实际上底层结构并未成立？
- [ ] 是否需要为中文市场常见类型（短剧复仇、豪门、逆袭、都市情感、古装权谋）建立独立类型包？
- [ ] 不同平台对同一类型的节奏和兑现要求是否应拆成不同子包？

### Rubrics
- [ ] 哪些 rubric 现在还过于“判断正确但执行不够细”，需要加入更可量化的问题？
- [ ] hard-fail 规则在哪些情况下会误伤实验性或边界型创作？
- [ ] rubric 是否需要增加“不可修复/需回退上一层”的明确标志？
- [ ] 商业和互动类 rubric 是否还缺少更强的平台适配项或系统一致性项？
- [ ] 能否为 rubric 建立“轻评估版”和“开发会版”两种粒度？

### Fixtures And Cases
- [ ] 当前 fixture 是否覆盖了足够多的模糊请求、混合请求、越层请求和错误请求？
- [ ] 哪些 case study 现在只证明了“正向样例”，却没有证明边界失败是如何发生的？
- [ ] 是否需要增加对“用户提问不专业但意图真实”的 fixture，避免只服务熟练用户？
- [ ] 哪些典型改稿场景还没有 golden example，例如中段塌陷、对白同质、卖点分散、伪选择？
- [ ] 当前 example 是否足以证明 route stability，而不只是说明仓库里有一些示例？

### Agent Routing And Governance
- [ ] 哪些用户请求最容易在 narrative / commercial / interactive 之间被误路由？
- [ ] 何时应该优先返回一个小产物并追问，何时应该直接完整输出？
- [ ] 哪些文件还没有插入待回答问题，导致后续扩写容易遗漏？
- [ ] 是否需要为“新增问题 -> 回答问题 -> 升格为知识资产”的流程建立一个显式 checklist？
- [ ] 哪些英文 agent-facing 合约和中文 practitioner-facing 正文仍然可能在概念上不同步？

