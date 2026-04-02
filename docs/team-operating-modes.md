# Team Operating Modes

This document turns real-world team patterns into reusable collaboration modes for the repository.

It does not claim that one film studio, agency, or game team represents a universal best practice. The point is narrower: identify repeatable workflow shapes from strong teams, then encode them as optional modes the root skill can select or adapt.

## Mode Selection Rule

Choose a mode by answering four questions:
- Is the project author-centered, room-centered, campaign-centered, system-centered, or continuity-centered?
- What must stay centralized, and what can safely run in parallel?
- Which artifacts need to exist before drafting accelerates?
- Which decisions must stay human-owned?

## Mode 1: Showrunner Room

Best for:
- serialized episodic drama;
- returning series with repeatable engines;
- room-heavy breaking and note circulation.

Operating shape:
- one final story owner, often a showrunner or equivalent human decision owner;
- a room captain who keeps the shared truth packet current;
- parallel lanes for season engine, episode breaks, character threads, and notes intake;
- clear gates for season lock, episode break lock, and production rewrite.

Why this mode exists:
- the WGA's staffing rules distinguish development rooms and regular writers' rooms, which implies real structural stages rather than one undifferentiated "team" state;
- current showrunner-led premium TV practice still depends on strong convergence authority, even when exploration is distributed.

Sources:
- [WGA 2023 MBA summary](https://www.wga.org/contracts/contracts/mba/summary-of-the-2023-wga-mba)
- [WGA staff size guide](https://www.wga.org/members/employment-resources/writers-deal-hub/staff-size-guide)
- [Shondaland / Bridgerton showrunner interview](https://www.shondaland.com/shondaland-series/shondaland-bridgerton-behind-the-scenes/a60702896/bridgerton-showrunner-jess-brownell/)

## Mode 2: Animation Story Trust

Best for:
- animation features;
- visually driven feature development;
- sequence-level iteration under strong peer review.

Operating shape:
- a small core team with story authority;
- repeated peer review cycles;
- research and world work feeding story rather than running separately;
- sequence packets and reel reviews instead of pure page-based iteration.

Why this mode exists:
- Disney's story trust-style peer review and research-heavy world development show a workflow where critique, visual story, and mythology refinement are inseparable.

Source:
- [Disneytoon interview on Story Trust, research, and peer review](https://thewaltdisneycompany.com/news/disneytoon-executive-on-the-animation-studio-behind-the-pirate-fairy-and-planes-fire-rescue/)

## Mode 3: Feature Development Pod

Best for:
- original features;
- prestige or indie feature development;
- projects that need concentrated authorship plus selected outside review.

Operating shape:
- small core pod: story architect, development producer, continuity or research support, human decision owner;
- short artifact ladder from premise slate to beat ladder to outline to scene packet;
- deliberate dissent retention because the team is small enough to converge too fast by accident.

Why this mode exists:
- small trusted teams are often faster for features, but only if they still preserve counterexamples and checkpoint discipline.

This mode is a synthesized pattern, not a direct one-studio copy. It combines the staffing realism of development-room thinking with manager-plus-specialist orchestration ideas from agent systems.

Sources:
- [WGA 2023 MBA summary](https://www.wga.org/contracts/contracts/mba/summary-of-the-2023-wga-mba)
- [OpenAI Agents SDK: agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)

## Mode 4: Campaign Strike Team

Best for:
- branded films;
- shortform campaign scripting;
- high-velocity multi-variant ad work.

Operating shape:
- one brand/message spine;
- fast parallel lanes for concept variants, platform adaptation, and performance review;
- explicit brand-fit and message-singularity gates before variant volume expands.

Why this mode exists:
- Wieden+Kennedy's Three "Pony" work shows cross-channel storytelling tied to one central message and social sharing mechanic;
- Google's Taxfix case shows modern creative production becoming variant-heavy, faster, and more testable, but still under human strategic control.

Sources:
- [Wieden+Kennedy: Three "Pony"](https://www.wk.com/work/three-pony/)
- [Google / Think with Google: Taxfix AI-first video production](https://business.google.com/en-all/think/search-and-video/taxfix-veo-youtube-ai-first/)

## Mode 5: Interactive Narrative Cell

Best for:
- game narrative;
- branching interactive drama;
- quest and state-heavy story work.

Operating shape:
- narrative and systems stay coupled from the start;
- branch logic, quest flow, VO/dialogue, and implementation notes run as distinct but tightly synchronized lanes;
- playability gates matter as much as story gates.

Why this mode exists:
- Ubisoft's narrative design description frames the role as cross-disciplinary and deeply tied to game design, audio, production, and quest teams;
- Story Creator Mode shows how browser tools, content hubs, and in-game execution can form one pipeline rather than separate silos.

Sources:
- [Ubisoft: What is Narrative Design?](https://news.ubisoft.com/en-gb/article/7m412GLSbfkaT0YheRYLVG/what-is-narrative-design)
- [Ubisoft: How Story Creator Mode works](https://news.ubisoft.com/en-us/article/1yMR91cFZCtrN7McYV4oeD/how-assassins-creed-odysseys-story-creator-mode-actually-works)

## Mode 6: Franchise Continuity Board

Best for:
- adaptation;
- returning IP;
- character/persona continuity-sensitive work.

Operating shape:
- continuity keeper and human decision owner are explicit, not implicit;
- canon anchors, voice guides, and continuity risk registers precede major new drafting;
- innovation is allowed, but must declare what anchor it bends and why.

Why this mode exists:
- series-based filmmaking on established worlds requires continuity decisions to be first-class, not post hoc corrections.

Source:
- [Disneytoon interview on expanding existing worlds and Story Trust](https://thewaltdisneycompany.com/news/disneytoon-executive-on-the-animation-studio-behind-the-pirate-fairy-and-planes-fire-rescue/)

## Agent-Orchestration Design Implications

The repository should not model these modes as six isolated prompt templates.

Mode selection is also not the same thing as cast selection.
After choosing a mode, the repo may still need:
- an `expert_subagent_cast` to decide which specialists and persona lenses actually enter;
- a `subagent_dispatch_plan` to decide how those specialists are staged, reviewed, and merged.

Instead, use two orchestration patterns from agent systems:
- manager-style orchestration when one room captain or showrunner agent should keep the final answer and call specialists as bounded tools;
- handoffs when a triage or room-captain layer should pass control to a specialist workflow that owns the next part of the turn.

The repo should also borrow two strong harness lessons:
- parallel specialists help only when handoffs stay narrow and merge ownership stays explicit;
- task-scoped tools or context packs are better than permanently loading every capability into every agent.

Sources:
- [OpenAI Agents SDK: agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)
- [oh-my-openagent README](https://github.com/code-yeongyu/oh-my-openagent)

## Non-Dogma Rule

These modes are reference operating shapes, not canonical pipelines.

The right output from the repository is usually:
- one primary mode;
- one backup mode or failure fallback when uncertainty is high;
- one explicit statement of what should stay human-owned.
