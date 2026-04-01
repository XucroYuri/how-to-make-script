---
{
  "id": "ka.dissent-preservation-loop",
  "type": "knowledge_atom",
  "title": "异议保留循环",
  "kind": "heuristic",
  "summary": "高水平团队不会把少数路线和专业反对意见过早消音，而是把它们保存到明确的收敛关口再处理。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "outline", "rewrite", "adaptation"],
  "problem": "团队表面达成一致很快，但真正有价值的反路径、反例和专业警告被太早抹平。",
  "decision_rules": [
    "把 dissent 当成待编码资产，而不是团队噪音。",
    "在 convergence gate 之前，至少保留一条高质量 alternative 和一条明确的 failure warning。",
    "异议如果削弱了规则但没有杀死它，优先转成 scope correction 或 boundary map。"
  ],
  "anti_patterns": [
    "谁声音大谁先定路线",
    "为了推进速度过早删掉 alternative",
    "把专业反对意见当成纯主观偏好"
  ],
  "prompt_primitives": [
    "当前主路线最有力的反路径是什么",
    "如果反对意见成立，它最可能在哪个 gate 爆炸",
    "哪些 dissent 需要保留到下一个 review，而不是现在就消音"
  ],
  "evaluation_checks": [
    "团队是否显式保存了 alternative 和 failure warning",
    "异议是否被编码进后续 asset，而不是停留在口头争执",
    "收敛是否发生在规定关口，而不是被权力或疲劳提前触发"
  ],
  "links": ["ka.creative-pluralism", "ka.scope-correction", "ka.divergence-convergence-loop"],
  "source_status": "synthesized"
}
---
# 异议保留循环

顶级团队并不等于“永远快速统一意见”。很多时候，真正让作品变强的恰恰是那些没被第一时间消掉的异议。问题不在于有没有分歧，而在于分歧有没有被体面地存活到正确的关口。

这也是为什么多智能体系统不能只追求“尽快出一个统一答案”。如果 alternative 没有地方存活，Agent 很快就会学会讨好主路线，结果看起来稳定，实际上丢掉了最有价值的对照判断。

所以异议保留循环的重点是：先让 dissent 有编码位置，再让 convergence 有明确时间。这样团队既不会永远开分岔，也不会因为赶进度把真正关键的警报当成杂音扔掉。

## TODOs：待回答问题

- [ ] 哪些 team mode 天然更需要正式 dissent log，哪些模式可以更轻？
- [ ] 如果 human decision owner 明确偏好某一路线，系统还要把 alternative 保留到什么程度？
- [ ] 异议保留是否需要和 fixture / example case 直接联动，形成回归样本？
- [ ] 对商业项目，什么时候 dissent 主要来自品牌和平台现实，而不是创意本身？
- [ ] 当 dissent 只是低质量反对而非高质量 alternative 时，仓库应如何快速识别并清理？
