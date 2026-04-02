# Failure Case Archive

This directory documents cases where the skill system produced suboptimal results despite correct routing.

## Purpose

- Preserve institutional memory of creative failures
- Feed counterexamples back into rubrics and protocols
- Prevent the knowledge base from becoming anechoic (only hearing successes)

## Format

Each failure case follows this structure:

```markdown
## Case: [id]

**Protocol used:** wp.xxx
**Skill used:** skill.xxx
**What went wrong:** [description]
**Root cause:** [why the protocol/rubric didn't prevent it]
**Correction:** [what was changed or should be changed]
**Status:** open | addressed | superseded
```

## Naming Convention

- `fail-001-xxx.md` — sequential numbering
- One failure per file
- Tag with protocol, skill, and failure category

## Failure Categories

- `premise_drift` — output lost the original premise's pressure source
- `voice_collapse` — all characters sounded the same
- `missing_parenthetical` — dialogue was delivered without any playable performance carrier
- `av_cue_omission` — needed `VFX` / `SFX` / `BGM` signals were dropped or scattered into freeform notes
- `mechanical_language_contamination` — writerly / LLM phrasing polluted downstream drafting stages
- `cross_artifact_naturalness_drift` — upstream and downstream artifacts broke naturalness consistency
- `false_structure` — structure looked correct but lacked dramatic escalation
- `audience_mismatch` — technically correct but missed the target audience
- `context_overload` — too much loaded context diluted the output quality
- `handoff_loss` — information lost between protocol transitions
