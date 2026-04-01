---
name: scope-correction
description: Use when a challenged screenplay claim should be narrowed, scoped, or split instead of being defended as universal.
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

## References
- `wp.scope-correction`
- `ka.scope-correction`
- `ka.false-universal-warning`
- `rb.scope-correction`
