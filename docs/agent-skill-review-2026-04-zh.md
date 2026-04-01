# Agent Skill 评审 2026-04

## 范围

这次评审不是把仓库当成“知识库”看，而是把它当成一个可执行的 Agent 系统来检查。

核心目标：
- root 里的说法和实际实现之间有没有逻辑闭环；
- 面对多样化剧本场景时，route 是否真的可靠；
- 渐进式披露是否真实存在，而不是永远最大化出场；
- docs、manifest、workflow、router、fixture 之间有没有语义漂移；
- 能不能通过更清晰的契约和治理，提升高水平结果的可获得概率。

## 主要发现

### 1. `constraints` 的作用之前被说大了

仓库之前的表述接近“按 `intent x medium x stage x output x constraints` 路由”，但可执行的 route 检查其实只用了前四维。

修复：
- root skill 和 routing policy 改成更诚实的描述；
- 给 router entry 增加了 `constraint_signals`；
- 更新 route check，让 `constraints` 在相邻 route 出现接近时可以做 tie-break，而不只是文档口号。

### 2. manifest 和 protocol 已经开始漂了

几个 skill manifest 已经不再覆盖自己 workflow protocol 真正依赖的 atoms。

修复：
- 把 manifest 补齐到至少覆盖 protocol 的 linked atoms；
- 增加语义一致性检查，把这类漂移正式纳入 CI。

### 3. public surface 和 internal surface 之前没有说清

仓库里已经出现了存在于 repo、但既不走 router、也不在 root skill 公开表面上的 skill。

修复：
- manifest 新增 `surface: internal`；
- CI 开始检查：public surface 必须可路由且 root 可见；internal surface 不能伪装成公开入口。

### 4. constraint key 已经出现 canonical 名称和历史细粒度键混用

fixtures 里混杂了 canonical family、旧 alias、以及一些更窄的 detail key。

修复：
- 明显应该成为一等 family 的约束被补进 taxonomy；
- 新增 constraint-key register 管理 alias 和允许存在的 detail key；
- CI 开始阻止未知 key 静默扩散。

### 5. 渐进式披露之前更多是“感觉上有”，但还不够显式

仓库已经有很多高级输出，但升级梯度主要还停留在隐式理解。

修复：
- 新增单独的 progressive disclosure policy；
- 把核心 artifact、校准 lens、诊断/发散层、协作设计层、长周期治理层正式分开。

## 当前残余风险

- 现在 `constraint_signals` 已存在，但 route 仍主要是 output-anchored。这对当前 matrix 是合理的，但后续新增 route 时必须保持诚实。
- 仓库本身已经很大了。后续质量更依赖治理纪律，而不是继续无上限加内容。
- pattern packs、team mode、project surface 这些层仍然很容易被滥用成“大而全的聪明回答”。

## 评审结论

现在这个设计已经比之前更像一个可持续演进的 Agent 系统：
- 更诚实地说明 route 到底怎么定；
- 更强地治理语义一致性；
- 更明确地控制高级层什么时候该出场；
- 更不容易在仓库继续扩展时发生静默漂移。
