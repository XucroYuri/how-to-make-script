---
{
  "id": "ka.animation-story-trust-loop",
  "type": "knowledge_atom",
  "title": "动画 Story Trust 循环",
  "kind": "pattern",
  "summary": "动画开发往往依赖导演、故事、美术和后续生产之间的反复可视化迭代，而不是纯文本房间推进。",
  "mediums": ["animation"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "rewrite"],
  "problem": "把动画开发当成纯剧本文本工作，忽略 story sketches、视觉开发、reel feedback 对叙事判断的影响。",
  "decision_rules": [
    "动画模式应把 visual development 和 story iteration 当成主循环的一部分，而不是后置附件。",
    "导演或 story lead 需要定期对 story lane 和 visual lane 做统一判断。",
    "文本决策应提前暴露 production feasibility，而不是等镜头阶段才发现问题。"
  ],
  "anti_patterns": [
    "故事和视觉完全串行分离",
    "文本改动不考虑 visual reel 和 production reality",
    "所有反馈只围绕对白和情节，不围绕可视化叙事"
  ],
  "prompt_primitives": [
    "当前问题更像 story logic、visual storytelling，还是 production feasibility",
    "哪些 lane 需要以可视化片段而不是文字摘要交接",
    "导演 synthesis 节点应在什么频率出现"
  ],
  "evaluation_checks": [
    "视觉与故事是否被同时纳入循环",
    "反馈是否以可视化叙事问题为单位而不只是对白问题",
    "team mode 是否保留了导演或 story lead 的强收束角色"
  ],
  "links": ["ka.team-topology-selection", "ka.scene-function", "ka.boundary-first-guidance"],
  "source_status": "curated"
}
---
# 动画 Story Trust 循环

动画开发常常不像 live-action 那样先把纸面剧本写稳再逐层交给下游。它更像一个反复试映和反复可视化的 story trust 循环：故事、美术、导演、后续生产约束持续互相拉扯，最后慢慢收成一版真正能成立的影片或系列。

这意味着 Agent 团队模式也不能只做“写字分工”。动画模式需要更强的：
- director/story lead 收束；
- text-to-visual 的交接意识；
- story lane 与 visual lane 的双轨并行；
- 提前暴露 production feasibility 的 review gate。

## TODOs：待回答问题

- [ ] 动画长片、动画剧集、学龄前动画是否需要不同 trust loop？
- [ ] 仓库是否需要单独增加 reel-feedback 与 story-sketch 相关资产，而不只是文本产物？
- [ ] 哪些动画问题实际上更像 layout/acting 问题，不应硬塞回剧本团队？
