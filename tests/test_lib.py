"""Unit tests for scripts/lib.py core functions: validate_schema and parse_markdown_asset."""
import unittest
from pathlib import Path

from scripts.lib import parse_markdown_asset, validate_schema


class ValidateSchemaTest(unittest.TestCase):
    """Tests for the recursive JSON schema validator."""

    # -- object type --

    def test_object_valid_with_required_keys(self):
        schema = {"type": "object", "required": ["name"], "properties": {"name": {"type": "string"}}}
        self.assertEqual(validate_schema({"name": "test"}, schema), [])

    def test_object_missing_required_key(self):
        schema = {"type": "object", "required": ["name"]}
        errors = validate_schema({}, schema)
        self.assertTrue(any("missing required key 'name'" in e for e in errors))

    def test_object_wrong_type(self):
        schema = {"type": "object"}
        errors = validate_schema("not_an_object", schema)
        self.assertTrue(any("expected object" in e for e in errors))

    def test_object_extra_keys_allowed(self):
        schema = {"type": "object", "required": ["a"], "properties": {"a": {"type": "string"}}}
        self.assertEqual(validate_schema({"a": "ok", "b": 1}, schema), [])

    # -- recursive nested object --

    def test_nested_object_valid(self):
        schema = {
            "type": "object",
            "required": ["inner"],
            "properties": {
                "inner": {
                    "type": "object",
                    "required": ["value"],
                    "properties": {"value": {"type": "string"}},
                }
            },
        }
        self.assertEqual(validate_schema({"inner": {"value": "deep"}}, schema), [])

    def test_nested_object_missing_deep_key(self):
        schema = {
            "type": "object",
            "required": ["inner"],
            "properties": {
                "inner": {
                    "type": "object",
                    "required": ["value"],
                    "properties": {"value": {"type": "string"}},
                }
            },
        }
        errors = validate_schema({"inner": {}}, schema)
        self.assertTrue(any("missing required key 'value'" in e for e in errors))

    def test_nested_object_wrong_deep_type(self):
        schema = {
            "type": "object",
            "required": ["inner"],
            "properties": {
                "inner": {
                    "type": "object",
                    "required": ["value"],
                    "properties": {"value": {"type": "string"}},
                }
            },
        }
        errors = validate_schema({"inner": {"value": 42}}, schema)
        self.assertTrue(any("expected string" in e for e in errors))

    # -- string type --

    def test_string_valid(self):
        self.assertEqual(validate_schema("hello", {"type": "string"}), [])

    def test_string_wrong_type(self):
        errors = validate_schema(123, {"type": "string"})
        self.assertTrue(any("expected string" in e for e in errors))

    # -- integer type --

    def test_integer_valid(self):
        self.assertEqual(validate_schema(42, {"type": "integer"}), [])

    def test_integer_wrong_type(self):
        errors = validate_schema("42", {"type": "integer"})
        self.assertTrue(any("expected integer" in e for e in errors))

    def test_integer_bool_rejected(self):
        errors = validate_schema(True, {"type": "integer"})
        self.assertTrue(any("expected integer" in e for e in errors))

    def test_integer_minimum_violation(self):
        errors = validate_schema(3, {"type": "integer", "minimum": 5})
        self.assertTrue(any("expected at least 5" in e for e in errors))

    def test_integer_minimum_met(self):
        self.assertEqual(validate_schema(5, {"type": "integer", "minimum": 5}), [])

    # -- boolean type --

    def test_boolean_valid(self):
        self.assertEqual(validate_schema(True, {"type": "boolean"}), [])

    def test_boolean_wrong_type(self):
        errors = validate_schema(1, {"type": "boolean"})
        self.assertTrue(any("expected boolean" in e for e in errors))

    # -- array type --

    def test_array_valid_with_items(self):
        schema = {"type": "array", "minItems": 1, "items": {"type": "string"}}
        self.assertEqual(validate_schema(["a", "b"], schema), [])

    def test_array_minitems_violation(self):
        schema = {"type": "array", "minItems": 2}
        errors = validate_schema(["a"], schema)
        self.assertTrue(any("expected at least 2 items" in e for e in errors))

    def test_array_wrong_type(self):
        errors = validate_schema("not_a_list", {"type": "array"})
        self.assertTrue(any("expected array" in e for e in errors))

    def test_array_nested_item_error(self):
        schema = {"type": "array", "items": {"type": "object", "required": ["id"], "properties": {"id": {"type": "string"}}}}
        errors = validate_schema([{"id": "ok"}, {}], schema)
        self.assertTrue(any("missing required key 'id'" in e for e in errors))

    def test_array_of_objects_valid(self):
        schema = {"type": "array", "items": {"type": "object", "required": ["id"], "properties": {"id": {"type": "string"}}}}
        self.assertEqual(validate_schema([{"id": "a"}, {"id": "b"}], schema), [])

    # -- const --

    def test_const_valid(self):
        self.assertEqual(validate_schema("exact", {"type": "string", "const": "exact"}), [])

    def test_const_violation(self):
        errors = validate_schema("wrong", {"type": "string", "const": "exact"})
        self.assertTrue(any("expected constant" in e for e in errors))

    # -- enum --

    def test_enum_valid(self):
        self.assertEqual(validate_schema("b", {"type": "string", "enum": ["a", "b", "c"]}), [])

    def test_enum_violation(self):
        errors = validate_schema("z", {"type": "string", "enum": ["a", "b", "c"]})
        self.assertTrue(any("expected one of" in e for e in errors))

    # -- nullable --

    def test_nullable_skips_validation(self):
        schema = {"type": "string", "nullable": True}
        self.assertEqual(validate_schema(None, schema), [])

    def test_nullable_false_rejects_null(self):
        schema = {"type": "string", "nullable": False}
        errors = validate_schema(None, schema)
        self.assertTrue(len(errors) > 0)

    # -- unsupported type --

    def test_unsupported_schema_type(self):
        errors = validate_schema({}, {"type": "datetime"})
        self.assertTrue(any("unsupported schema type" in e for e in errors))

    # -- null type (no type field) --

    def test_no_type_passes(self):
        self.assertEqual(validate_schema("anything", {}), [])

    # -- default path --

    def test_default_path_used(self):
        errors = validate_schema(True, {"type": "string"})
        self.assertTrue(all(e.startswith("$") for e in errors))


