from __future__ import annotations

from pathlib import Path
import unittest

from scripts.check_routes import match_route
from scripts.lib import collect_nl_routing_bench, load_json, load_router_matrix


ROOT = Path(__file__).resolve().parents[1]
ROUTE_INTENT_BEHAVIORS = {"should_route", "should_route_or_ask"}


class RoutingBenchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.entries = collect_nl_routing_bench(ROOT)
        cls.router_matrix = load_router_matrix(ROOT)
        cls.register = load_json(ROOT / "docs" / "shared" / "constraint-key-register.json")
        cls.routes = cls.router_matrix["routes"]

    def test_all_entries_have_required_fields(self) -> None:
        for entry in self.entries:
            with self.subTest(entry=entry["id"]):
                self.assertIn("id", entry)
                self.assertIn("query", entry)
                self.assertIn("expected_classification", entry)
                self.assertIn("expected_behavior", entry)

    def test_route_entries_match_expected_skill_and_protocol(self) -> None:
        """Entries with should_route behavior must match expected_route in router matrix.

        Reports pass/fail rates.  The benchmark includes forward-looking entries
        whose classifications (intent/stage/output) may not exist in the router
        matrix yet.  A configured minimum pass rate guards against regressions.
        """
        passed = 0
        failed = 0
        unmatched: list[str] = []
        mismatched: list[str] = []
        for entry in self.entries:
            eid = entry["id"]
            behavior = entry.get("expected_behavior", "")
            expected_route = entry.get("expected_route")
            if behavior not in ROUTE_INTENT_BEHAVIORS or not expected_route:
                continue

            classification = entry["expected_classification"]
            # Build a fixture-shaped dict for match_route
            fixture = {
                "intent": classification.get("intent", ""),
                "medium": classification.get("medium", ""),
                "stage": classification.get("stage", ""),
                "output": classification.get("output", ""),
                "constraints": {},
            }

            matches = [
                route for route in self.routes
                if match_route(self.register, route, fixture)
            ]

            if not matches:
                failed += 1
                unmatched.append(
                    f"{eid}: no route matched for {classification}"
                )
                continue

            matched = matches[0]
            route_ok = True
            for key in ("skill_id", "protocol_id"):
                if key in expected_route and matched[key] != expected_route[key]:
                    route_ok = False
                    mismatched.append(
                        f"{eid}: expected {key}={expected_route[key]!r}, "
                        f"got {matched[key]!r}"
                    )
            if route_ok:
                passed += 1
            else:
                failed += 1

        total = passed + failed
        pass_rate = (passed / total * 100) if total > 0 else 100.0
        detail_parts = [f"Pass rate: {pass_rate:.0f}% ({passed}/{total})"]
        if unmatched:
            detail_parts.append("\nUnmatched (future routes?):\n" + "\n".join(unmatched))
        if mismatched:
            detail_parts.append("\nMismatched:\n" + "\n".join(mismatched))

        msg = "\n".join(detail_parts)
        # Require at least 70% pass rate to guard against regressions
        self.assertGreaterEqual(
            pass_rate,
            70.0,
            f"Route match pass rate below 70% threshold\n{msg}",
        )

    def test_ambiguous_entries_do_not_match_any_route(self) -> None:
        """Entries whose classification is entirely AMBIGUOUS should not match."""
        for entry in self.entries:
            eid = entry["id"]
            classification = entry["expected_classification"]
            all_ambiguous = all(
                v == "AMBIGUOUS" for v in classification.values()
            )
            if not all_ambiguous:
                continue

            fixture = {
                "intent": classification.get("intent", ""),
                "medium": classification.get("medium", ""),
                "stage": classification.get("stage", ""),
                "output": classification.get("output", ""),
                "constraints": {},
            }

            matches = [
                route for route in self.routes
                if match_route(self.register, route, fixture)
            ]
            self.assertEqual(
                len(matches),
                0,
                f"{eid}: expected no route match for all-ambiguous classification, "
                f"got {len(matches)} matches",
            )

    def test_bench_has_minimum_coverage(self) -> None:
        self.assertGreaterEqual(len(self.entries), 10)
        behaviors = {e["expected_behavior"] for e in self.entries}
        self.assertIn("should_route", behaviors)
        self.assertIn("should_ask_clarification", behaviors)


if __name__ == "__main__":
    unittest.main()
