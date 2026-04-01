---
{
  "id": "wp.genre-adaptation",
  "type": "workflow_protocol",
  "title": "类型适配协议",
  "goal": "在不破坏核心叙事引擎的前提下，把项目适配到目标类型或媒介。",
  "input_contract": ["existing premise", "existing outline", "target genre", "target medium"],
  "output_contract": ["premise", "treatment", "outline", "scene_draft"],
  "preconditions": [
    "已有可被改造的故事材料"
  ],
  "steps": [
    "识别原始故事中不可破坏的核心引擎。",
    "抽取目标类型或媒介的关键承诺。",
    "决定哪些结构、场景和角色关系需要重写。",
    "输出适配版本与主要变化说明。"
  ],
  "fallbacks": [
    "若改动后核心引擎消失，收缩适配强度。",
    "若目标类型约束互相冲突，优先保护核心承诺。"
  ],
  "stop_conditions": [
    "适配版仍保有核心引擎",
    "目标类型或媒介承诺已被满足"
  ],
  "rubrics": ["rb.outline"],
  "linked_atoms": ["ka.genre-thriller", "ka.genre-romance", "ka.genre-comedy", "ka.medium-feature-film", "ka.medium-commercial", "ka.medium-branching-interactive"]
}
---
# 类型适配协议

适配不是换皮。它要求保住原始引擎，同时重写承诺形式。

很多所谓“改成惊悚版”“改成短剧版”“改成互动版”的失败，本质都在于只换了表面元素，却没有调整真正决定观看体验的结构承诺。类型适配要处理的不是词汇替换，而是节奏、压力、信息释放、情绪兑现和媒介约束。

专业改编时最该盯紧的一点是：哪些是原故事不可丢的核心引擎，哪些只是当前版本的表达外壳。分不清这件事，适配很容易不是增强，而是把故事拆散。

## TODOs：待回答问题

- [ ] 当前适配协议在处理“跨媒介 + 跨类型 + 跨平台”的多重改造时是否过于粗粒度？
- [ ] 哪些适配本质上已经不是 adaptation，而是 new development，仓库是否需要设置判定阈值？
- [ ] 如何把“保住核心引擎”这件事进一步形式化，而不是停留在经验判断？
- [ ] 原作的卖点如果恰好与目标类型冲突，应该优先保住题材钩子、人物关系还是情绪承诺？
- [ ] 类型适配是否需要先拆出“不可动层”“可重写层”“必须重建层”三类清单？
- [ ] 当目标媒介的时长极端压缩时，哪些元素最容易被误删，导致适配后只剩表皮？
- [ ] 观众既有预期和 IP 既有印象是否应单独视为 adaptation 约束，而不仅是 genre 约束？
