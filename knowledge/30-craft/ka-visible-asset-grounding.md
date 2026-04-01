---
{
  "id": "ka.visible-asset-grounding",
  "type": "knowledge_atom",
  "title": "可见资产锚定",
  "kind": "heuristic",
  "summary": "桥接到镜头或 clip 级时，要区分可见人物、画外音人物、可见道具和仅在语义层存在的信息，否则执行层会把文本暗示误当成画面证据。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video"],
  "stages": ["scene", "adaptation", "rewrite"],
  "problem": "桥接说明把 V.O.、背景设定、隐含道具和实际可见元素混成一层，导致镜头执行失真或资源判断错误。",
  "decision_rules": [
    "先区分可见证据与不可见信息，再写执行说明。",
    "画外音人物不能默认等于画面出现人物。",
    "道具是否写入执行层，应取决于它在当前镜头单元里是否可见、是否有功能。"
  ],
  "anti_patterns": [
    "所有提到的人物都被算进镜头出现人物",
    "剧情上重要但画面未证实的物件被当作可见道具",
    "声音、记忆、设定说明和镜头证据混成同一列表"
  ],
  "prompt_primitives": [
    "当前单元里真正可见的角色和道具是什么",
    "哪些信息只存在于对白、V.O. 或世界观说明中",
    "如果镜头必须删到最少，可见证据还剩下什么"
  ],
  "evaluation_checks": [
    "可见与不可见要素是否被清楚分层",
    "镜头执行说明是否基于当下证据而非全文脑补",
    "资产列表是否避免了无关噪音"
  ],
  "links": ["ka.source-span-traceability", "ka.screenplay-to-video-boundary", "ka.multilingual-visual-vocabulary"],
  "source_status": "derived"
}
---
# 可见资产锚定

剧本层可以容纳很多“被知道但没被看到”的信息，镜头层不行。

一旦进入 shot、subshot、clip 级容器，最重要的判断之一就是：这是谁真正在场、什么东西真被看见、哪些只是声音、回忆、设定或语义暗示。只要这一层没分清，后面的执行就会把文本理解错误地硬落成画面。

所以这个原子处理的不是“资产管理”，而是镜头证据诚实度。

## TODOs：待回答问题

- [ ] 对强调声音叙事的内容，V.O. 和 off-screen action 是否需要更细的分层规则？
- [ ] 商业广告与叙事场景在“可见道具”判定上是否应采用不同粒度？
- [ ] 当场景故意依赖留白和不展示时，系统如何避免把“不展示”误改成“展示补全”？
