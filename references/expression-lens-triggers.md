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
  - `ka.verbal-rhythm`
  - `ka.cinematic-prose-register` (scene_draft only)
- `commercial_script`
  - `ka.register-adaptation`
  - `ka.embodied-text-pressure`
  - `ka.verbal-rhythm`
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

## "Writerly Substitution" Operational Indicators

When the expression_integrity lens flags "writerly substitution", look for these concrete textual patterns:

1. **Symmetric sentence structure**: Characters in different emotional states produce syntactically identical sentences.
2. **Vocabulary uniformity across characters**: A street-smart teenager and a retired professor use the same word choices.
3. **Balanced clause construction**: Every line has a setup and payoff within the same sentence, like essay paragraphs. Real speech is often fragmented.
4. **Emotion label substitution**: "感到悲伤" / "有些失落" / "心中一紧" instead of actions, pauses, or topic shifts that SHOW the emotion.
5. **Explanation bridges**: Lines whose only function is making the audience understand motivation, spoken in a narrator-voice.
6. **Rhetorical completeness**: No sentence fragments, no trailing off, no repetition from hesitation. The dialogue is "well-formed" in a way real speech never is.

## Chinese Natural-Language Self-Check Points

When the output language is Chinese, add these checks on top of the six writerly substitution indicators:

1. **Four-character idiom overload（四字词语堆砌）**: Scenes or dialogue dense with 四字格、成语、书面短语 where spoken Chinese would use shorter, more direct language. If a character says things like 不由自主地、毫不犹豫地、情不自禁地、义无反顾地, the text reads like a translation, not a person.
2. **Emotion-label sentencing（情绪标签句）**: Lines that announce feelings through adjectives or noun phrases instead of actions: 感到一阵悲伤、心中涌起暖意、脸上浮现出失落的表情. Replace with what the camera can film or what the pause/silence conveys.
3. **Explanatory bridge lines（解释性过渡句）**: Sentences whose only job is making the audience understand motivation, spoken in narrator-register: 之所以这样做，是因为我太在乎你了. Real people under pressure do not narrate their own motivations in balanced subordinate clauses.
4. **Symmetric parallelism（对仗式对白）**: Two characters in conflict produce syntactically mirrored sentences: A says 我不想让你受到伤害, B replies 我也不想让你为我担心. Real conflict breaks symmetry.
5. **Register mismatch（语域错位）**: A street-smart teenager, a village elder, and a corporate lawyer all use the same sentence structure and vocabulary. Each character should carry their social position, education, and dialect range into word choice, sentence length, and topic preference.
6. **Complete-sentence disease（完整句病）**: Every line is a grammatically complete sentence with no fragments, no trailing off, no interrupted thoughts. Real spoken Chinese is full of omissions, topic drops, and sentences that end before they finish.

**Hard fail rule**: If three or more of these patterns appear in the same dialogue passage, the text fails expression_integrity and must be rewritten before proceeding.

## Guardrail

The expression lens is not a style template engine.
It should preserve a voice anchor, a register envelope, and a variability budget at the same time.
