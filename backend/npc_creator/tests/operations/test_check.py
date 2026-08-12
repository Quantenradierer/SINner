import unittest
from unittest.mock import patch, MagicMock

from django.test import TestCase

from npc_creator.models.entity import Entity
from npc_creator.operations.gpt.entity.check import Check as EntityCheck
from npc_creator.operations.gpt.npc.check import Check as NpcCheck
from npc_creator.operations.gpt.custom.check import Check as CustomCheck
from npc_creator.operations.return_types import Failure, Success


class TestCheckOperations(TestCase):
    def setUp(self):
        self.entity = Entity.objects.create(
            kind="npc",
            data={"name": "Test NPC", "age": 30},
            description="A test NPC"
        )

    @patch("npc_creator.operations.gpt.check.OpenAI")
    def test_entity_check_call_success(self, mock_openai):
        """Test successful entity check call."""
        # Set up mock
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = {
            "choices": [{
                "message": {
                    "content": "{}"  # Empty JSON = success
                }  
            }]
        }
        mock_client.chat.completions.create.return_value = mock_response
        
        check_op = EntityCheck(entity=self.entity)
        result = check_op.call()
        
        # Should succeed with empty response meaning no issues
        self.assertTrue(result.success)
        self.assertEqual(result.data, "{}")

    @patch("npc_creator.operations.gpt.check.OpenAI")
    def test_entity_check_call_failure(self, mock_openai):
        """Test failed entity check call."""
        # Set up mock  
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = {
            "choices": [{
                "message": {
                    "content": "{'name': 'inappropriate name'}"
                }
            }]
        }
        mock_client.chat.completions.create.return_value = mock_response
        
        check_op = EntityCheck(entity=self.entity)
        result = check_op.call()
        
        # Should fail with error from GPT
        self.assertFalse(result.success)
        self.assertEqual(result.data, "{'name': 'inappropriate name'}")

    @patch("npc_creator.operations.gpt.check.OpenAI")
    def test_npc_check_call_success(self, mock_openai):
        """Test successful NPC check call."""
        # Set up mock
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = {
            "choices": [{
                "message": {
                    "content": "{}"
                }
            }]
        }
        mock_client.chat.completions.create.return_value = mock_response
        
        check_op = NpcCheck(entity=self.entity)
        result = check_op.call()
        
        # Should succeed with empty response meaning no issues
        self.assertTrue(result.success)
        self.assertEqual(result.data, "{}")

    @patch("npc_creator.operations.gpt.check.OpenAI")
    def test_npc_check_call_failure(self, mock_openai):
        """Test failed NPC check call."""
        # Set up mock  
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = {
            "choices": [{
                "message": {
                    "content": "{'age': 'too young'}"
                }
            }]
        }
        mock_client.chat.completions.create.return_value = mock_response
        
        check_op = NpcCheck(entity=self.entity)
        result = check_op.call()
        
        # Should fail with error from GPT 
        self.assertFalse(result.success)
        self.assertEqual(result.data, "{'age': 'too young'}")

    @patch("npc_creator.operations.gpt.check.OpenAI")
    def test_custom_check_call_success(self, mock_openai):
        """Test successful custom check call."""
        # Set up mock
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = {
            "choices": [{
                "message": {
                    "content": "{}"
                }
            }]
        }
        mock_client.chat.completions.create.return_value = mock_response
        
        check_op = CustomCheck(entity=self.entity)
        result = check_op.call()
        
        # Should succeed with empty response meaning no issues
        self.assertTrue(result.success)
        self.assertEqual(result.data, "{}")

    @patch("npc_creator.operations.gpt.check.OpenAI")
    def test_custom_check_call_failure(self, mock_openai):
        """Test failed custom check call."""
        # Set up mock  
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        
        mock_response = {
            "choices": [{
                "message": {
                    "content": "{'custom_field': 'invalid value'}"
                }
            }]
        }
        mock_client.chat.completions.create.return_value = mock_response
        
        check_op = CustomCheck(entity=self.entity)
        result = check_op.call()
        
        # Should fail with error from GPT
        self.assertFalse(result.success)
        self.assertEqual(result.data, "{'custom_field': 'invalid value'}")

    def test_entity_check_interpret_result_success(self):
        """Test successful interpretation of result."""
        success_result = Success("{}")
        check_op = EntityCheck(entity=self.entity)
        
        interpreted = check_op.interpret_result(success_result)
        # Should return Success because empty JSON means no problems
        self.assertTrue(interpreted.success)

    def test_entity_check_interpret_result_failure(self):
        """Test failed interpretation of result."""
        failure_data = "{'name': 'inappropriate name'}"
        success_result = Success(failure_data)
        check_op = EntityCheck(entity=self.entity)
        
        interpreted = check_op.interpret_result(success_result)
        # Should return Failure because there were issues
        self.assertFalse(interpreted.success)
        self.assertEqual(interpreted.data, failure_data)

    def test_prompt_property(self):
        """Test prompt property for different check types."""
        entity_check = EntityCheck(entity=self.entity)
        npc_check = NpcCheck(entity=self.entity) 
        custom_check = CustomCheck(entity=self.entity)
        
        # All should have the right prompt method
        self.assertTrue(hasattr(entity_check, 'prompt'))
        self.assertTrue(hasattr(npc_check, 'prompt'))
        self.assertTrue(hasattr(custom_check, 'prompt'))

    def test_system_prompts(self):
        """Test that system prompts are correctly set."""
        entity_check = EntityCheck(entity=self.entity)
        npc_check = NpcCheck(entity=self.entity)
        custom_check = CustomCheck(entity=self.entity)
        
        # Check that system prompts exist
        self.assertIsNotNone(entity_check.system_prompt)
        self.assertIsNotNone(npc_check.system_prompt)
        self.assertIsNotNone(custom_check.system_prompt)