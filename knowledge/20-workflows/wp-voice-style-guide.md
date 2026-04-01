---
{
  "id": "wp.voice-style-guide",
  "type": "workflow_protocol",
  "title": "表达风格校准协议",
  "goal": "在正式写 scene、dialogue、commercial 或 adaptation 产物前，先产出一份 voice_style_guide，明确角色 / IP / 品牌 / 交互角色的表达锚点、可变区间和漂移警报。",
  "input_contract": [
    "character brief",
    "scene goal",
    "dialogue excerpt",
    "ip note",
    "brand persona",
    "medium and stage"
  ],
  "output_contract": [
    "voice_style_guide"
  ],
  "preconditions": [
    "已知目标媒介",
    "至少知道角色、IP、品牌人格或目标说话主体中的一个",
    "知道当前表达服务的场景或任务压力"
  ],
  "steps": [
    "识别当前是原创角色校准、IP 延续、品牌语体校准，还是互动角色去功能化。",
    "定义 voice anchors：世界观倾向、关系策略、羞耻点、表达节奏、常见回避方式。",
    "定义 lived pressure：角色如何把身体压力、社会风险和时间成本带进语言。",
    "定义 register envelope：允许的词汇层级、抽象度、修辞密度，以及明确禁行区。",
    "若涉及 IP、系列角色或品牌人格，写出 continuity anchors、variability budget 和 drift warnings。",
    "输出 guide：包含该怎么写、不要怎么写、为什么、以及这份 guide 只是一组可生成约束而不是模板。"
  ],
  "fallbacks": [
    "若信息不足以判断声音来源，优先补角色目标、关系位置和当前压力，而不是继续堆风格形容词。",
    "若问题本质是多语种镜头语言、视觉 handoff 或文化美学词汇选择，而不是角色 / IP / 品牌声音，转到 visual-language。",
    "若用户真正要的是成稿而不是指南，切回 scene-writing、dialogue-subtext、commercial-script 或 genre-adaptation，并把 guide 作为附加表达层。",
    "若问题本质是 audience fit 或 commissioning fit，而不是表达校准，转到 audience-insight 或 development-strategy。"
  ],
  "stop_conditions": [
    "guide 已能解释为什么这个表达像该角色 / 该 IP / 该品牌",
    "guide 已写清可变区间和失真红线",
    "guide 仍然保留创意空间，而不是把文本锁死成固定腔调"
  ],
  "rubrics": [
    "rb.voice-style-guide"
  ],
  "linked_atoms": [
    "ka.character-voice-consistency",
    "ka.ip-voice-continuity",
    "ka.register-adaptation",
    "ka.embodied-text-pressure",
    "ka.dialogue-subtext"
  ],
  "budget_class": "M",
  "mandatory_atom_count": 5,
  "expansion_allowed": true
}
---
# 表达风格校准协议

很多文本并不是不会写剧情，而是还没把“谁在说、怎么说、说到哪一步会失真”先拆清楚，于是成稿阶段只能一边写一边碰运气。

`voice_style_guide` 的作用，就是把这层隐性判断提前显式化。它不是让 Agent 背模板，更不是让每个角色都有一套僵硬腔调，而是把“表达锚点”和“允许变化的范围”先界定出来。这样后面的 scene、dialogue、commercial 或 adaptation 才不容易写着写着滑回作者腔、NPC 腔、假高级腔或 off-IP 腔。

这份协议的价值，恰恰在于它既约束漂移，也保护变化。因为真实的人和真实的 IP 都不会每句话一样，但他们会在变化里保持自己。

## TODOs：待回答问题

- [ ] `voice_style_guide` 是否应按 narrative / commercial / interactive 分出更细的子模版？
- [ ] 当项目同时涉及角色 voice、品牌 voice、平台语体三层冲突时，guide 应优先保哪一层？
- [ ] 这份协议是否需要显式产出“可接受变体区间”示例，以防 Agent 把 guide 理解得过窄？
- [ ] 如果只有少量现成对白样本，没有完整人物设定，最小 guide 应该怎么安全生成？
- [ ] 对多角色场景，是否需要扩展成 pairwise voice contrast，而不只是一人一份 guide？
- [ ] 什么时候 `voice_style_guide` 应被视为临时支架，写完场景后可以丢弃，什么时候它应进入长期 IP bible？
