---
{
  "id": "rb.rewrite-report",
  "type": "evaluation_rubric",
  "title": "Rewrite Report Rubric",
  "applies_to": ["rewrite_report"],
  "dimensions": [
    {"name": "diagnosis", "question": "问题层级判断是否准确"},
    {"name": "priority", "question": "建议是否按杠杆排序"},
    {"name": "actionability", "question": "建议是否具体可执行"},
    {"name": "layer_traceability", "question": "问题是否被正确地映射到具体层面（概念/结构/场景/对白）和具体位置？"},
    {"name": "revision_guidance", "question": "修改建议是否说明了\u201c改什么、怎么改、为什么这样改更好\u201d？"}
  ],
  "scoring_bands": {
    "excellent": "分层清晰、优先级合理、每个问题都映射到具体层面和位置、修改建议包含完整的 what/how/why。",
    "workable": "有诊断和建议，但层级或优先级仍略混，或部分问题未落到具体位置。",
    "weak": "只有泛泛建议，缺少病灶判断、执行路径，或未说明具体在哪个位置改。"
  },
  "hard_fail_rules": [
    "没有区分问题层级",
    "没有优先级排序",
    "建议停留在抽象评价",
    "问题只说了\u201c哪一层\u201d但没落到具体场景、节拍或对白回合",
    "修改建议只有\u201c应该更好\u201d但没有说明改什么、怎么改、为什么这样改更好"
  ],
  "rewrite_actions": [
    "先重做问题分层",
    "只保留高杠杆动作",
    "把建议翻译成场景或结构级动作",
    "为每个问题标注具体层面和位置（如：S3 开场对白段、M2 升级节拍）",
    "补齐修改建议的 what（改什么）、how（怎么改）、why（为什么更好）"
  ]
}
---
# Rewrite Report Rubric

用于判断改稿报告是不是能真正指导下一轮重写。

改稿报告的价值，不在于它指出了多少毛病，而在于它有没有帮助团队决定“下一轮最该先改什么”。这个 rubric 会特别强调分层、排序和可执行性，因为没有这三件事的诊断通常只会制造更多讨论，不会制造更好的稿子。
