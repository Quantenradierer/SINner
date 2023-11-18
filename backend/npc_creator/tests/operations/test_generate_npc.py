from unittest.mock import patch, mock_open


from npc_creator.tests.operations.base_integration_test import BaseIntegrationTest


class GenerateNpcTest(BaseIntegrationTest):
    def setUp(self):
        super().setUp()

        self.npc_id = 123

    def tearDown(self):
        super().tearDown()

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("openai.ChatCompletion.create")
    @patch(
        "npc_creator.operations.generate_npc.download_image.download_image_job_async"
    )
    def test_call_success(self, mock_generate_image_job, mock_create, _mock_open):
        content = "\n".join([f"{attr}: data" for attr in list(RELEVANT_ATTRIBUTES)])
        mock_create.return_value = {"choices": [{"message": {"content": content}}]}

        result_npc = GenerateNpc("some prompt").call()
        self.assertTrue(result_npc)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("openai.ChatCompletion.create", side_effect=Exception("Test Error"))
    @patch(
        "npc_creator.operations.generate_npc.download_image.download_image_job_async"
    )
    def test_call_gpt_unavailable(
        self, mock_generate_image_job, _mock_create, _mock_open
    ):
        result = GenerateNpc("some prompt").call()
        self.assertFalse(result)
        self.assertEqual("gpt_raised_an_error", result.error)
        mock_generate_image_job.assert_not_called()

    @patch(
        "npc_creator.operations.generate_npc.download_image.download_image_job_async"
    )
    def test_recreate_image_called(self, mock_generate_image_job):
        with patch("openai.ChatCompletion.create") as mock_create:
            content = "\n".join([f"{attr}: data" for attr in list(RELEVANT_ATTRIBUTES)])
            mock_create.return_value = {"choices": [{"message": {"content": content}}]}
            GenerateNpc("some prompt").call()
            self.assertTrue(mock_generate_image_job.called)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("openai.ChatCompletion.create")
    def test_call_with_incomplete_data(self, mock_create, _mock_open):
        mock_create.return_value = {"choices": [{"message": {"content": "Name: Test"}}]}
        result = GenerateNpc("some prompt").call()
        self.assertFalse(result)
        self.assertEqual("gpt_result_insufficient", result.error)

    @patch(
        "npc_creator.operations.generate_npc.download_image.download_image_job_async"
    )
    def test_repository_create_called(self, mock_generate_image_job):
        with patch("npc_creator.repositories.npc_repo.create") as mock_create:
            with patch("openai.ChatCompletion.create") as mock_gpt_create:
                content = "\n".join(
                    [f"{attr}: data" for attr in list(RELEVANT_ATTRIBUTES)]
                )
                mock_gpt_create.return_value = {
                    "choices": [{"message": {"content": content}}]
                }
                GenerateNpc("some prompt").call()
                self.assertTrue(mock_create.called)
