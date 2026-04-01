---
{
  "id": "ka.ip-voice-continuity",
  "type": "knowledge_atom",
  "title": "IP 角色语气延续",
  "kind": "heuristic",
  "summary": "IP 延续不是复刻名台词，而是保住角色看世界的方式、价值取舍、表达禁区和可变化范围。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["character", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "续写、改编或跨媒介开发时，角色表面像原角色，深层却已经变成另一个人。",
  "decision_rules": [
    "先提炼不能丢的 voice anchors，例如价值排序、羞耻点、常见回避动作和思维路径。",
    "把 continuity 建立在决策逻辑和表达禁区上，而不是建立在几句经典语录上。",
    "明确 variability budget，允许情境变化带来声调浮动，但不允许核心认知和关系反应断裂。"
  ],
  "anti_patterns": [
    "只靠模仿口头禅和名句维持所谓熟悉感",
    "为了新剧情便利强行改变角色的判断逻辑",
    "把续写写成作者对 IP 的印象拼贴"
  ],
  "prompt_primitives": [
    "这个角色最稳定的认知偏向是什么",
    "他在关系冲突里最常守住和最常回避的东西分别是什么",
    "哪些新写法会让熟悉这个 IP 的观众立刻觉得不对"
  ],
  "evaluation_checks": [
    "角色延续是否建立在深层逻辑而不只是表面模仿",
    "新场景里的语言变化是否仍在可接受的连续区间内",
    "是否明确写出了 drift risk 和不可越界点"
  ],
  "links": ["ka.character-voice-consistency", "ka.character-arc", "ka.creative-pluralism"],
  "source_status": "synthesized"
}
---
# IP 角色语气延续

做 IP 延续时，最常见的误判，是把“熟悉感”理解成“像”。于是文本会拼命复刻几个观众记得的句式、口头禅、态度标签，看起来像在尊重原作，实际上却把角色写扁了。

真正的 continuity 通常发生在更底层。观众认得一个角色，不只是因为他会怎么说，更因为他会怎么判断、怎么误判、怎么回避、怎么自保、怎么在关系里暴露自己的价值排序。只要这些东西还在，语言细部可以变；如果这些东西丢了，就算句型再像，也只是 cosplay。

所以 `IP continuity` 最实用的写法，不是让 Agent 死记台词，而是给它一份“声纹锚点 + 可变区间 + 漂移警报”的说明。这样既能守住角色，也不会把创作锁死成机械模仿。

## TODOs：待回答问题

- [ ] 面对跨年代重启或世界观再设定时，IP continuity 的“不可动核心”到底该怎么界定？
- [ ] 对品牌吉祥物、虚拟偶像、主播人格这类非传统剧情 IP，是否需要单独的 continuity 模型？
- [ ] 当原 IP 本身存在多版本演绎差异时，仓库应如何处理“多个 canon 声音”共存的情况？
- [ ] 角色成长、创伤事件、身份反转等重大剧情变化，在哪个阈值上可以合法改变声纹？
- [ ] 对粉丝高度敏感的 IP，是否需要把 continuity 风险进一步拆成“轻微漂移 / 核心崩坏 / 故意重构”三个等级？
- [ ] Agent 在缺乏完整 canon 材料时，最小 continuity bundle 应包含哪些信息才足够安全？
