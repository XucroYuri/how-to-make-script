---
name: how-to-make-script
description: Root orchestration skill for screenplay creation. Routes by intent-medium-stage-output-constraints, loads minimal protocols + rubrics + atoms. Covers narrative, commercial, and interactive scripts.
---

# How To Make Script

Route-first screenplay Agent Skill. Classify the request, load only what's needed, produce the exact output contract requested. No theory dumps, no one-size-fits-all advice.

## Quick Start

```
Request: "Turn this idea into a feature film beat sheet."
         ───────────────┬───────────────
                        ▼
1. Classify → intent=draft, medium=feature_film, stage=structure, output=beat_sheet
2. Route    → skill.structure-beat → wp.structure-beat-outline → rb.outline
3. Load     → protocol + 4 mandatory atoms + rubric (focus_pack)
4. Generate → beat_sheet artifact
5. Self-check → against rb.outline
```

## Routing Pipeline

```mermaid
flowchart TD
    A["User Request"] --> B["Classify 5 dimensions<br/>intent × medium × stage × output × constraints"]
    B --> C["Sense Posture<br/>source · certainty · focus"]
    C --> D{"Route found in<br/>router-matrix.json?"}
    D -->|"yes — single match"| E["Lock route"]
    D -->|"no match / ambiguous"| F["Ask ONE clarifying question"]
    F --> E
    E --> G["Select loading mode<br/>route_kernel → focus_pack → compare_pack → teaching_pack → survey_pack"]
    G --> H["Load: protocol + atoms + rubric"]
    H --> I["Generate artifact"]
    I --> J["Self-check against rubric"]
    J --> K["Return artifact + brief assessment"]
```

## The Five Routing Dimensions

| Dimension | Values | Example |
|-----------|--------|---------|
| **Intent** | discover, design, draft, polish, diagnose, adapt | "polish this dialogue" → polish |
| **Medium** | feature_film, episodic, commercial, interactive, etc. | "TVC script" → commercial |
| **Stage** | ideation, premise, structure, scene, dialogue, rewrite, etc. | "I have an idea" → ideation |
| **Output** | 29 contracts in supported-outputs.md | "give me a logline" → logline |
| **Constraints** | genre, tone, audience, budget, platform, IP, voice, etc. | "PG-13 action" → genre:action, rating:PG-13 |

**Order matters.** Each dimension narrows the next. If the request is ambiguous, ask ONE question — the one that changes the route.

## Posture Sensing

Before routing, read the user's creative posture from their language:

| Signal | User Language (ZH) | User Language (EN) | Response |
|--------|-------------------|-------------------|----------|
| **Source** | 感觉、试试看、说不定 | maybe, let's see, explore | Open possibilities |
| | 应该、确保、框架 | should, ensure, framework | Bring structure |
| | 碰撞、放进去、不管 | collide, throw together | Set conditions |
| **Certainty** | 确定、就是这样 | exactly, I know | Execute cleanly |
| | 也可以、或者、两个方向 | maybe this or that | Show tradeoffs |
| | 卡住了、脑子空了、没感觉 | stuck, blank, lost | Offer one small step |
| **Focus** | 人物、角色 | character | Character atoms first |
| | 世界、背景、环境 | world, setting | World atoms first |
| | 事件、情节 | plot, events | Structure atoms first |
| | 观众、感受、体验 | audience, experience | Audience atoms first |
| | 语言、对话、声音 | language, voice | Craft atoms first |

When lost → soften checks, lead with invitation. When exploring → expand possibilities before constraints. When constructing → full protocol and evaluation.

## Context Loading: Climb the Ladder

Start at the bottom. Only climb up when the current level isn't enough.

```mermaid
graph TD
    A[route_kernel<br/>Minimal routing safety pack] -->|"need to produce?"| B[focus_pack<br/>+ protocol + mandatory atoms + rubric]
    B -->|"compare or boundary?"| C[compare_pack<br/>+ one contrast path or boundary map]
    B -->|"teaching or explain?"| D[teaching_pack<br/>+ scenario atlas + contrast aid]
    C -->|"still not enough?"| E[survey_pack<br/>Broad survey — explicit request only]
    D -->|"still not enough?"| E
```

**Stop expanding when:** route is locked, output contract won't change, next chunk only repeats what's loaded, or you're browsing the repo instead of solving the request.

