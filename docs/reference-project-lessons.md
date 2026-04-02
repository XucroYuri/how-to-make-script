# Reference Project Lessons

This document records what this repository is learning from adjacent creative-agent projects.

The goal is not to copy those repos.
The goal is to extract durable design lessons that strengthen screenplay-agent work.

## Reference 1: InkOS

Source:
- [Narcooo/inkos](https://github.com/Narcooo/inkos)

High-value lessons:
- split long-horizon control documents from runtime compilation artifacts;
- compile inputs before writing instead of silently stuffing prompts;
- keep runtime traces inspectable;
- treat rules as a layered stack, not one flat instruction blob;
- keep human-readable intent notes separate from machine-facing state.

What this repo should absorb:
- stronger packet and surface thinking for future runtime layers;
- explicit distinction between long-term intent and current focus;
- inspectable packet assembly for high-value writing and review actions.

What this repo should not absorb directly:
- novel-specific word-count governance;
- chapter-oriented CLI command surfaces as-is;
- genre-specific novel telemetry that does not transfer cleanly to screenplay work.

## Reference 2: OpenWrite Skill

Source:
- [LiPu-jpg/Openwrite_skill](https://github.com/LiPu-jpg/Openwrite_skill)

High-value lessons:
- split long-horizon planning and drafting into separate entrypoints;
- require explicit handoff when planning assets are mature enough to write from;
- keep `src/` truth separate from `data/` runtime and mirrors;
- assemble canonical packets instead of relying on invisible context;
- expose context inspection and packet export for debugging and trust.

What this repo should absorb:
- clearer phase entrypoints for planning, drafting, review, and export;
- stronger source-of-truth vs runtime-state doctrine;
- explicit handoff gates between planning and drafting surfaces.

What this repo should not absorb directly:
- novel-specific hierarchy and chapter folder conventions;
- style-extraction pipelines that assume long-form prose as the primary target;
- one-to-one naming or command structure from Goethe/Dante.

## Reference 3: Short Drama

Source:
- [0xsline/short-drama](https://github.com/0xsline/short-drama)

High-value lessons:
- domain-specific workflows get stronger when stage-to-artifact mapping is explicit;
- command-to-artifact mapping reduces ambiguity in production pipelines;
- quality self-check, compliance review, and export deserve their own named surfaces;
- mode switching for overseas formatting and market adaptation should be explicit;
- short-drama workflows benefit from rhythm, hook, monetization, and compliance scaffolding.

What this repo should absorb:
- stronger artifact ladders for medium-specific workflows;
- clearer review, compliance, and export surfaces;
- better support for short-drama-specific production design without flattening everything into feature norms.

What this repo should not absorb directly:
- hard-coded hook ratios, paywall ratios, or genre presets as universal screenplay truth;
- platform- or market-specific compliance assumptions as repo-wide law;
- a short-drama command surface as the default for all screenplay work.

## Reference 4: Shanyin Screenwriting Master

Source:
- [Shanyin-ai/shanyin-screenwriting-master](https://github.com/Shanyin-ai/shanyin-screenwriting-master)

High-value lessons:
- separate format-specific process logic instead of pretending ultrashort, short, feature, and series work all scale from the same prompt shape;
- track outer plot rhythm and inner emotional rhythm as related but distinct waves;
- use memory checkpoints to preserve long-form continuity without defaulting to full-context reload;
- lock series container variables and arc budgets before spending major turns, reveals, and relationship jumps.

What this repo should absorb:
- a first-class continuity-compression surface rather than ad hoc “reload the whole draft” behavior;
- stronger serial-container and arc-budget logic in structure planning;
- explicit dual-track rhythm language for diagnosing why a draft feels busy but emotionally static, or intimate but dramatically stalled.

What this repo should not absorb directly:
- one giant integrated screenplay prompt as the main source of truth;
- hidden internal self-check loops that are not observable as protocols, rubrics, or artifacts;
- opaque packaged outputs whose editable source and machine-facing bundle can drift out of sync.

## Local Design Changes Motivated By These Repos

The repo now treats these as explicit design needs:
- `project_surface_map` as a first-class output;
- `story_memory_checkpoint` as a first-class long-horizon continuity output;
- source-of-truth vs runtime-state separation;
- canonical packet assembly;
- explicit phase entrypoints and handoffs;
- review and export surfaces as named workflow surfaces.
- format-aware structure scaling, dual-track rhythm, and serial arc budgeting instead of one universal outline heuristic.

## Non-Dogma Rule

External reference projects are evidence of useful workflow shapes, not proof that one creative-agent architecture is universally correct.

This repo should keep extracting:
- what generalizes;
- what stays medium-bound;
- what stays tool-bound;
- what should remain only as a case reference.
