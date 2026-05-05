---
name: quality-gating
description: Use when the user needs an adaptive screenplay quality gate, targeted audit, preflight check, or recheck plan rather than a normal rewrite diagnosis.
---

# Quality Gating

Use this skill when the request is primarily about checking, gating, preflighting, or rechecking an artifact.

## Workflow
1. Lock the target contract, medium, and audit scope first.
2. Apply the target artifact's native rubric or contract gate first.
3. Select the smallest useful lens stack for the artifact family.
4. Keep each review lens bounded and independent.
5. Separate hard fails from weighted weaknesses.
6. Return `quality_gate_report` with correction ladder and recheck logic.

## Output Contract
- `quality_gate_report`: adaptive audit report with selected lenses, hard fails, weighted weaknesses, correction priorities, and optional recheck plan.
- Use this instead of `rewrite_report` when the user needs multi-lens checking, stage-specific audit, preflight, industrial acceptance, or recheck.
- Keep the audit scoped; do not default to a fixed universal checklist.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Do not run a quality gate. Ask: "What are you most worried is wrong?" A single fear is a better entry point than a full audit checklist. Route to `rewrite-doctor` or `scope-correction` if the worry is more diagnostic than verificatory.

**When `certainty = certain`:**
Primary activation context. Apply the full workflow: lock target contract → apply native rubric → select smallest lens stack → separate hard fails from weighted weaknesses → return correction ladder with recheck logic.

**When `certainty = exploring`:**
Run a targeted lens only, not a full audit. Focus on the one lens most likely to determine whether the current direction is worth developing further.

**When `source = construct`:**
Gate against the output contract strictly. Hard fails are non-negotiable. Weighted weaknesses should have explicit correction priorities, not open-ended suggestions.

**When `focus = audience`:**
Audience experience is a valid quality lens but is suppressed in quality-gating unless the output contract is explicitly `audience_fit_note`. Use the audience lens to surface dropout risk and hook strength, not as a general quality proxy.

## References
- `wp.quality-gate-report`
- `rb.quality-gate-report`
- `ka.adaptive-quality-lens-selection`
- `ka.causality-chain`
- `ka.contract-first-quality-gating`
- `ka.hard-gate-soft-score-separation`
- `ka.metrics-handoff-compression`
- `ka.review-lens-isolation`
- `ka.targeted-recheck-loop`
