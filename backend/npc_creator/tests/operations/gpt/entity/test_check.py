import unittest
from unittest.mock import Mock, patch

from npc_creator.operations.gpt.custom.check import Check as CustomCheck
from npc_creator.operations.gpt.entity.check import Check as EntityCheck
from npc_creator.operations.gpt.npc.check import Check as NpcCheck
from npc_creator.operations.return_types import Failure, Success


def make_entity():
    entity = Mock()
    entity.attributes = {"name": "Test NPC"}
    return entity


class TestEntityCheck(unittest.TestCase):
    def setUp(self):
        prompt_patcher = patch("npc_creator.operations.gpt.entity.check.entity_prompt")
        self.addCleanup(prompt_patcher.stop)
        prompt_patcher.start().return_value = "{}"

    def test_prompt_is_a_list_of_a_single_rendered_prompt(self):
        check = EntityCheck(entity=make_entity())
        self.assertEqual(["{}"], check.prompt())

    def test_interpret_result_success_on_empty_data(self):
        check = EntityCheck(entity=make_entity())
        result = check.interpret_result(Success(""))
        self.assertTrue(result)

    def test_interpret_result_failure_on_nonempty_data(self):
        check = EntityCheck(entity=make_entity())
        result = check.interpret_result(Success("{'name': 'inappropriate name'}"))
        self.assertFalse(result)
        self.assertEqual("{'name': 'inappropriate name'}", result.error)

    def test_call_success(self):
        with patch(
            "npc_creator.operations.gpt.gpt_interface.ask_chatgpt_moderated"
        ) as mock_ask:
            mock_ask.return_value = Success("")
            result = EntityCheck(entity=make_entity()).call()

        self.assertTrue(result)

    def test_call_failure_when_gpt_flags_a_problem(self):
        with patch(
            "npc_creator.operations.gpt.gpt_interface.ask_chatgpt_moderated"
        ) as mock_ask:
            mock_ask.return_value = Success("{'name': 'inappropriate name'}")
            result = EntityCheck(entity=make_entity()).call()

        self.assertFalse(result)
        self.assertEqual("{'name': 'inappropriate name'}", result.error)

    def test_call_failure_when_gpt_is_unavailable(self):
        with patch(
            "npc_creator.operations.gpt.gpt_interface.ask_chatgpt_moderated"
        ) as mock_ask:
            mock_ask.return_value = Failure("gpt_raised_an_error")
            result = EntityCheck(entity=make_entity()).call()

        self.assertFalse(result)
        self.assertEqual("gpt_raised_an_error", result.error)


class TestNpcCheck(unittest.TestCase):
    def test_inherits_entity_check_system_prompt(self):
        entity_check = EntityCheck(entity=make_entity())
        npc_check = NpcCheck(entity=make_entity())
        self.assertEqual(entity_check.system_prompt, npc_check.system_prompt)


class TestCustomCheck(unittest.TestCase):
    def test_call_always_succeeds(self):
        self.assertTrue(CustomCheck(entity=make_entity()).call())
