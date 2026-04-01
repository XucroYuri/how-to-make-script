"""Tests for all phases: runtime index, route robustness, NL routing, loading budget."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

from scripts.check_nl_routing import check_nl_routing
from scripts.check_loading_budget import check_loading_budget
from scripts.lib import (
    collect_skill_manifests,
    load_router_matrix,
)


class GenerateIndexRuntimeTest(unittest.TestCase):
    root = Path(__file__).resolve().parents[1]

    def test_generate_index_runtime_mode_works(self):
        result = subprocess.run(
            [sys.executable, "scripts/generate_index.py", "--mode", "runtime"],
            capture_output=True, text=True,
        )
        data = json.loads(result.stdout)
        self.assertIn("route_lookup", data)
        self.assertIn("fallback_chains", data)
        self.assertIn("atom_by_protocol", data)
        self.assertIn("adjunct_bundles", data)


class RouteRobustnessTest(unittest.TestCase):
    root = Path(__file__).resolve().parents[1]

    def test_router_matrix_has_required_signals(self):
        matrix = load_router_matrix(self.root)
        for route in matrix["routes"]:
            self.assertIn("required_constraint_signals", route)

    def test_manifest_fallback_chains_are_valid(self):
        manifests = collect_skill_manifests(self.root)
        skill_ids = {m["id"] for m in manifests}
        for m in manifests:
            fallback = m.get("fallback_to_skill_id")
            if fallback is not None:
                self.assertIn(
                    fallback, skill_ids,
                    f"{m['id']}: fallback_to_skill_id '{fallback}' does not exist",
                )

    def test_manifest_default_loading_mode_set(self):
        from scripts.lib import collect_skill_manifests
        manifests = collect_skill_manifests(self.root)
        for m in manifests:
            self.assertIn(
                "default_loading_mode", m,
                f"{m['id']}: missing default_loading_mode",
            )


class NLRoutingBenchTest(unittest.TestCase):
    root = Path(__file__).resolve().parents[1]

    def test_nl_routing_bench_validates(self):
        report = check_nl_routing(self.root)
        self.assertEqual(report["errors"], [])

    def test_nl_routing_bench_has_minimum_coverage(self):
        report = check_nl_routing(self.root)
        coverage = report.get("coverage", {})
        self.assertGreaterEqual(coverage.get("entry_count", 0), 20)

    def test_nl_routing_bench_has_minimum_clarification_cases(self):
        report = check_nl_routing(self.root)
        coverage = report.get("coverage", {})
        self.assertGreaterEqual(
            coverage.get("behaviors", {}).get("should_ask_clarification", 0),
            3,
        )


class LoadingBudgetPhaseTest(unittest.TestCase):
    root = Path(__file__).resolve().parents[1]

    def test_loading_budgets_declared(self):
        report = check_loading_budget(self.root)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["protocol_count"], 28)


if __name__ == "__main__":
    unittest.main()
