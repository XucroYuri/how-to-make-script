---
{
  "id": "ka.interactive-branch-lab",
  "type": "knowledge_atom",
  "title": "互动分支实验室",
  "kind": "pattern",
  "summary": "互动叙事团队必须把 narrative、systems、state 和 test loop 放在同一工作流里，而不是先写完故事再补交互。",
  "mediums": ["game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "outline", "scene", "rewrite", "adaptation"],
  "problem": "把互动叙事写成线性剧本再强行切分支，导致假选择、状态失真和可玩性崩坏。",
  "decision_rules": [
    "interactive 模式至少并行 narrative lane、systems/state lane、test/qa lane。",
    "每轮 branch design 后都要有可玩性与逻辑一致性检查，而不是只看文本是否好看。",
    "当 branch explosion 风险升高时，应优先压缩 topology 而不是继续堆内容。"
  ],
  "anti_patterns": [
    "所有选择只改口气不改后果",
    "状态模型后置，导致 later branches 无法闭环",
    "没有 test lane，直到很晚才发现分支不可达或逻辑断裂"
  ],
  "prompt_primitives": [
    "当前问题更像 narrative promise、state logic，还是 qa visibility",
    "哪条 branch 需要 test loop 先行验证而不是继续扩写",
    "哪些内容必须回到 shared room 决定，哪些可以 lane 内解决"
  ],
  "evaluation_checks": [
    "narrative、systems、test 是否真的形成三角协作",
    "分支设计是否配套 state 与 QA gate",
    "团队模式是否有机制防止 branch explosion"
  ],
  "links": ["ka.medium-branching-interactive", "ka.scenario-factorization", "ka.boundary-first-guidance"],
  "source_status": "curated"
}
---
# 互动分支实验室

互动叙事不是多写几条支线，而是让故事、系统、状态和测试互相咬合。只要这四件事分开太久，最后一定会回到“文本像剧本、交互像补丁”的老问题。

所以 `interactive_branch_lab` 模式的关键不只是 narrative designer，而是 narrative、systems、QA 的三角关系。一个好的互动团队模式，应该让分支设计在一开始就带着状态逻辑和测试可视性推进，而不是等写完以后才问“这条路能不能玩”。

## TODOs：待回答问题

- [ ] 不同互动容器，例如 visual novel、RPG 支线、叙事手游事件，是否需要不同 lab 节奏？
- [ ] 仓库是否要进一步支持 automated branch test artifact，而不仅是地图和文本产物？
- [ ] 玩家数据回流进入 rewrite loop 时，interactive_branch_lab 应如何变化？
