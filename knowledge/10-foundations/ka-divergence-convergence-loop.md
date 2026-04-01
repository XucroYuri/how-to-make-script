---
{
  "id": "ka.divergence-convergence-loop",
  "type": "knowledge_atom",
  "title": "发散-收敛循环",
  "kind": "framework",
  "summary": "创作不是一路收敛，也不是无止境发散，而是在扩大可行空间和重新收束之间反复切换。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "rewrite", "adaptation"],
  "problem": "创作流程要么过早锁死，要么永远不收口，导致项目既没有探索深度，也没有交付节奏。",
  "decision_rules": [
    "先用发散阶段扩大 option space，再用收敛阶段引入当前最关键的约束。",
    "每次收敛都必须说明依据是什么，不要只因为维护者或用户更熟悉某条路就直接锁定。",
    "当现有路径全部显得平庸或互相矛盾时，应重新发散，而不是勉强在坏选项中选一个。"
  ],
  "anti_patterns": [
    "一上来就只剩一个答案",
    "持续发散但没有收敛节点",
    "收敛依据只是偏好或惯性"
  ],
  "prompt_primitives": [
    "此刻最该先发散还是先收敛",
    "本轮收敛依据的关键约束是什么",
    "如果当前解都不理想，应该回到哪一层重新发散"
  ],
  "evaluation_checks": [
    "是否存在清楚的发散阶段和收敛阶段",
    "收敛是否引用了明确约束而非空泛偏好",
    "项目卡住时是否知道该回退到哪一层"
  ],
  "links": ["ka.creative-pluralism", "ka.boundary-first-guidance", "ka.exploration-review-separation", "ka.rewrite-diagnosis"],
  "source_status": "synthesized"
}
---
# 发散-收敛循环

创作流程真正难的，不是只会发散，也不是只会收敛，而是知道什么时候应该切换。太早收敛，方案会平；太晚收敛，项目会散。发散-收敛循环讲的就是这种节奏控制。

这套循环对 Agent 尤其重要，因为系统很容易把“快速给出一个答案”误当成高能力。但创作里很多时候真正高能力的表现，是先展开几个 viable path，再根据约束和目标做后置收束。

好的收敛不是“终于拍板”，而是“知道为什么此刻该收”。同样，好的发散也不是“脑洞越多越好”，而是“把真正不同的可能性打开”。

## TODOs：待回答问题

- [ ] 哪些用户请求默认就该进入发散-收敛双阶段，而不是一步到位？
- [ ] 发散阶段最容易被哪些商业或审美偏好过早截断？
- [ ] rewrite 阶段是否也需要保留一次局部发散，而不只是修补原方案？
- [ ] 对高时限短内容项目，这个循环应该如何压缩但不失效？
- [ ] 如何判断当前项目的问题来自“发散不够”还是“收敛过晚”？
