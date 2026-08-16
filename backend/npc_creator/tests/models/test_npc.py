from django.test import TestCase
from pydantic import BaseModel, Field

from npc_creator.models.entity import Entity
from npc_creator.models.entities.npc import Npc


class TestEntity(TestCase):
    def test_has_image_description(self):
        entity = Entity(image_generator_description="Test description")
        self.assertTrue(entity.has_image_description())

    def test_has_no_image_description(self):
        entity = Entity()
        self.assertFalse(entity.has_image_description())

    def test_values_returns_attributes(self):
        entity = Entity(attributes={"name": "John"})
        self.assertEqual({"name": "John"}, entity.values)

    def test_schema_complete_true_when_all_fields_present(self):
        class SampleSchema(BaseModel):
            name: str

        entity = Entity(attributes={"name": "John"})
        entity.SCHEMAS = {"default": SampleSchema}

        self.assertTrue(entity.schema_complete("default"))

    def test_schema_complete_false_when_field_missing(self):
        class SampleSchema(BaseModel):
            name: str
            age: int

        entity = Entity(attributes={"name": "John"})
        entity.SCHEMAS = {"default": SampleSchema}

        self.assertFalse(entity.schema_complete("default"))


class TestEntityAddValues(TestCase):
    def test_add_values_stores_matching_attribute(self):
        npc = Npc()
        npc.add_values({"gender": "female"})

        self.assertEqual({"gender": "female"}, npc.attributes)

    def test_add_values_matches_case_insensitively_onto_canonical_key(self):
        npc = Npc()
        npc.add_values({"Gender": "female"})

        self.assertEqual({"gender": "female"}, npc.attributes)

    def test_add_values_ignores_attributes_not_in_any_schema(self):
        npc = Npc()
        npc.add_values({"not_a_real_attribute": "value"})

        self.assertEqual({}, npc.attributes)

    def test_add_values_ignores_blank_string_values(self):
        npc = Npc()
        npc.add_values({"gender": "   "})

        self.assertEqual({"gender": ""}, npc.attributes)
