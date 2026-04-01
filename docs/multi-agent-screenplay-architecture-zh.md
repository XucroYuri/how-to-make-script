# 多智能体剧本架构

当前仓库现在正式承认一件事：很多剧本问题不是“一个更聪明的 Agent”就能优雅解决的，而是需要像现实世界里的高水平团队一样，把不同判断层、不同产物层、不同审查层拆开协作。

这并不意味着每个请求都要上多智能体。它意味着仓库终于有了一层正式机制，来回答这些问题：
- 什么时候应该是一个总控加多个 specialist；
- 什么时候该平行发散，什么时候必须串行交接；
- 交接时到底传什么，不传什么；
- 哪些地方必须有人来做最后判断。

## 核心立场

仓库不走“一个万能总编剧 Agent”路线。

无论是公开的多智能体框架，还是现实中的影视开发流程，真正有效的模式都更像下面这样：
- 有一个总控负责路线和收束；
- specialist 只处理自己最该处理的问题；
- 交接用 bounded handoff，而不是上下文倾倒；
- 人只在高成本、高争议、高风险节点介入。

## 新增的协作层

这层加在普通 route 之上：

1. 先正常做 root route selection。
2. 再判断当前任务是否需要 `team mode`。
3. 若需要，就选择最合适的协作模式。
4. 再决定这次具体要哪些 `expert_subagent_cast` 进场。
5. 再决定这些 subagent 该按什么 `subagent_dispatch_plan` 运行。
6. 给不同角色分配最小 bundle。
7. 用 handoff packet 串起角色。
8. 用 review board 和 human gate 把高风险决策收住。

## 默认五种模式

### `feature_dev_pod`
- 适合：电影开发、改编重写、pitch 到 outline 的推进。
- 重点：mandate 清晰、强收束、阶段性评审。

### `showrunner_room`
- 适合：剧集 season engine、episode break、writers' room 型开发。
- 重点：允许并行拆活，但 showrunner 必须保收束权。

### `animation_story_trust`
- 适合：动画开发、story 和 visual 双轨迭代。
- 重点：文字判断和可视化判断必须同时推进。

### `brand_content_studio`
- 适合：广告、品牌片、短视频 campaign。
- 重点：creative、brand、distribution 三条线必须并行，但不能互相压死。

### `interactive_branch_lab`
- 适合：互动叙事、游戏剧情、分支结构设计。
- 重点：narrative、state、QA 三角协作，防止假选择和分支爆炸。

### `franchise_continuity_board`
- 适合：已有 IP、世界观连续性高压、角色人格不能轻易漂移的项目。
- 重点：把 canon、voice continuity 和 adaptation approval 提前做成明确关口，而不是后置救火。

## Handoff Packet 纪律

每个 specialist 的交接都不该是一段大作文，而该是一份小而准的交接包。

最小字段：
- `working_hypothesis`
- `loaded_bundle_ids`
- `open_questions`
- `confidence`
- `recommended_next_agent`
- `needs_human_review`

这其实就是 bounded loading 在团队层的延伸。

## Cast 与 Dispatch 不是一回事

很多系统会把“team mode”“角色表”“调度计划”混成一段大答案。

仓库现在把它们拆开：
- `team_workflow_blueprint` 回答“整体像哪种协作模式”；
- `expert_subagent_cast` 回答“这次具体让谁进场”；
- `subagent_dispatch_plan` 回答“这些 subagent 到底怎么跑、怎么 review、怎么 merge、什么时候该缩回去”。

这样做的好处是：不会因为多智能体需求一来，就把所有组织问题都糊成一张图。

## Human-In-The-Loop 放在哪里

不是哪里都放。

应该只放在真正贵、真的容易漂、出事代价高的节点：
- IP / franchise 连续性；
- audience fit 争议；
- brand / commissioning 边界冲突；
- 关键 scope correction；
- 最终交付批准。

## 为什么这层对仓库重要

因为如果没有这层，仓库再多知识也还是会默认一个隐含前提：所有高水平创作都能被一个 route + 一个 protocol 解决。

现实不是这样。
高水平创作更像是一套被精心组织过的协作，而不是一段更长的 prompt。

## 参考来源

- WGA writers' room 与 feature 开发资源：
  [Showrunners’ Guide to 2023 MBA Writers’ Room Provisions](https://www.wga.org/contracts/contracts/mba/showrunners-guide-to-2023-mba-writers-room-provisions)
  [Screenwriters Handbook](https://www.wga.org/members/employment-resources/screenwriters-handbook)
- 动画开发：
  [Disney Animation Story Artist](https://www.disneyanimation.com/team/story-artist/)
  [Pixar - Pete Docter](https://www.pixar.com/docter)
- 品牌内容：
  [Digitas branded content arm](https://www.digitas.com/en-us/pressroom/newfront-founder-digitas-unveils-branded-content-arm)
- 互动叙事：
  [inklewriter](https://www.inklestudios.com/inklewriter/)
  [ChoiceScript automated testing](https://www.choiceofgames.com/make-your-own-games/testing-choicescript-games-automatically/)
- 多智能体框架：
  [OpenAI Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
  [LangGraph Supervisor](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph-supervisor.html)
  [OpenAI Swarm](https://github.com/openai/swarm)
  [CrewAI HITL](https://docs.crewai.com/en/learn/human-in-the-loop)
  [oh-my-openagent](https://github.com/code-yeongyu/oh-my-opencode)
