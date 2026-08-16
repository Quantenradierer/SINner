from django.test import TestCase

from npc_creator.models.gpt_request import GptRequest


class TestGptRequest(TestCase):
    def test_gpt_request_creation(self):
        gpt_request = GptRequest.objects.create(
            input=["This is a test prompt"], kind="Fill"
        )

        self.assertEqual(gpt_request.input, ["This is a test prompt"])
        self.assertEqual(gpt_request.kind, "Fill")
        self.assertEqual(GptRequest.State.STARTED, gpt_request.state)
        self.assertIsNotNone(gpt_request.created_at)

    def test_finished_sets_completed_state(self):
        gpt_request = GptRequest.objects.create(input=["prompt"])

        gpt_request.finished()

        self.assertEqual(GptRequest.State.COMPLETED, gpt_request.state)

    def test_failed_sets_failed_state(self):
        gpt_request = GptRequest.objects.create(input=["prompt"])

        gpt_request.failed()

        self.assertEqual(GptRequest.State.FAILED, gpt_request.state)
