---
name: screen-to-video-bridge
description: Use when the user needs to translate screenplay material into a bounded, generation-ready or previz-ready video brief.
---

# Screen To Video Bridge

Use this skill when the user wants to turn a scene, ad beat, or adaptation fragment into a `screen_to_video_brief`.

Typical cases:
- bridge a scene into a Sora / Seedance / generic video-generation brief;
- prepare a previz-facing visual brief without flattening the original screenplay;
- split a scene into clip-sized units with invariants and control intensity;
- preserve dramatic intent while adapting to short clip duration and execution limits.

## Workflow
1. Identify the source container: scene draft, scene card, ad beat, or adaptation fragment.
2. Preserve source spans or evidence anchors whenever possible.
3. Extract the dramatic function and minimum non-negotiable beats.
4. Decide whether the work should stay one clip or be split into a clip chain.
5. For long material, batch by structure first, not by arbitrary chunk size.
6. Choose one main action and one main camera logic per clip.
7. Return a layered brief with invariants, avoid rules, grounded visible assets, and runtime-specific notes only when they materially matter.

## Output Contract
- `screen_to_video_brief`: a bounded bridge document with source-scene intent, clip structure, shot/action logic, invariants, avoid items, and runtime-facing notes.
- The brief should not replace the screenplay.
- Tool details belong only when they change execution decisions.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What is the single most important visual moment in this material — the one image that cannot be lost in translation?" One anchor image is enough to build the brief. Do not ask for a full source summary.

**When `source = construct`:**
Primary activation context. Apply the full workflow: identify source container → preserve source spans → extract dramatic function → decide clip vs. clip chain → choose main action and camera logic per clip → return layered brief with invariants and avoid rules.

**When `certainty = certain`:**
Apply full output contract strictly. The brief must not replace the screenplay. Tool-specific details belong only when they change execution decisions materially.

**When `focus = world`:**
Visual grounding in world-specific assets (locations, objects, light qualities) is the primary concern. Invariants should include world-consistent visual markers, not just character appearance.

**When `focus = audience`:**
The downstream execution audience — model prompt consumer or previz team — is the real audience here. Calibrate specificity to what they need to make decisions, not to what is interesting about the source.

## References
- `wp.screen-to-video-brief`
- `rb.screen-to-video-brief`
- `ka.cross-protocol-referral-edges`
- `ka.long-script-batch-planning`
- `ka.multilingual-visual-vocabulary`
- `ka.prompt-delegation-levels`
- `ka.screenplay-to-video-boundary`
- `ka.source-span-traceability`
- `ka.video-generation-shot-economy`
- `ka.visible-asset-grounding`
