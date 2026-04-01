---
{
  "id": "ka.adaptive-quality-lens-selection",
  "type": "knowledge_atom",
  "title": "自适应质检镜头选择",
  "kind": "heuristic",
  "summary": "通用质检不应把所有项目都塞进固定 stage 流程，而应按 medium、target contract、delivery pressure 选择 3-6 个最能改变判断的检查镜头。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "commercial", "branded_film", "shortform_video", "game_narrative", "branching_interactive"],
  "stages": ["premise", "character", "structure", "outline", "scene", "dialogue", "rewrite", "adaptation"],
  "problem": "专用 checker 往往在自己的任务里很强，但一旦把固定检查层直接推广到所有剧本场景，就会出现有的项目被过检、有的项目漏检，还有的项目被错检。",
  "decision_rules": [
    "按 target contract、medium 和 downstream pressure 选择最小有效 lens stack，而不是默认全开。",
    "每次质检至少保留一个 contract lens 和一个 execution or delivery lens，防止只审美不审落地。",
    "优先选择会改变修改优先级的镜头，不加载只会重复同一结论的检查层。"
  ],
  "anti_patterns": [
    "把一个专用工作流的固定阶段复制成仓库通用规则",
    "所有场景都跑满全量检查",
    "voice、interactive、team workflow、project surface 用同一套戏剧文本审查项"
  ],
  "prompt_primitives": [
    "这个 artifact 在当前 medium 下最容易出错的 3-6 个镜头是什么",
    "哪些检查镜头会真正改变修改优先级",
    "哪些镜头在这个场景里不该默认启用"
  ],
  "evaluation_checks": [
    "lens stack 是否与 medium 和 target contract 匹配",
    "是否避免了过检或漏检",
    "是否把最关键的风险镜头放进了必检层"
  ],
  "links": ["ka.contract-first-quality-gating", "ka.scenario-factorization", "ka.reference-expansion-balance"],
  "source_status": "synthesized"
}
---
# 自适应质检镜头选择

同样叫“检查”，短剧 hook、互动分支、品牌片脚本、voice guide、screen-to-video brief、team workflow blueprint 审的根本不是同一种东西。

这就是为什么当前仓库不应该照搬一个固定线性 stage 流程，而应该引入可选 lens stack。对 narrative scene，可能最该看的是 contract fit、dramatic mechanics、continuity、voice；对互动分支，更关键的是 agency、state continuity、convergence control；对 team 或 project surface，则应该把 handoff、packet、edit policy、delivery surfaces 拉到前面。

通用，不等于统一。真正强的通用层，是统一抽象而不是统一 checklist。

## TODOs：待回答问题

- [ ] 哪些 artifact family 需要独立 bundle，而不是继续并入更大类？
- [ ] 当前 repo 哪些 output 仍然缺少足够清楚的 default lens stack？
- [ ] 什么条件下应该强制从 targeted audit 升级成 full audit？
