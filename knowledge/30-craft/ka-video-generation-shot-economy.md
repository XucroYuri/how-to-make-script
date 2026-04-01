---
{
  "id": "ka.video-generation-shot-economy",
  "type": "knowledge_atom",
  "title": "视频生成镜头经济学",
  "kind": "heuristic",
  "summary": "短时长视频生成最怕多主动作、多主镜头和多主意图竞争，因此桥接层必须主动压缩成单一主动作、单一主镜头逻辑和清楚的不变量。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video"],
  "stages": ["scene", "rewrite", "adaptation"],
  "problem": "一个戏剧上成立的场景，直接进入 4 到 12 秒生成容器后，经常因为动作太多、转折太多、镜头太多而彻底失焦。",
  "decision_rules": [
    "每个短 clip 优先只保一条主动作线和一条主镜头线。",
    "把时长有限的 clip 当成证明某个戏剧动作成立的最小容器，而不是试图复刻整场戏。",
    "连续性需求要用 invariants 单列，而不是在正文里重复啰嗦。"
  ],
  "anti_patterns": [
    "一个 clip 里同时要求推进、转折、揭示、反转和抒情",
    "同时指定多个互相竞争的镜头运动",
    "靠堆细节代替筛选主信息"
  ],
  "prompt_primitives": [
    "这段 clip 最核心的动作证明是什么",
    "如果镜头只能做一次明显运动，最值得保留的是哪一次",
    "哪些连续性要素必须写成 invariants 才不会丢"
  ],
  "evaluation_checks": [
    "主动作是否单一且可视",
    "相机逻辑是否清楚且不过载",
    "不变量是否被明确列出并从正文噪音里分离"
  ],
  "links": ["ka.screenplay-to-video-boundary", "ka.prompt-delegation-levels", "ka.pacing-rhythm", "ka.medium-commercial"],
  "source_status": "derived"
}
---
# 视频生成镜头经济学

很多 scene 在剧本层是成立的，但一压进短视频生成容器就会坏掉。根本原因通常不是模型不够强，而是 brief 没有替它做“镜头经济学”。

所谓镜头经济学，说白了就是：在一个很短的 clip 里，到底什么值得留下来，什么必须被砍掉。剧本里可以同时存在关系变化、信息揭示、动作推进、情绪反转，但在 4 到 12 秒的可视化容器里，往往只能保最关键的那一下。其余内容不是进入下一条 clip，就是留在上游剧本里。

这对 Agent 特别关键，因为它天生倾向“把懂的都说出来”。而在视频生成 brief 里，说得越多，不一定越好，常常只是让多个主意图互相打架。

## TODOs：待回答问题

- [ ] 4 秒、8 秒、12 秒三种时长下，clip 允许承载的动作密度是否应形成更细的经验表？
- [ ] 不同类型内容里，“单一主动作”的容忍度是否不同，例如武打、广告、情绪戏、动画特效？
- [ ] 当用户坚持要求多动作、多镜头时，桥接层是否应自动拆分成 clip chain 而不是继续硬写？
- [ ] 对强调音画同步的内容，这条镜头经济学是否要把音频节拍视作和镜头同级的主线？
- [ ] continuity 要素过多时，仓库是否需要单独的 invariant ranking 规则？