class ParseMarkdownAssetTest(unittest.TestCase):
    """Tests for parsing JSON frontmatter from markdown files."""

    def test_valid_frontmatter(self):
        p = Path(__file__).with_name("_test_valid.md")
        p.write_text('---\n{"id": "test", "value": 42}\n---\n# Body text\n', encoding="utf-8")
        try:
            result = parse_markdown_asset(p)
            self.assertEqual(result["id"], "test")
            self.assertEqual(result["value"], 42)
            self.assertIn("# Body text", result["_body"])
            self.assertEqual(result["_path"], str(p))
        finally:
            p.unlink()

    def test_empty_frontmatter(self):
        p = Path(__file__).with_name("_test_empty.md")
        p.write_text('---\n{}\n---\n', encoding="utf-8")
        try:
            result = parse_markdown_asset(p)
            self.assertNotIn("id", result)
        finally:
            p.unlink()

    def test_missing_opening_fence(self):
        p = Path(__file__).with_name("_test_no_open.md")
        p.write_text('{"id": "test"}\n---\n# Body\n', encoding="utf-8")
        try:
            with self.assertRaises(ValueError) as ctx:
                parse_markdown_asset(p)
            self.assertIn("does not start with JSON frontmatter", str(ctx.exception))
        finally:
            p.unlink()

    def test_missing_closing_fence(self):
        p = Path(__file__).with_name("_test_no_close.md")
        p.write_text('---\n{"id": "test"}\n', encoding="utf-8")
        try:
            with self.assertRaises(ValueError) as ctx:
                parse_markdown_asset(p)
            self.assertIn("missing closing frontmatter fence", str(ctx.exception))
        finally:
            p.unlink()

    def test_frontmatter_only_no_body(self):
        p = Path(__file__).with_name("_test_no_body.md")
        p.write_text('---\n{"a": 1}\n---\n', encoding="utf-8")
        try:
            result = parse_markdown_asset(p)
            self.assertEqual(result["a"], 1)
            self.assertEqual(result["_body"], "")
        finally:
            p.unlink()


if __name__ == "__main__":
    unittest.main()
