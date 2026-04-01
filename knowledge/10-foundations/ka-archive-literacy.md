---
{
  "id": "ka.archive-literacy",
  "type": "knowledge_atom",
  "title": "编剧档案素养",
  "kind": "history",
  "summary": "研究 step outline、treatment、批注稿、口述史、未拍项目和版本链，能比只看定稿更真实地理解编剧工作是如何发生的。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["ideation", "premise", "structure", "rewrite", "adaptation"],
  "problem": "学习者和 Agent 只研究成片或最终剧本，把大量真实开发、协作和改稿知识都漏掉，导致对创作过程形成失真的想象。",
  "decision_rules": [
    "优先比较同一项目的多个阶段文档，而不是只盯着最后的 polished draft。",
    "把口述史、档案元数据和未拍项目当作过程证据，用来理解工作方法的适用边界。",
    "研究档案时关注版本、日期、批注者和使用场景，因为这些信息会改变你对文本的理解。"
  ],
  "anti_patterns": [
    "只研究最终剧本",
    "把档案当成收藏癖而不是过程知识",
    "忽略版本状态和来源信息"
  ],
  "prompt_primitives": [
    "这个项目如果看版本链，会暴露出哪些创作决策的真实演化",
    "哪些口述史和档案信息在修正对行业常识的误解",
    "这份材料到底是开发稿、生产稿还是归档稿"
  ],
  "evaluation_checks": [
    "是否区分了不同阶段文档的功能",
    "是否说明档案来源和版本状态为什么重要",
    "档案研究是否真正改变了当前的判断，而不是只增加典故"
  ],
  "links": ["ka.screenwriting-history-shift", "ka.room-artifact-ladder", "ka.source-of-truth-runtime-split", "ka.source-span-traceability", "ka.script-as-coordination-artifact"],
  "source_status": "curated"
}
---
# 编剧档案素养

如果你只研究最终上映作品或最终定稿，你看到的通常只是编剧工作的“表面胜利形态”。
真正决定项目怎么长出来、怎么被改掉、怎么进入不同版本的那些知识，很多都藏在档案里。

比如：

- step outline 和 treatment 能暴露项目最初是怎么组织的；
- 批注稿能暴露哪些问题是开发重点；
- 未拍项目能暴露哪些想法在当时被认为可行或不可行；
- 口述史能暴露很多不会写进“经验总结”的真实流程；
- 版本日期和 provenance 会告诉你，这份文本到底是在什么阶段服务什么目标。

所以档案素养不是“多知道一些老资料”。
它真正重要的地方，是帮助仓库和 Agent 不要把最终成型作品误当成创作过程本身。

## TODOs：待回答问题

- [ ] 是否需要为不同类型的档案材料建立更明确的可信度和用途标签？
- [ ] 公开档案中哪些材料最值得优先转译成 Agent 可调用知识，而不是停留在 source map 层？
- [ ] 口述史里的经验常带强烈个人风格，系统该如何提炼稳定部分而不抹掉个体差异？
- [ ] 对没有条件访问大型档案馆的创作者，哪些公开资料最适合替代性地培养档案素养？
