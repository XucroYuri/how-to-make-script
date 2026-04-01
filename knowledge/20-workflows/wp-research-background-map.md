---
{
  "id": "wp.research-background-map",
  "type": "workflow_protocol",
  "title": "研究背景图协议",
  "goal": "针对宽问题、理论支撑请求或 Agent Skill 设计请求，输出一份 research_background_map，明确问题镜头、稳定研究发现、来源簇、可调用知识资产和后续最值得进入的路线。",
  "input_contract": ["broad screenplay question", "research ask", "agent-skill design ask", "constraints", "none"],
  "output_contract": ["research_background_map"],
  "preconditions": [
    "用户明确要的是理论支撑、全景研究、背景信息或多角度梳理，而不是直接写一个剧本产物",
    "至少可以锁定一个宽主题或 research scope"
  ],
  "steps": [
    "先把宽问题拆成若干研究镜头，避免一上来套单一方法。",
    "从 background bundle registry 里选择一个最相关的研究包，而不是直接散读整个仓库。",
    "提炼最稳定的研究发现，区分稳定发现、局部经验、历史条件和开放争议。",
    "列出最相关的来源簇和可调用 atom，说明它们分别回答哪一类问题。",
    "指出如果用户下一步要继续推进，最应该切入哪个更窄的 output route。"
  ],
  "fallbacks": [
    "若用户实际要的是具体剧本产物，返回对应主路由并只附最小 research note。",
    "若用户问题仍然过宽，先锁定一个 research scope，再给背景图，而不是伪装成完整综述。"
  ],
  "stop_conditions": [
    "已经明确研究镜头、稳定发现、来源簇、可调用资产和建议下一步路线",
    "至少说明一个不该被误当成普遍真理的局部规则",
    "没有把研究背景误写成单一方法教条"
  ],
  "rubrics": ["rb.research-background-map"],
  "linked_atoms": ["ka.screenplay-lens-stacking", "ka.viewer-inference-guidance", "ka.script-as-coordination-artifact", "ka.screenwriting-deliberate-practice", "ka.feedback-subjectivity-management", "ka.archive-literacy", "ka.audience-need-state", "ka.commissioning-fit", "ka.screenwriting-history-shift"]
}
---
# 研究背景图协议

这个协议处理的不是“现在就写一版 premise / outline / scene”，而是“先把这个宽问题背后有哪些真正重要的镜头、发现、争议和后续路线梳理清楚”。

它的目标不是做论文综述，也不是做仓库目录导览，而是把研究背景转成一种 Agent 真能调用的结构化背景图。

最典型的使用场景就是：

- 用户问“如何创作剧本”；
- 用户在设计 Agent Skill，需要理论支撑层；
- 用户需要一个 broad research baseline，但不希望被一个方法流派绑架；
- 用户想知道这个仓库在某个宽问题上的背景知识到底怎么组织。

## TODOs：待回答问题

- [ ] `research_background_map` 是否还需要按方法论研究、观众认知研究、行业流程研究拆成二级模板？
- [ ] 对高度专业的用户，这个协议是否需要支持“只要 findings，不要教学解释”的压缩模式？
- [ ] 研究背景图是否需要显式输出“尚未沉淀为 atom 的高价值问题清单”？
- [ ] 什么时候应该把背景图升级成新的 protocol / rubric / skill，而不是继续停留在 research layer？
