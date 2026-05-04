# Posture-Weighted Atom Loading

Knowledge atoms now carry a `posture_relevance` field that enables the skill to load atoms in priority order based on the writer's current creative posture, rather than loading a flat bundle.

## Why This Matters

A fixed loading bundle treats all atoms as equally relevant at all times. A writer who is stuck and can't find an entry point does not need the same atoms as a writer who is drafting scene seven of a locked outline. Loading the wrong atoms at the wrong time adds noise instead of signal.

## The Three Axes

Each atom scores itself across three independent axes:

### Axis 1: Source Mode
How the writer is getting creative input right now.

| Value | Writer state |
|-------|-------------|
| `discover` | Exploring a vague feeling; story feels like it already exists and needs to be found |
| `construct` | Actively designing structure; working toward a specific planned output |
| `generate` | Setting conditions and watching what emerges; willing to be surprised |

### Axis 2: Certainty Mode
How confident the writer is about the current direction.

| Value | Writer state |
|-------|-------------|
| `certain` | Knows where they are going; needs execution precision |
| `exploring` | Comparing directions; actively choosing between paths |
| `lost` | Creative block; stuck, blank, or overwhelmed |

### Axis 3: Attention Focus
Which narrative layer the writer's attention is on right now.

| Value | Writer focus |
|-------|-------------|
| `character` | Character psychology, motivation, relationships, voice |
| `world` | World rules, consistency, setting, internal logic |
| `event` | Plot sequence, causality, beats, turns |
| `audience` | Viewer experience, retention, emotional arc |
| `language` | Dialogue, subtext, verbal rhythm, register |

## Relevance Levels

Each axis entry uses one of five levels:

| Level | Loading behaviour |
|-------|------------------|
| `primary` | Load first; this atom is the highest-value resource in this posture state |
| `high` | Load early in the bundle |
| `medium` | Load in the middle; useful but not the priority |
| `low` | Load only if context budget allows |
| `suppress` | Do not load; this atom would add noise rather than signal in this posture state |

## How the Skill Uses This

1. Detect the writer's current posture (see `SKILL.md` Posture Sync section).
2. For each candidate atom in the chosen route's focus pack, compute a composite relevance score across all three active axes.
3. Sort atoms by score: `primary` > `high` > `medium` > `low`; exclude `suppress`.
4. Load in that order, stopping when the context budget is reached.

## Composite Scoring Rule

When a specific posture state is active (e.g., `source=discover`, `certainty=lost`, `focus=character`), each atom's score is derived as follows:

- **Primary match on any axis** adds the most weight.
- **Suppress on any axis** overrides and removes the atom regardless of other scores.
- **Mixed signals** (e.g., `high` on source, `low` on certainty) produce a weighted average.

The exact weighting is left to the consuming agent's implementation; the `posture_relevance` field provides the raw per-axis signals.

## Example

For a writer who is **stuck** (`certainty=lost`) and focused on **character** (`focus=character`), the `ka.story-goal` atom scores:

```json
"certainty": { "lost": "primary" },
"focus":     { "character": "high" }
```

This places `story-goal` near the top of the loading queue — exactly the right primitive to help a blocked writer reconnect with what the character actually wants.

Meanwhile, `ka.bounded-context-loading` scores:

```json
"certainty": { "lost": "suppress" }
```

This removes it from the bundle entirely — a writer in crisis does not need meta-level loading theory.

## Schema

The field is optional. Atoms without `posture_relevance` receive neutral treatment (loaded by default route priority, not suppressed). All posture atoms (`ka.creative-posture-*`) do not carry this field as they are always loaded during the Posture Sync step regardless of posture state.
