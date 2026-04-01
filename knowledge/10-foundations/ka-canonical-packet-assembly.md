---
{
  "id": "ka.canonical-packet-assembly",
  "type": "knowledge_atom",
  "title": "Canonical Packet 组装",
  "kind": "workflow_rule",
  "summary": "一次具体写作、审查或导出动作，不应直接读取一大坨上下文，而应先把当前有效真源、规则层、状态层与手工约束编译成可检查的 canonical packet。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "如果 packet 组装是隐式的，系统会不知道‘这次到底读了什么’，也无法稳定复查为什么某次生成或审查结果会偏掉。",
  "decision_rules": [
    "任何高价值动作都应先生成可检查的 canonical packet，再进入写作或 review。",
    "packet 至少应包括 route anchor、当前有效真源、局部状态、规则层、显式约束与最近 handoff。",
    "packet 应区分 human-readable brief 与 machine-facing state，不把两者揉成一段大 prompt。"
  ],
  "anti_patterns": [
    "当前章节 / 当前场景写作时默认把所有相关资料全部塞给模型",
    "一次失败后无法回答‘这次到底加载了什么’",
    "packet 没有冻结版本，导致 review 无法重现输入条件"
  ],
  "prompt_primitives": [
    "这次动作的 canonical packet 应该由哪些层构成",
    "其中哪些内容是给人看的，哪些内容是给系统执行或调试的",
    "如果要导出 packet，最值得查看的字段是什么"
  ],
  "evaluation_checks": [
    "packet 是否足够解释本次动作读取了什么",
    "packet 是否避免了无边界上下文拼接",
    "packet 是否能支持 review、调试或追溯"
  ],
  "links": ["ka.source-of-truth-runtime-split", "ka.subagent-context-budgeting", "ka.handoff-packet-discipline"],
  "source_status": "synthesized"
}
---
# Canonical Packet 组装

当前仓库已经很重视 bounded loading，但外部项目给出的一个更进一步的提醒是：仅仅说“少加载一些”还不够，还应该知道“最终到底加载成了什么”。

这就是 canonical packet 的价值。它不是把上下文压得更小而已，而是把这次任务真正会看到的输入显式化、结构化、可检查化。这样无论是写作、改稿、审查，还是导出给下游视频 / 制片 / 编辑团队，都有机会追溯：这次动作是在什么真源、什么规则层、什么局部状态下做出的。

如果没有 packet，很多漂移会变成“感觉不对”；有了 packet，漂移至少可以被定位。

## TODOs：待回答问题

- [ ] 针对不同 output，canonical packet 的必选字段是否应不同？
- [ ] packet 是否应该默认落盘，还是只在高价值节点和调试模式下导出？
- [ ] 当 packet 太大时，应该先删哪一层，保哪一层？
- [ ] canonical packet 是否应直接进入未来 runtime planner 的标准契约？
