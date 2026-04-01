---
{
  "id": "ka.scope-correction",
  "type": "knowledge_atom",
  "title": "范围修正",
  "kind": "decision_heuristic",
  "summary": "当一条剧本规则被反例击中时，仓库不应只在“硬扛”与“全盘推翻”之间二选一，而应优先做 scope correction。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "structure", "rewrite", "adaptation"],
  "problem": "仓库中的强规则一旦被挑战，维护者或 Agent 很容易走向两个极端：要么继续把它写成普遍规律，要么直接翻成另一条同样粗暴的反向定律。",
  "decision_rules": [
    "先找出原规则中仍然成立的最小核心，再决定如何缩窄它的适用范围。",
    "scope correction 必须同时写出失效条件、反例上下文和仍可成立的条件。",
    "如果一条规则在不同媒介、平台、受众或工业条件下需要不同版本，应允许并行路径共存，而不是强压成单一说法。"
  ],
  "anti_patterns": [
    "被反例击中后直接翻成相反定律",
    "只说这条规则不对，却不说明哪里仍然有用",
    "承认有边界，但不把边界写出来"
  ],
  "prompt_primitives": [
    "这条规则最小仍然成立的核心是什么",
    "它在哪些条件下失效",
    "如果把它缩窄成诚实版本，具体该怎么写"
  ],
  "evaluation_checks": [
    "是否保留了仍然成立的核心判断",
    "是否写明至少一种失效条件或反例上下文",
    "是否说明修正后会影响哪些 route、rubric 或输出"
  ],
  "links": ["ka.false-universal-warning", "ka.creative-pluralism", "ka.boundary-first-guidance", "ka.exploration-review-separation"],
  "source_status": "derived"
}
---
# 范围修正

很多仓库在面对强反驳时，最容易犯的错不是“不肯改”，而是“只会二极管式地改”。一条规则被反例击穿之后，要么死守原表述，要么直接翻成反向口号。两种都不成熟。

成熟的处理方式是做范围修正。也就是承认：原规则也许不是普遍规律，但可能仍然在某些条件下有效。问题不是“这条规则是不是全错”，而是“它到底只在哪些地方还成立”。

对 Agent 来说，这个能力尤其重要。因为模型很容易为了显得果断，把一条被质疑的强规则，改写成另一条同样强、但方向相反的规则。scope correction 的作用，就是逼它从“立场切换”转向“适用范围澄清”。

## TODOs：待回答问题

- [ ] 哪些现有规则最需要先做 scope correction，而不是继续维持笼统写法？
- [ ] 当反例还不够多时，scope correction 应保守到什么程度？
- [ ] 不同媒介下，scope correction 最常发生在结构规则、人物规则还是商业规则？
- [ ] 如果两个 scope-corrected 版本长期并存，何时应该拆成独立 atom？
- [ ] scope correction 是否需要配套一个 counterexample registry 才足够稳？
