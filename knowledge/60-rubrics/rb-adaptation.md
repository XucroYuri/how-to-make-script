---
{
  "id": "rb.adaptation",
  "type": "evaluation_rubric",
  "title": "Adaptation Rubric",
  "applies_to": ["premise", "treatment", "outline", "scene_draft"],
  "dimensions": [
    {"name": "engine_preservation", "question": "原始核心引擎是否仍然成立，而不是只剩表面元素"},
    {"name": "target_promise_fit", "question": "目标类型或媒介承诺是否真的进入了结构、场景或表达层"},
    {"name": "translation_depth", "question": "改动是否触及节奏、信息释放、情绪兑现，而不只是换词换皮"},
    {"name": "output_viability", "question": "当前产物是否在自己的粒度上已经成立，而不是只在改编说明里成立"}
  ],
  "scoring_bands": {
    "excellent": "保住了核心引擎，也真正兑现了目标类型或媒介承诺。",
    "workable": "方向基本成立，但仍有换皮感、承诺不够深入或局部粒度不稳。",
    "weak": "不是核心引擎被冲掉，就是目标承诺仍停留在表层。"
  },
  "hard_fail_rules": [
    "改完后已无法说明原始核心引擎是什么",
    "目标类型或媒介承诺只体现在名词和表面气味上",
    "适配后的当前产物在其自身粒度上并不成立"
  ],
  "rewrite_actions": [
    "重新写出不可破坏的核心引擎",
    "把目标承诺落到结构、信息释放或场景执行上",
    "识别哪些地方只是换皮，哪些地方必须重写",
    "按当前产物粒度重建可执行版本，而不是只写适配说明"
  ]
}
---
# Adaptation Rubric

用于判断改编、类型适配和跨媒介适配是否真的成立。

这套 rubric 的重点不是“变得不像原来”，也不是“尽量不动原来”，而是看当前版本能不能既保住核心引擎，又真正兑现新的承诺。

## TODOs：待回答问题

- [ ] 哪些改编本质上已经越过 adaptation，进入 new development，需要单独出口？
- [ ] 当原作优势恰好与目标媒介节奏冲突时，engine_preservation 和 target_promise_fit 应如何取舍？
- [ ] 对 IP 连续性极强的项目，是否需要再补一层 continuity-specific hard fail？
