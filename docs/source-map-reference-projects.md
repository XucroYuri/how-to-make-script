# Source Map: Reference Creative-Agent Projects

This file records the external project sources used to refine this repository's design.

## 1. InkOS

Source:
- [Narcooo/inkos](https://github.com/Narcooo/inkos)

Observed signals:
- GitHub README shows separate long-term control documents such as `story/author_intent.md` and `story/current_focus.md`, plus runtime artifacts like `intent.md`, `context.json`, `rule-stack.yaml`, and `trace.json`.
- The README also describes compiling inputs before writing and keeping packet traces inspectable.

Inference:
- screenplay-agent systems benefit from separating long-term creative truth from per-task runtime compilation;
- packet assembly and trace surfaces should become explicit design objects rather than invisible prompt behavior.

## 2. Openwrite Skill

Source:
- [LiPu-jpg/Openwrite_skill](https://github.com/LiPu-jpg/Openwrite_skill)

Observed signals:
- GitHub README separates `Goethe` as the planning surface and `Dante` as the drafting surface.
- The README distinguishes `src/` truth from `data/` runtime and mirrors, and documents canonical packet assembly plus context inspection/export.

Inference:
- screenplay systems benefit from clearer phase entrypoints and explicit planning-to-drafting handoffs;
- a repo like this should expose project-surface design and packet assembly as first-class concepts, not just hidden implementation details.

## 3. Short Drama

Source:
- [0xsline/short-drama](https://github.com/0xsline/short-drama)

Observed signals:
- GitHub README maps each major step to a named artifact or command surface, from project start to plan, character system, episode directory, episode writing, self-check, compliance, and export.
- The README also exposes overseas mode and state tracking.

Inference:
- screenplay-agent systems benefit from stage-to-artifact mapping and explicit review/compliance/export surfaces;
- short-drama and other production-line media deserve clearer workflow surfaces instead of being flattened into a generic screenplay route.

## 4. Shanyin Screenwriting Master

Source:
- [Shanyin-ai/shanyin-screenwriting-master](https://github.com/Shanyin-ai/shanyin-screenwriting-master)

Observed signals:
- The repository ships a README plus a packaged `.skill` archive whose extracted references split guidance into `core-methodology`, `format-ultrashort`, `format-short`, `format-feature`, and `format-series`.
- The extracted materials repeatedly distinguish external plot rhythm from internal emotional rhythm, use “memory checkpoints” to carry long-form state, and ask series work to lock runtime/container parameters before allocating major turns.
- The integrated public-facing markdown surface is much larger and more overloaded than the bounded parts that are actually most transferable.

Inference:
- screenplay-agent systems benefit from a typed continuity-compression artifact rather than broad draft reload;
- serial and shortform structure design should explicitly lock the container before spending arc budget;
- the most valuable ideas inside a large creative prompt often live at the level of artifact logic, not prompt length;
- repos should separate editable source surfaces from packaged delivery surfaces so the latter do not become opaque truth.

## Adoption Rule

The repository should only absorb:
- durable architectural patterns;
- medium-relevant workflow ideas;
- explicit state, packet, and review concepts.

It should not absorb:
- tool-bound command syntax as universal workflow law;
- medium-specific ratios, presets, or compliance rules as global truth;
- product branding or persona naming as architectural necessity.
