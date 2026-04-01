---
{
  "id": "ka.prompt-delegation-levels",
  "type": "knowledge_atom",
  "title": "视觉提示委任层级",
  "kind": "heuristic",
  "summary": "从氛围级委任到动作级编排，视觉生成或跨团队镜头 brief 需要按控制强度分层，而不是默认越细越好。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["scene", "rewrite", "adaptation"],
  "problem": "Agent 在转写视觉 brief 时，要么控制太少，只剩氛围词；要么控制太多，变成冗长、互相打架的 shot soup。",
  "decision_rules": [
    "先判断当前任务需要的是氛围委任、动作控制、时间切分，还是精确编排，再决定提示层级。",
    "任务越短、镜头越少、模型越脆弱，越需要单一主动作和单一主相机逻辑。",
    "精度只应加到会改变结果的那一层；不会改变结果的细节不要提前锁死。"
  ],
  "anti_patterns": [
    "把所有层级的信息一次性全部写满",
    "4 到 8 秒短 clip 里同时塞入多个主动作、多个镜头运动和多个氛围反转",
    "把 screenplay 的叙事密度原封不动移植到生成提示里"
  ],
  "prompt_primitives": [
    "这次是让模型自由找调度，还是要锁动作顺序和时间切分",
    "当前 brief 的不可变项有哪些，哪些可以交给模型或下游团队二次决定",
    "如果只能保留一条动作线和一条镜头线，应该保哪两条"
  ],
  "evaluation_checks": [
    "控制粒度是否和任务复杂度匹配",
    "输出是否写清了固定项与可变项",
    "是否用更少但更有效的控制词替代了堆砌细节"
  ],
  "links": ["ka.bounded-context-loading", "ka.reference-expansion-balance", "ka.scenario-factorization", "ka.multilingual-visual-vocabulary"],
  "source_status": "derived"
}
---
# 视觉提示委任层级

很多视觉生成 brief 失败，不是因为它不够细，而是因为它没有分清楚“哪些东西必须被锁住，哪些东西应该留给模型或团队处理”。

这正是委任层级有用的地方。最低层可以只给气质、空间和主动作，把更多调度留给模型；中间层会锁住主体、动作、环境和主镜头；更高层才会进入时间切分、分段动作、甚至动作编排。问题不在于哪一层高级，而在于你是不是把控制强度放到了和任务匹配的地方。

对当前仓库来说，这层知识特别重要，因为它能把“写剧本”和“写可执行视频 brief”分开处理。剧本需要保留戏剧余量，视频 brief 则需要保留执行余量。两边都不该被另一边吞掉。

## TODOs：待回答问题

- [ ] 不同模型或平台下，这四层委任结构是否需要各自的适配版本？
- [ ] 哪些任务最适合从低层委任开始迭代，哪些则应一开始就给更强控制？
- [ ] 当团队协作里同时有导演、摄影和生成模型三类下游时，委任层级该如何拆给不同接收方？
- [ ] 如果用户要求高度 continuity，委任层级是否要显式加入“不可漂移要素”清单？
- [ ] 这套层级是否还需要和 `team_workflow_blueprint` 做更细的衔接，以区分谁负责锁定哪些层？

