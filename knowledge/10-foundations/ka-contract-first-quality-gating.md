---
{
  "id": "ka.contract-first-quality-gating",
  "type": "knowledge_atom",
  "title": "契约优先的质检逻辑",
  "kind": "workflow_rule",
  "summary": "自检不应先从泛泛‘好不好’开始，而应先确认当前 artifact 到底在交付什么 contract。只有 contract 先锁住，后续质量检查才不会漂到错题上。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "很多审查报告看似认真，实际上先审美、后定题，结果把 scene_draft 当 outline 审，把 project surface 当 story page 审，最终给出一堆方向错位的建议。",
  "decision_rules": [
    "先锁定当前正在审的 artifact contract，而不是直接进入泛泛点评。",
    "优先检查有没有做错题、漏交付、越权发挥，再检查实现质量。",
    "如果 target contract 不清楚，优先缩小问题范围或补最小必要信息，不要伪装成完整质检。"
  ],
  "anti_patterns": [
    "先给文风或好坏评价，再回头猜它本来要交什么",
    "用同一套剧本审美去审 branch map、team blueprint 或 project surface map",
    "contract 未锁定时就输出大段 rewrite 意见"
  ],
  "prompt_primitives": [
    "当前正在审的到底是什么 artifact，服务谁，成功条件是什么",
    "这份结果最先可能错在 contract、scope，还是实现质量",
    "如果 contract 还不清楚，最小补问或最小保守判断是什么"
  ],
  "evaluation_checks": [
    "是否先锁定了 target contract",
    "是否先做了 contract fit 再做质量判断",
    "是否避免了把错题写得更漂亮"
  ],
  "links": ["ka.two-stage-review-loop", "ka.scenario-factorization", "ka.boundary-first-guidance"],
  "source_status": "synthesized"
}
---
# 契约优先的质检逻辑

质检最怕一上来就“像个专业读者一样说很多”。真正高价值的质检，第一步不是发表判断，而是先确认这份东西本来在交什么题。

一个 `scene_draft` 应该先看场景功能、冲突和变化是否成立；一个 `screen_to_video_brief` 应该先看 clip 级不变量、桥接粒度和执行风险；一个 `project_surface_map` 则首先要看真源、运行态、handoff 和导出面有没有分清。题目都不同，检查入口当然不能混。

所以这个仓库的通用质检层必须先做 contract fit。只有题对了，后面的表达、节奏、完成度、自检分数才有意义。

## TODOs：待回答问题

- [ ] 哪些用户请求最容易把 `rewrite_report` 和 `quality_gate_report` 混为一谈？
- [ ] 当用户只给局部片段但要求全局判断时，contract-first 逻辑应如何限缩结论强度？
- [ ] 某些 hybrid artifact 同时服务人和工具时，contract 应如何分主次？
