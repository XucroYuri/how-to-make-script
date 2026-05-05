---
name: logline-premise
description: Use when the user needs a clear logline or premise for a narrative script idea.
---

# Logline Premise

Use this skill when the story engine exists but needs compression and clarity.

## Workflow
1. Lock protagonist, goal, obstacle, and stakes.
2. Check whether the current sentence is a real story engine or only a polished concept shell.
3. Remove abstract filler.
4. Return a one-line logline and a short premise.

## Output Contract
- `logline`: one sentence that carries protagonist, pressure, stakes, and motion.
- `premise`: a compact paragraph that makes the story engine legible for development.
- Prefer concrete nouns and active verbs.
- If the current idea is still a false logline, rewrite the engine before polishing the sentence.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "Who is most trapped by this situation — and what do they want out of it that they can't have?" One character under pressure is the engine. Do not ask about genre or structure yet.

**When `source = discover`:**
Do not optimise the sentence first. Surface the engine: "What force is pushing this character toward a decision they cannot avoid?" Once the engine is clear, compression follows naturally.

**When `source = construct`:**
Apply the full workflow: protagonist → goal → obstacle → stakes. Check whether the current sentence is a real story engine or a polished concept shell. Remove abstract filler.

**When `certainty = exploring`:**
Offer two logline versions: one that foregrounds external pressure, one that foregrounds internal contradiction. State what each version implies about the story's engine.

**When `focus = character`:**
The most useful logline question here is: "What does this character believe about themselves that the story will disprove?" Protagonist psychology is the engine, not the plot.

## References
- `wp.logline-premise`
- `rb.logline`
- `ka.causality-chain`
- `ka.conflict-pressure`
- `ka.cross-protocol-referral-edges`
- `ka.false-logline-warning`
- `ka.genre-pack-factorization`
- `ka.story-goal`
- `ka.viewer-inference-guidance`
