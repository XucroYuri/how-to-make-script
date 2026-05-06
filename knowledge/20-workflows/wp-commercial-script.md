---
{
  "id": "wp.commercial-script",
  "type": "workflow_protocol",
  "title": "商业脚本协议",
  "goal": "输出以单一核心信息为中心的 commercial script。",
  "input_contract": [
    "product brief",
    "campaign goal",
    "audience insight",
    "platform constraint"
  ],
  "output_contract": [
    "commercial_script",
    "branded_film_script"
  ],
  "preconditions": [
    "已知核心卖点或品牌任务"
  ],
  "steps": [
    "锁定单一核心信息与目标动作。",
    "按平台和时长决定钩子、证明、记忆点、CTA 的排序。",
    "把产品或品牌信息视觉化，而不是只口播化。",
    "输出短版脚本，并用商业 rubric 检查转化逻辑。"
  ],
  "fallbacks": [
    "若卖点太多，强制压缩到主信息与次信息两层。",
    "若平台未给定，默认按短视频环境优先设计开头抓力。"
  ],
  "stop_conditions": [
    "脚本具备明确核心信息、记忆点和 CTA"
  ],
  "rubrics": [
    "rb.commercial-script"
  ],
  "linked_atoms": [
    "ka.cross-protocol-referral-edges",
    "ka.medium-branded-film",
    "ka.medium-commercial",
    "ka.medium-shortform-video",
    "ka.platform-douyin",
    "ka.platform-reels",
    "ka.scene-function"
  ],
  "budget_class": "L",
  "mandatory_atom_count": 7,
  "expansion_allowed": true
}
---
# 商业脚本协议

商业脚本的评判标准不是”像不像电影”，而是”是否同时完成记忆与行动转化”。

商业脚本最怕两头落空：一头只有卖点堆砌，没有观看欲；另一头很好看，但看完不知道品牌、产品或行动指向是什么。这个协议把”传播目标”和”观看体验”捆在一起。

专业上可以把它理解成一条压缩后的信息链：先抓停留，再做理解，再做记忆，最后做行动。不同平台节奏不一样，但这条链路不能丢。
