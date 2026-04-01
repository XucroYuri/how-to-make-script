---
{
  "id": "ka.room-artifact-ladder",
  "type": "knowledge_atom",
  "title": "房间式产物梯子",
  "kind": "heuristic",
  "summary": "高水平团队不是靠一直开会达成一致，而是靠一串可收敛、可回收、可审阅的中间产物逐步逼近成稿。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "rewrite", "adaptation"],
  "problem": "团队讨论很多，但没有共享 artifact ladder，导致观点堆积、版本失控、回顾困难。",
  "decision_rules": [
    "先定义这个 team mode 的 artifact ladder，再安排 parallel lanes 和 review cadence。",
    "任何一次讨论都应指向某个明确产物的推进，而不是停留在抽象意见交换。",
    "中间产物要足够轻，能快速回收，也要足够实，能承载真实分歧。"
  ],
  "anti_patterns": [
    "只开讨论会，不沉淀中间产物",
    "过早追求完整成稿，跳过可回收的中间层",
    "不同团队成员对当前产物层级理解不一致"
  ],
  "prompt_primitives": [
    "在当前 team mode 里，最小可推进 artifact 是什么",
    "这一轮到底要锁 premise、engine、beat、scene packet 还是 revision list",
    "哪个产物最适合作为下一个 human checkpoint 的载体"
  ],
  "evaluation_checks": [
    "artifact ladder 是否清楚并可执行",
    "每一层产物是否有对应 owner 和 review gate",
    "团队是否能通过产物而不是抽象记忆维持共享上下文"
  ],
  "links": ["ka.divergence-convergence-loop", "ka.exploration-review-separation", "ka.scene-function"],
  "source_status": "synthesized"
}
---
# 房间式产物梯子

顶级团队看起来像是在“共同讨论出作品”，但真正起作用的通常不是讨论本身，而是讨论被压进了哪一层中间产物。没有 artifact ladder，room 很快就会变成口头协商现场：谁记得什么、谁以为已经定了什么，全靠记忆和气势。

一个健康的 artifact ladder 可以很轻，但不能没有。它可能是 premise slate、series engine memo、episode beat board、sequence reel、campaign script matrix、branch state map、rewrite hit list。名字可以不同，但作用相同：它让团队知道“此刻我们到底在推进哪一层”。

对多智能体系统来说，这层尤其重要。因为 Agent 之间没法像真人那样共享模糊默契，只能共享可指认的中间产物。没有梯子，协作就只剩下互相转述。

## TODOs：待回答问题

- [ ] narrative、commercial、interactive 三大类项目，artifact ladder 是否应分别冻结一套默认骨架？
- [ ] 对短周期 campaign 或短剧高速开发，哪些中间产物可以合并，哪些绝不能跳过？
- [ ] 当团队已有现成 DCC、看板或编剧室工具时，仓库中的 artifact ladder 应如何与外部工具映射？
- [ ] 是否需要单独增加“room packet / note packet / revision packet”这类更细粒度产物契约？
- [ ] 在强作者主导项目里，artifact ladder 是否应更短，但 gate 更硬？
