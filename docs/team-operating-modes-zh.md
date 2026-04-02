# 团队工作模式

这份文档不是想把“顶级团队怎么工作”总结成唯一答案，而是把现实中几种明显不同的工作形状提炼出来，作为仓库可调用的 team mode。

它的目标很务实：当用户要的不是单次文本，而是“这类项目应该怎么组织一支人类 + Agent 团队”，仓库就不能只给一些抽象管理口号，而要给出可运行的协作结构。

## 先问四件事，再选模式

1. 这个项目到底更像作者中心、showrunner 中心、品牌战役中心、系统设计中心，还是 continuity 中心？
2. 当前最该集中锁定的是什么，最适合并行跑的又是什么？
3. 在进入成稿前，哪些中间成果绝不能跳过？
4. 哪些判断必须保留给人类，而不能完全交给 Agent？

## 模式 1：Showrunner Room

适合：
- 长剧集、系列短剧、连续性很强的 episodic 项目；
- 需要 season engine、episode break、角色线并行推进的项目。

核心形态：
- 有一个明确的最终拍板者；
- 有 room captain 维护当前 truth 上下文包；
- 可以分 season engine、episode break、character threads、notes intake 几条 lane；
- 但 season lock、episode break lock、production rewrite 这几个 gate 必须非常明确。

为什么要有这个模式：
- WGA 的 development room / regular writers' room 规则说明，现实行业里这本来就是两种不同压力层级；
- 高水平 showrunner 体系不是“大家一起聊”，而是“大家一起推进，但最终有人负责收口”。

来源：
- [WGA 2023 MBA summary](https://www.wga.org/contracts/contracts/mba/summary-of-the-2023-wga-mba)
- [WGA staff size guide](https://www.wga.org/members/employment-resources/writers-deal-hub/staff-size-guide)
- [Shondaland / Bridgerton showrunner 访谈](https://www.shondaland.com/shondaland-series/shondaland-bridgerton-behind-the-scenes/a60702896/bridgerton-showrunner-jess-brownell/)

## 模式 2：Animation Story Trust

适合：
- 动画长片；
- 依赖 sequence 级别迭代和同业 peer review 的项目；
- 视觉叙事和世界研究深度耦合的开发流程。

核心形态：
- 核心团队不一定大，但 peer review 很强；
- 研究、reel、sequence note、世界观校准互相联动；
- review 不是等成稿后才做，而是跟着 sequence 和 story 上下文包一起走。

为什么要有这个模式：
- Disney 的 Story Trust 文化本质上就是“高密度反馈 + 世界研究 + 反复 sequence 级校正”；
- 这种模式对动画、IP 世界扩展和高视觉依赖项目特别有效。

来源：
- [Disneytoon 访谈：Story Trust、research、peer review](https://thewaltdisneycompany.com/news/disneytoon-executive-on-the-animation-studio-behind-the-pirate-fairy-and-planes-fire-rescue/)

## 模式 3：Feature Development Pod

适合：
- 原创电影；
- prestige / indie feature；
- 需要集中作者性、但又不能完全闭门造车的小团队开发。

核心形态：
- 团队更小，更像 writer-director-producer pod；
- 重点不是 room 规模，而是 artifact ladder 和外部 checkpoint；
- 必须明确保留 dissent，不然小团队会过快达成”假一致”。

为什么要有这个模式：
- 电影开发常常不适合大 room，但也不能没有开发节律和外部反馈；
- 对 Agent 来说，这种模式意味着更少 lane、更严格的 gate、更清晰的 owner。

来源：
- [WGA 2023 MBA summary](https://www.wga.org/contracts/contracts/mba/summary-of-the-2023-wga-mba)
- [OpenAI Agents SDK: agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)

说明：
- 这是一个综合型推导模式，不是某一家公司的照搬。

## 模式 4：Campaign Strike Team

适合：
- 品牌片；
- 广告 campaign；
- 高频版本测试、跨平台适配、短周期商业脚本。

核心形态：
- 必须先锁 message spine；
- 然后才让 variants、platform cuts、performance review 并行；
- brand fit gate 和 message singularity gate 比“多出几个版本”更重要。

为什么要有这个模式：
- W+K 的 Three “Pony” 案例体现了“一个核心表达，跨 TV / digital / share mechanic 扩张”的工作方式；
- Google / Taxfix 的案例则说明现代 creative production 已经越来越依赖快速变体、测试、再收敛，但战略判断和品牌控制仍然在人手里。

来源：
- [Wieden+Kennedy: Three “Pony”](https://www.wk.com/work/three-pony/)
- [Google / Taxfix：AI-first video production](https://business.google.com/en-all/think/search-and-video/taxfix-veo-youtube-ai-first/)

## 模式 5：Interactive Narrative Cell

适合：
- 游戏叙事；
- 分支互动剧情；
- 任务、状态、对白和实现约束紧耦合的项目。

核心形态：
- narrative 不和 systems 分家；
- branch logic、quest/state、VO/dialogue、implementation notes 同时推进但要强同步；
- playability gate 和 story gate 同等重要。

为什么要有这个模式：
- Ubisoft 对 narrative design 的定义很明确：它本来就是跨 game design、audio、production、quest design 的接口工作；
- Story Creator Mode 也说明互动叙事不是“先写完再实现”，而是工具、内容中心和游戏内执行一起构成流程。

来源：
- [Ubisoft: What is Narrative Design?](https://news.ubisoft.com/en-gb/article/7m412GLSbfkaT0YheRYLVG/what-is-narrative-design)
- [Ubisoft: Story Creator Mode](https://news.ubisoft.com/en-us/article/1yMR91cFZCtrN7McYV4oeD/how-assassins-creed-odysseys-story-creator-mode-actually-works)

## 模式 6：Franchise Continuity Board

适合：
- 改编；
- 续作；
- 强 IP / 强 persona 项目；
- 品牌人格或 lore 风险极高的项目。

核心形态：
- continuity keeper 必须明确存在；
- canon anchor、voice guide、risk register 先于大规模 drafting；
- 创新不是不能做，但必须明确写出”改了哪个关键设定，为什么能改”。

为什么要有这个模式：
- 在系列世界里，continuity 不是返工阶段顺手查查，而是前置的决策机制。

来源：
- [Disneytoon 访谈：扩展既有世界与 Story Trust](https://thewaltdisneycompany.com/news/disneytoon-executive-on-the-animation-studio-behind-the-pirate-fairy-and-planes-fire-rescue/)

## 对 Agent 机制的直接启发

这套仓库不应该把这些模式写成 6 套死 prompt，而应该吸收两类多智能体模式：

- `manager / specialist`：适合 room captain 或 showrunner 持有最终回答、调用 specialist 做窄子任务；
- `handoff`：适合先 triage，再把下一段工作直接交给当前最合适的 specialist。

同时还要吸收两条很关键的工程教训：
- 并行 specialist 只有在 handoff 很窄、merge owner 很清楚时才真的会加速；
- 工具和上下文最好按任务加载，而不是所有 agent 永久背着全部能力。

来源：
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/multi_agent/)
- [oh-my-openagent README](https://github.com/code-yeongyu/oh-my-openagent)

## 最后一句

team mode 是参考路径，不是唯一标准。真正应该输出的是：
- 一条主模式；
- 一条在高不确定度下的备选模式；
- 一条明确写出的“哪些判断必须留给人类”。
