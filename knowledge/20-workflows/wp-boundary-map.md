---
{
  "id": "wp.boundary-map",
  "type": "workflow_protocol",
  "title": "边界地图协议",
  "goal": "为一个创作任务明确 hard-no、soft-risk、bold-safe 和 defer-to-review 区域，防止把所有约束写成同一等级。",
  "input_contract": [
    "brief",
    "draft",
    "known constraints",
    "risk concern",
    "delivery context"
  ],
  "output_contract": [
    "boundary_map"
  ],
  "preconditions": [
    "用户需要判断当前任务中哪些边界不可跨越、哪些约束可暂缓、哪些区域可大胆探索",
    "至少存在一个明确的问题、任务或待判断方向"
  ],
  "steps": [
    "识别始终有效的 hard boundary。",
    "识别当前阶段可暂挂的 soft constraint 与需要后置判断的 review gate。",
    "标出此刻可以放心大胆探索的 bold-safe zone。",
    "输出 boundary_map，并说明哪些检查应在 review 阶段重新加回。"
  ],
  "fallbacks": [
    "若约束来源太多，先按 safety、legal、audience、production、platform、brand 六类归并。",
    "若用户把所有约束都当成硬边界，先拆出真正不可谈判项。"
  ],
  "stop_conditions": [
    "边界等级清楚，不再混淆 hard 和 soft",
    "后续 exploration 与 review 的分工清楚"
  ],
  "rubrics": [
    "rb.boundary-map"
  ],
  "linked_atoms": [
    "ka.boundary-first-guidance",
    "ka.exploration-review-separation",
    "ka.platform-attention-economy",
    "ka.commissioning-fit"
  ],
  "budget_class": "M",
  "mandatory_atom_count": 4,
  "expansion_allowed": true
}
---
# 边界地图协议

这个协议的作用，不是替用户做内容审判，而是帮助用户看清楚：哪些边界必须一直保留，哪些约束可以后置，哪些区域当前反而应该大胆试。

很多项目一上来就卡住，不是因为想法太少，而是因为约束没有分级。品牌、平台、审美、市场、团队偏好、风险判断全挤成一团，最后创意还没展开就先被自己压死了。边界地图就是用来拆这团线。

做得好的 boundary_map，能让团队把争论从“到底能不能写”转成“现在先写到哪、后面在哪一关再收”。

## TODOs：待回答问题

- [ ] `boundary_map` 是否需要按 narrative / commercial / interactive 做不同模版？
- [ ] 在高度监管或高风险分发环境中，哪些 soft constraint 会前移成 route-critical constraint？
- [ ] 对品牌项目来说，brand consistency 何时只是 soft constraint，何时接近 hard boundary？
- [ ] 用户若明确想打破某个惯例，系统应如何区分“必要突破”与“误判风险”？
- [ ] boundary_map 是否应与 development_brief 联动，形成一前一后的工作组合？
