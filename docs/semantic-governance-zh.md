# 语义治理

仓库现在已经不是几份文档和几个 skill 的体量了。只要 root skill、router、manifest、workflow、fixture、docs 之间的概念开始各说各话，Agent 的执行质量就会明显下滑。

这份规则的目标只有一个：同一个概念，在不同层里不能悄悄变成不同含义。

## 治理规则

1. 一个公开概念尽量只有一个主名称。
2. 旧叫法可以保留，但必须通过明确的 alias 或 detail-key register 保留。
3. `public` skill surface 必须能被路由，也必须能从 root skill 找到。
4. 内部辅助 skill 可以存在，但必须声明 `surface: internal`。
5. skill manifest 至少要覆盖它对应 primary protocol 需要的 atoms。
6. 输出契约必须在这些层保持一致：
   - `SKILL.md`
   - [`references/supported-outputs.md`](../references/supported-outputs.md)
   - [`references/taxonomy.md`](../references/taxonomy.md)
   - `workflow_protocol.output_contract`
   - 被路由的 skill manifest
   - fixtures
7. route 的说法必须诚实。
   - 如果 `constraints` 只影响 loading，就不要假装它已经决定了 route。
   - 如果 `constraints` 真在做 route signal / tie-break，就要明确声明出来。

## Constraint Key 策略

公开的 canonical family 放在 [`references/taxonomy.md`](../references/taxonomy.md)。

历史 alias 和允许存在的 detail key 放在 [`references/constraint-key-register.json`](../references/constraint-key-register.json)。

这个 register 的用途不是鼓励继续乱命名，而是给仓库一个可治理的兼容层：
- 旧 fixture 还能活；
- 更细的制作细节还能表达；
- 新增内容不会继续无限漂。

## Route Signal 策略

`router-matrix` 里的 `constraint_signals` 只做三件事：
- 解释为什么这个 route 合理；
- 当相邻 route 未来开始接近时，提供 tie-break 依据；
- 让 loading 判断可追踪，而不是黑箱。

它不是为了把 router 重新做成关键词猜测器。

## Surface 策略

- `public` surface 是 root orchestration 的正式公开能力。
- `internal` surface 可以作为拆分层、迁移层、对比层存在，但不应该被误认为是公开入口。

## 验证

这层治理现在由这些脚本保障：
- [`scripts/check_semantic_consistency.py`](../scripts/check_semantic_consistency.py)
- [`scripts/check_routes.py`](../scripts/check_routes.py)
- [`scripts/check_route_overlaps.py`](../scripts/check_route_overlaps.py)

目标不是追求“概念完美”，而是防止仓库在不知不觉中开始对 Agent 讲互相矛盾的话。
