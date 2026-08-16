import unittest
from unittest.mock import MagicMock, Mock, patch

from npc_creator.operations.gpt.entity.fill import Fill
from npc_creator.operations.return_types import Failure, Success


def make_entity(schema_complete=False):
    entity = Mock()
    entity.id = None
    entity.uuid = "test-uuid"
    entity.prompt = "make me an NPC"
    entity.schema_complete.return_value = schema_complete
    return entity


class TestFill(unittest.TestCase):
    def setUp(self):
        lock_patcher = patch("npc_creator.operations.gpt.entity.fill.FileLock")
        self.addCleanup(lock_patcher.stop)
        mock_filelock_cls = lock_patcher.start()
        mock_filelock_cls.return_value = MagicMock()

        prompt_patcher = patch("npc_creator.operations.gpt.entity.fill.entity_prompt")
        self.addCleanup(prompt_patcher.stop)
        prompt_patcher.start().return_value = "{}"

    def test_schema_already_complete_skips_gpt_call(self):
        entity = make_entity(schema_complete=True)

        with patch(
            "npc_creator.operations.gpt.gpt_interface.ask_chatgpt_moderated"
        ) as mock_ask:
            result = Fill(entity=entity).call()

        self.assertTrue(result)
        mock_ask.assert_not_called()
        entity.add_values.assert_not_called()

    def test_incomplete_schema_calls_gpt_and_fills_entity(self):
        entity = make_entity(schema_complete=False)

        with patch(
            "npc_creator.operations.gpt.gpt_interface.ask_chatgpt_moderated"
        ) as mock_ask:
            mock_ask.return_value = Success({"name": "John"})

            result = Fill(entity=entity).call()

        self.assertTrue(result)
        mock_ask.assert_called_once()
        entity.add_values.assert_called_once_with({"name": "John"})
        entity.save.assert_called_once()

    def test_gpt_failure_does_not_fill_entity(self):
        entity = make_entity(schema_complete=False)

        with patch(
            "npc_creator.operations.gpt.gpt_interface.ask_chatgpt_moderated"
        ) as mock_ask:
            mock_ask.return_value = Failure("gpt_raised_an_error")

            result = Fill(entity=entity).call()

        self.assertFalse(result)
        self.assertEqual("gpt_raised_an_error", result.error)
        entity.add_values.assert_not_called()

    def test_existing_entity_refreshes_from_db_before_checking_schema(self):
        entity = make_entity(schema_complete=True)
        entity.id = 42

        with patch("npc_creator.operations.gpt.gpt_interface.ask_chatgpt_moderated"):
            Fill(entity=entity).call()

        entity.refresh_from_db.assert_called_once()
