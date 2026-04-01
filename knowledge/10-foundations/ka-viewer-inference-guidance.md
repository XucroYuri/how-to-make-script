---
{
  "id": "ka.viewer-inference-guidance",
  "type": "knowledge_atom",
  "title": "观众推理引导",
  "kind": "research",
  "summary": "观众不会被动接收剧本信息，而是在不断推理角色目标、因果关系、情绪状态与故事契约，写作必须管理这种推理负荷。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "structure", "outline", "scene", "dialogue", "rewrite"],
  "problem": "文本只顾隐藏信息、制造气氛或堆事件，却没有照顾观众如何理解、记住和情绪跟进，导致作品看似复杂，实则理解链条断裂。",
  "decision_rules": [
    "把角色目标变化、地点转换、关系翻转和关键物件状态变化当作观众理解边界来写，而不是只当作剧情事实。",
    "允许悬念、延迟揭示和非线性存在，但必须保留后续可恢复的因果拼接点。",
    "在开头和关键转场处提供足够 framing，让观众知道自己现在进入的是哪种故事契约。"
  ],
  "anti_patterns": [
    "把混乱误当复杂",
    "为了神秘感长期不给理解锚点",
    "情绪和因果都依赖观众自行脑补却没有足够证据"
  ],
  "prompt_primitives": [
    "观众在这一段最先需要搞明白什么",
    "这个转折是信息边界、情绪边界还是因果边界",
    "哪些信息可以延后，哪些信息延后会让理解链断掉"
  ],
  "evaluation_checks": [
    "关键边界点是否真的承担了理解更新功能",
    "因果链是否允许观众在后续完成拼接",
    "情绪状态是否足够可推理而不是只能靠外部解释"
  ],
  "links": ["ka.causality-chain", "ka.exposition-control", "ka.audience-need-state", "ka.opening-job-selection", "ka.scene-function", "ka.pacing-rhythm"],
  "source_status": "curated"
}
---
# 观众推理引导

观众在看剧本对应的成片时，并不是在接收一个已经完全解释好的世界。他们是在边看边猜、边比对、边修正自己的理解模型。

这件事非常重要，因为很多写作失误表面上像“节奏不好”“设定太多”“人物不成立”，底层其实是观众无法顺利完成推理：不知道谁在要什么、不知道眼前的变化意味着什么、不知道该把这一段当成铺垫、误导、反转还是情绪沉淀。

所以真正高水平的写法，不是把所有信息都讲明白，也不是故意把所有信息都藏起来，而是管理“观众此刻应该知道什么、应该猜到什么、可以暂时不知道什么”。

这也是为什么开头、转场、scene ending、payoff 会比表面上看起来更关键。那些位置不是单纯的剧情路标，而是理解和记忆的高杠杆位置。

## TODOs：待回答问题

- [ ] 不同媒介下，观众推理负荷的安全上限应如何调整？
- [ ] 对群像、谜题、强非线性项目，系统是否需要单独的因果可恢复性检查？
- [ ] 情绪误读和因果误读，哪一种在不同类型里代价更高？
- [ ] 观众推理引导是否应该扩展到声音、表演和镜头预期，而不只是文本层？
