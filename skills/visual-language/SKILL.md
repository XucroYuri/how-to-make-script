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

## References
- `wp.visual-language-pack`
- `ka.multilingual-visual-vocabulary`
- `ka.cultural-aesthetic-registers`
- `ka.prompt-delegation-levels`
- `rb.visual-language-pack`

