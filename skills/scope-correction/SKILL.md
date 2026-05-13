---
name: scope-correction
description: 当受到质疑的剧本主张应被收窄、限定或拆分而非作为普适原则辩护时使用。
---

# Scope Correction

Use this skill when a rule, rubric, route, or knowledge claim has been challenged and the right move is to narrow it, not to pretend it still applies everywhere.

## Workflow
1. Identify the exact challenged claim or route.
2. Preserve the smallest surviving core.
3. Name the failure context, boundary condition, or counterexample.
4. Return `scope_correction` with revised scope, rival-path note if needed, and downstream update implications.

## Output Contract
- `scope_correction`: a narrowed statement that keeps the valid core, names where it breaks, and explains what else in the repo should change.
- Do not replace one universal with its opposite mirror-universal.
- If no surviving core exists, say so explicitly and escalate to full replacement instead of faking a scope correction.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What is the narrowest version of the claim that you still believe is true?" One surviving core is enough to begin. Do not attempt a full scope correction until that narrow claim is articulated.

**When `certainty = exploring`:**
Primary activation context. Surface both the valid core and the counterexample cleanly. The most useful scope correction leaves the writer with something more precise, not something more complicated.

**When `source = construct`:**
Apply the full workflow: identify challenged claim → preserve smallest surviving core → name failure context and boundary condition → return revised scope with downstream update implications.

**When `source = discover`:**
Treat scope correction as a discovery: "What is this rule actually good for?" Let the counterexample lead to a smaller, truer claim rather than forcing a premature conclusion.

**When `focus = event`:**
Event-layer scope corrections most often involve structure claims that are medium-specific being applied universally. Anchor the correction to the specific medium and stage where the rule holds.

## References
- `wp.scope-correction`
- `rb.scope-correction`
- `ka.boundary-first-guidance`
- `ka.creative-pluralism`
- `ka.cross-protocol-referral-edges`
- `ka.false-universal-warning`
- `ka.scope-correction`
