---
{
  "id": "ka.reference-pattern-usage",
  "type": "knowledge_atom",
  "title": "参考范式使用法",
  "kind": "framework",
  "summary": "成功范式样本的价值，不在于给出唯一标准答案，而在于把高概率有效的写法、常见失败写法和背后的判断差异显式化。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "很多创作者和 Agent 在学习剧本时，要么只拿到抽象原则，不知道如何落地；要么直接把单个成功样本当成唯一模板，导致机械模仿。",
  "decision_rules": [
    "参考范式必须同时提供成功写法、失败对照和差异解释，而不是只给一个看似漂亮的答案。",
    "任何参考样本都应明确它解决的创作问题、适用条件和可能失效的边界。",
    "参考范式用于提高判断清晰度，不用于封死新的创意路径。"
  ],
  "anti_patterns": [
    "把成功样本当成唯一模板",
    "只给正例，不给失败对照",
    "解释为什么有效时只说感觉对"
  ],
  "prompt_primitives": [
    "这个样本具体解决了什么创作问题",
    "它为什么比常见失败写法更强",
    "除了这个范式，还有哪些替代路径也可能成立"
  ],
  "evaluation_checks": [
    "是否给出了强样本和弱样本的清楚对比",
    "是否说明了强样本的成功机制而非只给结论",
    "是否明确写出非唯一范式声明"
  ],
  "links": ["ka.scenario-factorization", "ka.creative-pluralism", "ka.false-universal-warning", "ka.scope-correction"],
  "source_status": "derived"
}
---
# 参考范式使用法

所谓“成功范式”，最容易被用坏的地方，是它明明是帮助判断的参考，最后却被误用成模板教条。仓库如果要收录这类内容，就必须把它设计成对照式的，而不是神谕式的。

一个真正有用的参考范式，至少应该同时回答四件事：它在解决什么问题、它为什么有效、常见失败写法为什么弱、以及除了它之外还有没有别的路能走。少了任何一项，这个范式都容易从“参考”滑成“背答案”。

对 Agent 来说，这一点尤其重要。因为模型天然倾向于把示范输出当成“最该模仿的单一路径”。所以仓库必须主动提醒：范式是高概率参考，不是宇宙唯一正确答案。

## TODOs：待回答问题

- [ ] 哪些参考范式最容易被新手和 Agent 误当成模板？
- [ ] 成功范式和失败对照之间的差异，哪些维度最值得标准化记录？
- [ ] 什么时候一个范式已经过时，应该退到历史语境里而不是继续放在默认推荐位？
- [ ] 是否需要为高风险题材单独记录“成功但不可直接照搬”的说明？
- [ ] 一个场景里如果存在两种同样强但方向不同的成功范式，仓库应如何并列展示？
