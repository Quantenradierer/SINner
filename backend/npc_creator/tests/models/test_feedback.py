import unittest

from django.test import TestCase
from django.contrib.auth import get_user_model

from npc_creator.models.feedback import Feedback

User = get_user_model()


class TestFeedback(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )

    def test_feedback_creation(self):
        """Test that feedback can be created successfully."""
        feedback = Feedback.objects.create(
            user=self.user,
            content="This is a test feedback",
            rating=5
        )
        
        self.assertEqual(feedback.user, self.user)
        self.assertEqual(feedback.content, "This is a test feedback")
        self.assertEqual(feedback.rating, 5)
        self.assertIsNotNone(feedback.created_at)

    def test_feedback_str_representation(self):
        """Test that the string representation is correct."""
        feedback = Feedback.objects.create(
            user=self.user,
            content="This is a test feedback",
            rating=5
        )
        expected_str = f"Feedback from {feedback.user.username}: {feedback.content[:20]}..."
        self.assertEqual(str(feedback), expected_str)