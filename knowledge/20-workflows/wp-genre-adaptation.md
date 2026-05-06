---
{
  "id": "wp.genre-adaptation",
  "type": "workflow_protocol",
  "title": "类型适配协议",
  "goal": "在不破坏核心叙事引擎的前提下，把项目适配到目标类型或媒介。",
  "input_contract": [
    "existing premise",
    "existing outline",
    "target genre",
    "target medium"
  ],
  "output_contract": [
    "premise",
    "treatment",
    "outline",
    "scene_draft",
    "interactive_branch_map"
  ],
  "preconditions": [
    "已有可被改造的故事材料"
  ],
  "steps": [
    "识别原始故事中不可破坏的核心引擎。",
    "抽取目标类型或媒介的关键承诺。",
    "决定哪些结构、场景和角色关系需要重写。",
    "输出适配版本与主要变化说明。"
  ],
  "fallbacks": [
    "若改动后核心引擎消失，收缩适配强度。",
    "若目标类型约束互相冲突，优先保护核心承诺。"
  ],
  "stop_conditions": [
    "适配版仍保有核心引擎",
    "目标类型或媒介承诺已被满足"
  ],
  "rubrics": [
    "rb.adaptation"
  ],
  "linked_atoms": [
    "ka.cross-protocol-referral-edges",
    "ka.genre-action",
    "ka.genre-comedy",
    "ka.genre-family",
    "ka.genre-horror",
    "ka.genre-pack-factorization",
    "ka.genre-romance",
    "ka.genre-satire",
    "ka.genre-thriller",
    "ka.genre-suspense",
    "ka.genre-wuxia",
    "ka.medium-branching-interactive",
    "ka.medium-commercial",
    "ka.medium-feature-film"
  ],
  "budget_class": "L",
  "mandatory_atom_count": 14,
  "expansion_allowed": true
}
---
# 类型适配协议

适配不是换皮。它要求保住原始引擎，同时重写承诺形式。

很多”改成惊悚版””改成短剧版””改成互动版”的失败，本质都在于只换了表面元素，却没有调整真正决定观看体验的结构承诺。类型适配要处理的不是词汇替换，而是节奏、压力、信息释放、情绪兑现和媒介约束。

专业改编时最该盯紧的一点：哪些是原故事不可丢的核心引擎，哪些只是当前版本的表达外壳。分不清这件事，适配很容易不是增强，而是把故事拆散。