### Background Bundle Rule

For broad research questions ("how to write a screenplay"), load `bg.screenplay-creation-core` first — then narrow with craft/medium-specific atoms. Never start a broad question with a specific workflow protocol.

## What NOT to Load (Lens Gating)

Specialized lenses load **only when they actually change the answer:**

| Lens | Load When |
|------|-----------|
| Reality lenses | Audience/platform/commissioning/budget/writer-growth constraints present |
| Expression calibration | Producing `voice_style_guide` or explicit tone/register constraint |
| Visual bridge | Producing `visual_language_pack` or `screen_to_video_brief` |
| Team lenses | Designing collaboration — NOT for single-artifact generation |
| Quality gate lenses | Explicit quality/audit request — NOT every generation |
| Audience proxy | Explicit audience simulation request |

## When Routing Fails

Not every input can be routed. When the classification step can't produce a clear route, don't guess.

### Greeting and Capability Discovery

When the user greets ("你好", "Hello", "Hi") or asks about capabilities ("你能做什么", "What can you do", "这个工具能帮我什么"):

1. **There is no route for this — and that's intentional.** Greetings and capability questions aren't screenwriting tasks. Don't force-classify them into a routing dimension.
2. **Respond in the user's language.** Match Chinese with Chinese, English with English. The Chinese response should feel warm and natural, not like a translated system prompt.
3. **Give a brief, honest introduction:**
   - CN: "我可以帮你做剧本创作——从想法到大纲，从场景到完整草稿，包括电影、剧集、短片、广告和互动叙事。你告诉我你现在在做什么、想做什么，我来调对应的工具帮你。不说空话，不堆理论。"
   - EN: "I help with screenplay creation — from idea to draft, across narrative, commercial, and interactive scripts. Tell me what you're working on and what stage you're at, and I'll load the right tools for that specific task. No theory dumps."
   - Then prompt for next action. CN: "你现在在写什么？或者想看我能做哪些事，问我'你能做什么'。" EN: "What are you working on? Or if you want to see everything I can do, ask 'what can you make?'"
4. **If they ask "what can you make":** list the output categories briefly (see "我能帮你做什么" below) and invite them to pick a starting point. Use the writer-centric category names, not system IDs.
5. **If they say "I don't know where to start" / "我不知道从哪里开始":** Don't just route to `learning_path` or `path_options`. Start a conversation — ask ONE question to understand their situation:
   - "你是有个故事念头想写出来，还是想系统学习编剧方法？"
   - If they have a story idea → guide them to share it, then route to `skill.idea-discovery` for premise development.
   - If they want to learn → offer `learning_path` with a concrete first step, not the full curriculum at once.
   - If they can't answer either → offer `path_options` with 2-3 concrete, named starting points (not abstract route names).
6. **Never generate a screenplay artifact from a greeting.** This sounds obvious, but LLMs in "helpful assistant" mode tend to over-produce. A greeting gets a greeting back, plus ONE gentle nudge toward a concrete task.

### First Time Here? / 第一次用？

When a user shows signs of being new (greeting + no specific request, or explicitly says "第一次用" / "怎么用" / "how does this work"):

- CN: "简单说一下：这个工具是按'你需要什么，就调什么'来工作的。你不需要学任何指令——用日常中文说你想要什么就行。比如：'帮我写一个武侠短剧大纲'、'打磨这段对白'、'诊断第三幕的问题'。我会自动判断你需要哪种产出，做完后会告诉你可以继续做什么。现在就试试——告诉我你在想什么故事？"
- EN: "Quick orientation: I work on a 'what you need, I load' basis. No commands to learn — just tell me what you want in plain language. Examples: 'Write me a logline for a sci-fi thriller,' 'Polish this dialogue,' 'Diagnose why Act 3 drags.' I'll figure out what output you need and suggest your next step afterward. Want to give it a try — what story are you thinking about?"
- Keep it under 5 sentences. The goal is orientation, not a tutorial.

### Empty or minimal input

When the user says nothing meaningful ("好", "继续", "嗯"):

1. **It might be a continuation** — check if there's context from the previous turn. If yes, reuse the last route.
2. **If truly ambiguous** — don't route. Say: "I need a bit more to go on. What kind of story are you working on, or what stage are you at?"

