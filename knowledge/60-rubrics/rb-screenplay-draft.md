---
{
  "id": "rb.screenplay-draft",
  "type": "evaluation_rubric",
  "title": "Screenplay Draft Rubric",
  "applies_to": ["screenplay_draft"],
  "dimensions": [
    {"name": "scene_chain", "question": "多场景链条是否形成持续推进，而不是一组松散片段"},
    {"name": "performance_carry", "question": "每个对白回合是否都挂在可执行的表演承载上"},
    {"name": "format_handoff", "question": "场景、动作、对白、AV 标记是否足够稳定，能直接交给下游检查或改写"},
    {"name": "expression_integrity", "question": "整份页稿是否持续避免作者腔、机械语症和语言自然度断层"}
  ],
  "scoring_bands": {
    "excellent": "页稿链条稳定，场景接力清楚，表演承载完整，格式可交接，自然度前后一致。",
    "workable": "能看出页稿推进，但局部仍有格式松散、承载缺失或自然度回落。",
    "weak": "更像场景摘录或对白堆叠，既不稳也不好交接。"
  },
  "hard_fail_rules": [
    "页稿不包含至少两个可成立的场景块",
    "存在裸对白回合：对白没有 inline performance，也没有紧邻动作拍点承载",
    "场景之间推进关系不清，只是片段堆叠",
    "中文输出存在三个以上机械语症：四字词语堆砌、情绪标签句、解释性过渡句、对仗式对白、语域错位、完整句病"
  ],
  "rewrite_actions": [
    "补足场景链条中的进入、升级和离开点",
    "给所有对白回合补表演承载",
    "统一页稿的块级格式与 AV 标记",
    "按场景回查机械语症，并修掉跨工件自然度断层"
  ]
}
---
# Screenplay Draft Rubric

这份 rubric 关心的不是“页数够不够像页稿”，而是它能不能作为一个真的活剧本草稿继续往下游流动。

一份页稿级 `screenplay_draft` 至少要同时成立四件事：场景链条在推进，角色说话有人味且不脱表演，格式能被检查器和下游人工稳定接住，以及自然度不会一场像人写、一场又滑回 AI 腔。

## TODOs：待回答问题

- [ ] 当页稿故意追求极简对白和长动作段时，`performance_carry` 的判定阈值要如何调整？
- [ ] 多线程群像页稿里，scene chain 的“持续推进”应如何避免误判成并行散点？
- [ ] 如果某些视听设计会在导演阐述或 shot list 层补足，`format_handoff` 对 `VFX / SFX / BGM` 的要求是否需要按项目类型分级？
