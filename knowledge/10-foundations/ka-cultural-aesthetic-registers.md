---
{
  "id": "ka.cultural-aesthetic-registers",
  "type": "knowledge_atom",
  "title": "文化美学语汇锚点",
  "kind": "heuristic",
  "summary": "跨语种视觉词汇包里最有价值的不是生硬的国别标签，而是能稳定牵引情绪、时间感、空间质地与人物关系的文化美学锚点。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "scene", "dialogue", "adaptation"],
  "problem": "Agent 在借用日语、韩语、俄语、西语、中文视觉词时，容易把文化概念写成空洞标签或旅游宣传腔，导致气质假、判断浅。",
  "decision_rules": [
    "只保留那些会改变镜头、节奏、质感或人物关系的文化词，不要收集猎奇标签。",
    "把文化美学词作为约束镜头选择和情绪密度的锚点，而不是替代戏剧动作本身。",
    "一旦一个文化词无法落到具体的画面、动作、时间感或留白策略，它就不该进入当前包。"
  ],
  "anti_patterns": [
    "把文化概念当作风格贴纸",
    "只会列名词，不会说明它怎么改变镜头和文本",
    "把复杂文化语义直接扁平成一种单一情绪"
  ],
  "prompt_primitives": [
    "这次真正需要的文化锚点，是时间感、留白感、悲怆感、热烈感，还是都市流行感",
    "这个词会改变什么：镜头节奏、构图倾向、动作密度、声音处理，还是表演方式",
    "如果不用这个词，当前 brief 会失去哪一层真实表达"
  ],
  "evaluation_checks": [
    "文化词是否改变了可执行的镜头与表达决策",
    "是否避免了地域刻板化与廉价 exoticization",
    "是否把文化美学和场景问题真正扣在了一起"
  ],
  "links": ["ka.multilingual-visual-vocabulary", "ka.creative-pluralism", "ka.false-universal-warning", "ka.register-adaptation"],
  "source_status": "derived"
}
---
# 文化美学语汇锚点

多语种视觉包真正危险的地方，不是“词不够多”，而是文化词一多，Agent 很容易开始演风格。

像 `侘寂`、`物哀`、`韩式的 han / jeong`、`俄语里的 toska`、`realismo mágico`、`duende` 这种词，如果只是被当成漂亮标签贴在 prompt 上，最后往往什么都没控制住。它们真正有用的时候，是能让镜头、时间感、色调、动作密度、留白策略和人物关系一起发生偏转。

所以这层知识不是在教“怎么异国风”，而是在教：哪些文化概念会改变真实的视听决策。一个词如果不能说明它如何改变构图、节奏、灯光、表演或气氛，就不该被留在高价值包里。

对编剧 Agent 来说，这层尤其重要，因为它可以避免把“剧本阶段的情绪判断”和“视频生成阶段的美学判断”混成同一件事。文化美学词应该帮助它更准确地桥接，不应该帮助它更花哨地乱写。

## TODOs：待回答问题

- [ ] 哪些文化美学词适合作为 brief 入口，哪些更适合作为后期细化层？
- [ ] 当用户只会给出一个模糊文化词，例如“日式”“韩式”“俄式”，仓库应如何把它拆成更具体的可执行维度？
- [ ] 商业品牌内容里，使用文化美学锚点时应如何避免把品牌策略误写成文化 cosplay？
- [ ] 这层是否需要加入“高误用风险词”列表，提醒哪些概念最容易被写成标签化空话？
- [ ] 如果不同语言对同一视觉气质的切分方式不同，visual_language_pack 应如何处理这些不对齐？

