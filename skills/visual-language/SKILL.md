---
name: visual-language
description: Use when the user needs multilingual film vocabulary, cross-lingual shot language, or a task-specific visual language pack.
---

# Visual Language

Use this skill when the user needs a `visual_language_pack` for multilingual visual communication.

Typical cases:
- translate scene intent into Chinese / Japanese / Korean / Russian / Spanish film-language terms;
- prepare shot-language packs for cross-border teams or prompt-writing workflows;
- choose cultural-aesthetic anchors without turning them into stereotypes;
- decide whether the task needs atmosphere-level wording or more precise shot-level control.

## Workflow
1. Identify the receiving context: human crew, model prompt, style calibration, or adaptation handoff.
2. Choose the narrowest useful working language or hybrid mode.
3. Select only the term classes that matter for the task.
4. Add prompt-delegation guidance and misuse warnings.
5. Return a pack that improves execution rather than displaying vocabulary breadth.

## Output Contract
- `visual_language_pack`: a task-specific pack with chosen working language, selected film terms, hybrid anchors when useful, prompt-ready phrases, and misuse warnings.
- The pack should not be a whole dictionary.
- Cultural terms should be tied to executable visual consequences, not used as decorative labels.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What is the single image in this scene that you most want the viewer to carry away?" One target image is enough to anchor a visual vocabulary pack. Do not ask for a full locale and term-class selection.

**When `source = discover`:**
Start from atmosphere, not from terminology. "What does this world feel like at its most itself — weight, light, texture, pace?" Let the sensory description select the cultural-aesthetic anchors.

**When `source = construct`:**
Apply the full workflow: receiving context → working language → term classes → prompt-delegation guidance → misuse warnings → return task-specific pack. The pack should improve execution, not display vocabulary breadth.

**When `focus = world`:**
World-consistent visual vocabulary is the primary concern. Cultural-aesthetic anchors should reflect the world's internal rules, not just its geographic origin.

**When `focus = language`:**
Visual language and verbal register are adjacent. When language focus is active, check whether visual vocabulary is creating tonal consistency or tonal contradiction with the dialogue register.

## References
- `wp.visual-language-pack`
- `rb.visual-language-pack`
- `ka.cross-protocol-referral-edges`
- `ka.cultural-aesthetic-registers`
- `ka.multilingual-visual-vocabulary`
- `ka.prompt-delegation-levels`
- `ka.register-adaptation`
