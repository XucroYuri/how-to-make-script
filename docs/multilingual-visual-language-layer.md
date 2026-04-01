# Multilingual Visual Language Layer

This repository now treats multilingual visual language as a screenplay-adjacent capability, not as a generic prompt-engineering stunt.

The value is straightforward:
- screenwriting increasingly sits next to previz, video generation, global collaboration, and prompt-mediated production;
- many failures happen not because the scene is wrong, but because the visual intent gets translated into weak, generic, or culturally flat language;
- a screenplay agent should know when it needs a controlled visual-language pack instead of a full rewrite.

## What This Layer Adds

The layer is built around five practical ideas:

- not every task needs a full vocabulary table;
- different languages carry different useful densities for shot, lighting, mood, and aesthetic signaling;
- cultural-aesthetic concepts should only be used when they change executable choices;
- hybrid phrasing is often better than fake purity;
- a vocabulary pack should help execution, not perform expertise.

## Languages Currently Anchored

- Chinese: high-density shot, lighting, and production shorthand.
- Japanese: strong aesthetic and pause-oriented concepts for atmosphere and restraint.
- Korean: sharp support for melodrama, MV cadence, and contemporary screen energy.
- Russian: strong support for montage, poetic duration, documentary gravity, and melancholy textures.
- Spanish: strong support for warm visuality, magical realism, and emotionally charged scene color.

## Design Boundary

This is not a license to stuff multilingual terms into every answer.

Use the layer only when one of these is true:
- the user explicitly wants multilingual film vocabulary;
- the task involves cross-language collaboration;
- the scene must be translated into a visual brief for downstream generation or previz;
- the aesthetic contract is difficult to express cleanly in the current working language alone.

## Related Assets

- `visual_language_pack`
- `ka.multilingual-visual-vocabulary`
- `ka.cultural-aesthetic-registers`
- `ka.prompt-delegation-levels`
- `wp.visual-language-pack`
- `rb.visual-language-pack`

