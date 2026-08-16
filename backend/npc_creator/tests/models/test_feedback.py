from django.test import TestCase

from npc_creator.models.feedback import Feedback


class TestFeedback(TestCase):
    def test_feedback_creation(self):
        feedback = Feedback.objects.create(
            email="test@example.com", comment="This is a test feedback"
        )

        self.assertEqual(feedback.email, "test@example.com")
        self.assertEqual(feedback.comment, "This is a test feedback")

    def test_feedback_can_be_created_without_email(self):
        feedback = Feedback.objects.create(comment="Anonymous feedback")

        self.assertEqual(feedback.email, "")
        self.assertEqual(feedback.comment, "Anonymous feedback")