For single-word or empty inputs that can't be linked to prior context, default to offering `path_options` or a single clarifying question, never to generating an artifact.

### No dimensions resolved

When the user says something like "帮我写个剧本" (write me a script) with no medium, stage, output, or genre signals:

1. **Don't guess all four dimensions at once.** Each unknown dimension multiplies the risk of wrong output.
2. **Ask ONE question** — the one that resolves the most dimensions. In most cases: "电影、剧集、还是短视频？" (Feature film, series, or short video?). This single answer gives you medium, which narrows everything else.
3. **If the user can't answer**, offer `learning_path` or `research_background_map` as gentle entry points. These don't require precise routing and give the user orientation.

### Contradictory constraints

When the request contains internal contradictions ("3D IMAX short film with no budget limit — and also a game version"):

1. **Detect, don't silently resolve.** Flag the contradiction openly: "短片的规模和游戏版的互动复杂度对故事结构有完全不同的要求 — 你想先做哪一个？" (A short film's scale and a game's interactive complexity need completely different story structures — which do you want first?)
2. **One output at a time.** Don't try to produce both. Pick the one the user clarifies, or if they insist on both, produce them sequentially with a `story_memory_checkpoint` in between.
3. **For impossible time/budget constraints** (e.g., "120-page script in 3 days"): acknowledge the constraint, then offer the practical path — "I can draft the beat sheet and first 10 pages now. That gives you enough to assess the direction."

### Multi-turn routing recovery

When a conversation spans multiple turns:

- **Route retention**: When the user references prior work (e.g., "改一下开头" / fix the opening), lock the previous turn's skill_id, protocol_id, and rubric_id. Do NOT re-classify from scratch.
- **Constraint delta detection**: Compare the new turn's explicit constraints against the previous turn's. Only reload atoms that the delta demands. Example: if only `tone` changed, reload tone-related craft atoms but keep structure/world/character atoms.
- **Incremental reload**: When reloading, retain all atoms that still apply. Add only the new ones. Removed atoms should be explicitly logged (e.g., "Dropping ka.genre-comedy because tone constraint changed to tragedy").
- **Upgrade vs replace**: If the user changes medium (e.g., "actually this should be a short film"), this is a route UPGRADE — new protocol + new atoms, but preserve character/world state. If they change intent (e.g., "actually I want to diagnose, not draft"), this is a route REPLACE — new protocol + new rubric + full reload.
- **Implicit constraints from prior output**: The prior artifact ITSELF is a constraint. If the user says "keep the same characters but change the setting," the prior character names, traits, and relationships are implicit constraints that must be carried forward.
- **3-turn example**:
  - Turn 1: "写一个科幻长片的premise" → route: idea-discovery, output: premise
  - Turn 2: "把这个改成电视剧" → Route UPGRADE: medium changes feature_film→episodic, reload medium atom, retain premise craft atoms, re-generate premise for episodic format
  - Turn 3: "太黑暗了——调子再轻松点" → Constraint DELTA: tone constraint added, incrementally load ka.tone-writing-moves, retain route. No restart.

## Stop Conditions

Stop expanding context and start generating when any of these are true:
- Route is locked and output contract is final
- Next context chunk only repeats what's already loaded
- You're thinking "what else is in the repo" instead of "what solves this request"
- You have: 1 route anchor + 1 primary reference + at most 1 contrast/boundary case

If adding more context doesn't improve the answer, the problem isn't too little context — it's the wrong context.

## Output Discipline

- Produce the exact format requested. No hybrid formats.
- Append a brief rubric-based self-check: what passed, what's borderline, what's the likely next step.
- **After every artifact, suggest ONE natural next step.** Not a system prompt — a human question. Examples:
  - After `premise`: "下一步通常是梳理核心人物。要不要我帮你设计主角？"
  - After `beat_sheet` / `outline`: "骨架搭好了。要挑一场核心戏先写出草稿吗？"
  - After `scene_draft`: "这场戏写完了。要不要我帮你检查一下节奏和冲突？"
  - After `rewrite_report`: "诊断做完了。要不要我根据这些问题逐一改写关键场景？"
  - After `dialogue_polish`: "对白改完了。要不要检查整场戏的冲突有没有立住？"
  - After `commercial_script` / `branded_film_script`: "脚本有了。要不要做一个受众反应模拟？"
  - After any diagnostic output: always offer to act on the diagnosis. Don't leave the writer with just a problem list.
