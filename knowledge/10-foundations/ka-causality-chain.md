---
{
  "id": "ka.causality-chain",
  "type": "knowledge_atom",
  "title": "因果链",
  "kind": "principle",
  "summary": "强叙事依赖因果推进，而不是一连串彼此无关的漂亮事件。",
  "mediums": [
    "feature_film",
    "episodic",
    "short_drama",
    "animation",
    "game_narrative",
    "branching_interactive"
  ],
  "stages": [
    "premise",
    "structure",
    "outline",
    "character",
    "scene",
    "dialogue",
    "rewrite",
    "adaptation"
  ],
  "problem": "大纲里每个点都单独成立，但连起来像拼盘，没有不可替代的顺序。",
  "decision_rules": [
    "让每个关键事件都由前一个选择或失败触发。",
    "优先写'因此'与'但是'，少写'然后'。",
    "如果拿掉一个节点不影响后续，多半该节点尚未嵌入因果链。"
  ],
  "anti_patterns": [
    "场景顺序可随意调换",
    "关键转折只靠信息突然出现",
    "高潮与前文没有足够因果蓄力"
  ],
  "prompt_primitives": [
    "上一场的结果怎样逼出了这一场",
    "这次行动失败后带来了什么新局面",
    "如果删除这个节点，哪些后果会消失"
  ],
  "evaluation_checks": [
    "关键节点之间能否用因果句连接",
    "高潮是否由一连串错误或选择自然累积",
    "角色是否在因果链中承担责任"
  ],
  "links": [
    "ka.story-goal",
    "ka.rewrite-diagnosis"
  ],
  "source_status": "synthesized"
}
---
# 因果链

因果链负责把“有内容”变成“必须按这个顺序发生”。结构松散的大纲通常不是缺桥段，而是缺因果粘合力。

专业一点说，因果链决定了故事的不可替代性。观众之所以愿意一路看下去，不是因为桥段很多，而是因为每一步都由前一步逼出来，角色越走越回不了头。

一个很好用的诊断办法是把大纲里的“然后”改写成“因此”或“但是”。如果改不动，说明这个节点大概率只是内容填充，还没有真正嵌入叙事机制。
