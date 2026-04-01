---
{
  "id": "ka.commissioning-fit",
  "type": "knowledge_atom",
  "title": "委制适配",
  "kind": "principle",
  "summary": "一个概念是否值得推进，不只取决于它好不好看，也取决于它是否匹配具体的立项、委制、分发和交付逻辑。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "outline", "rewrite", "adaptation"],
  "problem": "剧本想法本身有趣，但不知道在真实平台、品牌、片方、工作室或游戏团队语境里该如何被开发和交付。",
  "decision_rules": [
    "先明确是谁在委制、为什么委制、交付什么，再决定创作优先级。",
    "把创作目标和商业目标拆开写，避免把所有诉求都塞进故事本体。",
    "当交付场景不同，允许同一概念有 pitch 版、development 版和 production 版三种不同表达深度。"
  ],
  "anti_patterns": [
    "把所有项目都按作者长片逻辑开发",
    "平台语境和发行窗口不明却先写满结构",
    "品牌或业务目标直到最后才硬贴进文本"
  ],
  "prompt_primitives": [
    "这个项目首先要满足谁的决策需要",
    "什么样的交付物最能推动下一步立项或生产",
    "哪些创作选择会与预算、平台、发行或品牌目标冲突"
  ],
  "evaluation_checks": [
    "是否明确了委制主体与首要目标",
    "输出物是否匹配当前开发阶段",
    "创作建议是否考虑了平台和交付现实"
  ],
  "links": ["ka.platform-attention-economy", "ka.medium-commercial", "ka.medium-branded-film", "ka.medium-episode", "ka.medium-feature-film"],
  "source_status": "derived"
}
---
# 委制适配

很多剧本不是死在“写得不好”，而是死在“开发方式不对”。委制适配讲的就是这个问题：同样一个想法，给电影公司、流媒体、品牌客户、短剧团队、游戏叙事团队，开发策略和交付形态并不一样。

如果不知道谁在为这个项目买单、承担风险、决定去留，创作者就容易把所有判断都压回到文本内部。结果是文字看起来有创作冲动，但既不利于提案，也不利于进入下一轮开发。

委制适配不是让内容跪着写，而是让创作知道自己在哪个工业局面里说话。你越清楚当前阶段要解决的是“立项信心”“平台匹配”“品牌诉求”“发行窗口”还是“生产可执行性”，就越能决定现在该写 premise、写 brief、写 outline，还是先停下来改路。

## TODOs：待回答问题

- [ ] 委制适配是否应该按平台型项目、品牌型项目、作者驱动项目、IP 型项目进一步拆包？
- [ ] 哪些创作建议在 pitch 阶段有效，但到了 production 阶段会变成噪音？
- [ ] 对独立创作项目来说，没有明确委制方时，系统应如何构造一个临时的开发坐标？
- [ ] 当项目天然跨越多个委制方，例如品牌联动剧或平台联名互动项目，适配逻辑应如何表达？
- [ ] 如何在保证创作表达的前提下，把品牌或平台目标纳入项目，而不是让它们变成后贴标签？
- [ ] `development_brief` 与普通 outline 的边界应该如何在使用说明里继续拉开？
