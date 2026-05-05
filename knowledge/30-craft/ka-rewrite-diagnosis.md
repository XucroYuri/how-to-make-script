---
{
  "id": "ka.rewrite-diagnosis",
  "type": "knowledge_atom",
  "title": "改稿诊断",
  "kind": "workflow_fragment",
  "summary": "改稿优先识别病灶层级：概念、结构、场景、对白，避免在错误层级上勤奋。",
  "mediums": [
    "feature_film",
    "episodic",
    "short_drama",
    "animation",
    "commercial",
    "branded_film",
    "game_narrative",
    "branching_interactive"
  ],
  "stages": [
    "rewrite"
  ],
  "problem": "改稿时只改句子和局部桥段，却没有解决真正导致失效的结构病灶。",
  "decision_rules": [
    "先判断问题发生在哪一层，再决定改什么。",
    "概念和结构病不能靠对白修复。",
    "改稿建议必须排序：先高杠杆，后低杠杆。"
  ],
  "anti_patterns": [
    "把所有问题都归因于台词不够好",
    "结构问题用加戏拖过去",
    "没有优先级的改稿清单"
  ],
  "prompt_primitives": [
    "这是概念问题、结构问题、场景问题还是对白问题",
    "如果只能改三件事，哪三件杠杆最大",
    "这处症状的上游原因是什么"
  ],
  "evaluation_checks": [
    "诊断是否分层",
    "建议是否按影响力排序",
    "建议是否对应到可执行修改动作"
  ],
  "links": [
    "ka.causality-chain",
    "ka.scene-function",
    "ka.dialogue-subtext"
  ],
  "source_status": "synthesized"
}
---
# 改稿诊断

低层修补不能替代高层纠偏。先找病灶层级，再决定动刀位置。

这条知识单元最适合拿来做项目中后期返修。一旦故事进入多轮开发，局部字句通常已打磨得不错，但真正拖后腿的，反而是更上游的 premise、结构和场景分配。

一个很重要的专业习惯是：别把”读起来别扭”直接翻译成”台词不好”。它有可能是前一层的冲突不成立，也可能是人物目标不清，甚至可能是整条因果链松了。
