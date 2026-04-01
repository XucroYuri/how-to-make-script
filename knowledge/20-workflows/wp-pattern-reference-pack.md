---
{
  "id": "wp.pattern-reference-pack",
  "type": "workflow_protocol",
  "title": "范式参考包协议",
  "goal": "针对一个明确的剧本创作问题，返回一份 pattern_reference_pack，给出场景分类、强样本、失败对照、成功/失败机制解释和非教条使用说明。",
  "input_contract": ["creative problem", "medium", "stage", "constraints", "none"],
  "output_contract": ["pattern_reference_pack"],
  "preconditions": [
    "用户需要参考范式、成功样本、失败对照或比较性教学",
    "至少可以锁定一个创作问题、媒介或阶段"
  ],
  "steps": [
    "先用场景分类法锁定当前问题属于哪类创作场景，而不是直接给样本。",
    "选择最相关的成功范式样本，并明确该样本主要解决的创作问题。",
    "给出一个失败或较弱的对照写法，确保差异不是只停留在风格喜好层。",
    "解释为什么强样本更有效、弱样本为什么失效，并写出适用条件与失效边界。",
    "补一段 non-dogma note，说明这只是高概率参考而不是唯一范式。"
  ],
  "fallbacks": [
    "若用户问题过宽，先压缩成一个最小创作问题再给参考包。",
    "若没有单一最佳范式，应返回 2-3 个同级参考方向，而不是伪装成单一答案。"
  ],
  "stop_conditions": [
    "成功样本、失败对照和差异解释同时存在",
    "至少写明一个适用条件和一个失效边界",
    "明确声明样本是参考而非唯一模板"
  ],
  "rubrics": ["rb.pattern-reference-pack"],
  "linked_atoms": ["ka.reference-pattern-usage", "ka.scenario-factorization", "ka.creative-pluralism", "ka.false-universal-warning"]
}
---
# 范式参考包协议

这个协议不是为了把仓库变成“最佳片段大全”，而是为了让范式参考变成一种可控的教学输出。它的重点不是“给你看一个好例子”，而是“让你看懂它为什么在这个问题上更强”。

真正好的 reference pack，一定要带失败对照。因为没有对照，成功很容易被误解成纯天赋、纯风格，或者更糟，误解成“只要长得像这样就对了”。对照一出来，创作判断点才会变清楚。

## TODOs：待回答问题

- [ ] 哪些问题最适合直接返回一个参考包，哪些问题更适合先走 path_options？
- [ ] 参考包是否需要按受众成熟度区分“新手版”和“专业版”？
- [ ] 当一个问题本身就存在两种同样常见的成功路径时，协议应如何避免伪单解？
- [ ] 是否需要给 reference pack 单独加“历史语境说明”，防止旧范式被误当成当下默认？
- [ ] 当样本来自商业或互动场景时，是否需要额外解释工业约束对成功定义的改变？
