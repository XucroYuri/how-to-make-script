---
{
  "id": "ka.showrunner-room-cadence",
  "type": "knowledge_atom",
  "title": "Showrunner 房间节奏",
  "kind": "pattern",
  "summary": "TV writers' room 的核心不是多人热闹，而是由 showrunner 驱动的持续分工、反复汇总和生产关联写作。",
  "mediums": ["episodic", "short_drama"],
  "stages": ["premise", "character", "structure", "outline", "scene", "rewrite"],
  "problem": "把剧集开发写成 feature 式单线程，或误把 room 理解成无限平权发散，导致 season engine 和 episode breakdown 失控。",
  "decision_rules": [
    "showrunner 负责 season engine、voice ceiling、production reality 和最终收束。",
    "room 内允许平行拆 episode、A/B/C 线和 scene problem，但必须有定期 synthesis 节点。",
    "development room 与 post-greenlight room 不是同一强度的 workflow，人员和交付物都应调整。"
  ],
  "anti_patterns": [
    "没有 showrunner synthesis 的平行碎片化输出",
    "剧集房间只讨论单集而不维护 season engine",
    "房间结束后继续把关键写作外包成无主 freelance patching"
  ],
  "prompt_primitives": [
    "当前 room 是 pre-greenlight 还是 regular room",
    "本轮需要拆的是 season arc、episode beat，还是 production rewrite",
    "哪些问题可以分 lane，哪些问题必须回到 room 共识"
  ],
  "evaluation_checks": [
    "season engine 是否被持续维护",
    "房间 cadence 是否有清晰的拆分和收束节奏",
    "输出是否匹配当前房间阶段而不是一锅炖"
  ],
  "links": ["ka.team-topology-selection", "ka.audience-need-state", "ka.conflict-pressure"],
  "source_status": "curated"
}
---
# Showrunner 房间节奏

writers' room 最容易被浪漫化成“大家一起想点子”，但专业房间真正稀缺的是节奏控制。showrunner 不只是最有经验的编剧，而是决定哪些问题要 room 里集体解决，哪些问题可以分给单个 writer-producer 或 lane 去消化，再在什么节点拉回统一世界观、统一 tone、统一 production reality。

Agent 版本的 `showrunner_room` 也应该保留这个逻辑。它不该是所有 specialist 平权并行到最后，而应是：
- showrunner_orchestrator 锁定目标和 ceiling；
- 并行 lanes 解决不同层级的问题；
- 固定 cadence 回到统一收束；
- 高风险问题进入 human review。

## TODOs：待回答问题

- [ ] 长剧、迷你剧、短剧的 room cadence 是否需要独立模式？
- [ ] 当平台给出强命题时，showrunner room 的发散空间应如何缩窄？
- [ ] 哪些 episode-level 工作最值得下放给 specialist，哪些必须永远由 showrunner 守住？
