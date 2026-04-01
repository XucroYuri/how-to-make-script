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

## References
- `wp.screen-to-video-brief`
- `ka.screenplay-to-video-boundary`
- `ka.video-generation-shot-economy`
- `ka.prompt-delegation-levels`
- `ka.source-span-traceability`
- `ka.long-script-batch-planning`
- `ka.visible-asset-grounding`
- `rb.screen-to-video-brief`
