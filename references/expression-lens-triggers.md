# Expression Lens Triggers

This file defines when voice and expression assets should be loaded as a bounded adjunct, instead of being treated as the default for every route.

## Direct Route

Prefer `voice_style_guide` when the user explicitly asks for:
- language style calibration;
- character voice separation;
- IP or franchise voice continuity;
- stronger "alive", "human", "embodied", or "non-writerly" expression;
- brand tone that should persuade without sounding like a pasted ad voice.

## Adjunct Triggers

Keep the primary route unchanged, but load the expression lens when the request stays in `scene_draft`, `dialogue_polish`, `commercial_script`, or adaptation outputs and one of these is true:
- constraints include `voice_target`;
- constraints include `language_register`;
- constraints include `ip_continuity`;
- constraints include `experiential_depth`;
- the draft fails because all characters sound alike;
- the draft feels writerly, fake-premium, NPC-like, or off-model for the target IP.

## Minimal Lens Bundles

- `scene_draft` or `dialogue_polish`
  - `ka.character-voice-consistency`
  - `ka.embodied-text-pressure`
  - `ka.dialogue-subtext`
- `commercial_script`
  - `ka.register-adaptation`
  - `ka.embodied-text-pressure`
  - the relevant medium atom
- `adaptation`
  - `ka.ip-voice-continuity`
  - `ka.character-voice-consistency`
  - `ka.register-adaptation`

## Stop Rules

Stop expanding the expression lens when:
- the guide already changes line choice, rhythm, and red-flag detection;
- the next asset would only add more adjectives instead of more constraints;
- the route would be better served by `audience_fit_note`, `development_brief`, or `pattern_reference_pack`.

## Guardrail

The expression lens is not a style template engine.
It should preserve a voice anchor, a register envelope, and a variability budget at the same time.
