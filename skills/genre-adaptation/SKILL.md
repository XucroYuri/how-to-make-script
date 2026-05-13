---
name: genre-adaptation
description: 需要将故事调整为另一种类型、媒介或受众承诺时使用。
---

# Genre Adaptation

Use this skill to preserve the engine while changing the promise surface.

## Pre-Adaptation Extraction

When the source material is not already a screenplay or structured story document, extract a dramatic premise before entering adaptation workflow. This step is **not** adaptation — it is premise-finding from unstructured source material.

- **When source is non-narrative**（novel, essay, song lyrics, painting, news article）: extract the dramatic premise first（protagonist + goal + obstacle + stakes). Do not skip directly to adaptation decisions before the dramatic engine is clear.
- **When source is a poem**: identify emotional rhythm and imagery as potential dramatic anchors. Poems rarely contain explicit protagonists or goals — let the emotional movement and sensory imagery suggest where dramatic tension might live.
- **When source is news**: identify the human conflict behind the facts. News reports events; drama needs desire, fear, and institutional pressure. Extract the human story beneath the headline, not the headline itself.
- **When source has no identifiable premise**（abstract poem, purely conceptual prose, atmospheric artwork）: say so honestly. Do not manufacture a false dramatic premise to fill a gap. Offer `path_options`:
  - Try a different entry point（e.g., pick one image or moment from the source and build outward）
  - Ask the user for a character or situation to anchor the adaptation
  - Flag that the source may work better as a tonal reference than as a narrative source

Once a premise is extracted（or the impossibility is honestly flagged）, proceed to the adaptation workflow below.

## Workflow
1. Identify the non-negotiable core.
2. Map the target genre or medium promises.
3. Rewrite only the layers required to satisfy the new promise.
4. If the source depends on a recognizable voice, lock continuity anchors before rewriting surface language.

## Output Contract
- Preserve the original engine unless the request explicitly asks for a deeper rewrite.
- Change the surface promise only as far as the target genre or medium requires.
- Call out what stays fixed and what must be rewritten.
- When adapting known IP or a strong persona, continuity lives in voice logic, not in quote imitation.

## Posture-Adaptive Guidance

**When `certainty = lost`:**
Ask: "What is the one thing in the original that you refuse to lose, no matter what?" The answer is the non-negotiable core. Everything else is negotiable until that is named.

**When `source = discover`:**
Surface the engine first: what makes this story run, independent of its genre surface? Adaptation decisions follow from engine clarity, not from genre checklists.

**When `source = construct`:**
Apply the full workflow: identify non-negotiable core → map target genre promises → rewrite only the layers required → lock continuity anchors before touching surface language.

**When `focus = world`:**
Genre adaptation often requires world-rule translation. What world-logic works in the source genre but breaks under the target genre's physical or social rules?

**When `focus = character`:**
Voice continuity is the highest-risk surface in adaptation. Lock the voice anchors before rewriting any lines.

## References
- `wp.genre-adaptation`
- `rb.outline`
- `ka.cross-protocol-referral-edges`
- `ka.genre-action`
- `ka.genre-comedy`
- `ka.genre-family`
- `ka.genre-horror`
- `ka.genre-pack-factorization`
- `ka.genre-romance`
- `ka.genre-satire`
- `ka.genre-thriller`
- `ka.genre-suspense`
- `ka.genre-wuxia`
- `ka.medium-branching-interactive`
- `ka.medium-commercial`
- `ka.medium-feature-film`
