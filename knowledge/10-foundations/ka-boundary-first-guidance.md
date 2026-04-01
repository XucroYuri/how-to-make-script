---
{
  "id": "ka.boundary-first-guidance",
  "type": "knowledge_atom",
  "title": "边界优先导向",
  "kind": "principle",
  "summary": "与其假装存在唯一正确创作法，不如先明确哪些是硬边界、哪些是软约束、哪些区域可以大胆探索。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "rewrite", "adaptation"],
  "problem": "系统把大量不同等级的限制混写在一起，结果不是过于保守，就是边界失真。",
  "decision_rules": [
    "先区分 hard boundary 和 soft constraint，再决定探索或收敛策略。",
    "能后置的约束不要前置成探索阶段的教条。",
    "任何建议都应该至少说明：什么绝对不能做，什么可以先大胆试，什么要留到 review 再判断。"
  ],
  "anti_patterns": [
    "把风格偏好写成底线",
    "把真正底线写成可谈判偏好",
    "一开始就用全部现实约束锁死探索"
  ],
  "prompt_primitives": [
    "当前有哪些 hard boundary 永远不能越过",
    "哪些 soft constraint 可以先暂挂",
    "当前最值得大胆探索的区域在哪里"
  ],
  "evaluation_checks": [
    "边界级别是否分类清楚",
    "是否保留了足够的可探索空间",
    "是否避免了把软约束误写成硬规则"
  ],
  "links": ["ka.exploration-review-separation", "ka.platform-attention-economy", "ka.commissioning-fit", "ka.audience-need-state"],
  "source_status": "synthesized"
}
---
# 边界优先导向

当创作问题太复杂时，“直接给正确答案”往往是假精确。更可靠的做法，常常是先告诉使用者：哪些东西绝对不能碰，哪些东西只是暂时偏好，哪些区域可以放心做更大胆的实验。

边界优先的价值在于，它能给创作留出空间，同时又不至于把系统变成完全失控的发散器。你不是在告诉用户“随便来”，而是在告诉他“这几块是铁边界，这几块先别急着自我审查，这几块后面再回看”。

这比提前灌输一个看似正确的创作路径更诚实，也更适合真实项目开发。

## TODOs：待回答问题

- [ ] 对商业脚本和作者表达项目，边界优先的表达方式是否应该不同？
- [ ] 哪些常见 soft constraint 最容易在中文创作环境里被误当成 hard boundary？
- [ ] 什么时候“边界优先”会被误用成逃避判断，仓库该如何防止？
- [ ] 哪些 boundary map 应该在 ideation 阶段就生成，哪些只在 rewrite 阶段才有意义？
- [ ] 当用户自己把 soft constraint 当成铁律时，Agent 应如何温和拆解？