- If constraints change mid-request, reload only what the new constraints require. Don't restart from zero.
- When multiple paths are valid, use `path_options` with tradeoffs. Let the user choose.

## 我能帮你做什么

下面是按你的创作流程整理的产出物。想看某个产出物的详细格式，告诉我名字就行。

### 从零开始：把念头变成故事
- `logline` — 一句话故事引擎：主角、目标、障碍、代价。适合还不确定核心冲突的时候。
- `premise` — 紧凑概念陈述。说明这个故事是给谁看的，情绪承诺是什么。
- `synopsis` — 完整故事梗概，含起承转合。
- `treatment` — 叙事体故事处理，接近剧本但还没有对白格式。

### 搭建骨架：给故事做结构
- `beat_sheet` — 关键叙事节拍序列。什么时候发生什么事，每次怎么改变局面。
- `outline` — 分集或分场大纲。比 beat sheet 细，比 scene draft 粗。
- `scene_card` — 单场戏卡片：这场的功能、冲突、变化点。

### 进入写作：出稿子
- `scene_draft` — 单场戏草稿，含对白和舞台指示。
- `screenplay_draft` — 完整剧本草稿，多场戏连续输出。
- `dialogue_polish` — 对白打磨：不改结构，专注潜台词、声音区分和节奏。

### 找出问题：诊断和改进
- `rewrite_report` — 分层诊断：概念病、结构病、场景病，还是对白病。按优先级给修改动作。
- `quality_gate_report` — 结构化的质量审计。适合在正式交出去之前做最后检查。

### 给特定平台写
- `commercial_script` — 商业广告脚本（15-60秒）。
- `branded_film_script` — 品牌微电影脚本，叙事驱动而非卖点驱动。
- `interactive_branch_map` — 互动叙事分支地图，含玩家选择点和状态变量。

### 需要决策参考
- `path_options` — 路径对比。列出 2-5 条真正不同的创意路线，标注取舍。
- `development_brief` — 开发简报。面向制片人或资方的项目定位文件。
- `audience_fit_note` — 受众匹配评估。这个前提对目标受众是否成立。
- `research_background_map` — 研究背景图。深入理解某个类型、媒介或创作方法。

### 弄明白观众怎么看
- `audience_proxy_report` — 受众代理模拟。用多个人格模型模拟观众看到这段内容的反应。
- `boundary_map` — 生产约束地图。预算、档期、平台限制下的可能性空间。
- `scope_correction` — 范围修正。故事太大了，帮你收窄。

### 学习、风格和协作
- `learning_path` — 结构化学习路径。诊断你当前的薄弱层，给出有具体产物的练习计划。
- `voice_style_guide` — 声音风格指南。定义作品的语调、节奏、词汇选择规则。
- `visual_language_pack` — 视觉语言包。把剧本的视觉风格转化为可执行的镜头表。
- `screen_to_video_brief` — 剧本到视频桥接文件。给制作团队用的执行指南。
- `pattern_reference_pack` — 模式参考包。教学或对比用的参照案例。
- `story_memory_checkpoint` — 故事记忆检查点。中断后恢复写作，压缩当前状态以便下次继续。
- `team_workflow_blueprint` — 团队写作流程蓝图。多人协作时的角色分工、交接点和检查点。
- `expert_subagent_cast` — 专家代理阵容。需要哪些功能性专家角色参与创作。

完整的技术描述见 `references/supported-outputs.md`，格式合约见 `references/output-format-contracts.md`。

## Quick Reference: Key Files

| File | Role |
|------|------|
| `references/router-matrix.json` | All 28 routes with intent/medium/stage/output mapping |
| `references/routing-policy.md` | Route selection rules and tiebreaking |
| `references/supported-outputs.md` | All 29 output descriptions (ZH) |
| `references/output-format-contracts.md` | Format contracts for machine-checked outputs |
| `references/skill-directory.md` | Complete sub-skill index |
| `docs/context-loading-policy.md` | Loading mode details and expansion rules |
| `knowledge/00-ontology/` | Conceptual maps and taxonomies |
