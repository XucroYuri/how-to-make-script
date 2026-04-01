---
{
  "id": "ka.feedback-subjectivity-management",
  "type": "knowledge_atom",
  "title": "反馈主观性管理",
  "kind": "heuristic",
  "summary": "剧本反馈天然带主观性，但主观性不等于无效；有效的处理方式是聚类重复信号、翻译底层病灶，并保护仍然成立的创作核心。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "创作者要么把每条 note 都当圣旨执行，要么因为反馈彼此矛盾就干脆全部无视，导致改稿失去判断力。",
  "decision_rules": [
    "先区分 note 的表面措辞和它可能指向的底层病灶，再决定是否采纳。",
    "优先关注不同读者之间重复出现的症状，而不是最强势或最会说话的单条意见。",
    "在保留作者核心意图的前提下，修复真实反复出现的理解、节奏、角色或结构问题。"
  ],
  "anti_patterns": [
    "逐条执行所有反馈",
    "用“创作没有标准答案”挡掉全部反馈",
    "为了回应 note 而改动表面，却没有处理真正病因"
  ],
  "prompt_primitives": [
    "这条反馈到底在描述症状、原因还是个人偏好",
    "多个反馈之间重复出现的病灶是什么",
    "哪些核心表达必须保住，哪些只是可替换实现"
  ],
  "evaluation_checks": [
    "是否说明了哪些反馈只是局部口味",
    "是否识别出重复信号背后的底层问题",
    "修改建议是否真的对应病因，而不是只回应措辞"
  ],
  "links": ["ka.dissent-preservation-loop", "ka.scope-correction", "ka.rewrite-diagnosis", "ka.targeted-recheck-loop", "ka.screenplay-lens-stacking"],
  "source_status": "curated"
}
---
# 反馈主观性管理

剧本反馈几乎不可能完全客观。
但这不代表反馈只能靠“谁更有权威”或者“谁声音更大”来决定。

真正成熟的改稿能力，来自对反馈主观性的管理，而不是对主观性的否认。你需要判断：

- 这条 note 是在说个人口味，还是在暴露一个真实症状；
- 它描述的是表面问题，还是已经碰到了底层病灶；
- 它要求的解决方案对不对，还是只是把问题说对了、解法说错了。

Agent 如果做不好这一层，就会变成一种非常危险的工具：谁给它输入 note，它就帮谁放大。
所以这条原子的重点，就是让系统有能力在保住创作核心的前提下，提炼反馈里的有效信号。

## TODOs：待回答问题

- [ ] 仓库是否需要给不同类型的反馈建立更明确的置信等级系统？
- [ ] 当商业方、平台方、导演、编剧本人给出的反馈彼此冲突时，应如何做优先级治理？
- [ ] 某些高质量作品的关键魅力恰好来自对常见反馈的逆向坚持，这类情况应如何编码？
- [ ] 什么时候应该建议“先不要改”，而是先补更多读者或更多证据？
