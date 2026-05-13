---
name: pattern-reference
description: 需要场景特定的剧本参考包，包含成功范例、失败对比和说明时使用。
---

# Pattern Reference

Use this skill when the user asks for success patterns, reference scenes, contrastive examples, or "why this works better than that" guidance for a screenplay problem.

## Workflow
1. Classify the scenario before selecting any example.
2. Pick the closest pattern family for the current medium, stage, and problem.
3. Return one strong synthetic sample and one weaker contrast.
4. Explain the success and failure mechanisms.
5. State the boundary: this is a reference path, not the only valid path.

## Output Contract
- `pattern_reference_pack`: scenario framing, strong sample, weaker contrast, mechanism analysis, failure analysis, and non-dogma note.
- Samples should be original synthetic examples, not quotations or close imitations of specific copyrighted scripts.
- If no single pattern family dominates, return multiple reference directions instead of a fake canonical answer.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What problem are you trying to solve in this scene or beat?" One specific failure state is enough to find a useful reference pattern. Do not ask for a full scenario brief first.

**When `source = discover`:**
Lead with the failure contrast: "Here is a version that doesn't work — and here is why." The negative example often teaches faster than the positive one for writers in discovery mode.

**When `source = construct`:**
Apply the full workflow: classify scenario → pick pattern family → strong sample → weaker contrast → mechanism analysis → non-dogma boundary note.

**When `focus = event`:**
Pattern references are most useful for event-layer problems: opening hooks, midpoint turns, reveal mechanics, escalation logic. Load the scenario-factorization atom first.

**When `focus = language`:**
For language-layer problems, show voice rather than structure. A reference that demonstrates register, rhythm, and subtext is more useful than a beat-structure sample.

## References
- `wp.pattern-reference-pack`
- `rb.pattern-reference-pack`
- `ka.creative-pluralism`
- `ka.cross-protocol-referral-edges`
- `ka.false-universal-warning`
- `ka.reference-pattern-usage`
- `ka.scenario-factorization`
