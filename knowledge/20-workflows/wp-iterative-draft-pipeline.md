---
{
  "id": "wp.iterative-draft-pipeline",
  "type": "workflow_protocol",
  "title": "迭代草稿流水线",
  "goal": "通过 生成→受众代理评审→修改 的循环，驱动场景草稿从初稿质量向真实观看体验质量收敛。",
  "input_contract": [
    "scene_card",
    "scene_draft",
    "outline"
  ],
  "output_contract": [
    "scene_draft",
    "screenplay_draft"
  ],
  "preconditions": [
    "已有可评审的初稿或场景卡",
    "已明确目标受众和媒介"
  ],
  "steps": [
    "基于 scene_card 或 outline 生成初稿：只完成场景功能骨架，不追求语言精炼，目标是产生可供评审的最小可用文本。",
    "用 wp.audience-proxy-review 对初稿运行受众代理评审：激活 2-3 个代理，输出各代理的 patience 变化和最关键的 concern。",
    "从评审报告中提取最高优先级修改点（1-2条），忽略次要问题，专注于造成 patience 下跌的根本原因。",
    "针对提取的修改点重写该段，只改需要改的部分，不做全文润色。",
    "对修改后的版本重跑受众代理评审，检查 patience 曲线是否改善，concern 是否解消。",
    "若改善达标（patience 涨幅≥10 或 concern 数量减少），输出当前版本；若未达标，回到步骤3重复，最多3轮。"
  ],
  "fallbacks": [
    "若3轮后 patience 仍未改善，标记为结构性问题，回退到 outline 层重新设计场景功能，而非继续局部修改。",
    "若代理关切高度分歧（无共识），选择最接近主受众的代理作为主评审人，记录分歧供作者判断。"
  ],
  "stop_conditions": [
    "受众代理至少一个达到 hooked=true",
    "共识 concern 数量为0或已全部有回应",
    "已达最大迭代轮次（3轮）"
  ],
  "rubrics": [
    "rb.scene-draft",
    "rb.audience-experience"
  ],
  "linked_atoms": [
    "ka.audience-proxy-personas",
    "ka.conflict-pressure",
    "ka.cross-protocol-referral-edges",
    "ka.scene-function",
    "ka.specificity-pressure"
  ],
  "budget_class": "M",
  "mandatory_atom_count": 5,
  "expansion_allowed": true
}
---
# 迭代草稿流水线

迭代不是为了让草稿"更好"，而是为了让草稿更诚实。受众代理告诉你的是编辑逻辑无法告诉你的真相：一个真实观看者在哪里开始失去耐心、为什么失去，以及这种失去是否有结构性原因。

每一轮修改的目标不是让所有问题消失，而是让最重要的那个问题消失。提取 1-2 条最高优先级修改点，忽略其余，是这个协议最核心的执行纪律。一次想改五处，等于一处都没有真正改。

最多 3 轮是硬停止。3 轮之后如果 patience 仍未改善，问题已经不在文本层面，而在场景功能的设计层面。继续局部修改只会消耗预算而不产生收敛，此时唯一正确的动作是回退到 outline 重新问：这场戏究竟应该做什么。
