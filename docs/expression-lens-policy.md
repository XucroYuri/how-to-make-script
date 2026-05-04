# Expression Lens Policy

Language style and "alive" character expression is a first-class layer in this repository, but not a universal route. If every request loads voice and style assets, the repo drifts toward context stuffing and generic style talk. If style is never made explicit, the agent produces competent but lifeless drafts.

The right balance: add a `voice_style_guide` output for direct calibration requests. For normal drafting, load a small expression lens only when the request or draft actually needs it.

## What The Lens Is For

The expression lens helps the model answer questions like:
- Why does this character sound like a writer instead of a person?
- How do I keep an existing IP voice without parroting old lines?
- How do I make premium brand language feel persuasive instead of fake-premium?
- How do I write an interactive suspect who feels evasive rather than like a functional NPC?

## When To Load The Lens

Use `voice_style_guide` when the user explicitly wants calibration.

For ordinary drafting, keep the original route and load only the expression atoms named in [`../references/expression-lens-triggers.md`](../references/expression-lens-triggers.md) when:
- The user asks for voice or register control
- The draft feels flat, samey, writerly, fake-premium, or off-IP
- Adaptation or continuity work requires a continuity anchor before new lines can be written

## What A Usable Expression Layer Must Contain

Every usable expression layer should preserve four things at once:

1. **A voice anchor** -- worldview, strategy, status position, shame line, and default rhythm
2. **A lived-pressure layer** -- what the body, situation, and risk do to language
3. **A register envelope** -- what kinds of diction, abstraction, and polish fit this medium and what breaks it
4. **A variability budget** -- what can change scene to scene without breaking identity

If any of these is missing, the result becomes either generic advice or rigid imitation.

## Failure Modes To Avoid

- Style adjectives without usable constraints
- Voice reduced to catchphrases
- Embodied feeling replaced by abstract emotion summaries
- Brand tone confused with generic luxury copy
- Continuity treated as imitation instead of decision-logic preservation
- Loading so many style references that the answer becomes mannered and inert

## Operational Rule

The style layer should change writing decisions, not just descriptions of writing. If the added expression asset does not change what words, rhythms, silences, or red flags the model can produce, it is not worth loading.
