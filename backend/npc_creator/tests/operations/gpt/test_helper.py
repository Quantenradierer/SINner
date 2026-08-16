import json
import unittest
from enum import Enum
from unittest.mock import Mock

from pydantic import BaseModel, Field

from npc_creator.operations.gpt.helper import entity_prompt


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class SampleSchema(BaseModel):
    name: str = Field(description="Name of the character")
    age: int
    gender: Gender


def make_entity(values):
    entity = Mock()
    entity.values = values
    entity.SCHEMAS = {"default": SampleSchema}
    return entity


class TestEntityPrompt(unittest.TestCase):
    def test_filled_values_includes_only_present_attributes(self):
        entity = make_entity({"name": "John"})

        result = entity_prompt(entity, "default", filled_values=True)

        self.assertIn(f"'name': {json.dumps('John')} // Name of the character", result)
        self.assertNotIn("'age'", result)
        self.assertNotIn("'gender'", result)

    def test_missing_values_includes_only_absent_attributes(self):
        entity = make_entity({"name": "John"})

        result = entity_prompt(entity, "default", filled_values=False)

        self.assertNotIn("'name'", result)
        self.assertIn(f"'age': {json.dumps(0)}", result)
        self.assertIn("'gender': \"\"", result)

    def test_missing_enum_attribute_defaults_to_empty_string(self):
        entity = make_entity({})

        result = entity_prompt(entity, "default", filled_values=False)

        self.assertIn("'gender': \"\"", result)

    def test_missing_non_enum_attribute_defaults_to_type_default(self):
        entity = make_entity({})

        result = entity_prompt(entity, "default", filled_values=False)

        self.assertIn(f"'age': {json.dumps(0)}", result)

    def test_result_is_wrapped_in_braces(self):
        entity = make_entity({"name": "John"})

        result = entity_prompt(entity, "default", filled_values=True)

        self.assertTrue(result.startswith("{\n"))
        self.assertTrue(result.endswith("\n}"))
