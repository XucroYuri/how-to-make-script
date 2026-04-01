---
{
  "id": "ka.subagent-context-budgeting",
  "type": "knowledge_atom",
  "title": "Subagent 上下文预算",
  "kind": "heuristic",
  "summary": "subagent 的价值来自角色专注和上下文克制，而不是共享整个知识仓。每条 lane 都应该有自己的 context budget。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "一旦 subagent 都拿到全量上下文，系统就会失去专业分工带来的清晰度，最终变成多个大而全但同质化的代理互相转述。",
  "decision_rules": [
    "每个 subagent 都必须基于当前 mandate 领取最小 bundle，而不是继承主控上下文。",
    "persona lens 的加载预算必须小于功能型 subagent 的加载预算。",
    "需要跨 lane 共识的内容，应进入 handoff packet 或 truth packet，而不是通过隐式全文共享。"
  ],
  "anti_patterns": [
    "所有 lane 都读完整 router、scenario atlas、reference pack 和全部历史讨论",
    "用‘信息充分’之名掩盖上下文污染",
    "让 review subagent 读比 implementer 还多的无关材料"
  ],
  "prompt_primitives": [
    "这个 subagent 为了完成当前 mandate 最少需要哪些协议、rubric、atom 和事实",
    "哪些内容应该进入 handoff packet，哪些不应该继续带下去",
    "如果要加一层比较或反例，哪一层最值得加，哪一层不值得"
  ],
  "evaluation_checks": [
    "lane 是否遵守了 context budget",
    "共享信息是否通过 packet 明示，而不是隐式扩散",
    "扩容是否真的改变了判断，而不是制造噪音"
  ],
  "links": ["ka.bounded-context-loading", "ka.context-corrosion-signals", "ka.reference-expansion-balance", "ka.handoff-packet-discipline"],
  "source_status": "synthesized"
}
---
# Subagent 上下文预算

很多多智能体系统失败，不是因为专家不够，而是因为所有专家最后都变成了“同一个大模型读了更多东西”。这会让 lane 看上去很多，实际上每个 lane 都在重复理解同一批上下文。

真正的 subagent 设计，应该像真实团队分工一样：谁只拿 premise slate，谁只拿当前 scene packet，谁只拿 audience fit note，谁只拿 continuity anchors。不是信息越多越专业，而是信息越贴 mandate 越专业。

在这个仓库里，context budget 不只是性能问题，也是创作质量问题。角色越清晰，加载越克制，subagent 才越像真实的专业角色，而不是另一个隐形 root skill。

## TODOs：待回答问题

- [ ] 是否需要把不同 subagent 的默认 loading tier 固化为 machine-readable policy？
- [ ] 哪些跨 lane 的共享信息最容易误伤创造力，最应该被压缩进 packet？
- [ ] 如果某个 subagent 连续两轮都要求扩容，系统应默认它不适配当前 lane 吗？
- [ ] human gate 节点是否也应该有明确的 context budget，而不是默认看全量？
- [ ] 如何在保留反例和 dissent 的同时，避免 compare_pack 被滥用成全局扩容借口？
