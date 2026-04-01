---
{
  "id": "ka.triggered-behavior-profile",
  "type": "knowledge_atom",
  "title": "触发式行为画像",
  "kind": "technique",
  "summary": "与其堆性格形容词，不如描述角色在特定刺激下会怎样反应、怎样误判、怎样自保，这种触发式画像更适合进入场景和对白。",
  "mediums": ["feature_film", "episodic", "short_drama", "animation", "game_narrative", "branching_interactive"],
  "stages": ["character", "scene", "dialogue", "rewrite"],
  "problem": "角色设定停留在标签层，无法稳定预测人物在具体情境下会说什么、做什么。",
  "decision_rules": [
    "优先描述刺激-反应对，而不是堆抽象形容词。",
    "行为画像应覆盖压力、羞耻、误解、诱惑、被质疑等高频场景。",
    "画像必须能被场景验证，而不是只能在角色表里显得完整。"
  ],
  "anti_patterns": [
    "性格词很多，但进戏后什么都解释不了",
    "角色在不同场景像不同人",
    "所有触发场景都被写成同一种单一情绪爆发"
  ],
  "prompt_primitives": [
    "这个角色被戳到痛点时第一反应是什么",
    "他被误解、被夸奖、被威胁时分别会怎样自保",
    "哪些触发会让他违背自己平时的表层形象"
  ],
  "evaluation_checks": [
    "画像是否足够具体到能写进场景",
    "是否覆盖了高压和失控情境",
    "能否帮助区分人物声音和行为逻辑"
  ],
  "links": ["ka.character-drive-quartet", "ka.character-voice-consistency", "ka.dialogue-subtext"],
  "source_status": "derived"
}
---
# 触发式行为画像

“他很聪明”“她很敏感”这种描述，只有在角色没进戏之前看着有用。

一旦进入具体场景，真正有用的问题会变成：他被羞辱时怎么回避？她被误解时会立刻解释还是先装没事？他被夸奖时会飘，还是会怀疑对方别有用心？这些才是能被写成场景和对白的材料。

所以触发式行为画像的目标，是把人物从标签层拉回行为层。

## TODOs：待回答问题

- [ ] 触发式画像应覆盖多少类高频情境，才不会过少或过度表格化？
- [ ] 当角色在成长过程中会改变反应模式时，旧画像和新画像如何并存？
- [ ] 哪些触发更适合作为 voice style guide 的输入，哪些只适合留在角色层？
