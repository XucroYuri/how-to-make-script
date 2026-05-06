---
{
  "id": "wp.dialogue-polish",
  "type": "workflow_protocol",
  "title": "对白打磨协议",
  "goal": "提高对白的角色声音、潜台词、信息效率和戏剧张力。",
  "input_contract": [
    "scene_draft",
    "dialogue excerpt"
  ],
  "output_contract": [
    "dialogue_polish"
  ],
  "preconditions": [
    "已知说话双方的目标和关系"
  ],
  "steps": [
    "识别每位角色的表层说辞与真实目标。",
    "压缩显性解释，保留必要信息。",
    "区分角色声音、策略和权力位置。",
    "输出 revised dialogue，并附带关键调整说明。"
  ],
  "fallbacks": [
    "若场景冲突本身无力，先退回 scene 级处理。",
    "若人物声音模糊，补角色执念与社会位置。"
  ],
  "stop_conditions": [
    "对白不再只是解释",
    "角色声音可区分",
    "信息揭示服务冲突"
  ],
  "rubrics": [
    "rb.dialogue"
  ],
  "linked_atoms": [
    "ka.conflict-pressure",
    "ka.cross-protocol-referral-edges",
    "ka.dialogue-subtext",
    "ka.exposition-control"
  ],
  "budget_class": "S",
  "mandatory_atom_count": 4,
  "expansion_allowed": false
}
---
# 对白打磨协议

对白打磨不是句子美容，而是重新安排策略、遮蔽和权力。

专业对白修改很少只是”换几句更好听的话”。真正的工作通常包括三件事：让人物说话更像他自己、让表层话语和真实目的分开、让信息暴露服从当前冲突而不是作者的解释欲。

如果一句对白改了很多遍还是像说明书，问题通常不在字句，而在人物目标、权力关系或场景冲突本身还不够明确。
