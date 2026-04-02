# Canonical 术语治理策略

## 目的

这个仓库的术语治理要同时满足两件事：
- 人类读起来顺，不像翻译腔或 AI 机械词；
- Agent 看到的是稳定概念，不会因为不同文档各说各话而漂移。

核心规则很简单：
- 一个公开概念，尽量只有一个主名称；
- 面向人的 prose 允许更自然，但不能越过概念边界；
- 面向机器的 ID、schema、route contract 不因为显示文案优化而反复改名。

这份策略和以下文档一起工作：
- [`docs/semantic-governance-zh.md`](./semantic-governance-zh.md)
- [`docs/bilingual-authoring.md`](./bilingual-authoring.md)
- [`references/canonical-term-register.json`](../references/canonical-term-register.json)

## 治理对象分层

### `L0` 合约层

包括：output ID、schema field、router output、manifest key、fixture contract key、checker 识别名。

规则：
- 只用 canonical 名；
- 不在机器字段里混进 prose 别名；
- 除非要正式迁移公共接口，否则不要改稳定 ID。

例子：
- `voice_style_guide` 继续作为 output ID 保留。

### `L1` 执行层

包括：workflow、rubric、policy、supported outputs、execution-facing reference。

规则：
- 默认使用 canonical 显示词；
- 如果 English contract 名必须一起出现，首现可加一次括注；
- 用词要让 Agent 能明确区分相邻概念，不能为了顺口把边界写糊。

### `L2` 阅读层

包括：README、reference pack、examples、onboarding、贡献者指引。

规则：
- 以“人读着顺”为先；
- 但必须和 `L0`、`L1` 指向同一个概念；
- 只有在读者大概率更熟旧叫法或更熟英文内部名时，才加括注。

### `L3` 历史层

包括：roadmap、review note、archive 类文档。

规则：
- 可以保留旧词；
- 如果旧词还会影响理解，首现加一个短映射说明，避免历史漂移重新污染现行表面。

## 处理规则

### 硬改

以下情况直接替换，不保留旧词：
- 词本身带错域含义；
- 在目标语言里机械感太重；
- 会把 route、review 或概念边界带偏。

例子：
- `声纹` -> `角色声音`
- `voiceprint` -> `character voice` 或其他领域正确词
- `表达镜头` -> `表达校准包`
- `Voice Pattern Pack` -> `Character Voice Reference Pack`

### 保留并加括注

以下情况保留内部名，但需要显示词辅助：
- 机器名必须稳定；
- English contract 名对跨文档查找仍然重要；
- 仓库正在从旧显示词迁移到新显示词。

例子：
- 继续写 `voice_style_guide`，但附近 prose 用“表达风格指南”；
- 中文治理文档首现 `expression lens` 时，可写成 `expression lens（表达校准包）`，如果确实要对照英文内部名。

### 原样保留

以下情况不改：
- 已经是稳定公共接口；
- 本来就是该层正常、准确的术语；
- 改了只会新增漂移，不会减少漂移。

例子：
- `voice_style_guide`
- `taxonomy`
- `canonical packet`

## 当前 canonical 决议

- `character voice`
  - 中文主词：`角色声音`
  - 对白细分语境允许：`角色口吻`
  - 禁用漂移词：`声纹`、`voiceprint`
- `voice_style_guide`
  - 稳定 output ID：`voice_style_guide`
  - 英文显示名：`Voice Style Guide`
  - 中文显示名：`表达风格指南`
- `expression lens`
  - 中文显示名：`表达校准包`
  - 禁用中文漂移词：`表达镜头`
- 声音参考包类表面
  - 英文显示名：`Character Voice Reference Pack`
  - 中文显示名：`角色声音参考包`

## 执行与约束

[`references/canonical-term-register.json`](../references/canonical-term-register.json) 是禁用词和迁移敏感词的机器可读注册表。

[`scripts/check_canonical_terms.py`](../scripts/check_canonical_terms.py) 会：
- 扫描高风险公开表面；
- 排除已声明的历史层文档，避免历史记录反向污染现行表面；
- 拦截禁用词；
- 防止仓库把已经废止的词悄悄写回来。

## 变更流程

当仓库要引入或改一个公开概念时：
1. 先改 register；
2. 再改 policy / governance prose；
3. 再改活跃 public surfaces；
4. 最后才处理 examples、reference pack 和更外围的阅读表面。
