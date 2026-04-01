# Bilingual Authoring Policy

## Purpose

This repository uses a deliberate dual-track content model instead of trying to make one text serve every audience equally.

- English content is optimized for agent execution, routing clarity, contract readability, and downstream automation.
- Chinese content is optimized for screenplay professionals, script doctors, planners, and creators who need practical terminology without academic stiffness.

The two tracks should align in intent, but they do not need to be sentence-by-sentence translations.

## English Track

English content should read like operational infrastructure for agents.

Priorities:
- explicit routing and interface language;
- crisp task boundaries;
- stable output contracts;
- minimal ambiguity around decision order;
- reusable instructions over rhetorical explanation.

Preferred tone:
- compact;
- precise;
- execution-facing;
- low-fluff.

Avoid:
- marketing language;
- vague “creative inspiration” phrasing without action value;
- long theory exposition where a protocol, rule, or checklist is better.

## Chinese Track

Chinese content should read like working knowledge for screenplay practitioners.

Priorities:
- 编剧、策划、剧本医生能直接拿来用的术语和判断框架；
- 既专业又顺口，不写成翻译腔；
- 说清楚“为什么这会坏、怎么改会更好、在什么场景下用”；
- 尽量把抽象理论落到角色目标、冲突压力、结构节点、场景功能、对白策略、改稿动作。

Preferred tone:
- 专业，但不拿腔；
- 直给，但不粗糙；
- 有行业辨识度，也能让非学院派创作者读懂。

Avoid:
- 只剩术语堆砌；
- 纯理论化、教科书化表述；
- 为了“高端”而牺牲可执行性。

## Alignment Rules

- IDs, schema fields, and route contracts stay language-stable.
- English and Chinese bodies may differ in phrasing density and examples.
- If one track adds a materially new concept, the other track should at least reflect the capability, even if not with the same wording.
- When conflict appears, preserve structured contract correctness first, then improve prose.

## Practical Heuristic

When editing:
- ask “Would an agent know exactly what to do next?” for English;
- ask “Would a working writer or script doctor actually say this?” for Chinese.

