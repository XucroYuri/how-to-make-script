# Expression Lens Policy

The repository now treats language style and "alive" character expression as a first-class layer, but not as a universal route.

That distinction matters. If every request loads voice and style assets by default, the repo will drift back toward context stuffing and generic style talk. If style is never made explicit, the agent will keep producing competent but bloodless drafts.

The right middle path is:
- add an explicit `voice_style_guide` output for direct calibration requests;
- allow normal drafting routes to load a small expression lens only when the request or draft actually needs it.

That does not mean every cross-language or visual-expression problem belongs to the voice layer.
If the user really needs multilingual shot language or downstream visual handoff wording, use the visual-language or video-bridge layer instead of stretching `voice_style_guide` too far.

## What The Lens Is For

The expression lens exists to help the model answer questions like:
- Why does this character sound like a writer instead of a person?
- How do I keep an existing IP voice without parroting old lines?
- How do I make premium brand language feel persuasive instead of fake-premium?
- How do I write an interactive suspect who feels evasive rather than like a functional NPC?

## What The Lens Must Preserve

Every usable expression layer should preserve four things at once:
- a voice anchor: worldview, strategy, status position, shame line, and default rhythm;
- a lived-pressure layer: what the body, situation, and risk do to language;
- a register envelope: what kinds of diction, abstraction, and polish fit this medium and what breaks it;
- a variability budget: what can change scene to scene without breaking identity.

If any of these is missing, the result usually becomes either generic advice or rigid imitation.

## Design Rule

Use `voice_style_guide` when the user explicitly wants calibration.

For ordinary drafting, keep the original route and load only the expression atoms named in [`references/expression-lens-triggers.md`](../references/expression-lens-triggers.md) when:
- the user asks for voice or register control;
- the draft feels flat, samey, writerly, fake-premium, or off-IP;
- adaptation or continuity work requires a continuity anchor before new lines can be written.

## Failure Modes To Avoid

- style adjectives without usable constraints;
- voice reduced to catchphrases;
- embodied feeling replaced by abstract emotion summaries;
- brand tone confused with generic luxury copy;
- continuity treated as imitation instead of decision-logic preservation;
- loading too many style references until the answer becomes mannered and inert.

## Operational Rule

The style layer should change writing decisions, not just descriptions of writing.

If the added expression asset does not change what words, rhythms, silences, or red flags the model can see, it is probably not worth loading.
