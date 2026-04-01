---
{
  "id": "ka.convergence-owner-discipline",
  "type": "knowledge_atom",
  "title": "收敛负责人纪律",
  "kind": "heuristic",
  "summary": "多智能体系统必须明确谁负责 merge、谁负责 veto、谁负责决定‘现在该停’；否则并行越强，结果越散。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "系统常常知道怎么开更多 lane，却没有清楚定义谁来结束分歧、锁定版本和决定下一步，从而让多智能体协作退化成永无止境的审稿会。",
  "decision_rules": [
    "每个多 lane 任务都必须显式指明 convergence owner 或 merge owner。",
    "reference persona 和 review board 可以施压、否决或要求补证据，但默认不拥有最终起草权。",
    "当多个 lane 的结论互相冲突时，收敛负责人必须输出 surviving core、dropped paths 和 reopen trigger。"
  ],
  "anti_patterns": [
    "默认所有专家共同拍板",
    "每次 merge 都重新讨论所有历史分歧",
    "review 节点不断加意见，但没有人负责定版"
  ],
  "prompt_primitives": [
    "谁拥有当前阶段的 merge authority，谁只提供 pressure 或 challenge",
    "如果现在必须删掉两条路径，谁来做决定，依据是什么",
    "什么条件下当前锁定版本可以重新打开"
  ],
  "evaluation_checks": [
    "收敛负责人是否明确且与当前阶段匹配",
    "分歧保留是否有退出条件，而不是永久挂起",
    "merge 结果是否同时记录 surviving core 与 dropped alternatives"
  ],
  "links": ["ka.dissent-preservation-loop", "ka.team-topology-selection", "ka.two-stage-review-loop"],
  "source_status": "synthesized"
}
---
# 收敛负责人纪律

高水平团队并不是没有分歧，而是知道分歧该由谁来收束。没有 convergence owner 的多智能体系统，看起来很民主，实际上最容易把最贵的时间浪费在反复 reopen 已经讨论过的问题上。

对剧本创作来说，分歧当然重要，但分歧的价值在于让系统看到更多可能性，而不是让每条可能性都永远活着。真正专业的协作，是在合适的时候保留异议，在合适的时候定版，并且知道什么证据足以推翻已经锁定的版本。

## TODOs：待回答问题

- [ ] 不同阶段的 convergence owner 是否应该固定，还是可以在 premise / outline / rewrite 间切换？
- [ ] 某些 team mode 是否需要双收敛结构，例如 creative owner + production owner？
- [ ] 当 human decision owner 缺位时，系统应该自动降级成更保守的 merge 机制吗？
- [ ] 是否应该把 reopen trigger 固化成 handoff packet 的标准字段？
- [ ] 什么时候 review board 可以合法升级为 convergence owner？
