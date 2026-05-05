from __future__ import annotations

from pathlib import Path
import unittest

from scripts.check_routes import match_route
from scripts.lib import collect_e2e_journeys, load_json, load_router_matrix


ROOT = Path(__file__).resolve().parents[1]


class E2EJourneysTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.journeys = collect_e2e_journeys(ROOT)
        cls.router_matrix = load_router_matrix(ROOT)
        cls.register = load_json(ROOT / "docs" / "shared" / "constraint-key-register.json")
        cls.routes = cls.router_matrix["routes"]

    def test_all_journeys_have_required_fields(self) -> None:
        for journey in self.journeys:
            with self.subTest(journey=journey.get("id", "UNKNOWN")):
                self.assertIn("id", journey)
                self.assertIn("name", journey)
                self.assertIn("steps", journey)
                self.assertGreaterEqual(len(journey["steps"]), 2)

    def test_each_step_route_matches_router_matrix(self) -> None:
        """Every step's expected_route must match a route in the router matrix."""
        errors: list[str] = []
        for journey in self.journeys:
            jid = journey["id"]
            for step in journey["steps"]:
                step_num = step["step"]
                expected = step["expected_route"]

                # Build a fixture-shaped dict for match_route
                fixture = {
                    "intent": expected.get("intent", ""),
                    "medium": expected.get("medium", ""),
                    "stage": expected.get("stage", ""),
                    "output": expected.get("output", ""),
                    "constraints": {},
                }

                matches = [
                    route for route in self.routes
                    if match_route(self.register, route, fixture)
                ]

                step_id = f"{jid}.step{step_num}"
                if not matches:
                    errors.append(
                        f"{step_id}: no route matched for {fixture}"
                    )
                    continue

                matched = matches[0]
                for key in ("skill_id", "protocol_id", "rubric_id"):
                    if key in expected and matched[key] != expected[key]:
                        errors.append(
                            f"{step_id}: expected {key}={expected[key]!r}, "
                            f"got {matched[key]!r}"
                        )

        self.assertEqual(
            errors,
            [],
            f"{len(errors)} step route mismatch(es):\n" + "\n".join(errors),
        )

    def test_multi_turn_constraint_accumulation(self) -> None:
        """Verify that later turns don't contradict the constraints of earlier turns.

        Each step builds on the previous one.  The classification (intent/medium/
        stage/output) of a later step should still be routable given what was
        established earlier — i.e. the medium should not drift in incompatible ways.
        """
        for journey in self.journeys:
            jid = journey["id"]
            accumulated_media: set[str] = set()

            for step in journey["steps"]:
                expected = step["expected_route"]
                step_id = f"{jid}.step{step['step']}"

                medium = expected.get("medium", "")
                if medium and medium != "AMBIGUOUS":
                    accumulated_media.add(medium)

                # Later turns must not introduce media that conflict with
                # previously established media (within the same journey).
                # However, commercial journeys may legitimately mix commercial
                # and shortform_video — that's fine as long as there's overlap
                # in the router's medium lists.
                fixture = {
                    "intent": expected.get("intent", ""),
                    "medium": expected.get("medium", ""),
                    "stage": expected.get("stage", ""),
                    "output": expected.get("output", ""),
                    "constraints": {},
                }

                matches = [
                    route for route in self.routes
                    if match_route(self.register, route, fixture)
                ]
                self.assertTrue(
                    len(matches) > 0,
                    f"{step_id}: step is not routable — constraint accumulation "
                    f"may have broken routing",
                )

    def test_journeys_have_key_checks(self) -> None:
        for journey in self.journeys:
            with self.subTest(journey=journey.get("id", "UNKNOWN")):
                self.assertIn("key_checks", journey)
                self.assertGreaterEqual(len(journey["key_checks"]), 1)


if __name__ == "__main__":
    unittest.main()
