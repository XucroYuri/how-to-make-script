## Case: fail-001

**Protocol used:** wp.idea-discovery
**Skill used:** skill.idea-discovery
**Failure category:** premise_drift

**What went wrong:**
User gave a vague concept about "a lonely AI in a post-apocalyptic city." The protocol correctly generated a premise, but the premise drifted toward a generic "robots learn to feel" theme, losing the specific pressure source (loneliness in a world designed for connection) that the original concept implied.

**Root cause:**
The protocol's step 1 asks to "identify protagonist, desire, obstacle, cost" but doesn't explicitly guard against generic theming when the raw idea contains an implicit tension between the character's nature and their environment.

**Correction:**
Added `ka.theme-pressure` to the protocol's linked atoms (already present in current version). The atom explicitly warns against replacing a specific tension with a generic thematic label.

**Status:** addressed

**Lesson:**
When the user's raw idea contains an implicit paradox (e.g., a lonely entity in a connected world), the premise must preserve that paradox rather than flatten it into a familiar genre theme.
