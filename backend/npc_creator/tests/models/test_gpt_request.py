import unittest

from django.test import TestCase
from django.contrib.auth import get_user_model

from npc_creator.models.gpt_request import GptRequest

User = get_user_model()


class TestGptRequest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )

    def test_gpt_request_creation(self):
        """Test that a GPT request can be created successfully."""
        gpt_request = GptRequest.objects.create(
            user=self.user,
            prompt="This is a test prompt",
            response="This is a test response",
            model="gpt-3.5-turbo"
        )
        
        self.assertEqual(gpt_request.user, self.user)
        self.assertEqual(gpt_request.prompt, "This is a test prompt")
        self.assertEqual(gpt_request.response, "This is a test response")
        self.assertEqual(gpt_request.model, "gpt-3.5-turbo")
        self.assertIsNotNone(gpt_request.created_at)

    def test_gpt_request_str_representation(self):
        """Test that the string representation is correct."""
        gpt_request = GptRequest.objects.create(
            user=self.user,
            prompt="This is a test prompt",
            response="This is a test response",
            model="gpt-3.5-turbo"
        )
        expected_str = f"GPT Request: {gpt_request.prompt[:20]}..."
        self.assertEqual(str(gpt_request), expected_str)