---
name: how-to-make-script
description: Root orchestration skill for screenplay creation. Routes requests by intent, medium, stage, output, and constraints, then loads the minimum necessary protocols, rubrics, and knowledge atoms.
---

# How To Make Script

## Purpose
Use this skill when the user asks how to create, diagnose, improve, structure, or adapt a script across narrative, commercial, or interactive media.

This is the root orchestrator. It does not carry all theory inline. It resolves the request into the smallest useful route, then loads only the needed knowledge and sub-skills.

## Non-Negotiables
- Route by `intent x medium x stage x output x constraints`.
- Do not rely on loose keyword matching alone.
- Do not duplicate theory from `knowledge/` into sub-skills.
- Prefer the smallest protocol that can satisfy the request.
- Ask only for missing information that changes the route or output contract.
- Always attach a brief rubric-based self-check to the final result.
- Load reality-lens atoms only when they change routing or output quality.

## Route Selection Heuristics
- Prefer exact medium matches over generic narrative reuse.
- Prefer exact output-contract matches over broad stage matches.
- Prefer diagnostic routing when the user brings existing text and asks what is wrong with it.
- Prefer one narrow protocol over a broad mixed-context answer.
- Prefer reality-grounded routes when the user asks for audience fit, commissioning fit, or writer growth strategy.

## Reality-Lens Loading Rule
Load audience, industry, history, writer-development, and platform-attention lenses only when one of these is true:
- the requested output is `audience_fit_note`, `development_brief`, or `learning_path`;
- constraints include audience segment, audience need state, commissioning context, business model, release window, platform logic, writer maturity, or reference bar;
- the current draft fails because audience promise and delivery are misaligned.

Keep lens loading bounded: select only the linked atoms required by the chosen protocol.

## Routing Steps
1. Classify the request:
   - `intent`: discover, design, draft, polish, diagnose, adapt
   - `medium`: feature_film, episodic, short_drama, animation, commercial, branded_film, shortform_video, game_narrative, branching_interactive
   - `stage`: ideation, premise, character, structure, outline, scene, dialogue, rewrite, adaptation
   - `output`: one of the public contracts in [`references/supported-outputs.md`](references/supported-outputs.md)
   - `constraints`: duration, audience segment, audience need state, platform, release window, commissioning context, business model, rating, budget, interactivity, franchise/IP limits, writer maturity, reference bar
2. Look up the preferred route in [`references/router-matrix.json`](references/router-matrix.json).
3. Load:
   - one primary workflow protocol;
   - one primary skill wrapper;
   - the linked atoms required by the protocol;
   - the rubric that governs the requested output.
4. If the request is underspecified, ask only for the minimum missing information that changes the route or output contract.
5. Produce the requested artifact and a compact self-check using the selected rubric.

## Output Pattern
- Return the requested artifact in the requested format.
- Add a brief rubric-based self-check or revision note when useful.
- If the user asks for teaching or explanation, anchor the answer in the relevant protocol and atom references.

## What This Skill Should Prevent
- loading unrelated theory just because it exists in the repo;
- answering a commercial brief as if it were a feature outline;
- flattening interactive branching into ordinary linear plotting;
- giving rewrite advice without identifying the failure layer first;
- giving craft advice detached from audience demand and production context.

## Default Output Contracts
- `logline`
- `premise`
- `synopsis`
- `treatment`
- `beat_sheet`
- `outline`
- `scene_card`
- `scene_draft`
- `dialogue_polish`
- `rewrite_report`
- `commercial_script`
- `interactive_branch_map`
- `audience_fit_note`
- `development_brief`
- `learning_path`

## Sub-Skills
- [`skills/idea-discovery/SKILL.md`](skills/idea-discovery/SKILL.md)
- [`skills/logline-premise/SKILL.md`](skills/logline-premise/SKILL.md)
- [`skills/character-world/SKILL.md`](skills/character-world/SKILL.md)
- [`skills/structure-beat/SKILL.md`](skills/structure-beat/SKILL.md)
- [`skills/scene-writing/SKILL.md`](skills/scene-writing/SKILL.md)
- [`skills/dialogue-subtext/SKILL.md`](skills/dialogue-subtext/SKILL.md)
- [`skills/rewrite-doctor/SKILL.md`](skills/rewrite-doctor/SKILL.md)
- [`skills/commercial-script/SKILL.md`](skills/commercial-script/SKILL.md)
- [`skills/interactive-branching/SKILL.md`](skills/interactive-branching/SKILL.md)
- [`skills/genre-adaptation/SKILL.md`](skills/genre-adaptation/SKILL.md)
- [`skills/audience-insight/SKILL.md`](skills/audience-insight/SKILL.md)
- [`skills/development-strategy/SKILL.md`](skills/development-strategy/SKILL.md)
- [`skills/writer-development/SKILL.md`](skills/writer-development/SKILL.md)

## Primary References
- [`references/taxonomy.md`](references/taxonomy.md)
- [`references/routing-policy.md`](references/routing-policy.md)
- [`references/id-policy.md`](references/id-policy.md)
- [`docs/content-model.md`](docs/content-model.md)
- [`docs/reality-lenses.md`](docs/reality-lenses.md)
- [`docs/source-map-real-world.md`](docs/source-map-real-world.md)

## Operating Principle
Resolve the route first. Load the minimum context second. Generate third. Self-check last.
