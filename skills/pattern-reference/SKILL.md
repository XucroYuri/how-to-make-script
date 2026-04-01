---
name: pattern-reference
description: Use when the user wants a scenario-specific screenplay reference pack with a strong sample, failure contrast, and explanation.
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

## References
- `wp.pattern-reference-pack`
- `ka.reference-pattern-usage`
- `ka.creative-pluralism`
- `rb.pattern-reference-pack`
