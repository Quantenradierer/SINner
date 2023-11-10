import unittest
from npc_creator.services.gpt_prompts import create_npc_prompt


class TestCreateNpcPrompt(unittest.TestCase):
    def test_basic(self):
        prompt = "Create a NPC"
        attributes = {"name": "John", "age": "30"}
        relevant = ["name", "job", "age", "height"]

        result = create_npc_prompt(prompt, attributes, relevant)
        self.assertEqual(
            result, [prompt, {"name": "John", "age": "30"}, {"job": "", "height": ""}]
        )

    def test_empty_attributes(self):
        prompt = "Create a NPC"
        attributes = {}
        relevant = ["name", "job", "age", "height"]

        result = create_npc_prompt(prompt, attributes, relevant)
        self.assertEqual(
            result, [prompt, {}, {"name": "", "job": "", "age": "", "height": ""}]
        )

    def test_no_relevant_attributes(self):
        prompt = "Create a NPC"
        attributes = {"name": "John", "age": "30"}
        relevant = []

        result = create_npc_prompt(prompt, attributes, relevant)
        self.assertEqual(result, [prompt, {"name": "John", "age": "30"}, {}])

    def test_all_attributes(self):
        prompt = "Create a NPC"
        attributes = {"name": "John", "age": "30", "job": "Engineer", "height": "6ft"}
        relevant = ["name", "job", "age", "height"]

        result = create_npc_prompt(prompt, attributes, relevant)
        self.assertEqual(result, [prompt, attributes, {}])

    def test_no_user_prompt(self):
        prompt = ""
        attributes = {"name": "John", "age": "30"}
        relevant = ["name", "job", "age", "height"]

        result = create_npc_prompt(prompt, attributes, relevant)
        self.assertEqual(
            result, [prompt, {"name": "John", "age": "30"}, {"job": "", "height": ""}]
        )

    def test_empty_attributes(self):
        prompt = "Create a NPC"
        attributes = {"name": "", "job": ""}
        relevant = ["name", "job", "age", "height"]

        result = create_npc_prompt(prompt, attributes, relevant)
        self.assertEqual(
            result, [prompt, {}, {"name": "", "job": "", "age": "", "height": ""}]
        )

    def test_missing_attributes(self):
        prompt = "Create a NPC"
        attributes = {"name": "John"}
        relevant = ["name", "job", "age", "height"]

        result = create_npc_prompt(prompt, attributes, relevant)
        self.assertEqual(
            result, [prompt, {"name": "John"}, {"job": "", "age": "", "height": ""}]
        )
