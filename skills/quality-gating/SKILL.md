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

## References
- `wp.quality-gate-report`
- `ka.contract-first-quality-gating`
- `ka.adaptive-quality-lens-selection`
- `ka.review-lens-isolation`
- `ka.hard-gate-soft-score-separation`
- `rb.quality-gate-report`
