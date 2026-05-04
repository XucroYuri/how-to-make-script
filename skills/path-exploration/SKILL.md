---
name: path-exploration
description: Use when the user should see multiple viable creative paths before converging to one route.
---

# Path Exploration

Use this skill to keep screenplay development from collapsing into one answer too early.

## Workflow
1. Lock the non-negotiable part of the brief.
2. Generate 2-5 genuinely different candidate paths, depending on how wide the task really is.
3. State what each path optimizes, sacrifices, and assumes.
4. Return `path_options` with convergence triggers.

## Output Contract
- `path_options`: contrasted creative paths with tradeoffs, fit notes, and convergence triggers.
- Paths must be meaningfully different, not cosmetic rewrites of the same direction.
- Explain why more than one route remains valid at this stage.

## Posture-Adaptive Guidance

**When `certainty = exploring`:**
Primary activation context. Generate 2-5 genuinely different paths. State what each path optimises, sacrifices, and assumes. Explain why more than one route remains valid.

**When `certainty = lost`:**
Do not generate five paths. Ask: "Which direction feels most alive to you right now, even if it's wrong?" One path that excites is better than five paths that don't. Let the writer pick the wrong one confidently.

**When `certainty = certain`:**
Path exploration is unusual when certainty is high. If routed here, the user is testing their certainty, not escaping it. Surface the strongest counterargument to their chosen path before validating it.

**When `source = discover`:**
Primary activation context. Keep paths loose and sensory: "Path A feels like a pressure cooker. Path B feels like a long walk that turns into a sprint." Make the trade-offs felt, not just listed.

**When `source = construct`:**
Make the trade-offs structural: what must be true about the outline for each path to work? Convergence triggers should be specific enough to use as design gates.

## References
- `wp.path-options`
- `ka.creative-pluralism`
- `ka.divergence-convergence-loop`
- `rb.path-options`
