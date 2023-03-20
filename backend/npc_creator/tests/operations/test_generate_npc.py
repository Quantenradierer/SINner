from unittest.mock import patch, mock_open

from npc_creator.config import RELEVANT_ATTRIBUTES
from npc_creator.operations.generate_npc import GenerateNpc
from npc_creator.tests.operations.base_integration_test import BaseIntegrationTest


class GenerateNpcTest(BaseIntegrationTest):
    def setUp(self):
        super().setUp()

        self.npc_id = 123

    def tearDown(self):
        super().tearDown()

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('openai.ChatCompletion.create')
    @patch('npc_creator.operations.generate_npc.download_image.download_image_job_async')
    def test_call_success(self, mock_generate_image_job, mock_create, _mock_open):
        mock_gpt_create_npc = {'choices': [{'message': {'content': '\n'.join([f'{attr}: test' for attr in list(RELEVANT_ATTRIBUTES)])}}]}
        mock_gpt_translation = {'choices': [{'message': {'content': 'the person looks cool, man.'}}]}
        mock_create.side_effect = mock_gpt_create_npc, mock_gpt_translation

        result_npc = GenerateNpc('some prompt').call()
        self.assertTrue(result_npc)
        self.assertEqual('the person looks cool, man.', result_npc.data.image_generator_description)
        mock_generate_image_job.assert_called_once()

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('openai.ChatCompletion.create', side_effect=Exception('Test Error'))
    @patch('npc_creator.operations.generate_npc.download_image.download_image_job_async')
    def test_call_gpt_unavailable(self, mock_generate_image_job, _mock_create, _mock_open):
        result = GenerateNpc('some prompt').call()

        self.assertFalse(result)
        self.assertEqual('gpt not available', result.error)
        mock_generate_image_job.assert_not_called()

