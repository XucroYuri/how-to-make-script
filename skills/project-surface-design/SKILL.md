---
name: project-surface-design
description: Use when the user needs a long-running screenplay project surface design with source-of-truth, runtime state, packet assembly, review surfaces, and export surfaces.
---

# Project Surface Design

Use this skill when the user asks how a screenplay project should persist state, separate editable truth from runtime artifacts, expose phase entrypoints, or assemble inspectable packets for writing and review.

## Workflow
1. Identify the medium, phase pressure, and collaboration shape.
2. Separate canonical source from runtime state.
3. Define entrypoints, handoffs, packet assembly, review surfaces, and export surfaces.
4. State sync rules and human-edit policy explicitly.
5. Return a map that can support long-running work without silent drift.

## Output Contract
- `project_surface_map`: source-of-truth artifacts, runtime surfaces, phase entrypoints, canonical packet layers, review surfaces, export surfaces, sync rules, drift risks, and future runtime hooks.
- Keep the map medium-aware. A short-drama production line is not the same as a feature development workspace.
- Prefer explicit human-edit policy over silent assumptions.

## References
- `wp.project-surface-map`
- `ka.source-of-truth-runtime-split`
- `ka.canonical-packet-assembly`
- `ka.phase-entrypoint-handoff`
- `ka.command-artifact-mapping`
- `rb.project-surface-map`
