---
{
  "id": "ka.screenplay-to-video-boundary",
  "type": "knowledge_atom",
  "title": "剧本与视频生成 brief 的边界",
  "kind": "heuristic",
  "summary": "剧本负责戏剧、人物与场景功能，视频生成 brief 负责把其中一段内容翻译成时长受限、镜头受限、执行受限的可视化约束，不应相互吞并。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video"],
  "stages": ["scene", "rewrite", "adaptation"],
  "problem": "一旦把剧本文本直接压扁成视频提示词，要么戏剧目的丢失，要么生成 brief 过长过杂，既不像剧本，也不像可执行的视觉指令。",
  "decision_rules": [
    "先提取 scene 的戏剧任务、关系压力和非丢不可的信息，再做视觉翻译。",
    "视频生成 brief 只保留会改变画面执行的元素：动作、镜头、灯光、时长、音频、文字、不变量。",
    "任何只属于 screenplay 的叙事解释、心理旁白和冗余世界说明，都不应直接进入短 clip brief。"
  ],
  "anti_patterns": [
    "把整段剧本原封不动塞进视频生成模型",
    "为了可执行而把人物关系与戏剧压力全删光",
    "一份 brief 同时承担剧本、分镜、镜头表、拍摄计划和模型提示的全部功能"
  ],
  "prompt_primitives": [
    "这场戏真正不能丢的是哪条关系、动作或信息，不是哪些修辞句子",
    "如果当前段落只能变成 4 到 12 秒 clip，最该保住的戏剧动作是什么",
    "哪些内容该留在 screenplay，哪些内容才该翻进视频 brief"
  ],
  "evaluation_checks": [
    "翻译后是否仍然保住场景的戏剧功能",
    "brief 是否比原剧本更可执行，而不是更混乱",
    "是否明确区分了 screenplay residue 与 video-execution constraints"
  ],
  "links": ["ka.scene-function", "ka.multilingual-visual-vocabulary", "ka.prompt-delegation-levels", "ka.medium-shortform-video"],
  "source_status": "derived"
}
---
# 剧本与视频生成 brief 的边界

剧本和视频生成 brief 看起来都在描述“这段内容长什么样”，但它们不是同一种东西。

剧本的主要责任，是把人物、冲突、关系、场景功能和叙事推进讲清楚。视频生成 brief 的责任，则是把其中一小段翻译成模型或视觉团队可以执行的约束：主体是谁，动作是什么，镜头怎么运动，灯光和气质怎么锁，哪些东西不能漂移。

一旦不区分这两层，最常见的结果只有两个。一个是把剧本压扁成一大串镜头词，最后人物和戏剧死掉；另一个是把所有叙事说明全都保留，导致 brief 太长太散，模型或协作方都抓不住重点。

所以这层不是教人“怎么写视频提示词”，而是教 Agent 识别：什么还属于剧本，什么已经该进入视觉执行容器。只有边界稳住，桥接层才不会把整个仓库带偏。

## TODOs：待回答问题

- [ ] 当用户真正要的是 previz / storyboard 而不是生成模型 brief 时，这条边界该如何再细分？
- [ ] 长场景拆成多 clip chain 时，仓库是否需要单独的 continuity 协议来承接跨 clip 的稳定项？
- [ ] 哪些媒体更适合直接桥接成视频 brief，哪些媒体更适合先经过 outline / shot list 再桥接？
- [ ] 如果商业内容要求强 CTA，而视频 brief 又要求单一动作，仓库应怎样处理行动密度与信息密度的冲突？
- [ ] 当前桥接层是否还需要显式记录“哪些说明是给模型看的，哪些说明是给人看的”双层输出？

