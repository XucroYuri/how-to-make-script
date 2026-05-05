---
{
  "id": "ka.team-mode-recipes",
  "type": "knowledge_atom",
  "title": "团队协作模式图谱",
  "kind": "pattern",
  "summary": "不同媒介需要不同的团队协作拓扑——电影是受控串行开发，剧集是showrunner驱动的持续分工，动画是故事与视觉的双轨并行，品牌内容需要创意/品牌/分发三线协作，互动叙事需要叙事/系统/测试三角咬合。",
  "mediums": [
    "feature_film",
    "episodic",
    "short_drama",
    "animation",
    "commercial",
    "branded_film",
    "shortform_video",
    "game_narrative",
    "branching_interactive"
  ],
  "stages": [
    "ideation",
    "premise",
    "character",
    "structure",
    "outline",
    "scene",
    "dialogue",
    "rewrite",
    "adaptation"
  ],
  "problem": "不同媒介使用同一套团队协作模式，导致分工失配、反馈错位和产出崩坏。",
  "decision_rules": [
    "Feature模式应先锁概念/rights/mandate，再进入draft与rewrite lanes。",
    "Showrunner负责season engine、voice ceiling、production reality和最终收束。",
    "动画模式应将visual development和story iteration作为主循环的一部分，而非后置附件。",
    "品牌模式至少需并行处理creative lane、brand lane、distribution lane。",
    "Interactive模式至少并行narrative lane、systems/state lane、test/QA lane。",
    "当branch explosion风险升高时，应优先压缩topology而非继续堆内容。"
  ],
  "anti_patterns": [
    "像room一样无限发散但无人负责收束",
    "没有showrunner synthesis的平行碎片化输出",
    "故事和视觉完全串行分离",
    "品牌植入太晚，最后只好强行补CTA",
    "所有选择只改口气不改后果",
    "状态模型后置，导致later branches无法闭环"
  ],
  "prompt_primitives": [
    "当前轮次最需要锁定的是概念、结构、人物还是production note",
    "哪些问题可以分lane，哪些问题必须回到room共识",
    "当前问题更像narrative promise、state logic，还是QA visibility",
    "哪些lane需要以可视化片段而非文字摘要交接"
  ],
  "evaluation_checks": [
    "团队模式是否保留了强收束角色",
    "跨lane协作是否有清晰的拆分和收束节奏",
    "高风险决策是否留给了合适的review gate",
    "团队模式是否有机制防止scope explosion"
  ],
  "links": [
    "ka.team-topology-selection",
    "ka.commissioning-fit",
    "ka.boundary-first-guidance",
    "ka.audience-need-state",
    "ka.conflict-pressure",
    "ka.scene-function",
    "ka.register-adaptation",
    "ka.medium-branching-interactive",
    "ka.scenario-factorization"
  ],
  "source_status": "curated"
}
---
# 团队协作模式图谱

不同媒介对"谁来想、谁来写、谁来做决定"的需求差异极大。把这套需求压进同一套团队模式里，要么过度并行导致没人收束，要么过度串行导致反馈太晚——无论哪种，产出都会在分工、反馈和落地之间崩坏。以下五种模式分别对应五种媒介族群的团队拓扑，核心问题是：谁有权限定义每一轮到底要改什么，以及哪些决策必须在哪个lane里解决。

## 电影开发小组

电影开发通常不是常态化 writers' room。它更常见的是一个相对窄的责任链：编剧、制片、导演、公司开发或 exec，在不同阶段以不同密度介入。它的重点不在于"多少人一起想"，而在于"谁有权定义这一轮到底要改什么"。

因此 feature 的团队模式应该优先强调：
- 清晰的开发 mandate；
- 有限但高价值的 specialist lane；
- 强收束的 synthesis 角色；
- 阶段性人工 gate。

如果把它做成无限并行 brainstorm，很容易看起来热闹，实则没有任何人对一版可落地的 draft 负责。

## 剧集编剧室

writers' room 最容易被浪漫化成"大家一起想点子"，但专业房间真正稀缺的是节奏控制。showrunner 不只是最有经验的编剧，而是决定哪些问题要 room 里集体解决，哪些问题可以分给单个 writer-producer 或 lane 去消化，再在什么节点拉回统一世界观、统一 tone、统一 production reality。

Agent 版本的 `showrunner_room` 也应该保留这个逻辑。它不该是所有 specialist 平权并行到最后，而应是：
- showrunner_orchestrator 锁定目标和 ceiling；
- 并行 lanes 解决不同层级的问题；
- 固定 cadence 回到统一收束；
- 高风险问题进入 human review。

## 动画 Story Trust

动画开发常常不像 live-action 那样先把纸面剧本写稳再逐层交给下游。它更像一个反复试映和反复可视化的 story trust 循环：故事、美术、导演、后续生产约束持续互相拉扯，最后慢慢收成一版真正能成立的影片或系列。

这意味着 Agent 团队模式也不能只做"写字分工"。动画模式需要更强的：
- director/story lead 收束；
- text-to-visual 的交接意识；
- story lane 与 visual lane 的双轨并行；
- 提前暴露 production feasibility 的 review gate。

## 品牌内容工作室

品牌内容的困难不在于"怎么写个短片"，而在于同时服务多个系统：品牌人格、平台分发、观众注意力、导演表达、活动节点、后续 campaign 延展。一个只懂叙事的人可能写得很美，但不落地；一个只懂转化的人则容易把文本写成信息噪音。

因此 `brand_content_studio` 模式应天然是 cross-functional 的。它至少需要：
- creative lane 去守故事和生活纹理；
- brand lane 去守人格和禁行区；
- distribution lane 去守平台与传播逻辑；
- 最后由 creative director / strategist-like 角色收束。

## 互动分支实验室

互动叙事不是多写几条支线，而是让故事、系统、状态和测试互相咬合。只要这四件事分开太久，最后一定会回到"文本像剧本、交互像补丁"的老问题。

所以 `interactive_branch_lab` 模式的关键不只是 narrative designer，而是 narrative、systems、QA 的三角关系。一个好的互动团队模式，应该让分支设计在一开始就带着状态逻辑和测试可视性推进，而不是等写完以后才问"这条路能不能玩"。
