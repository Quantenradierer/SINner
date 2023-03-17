import os
from unittest import TestCase
from unittest.mock import patch, Mock, mock_open

from openai import OpenAIError

import config
from operations.generate_npc import GenerateNpc
from repositories.npc import NpcRepository
from tests.operations.base_integration_test import BaseIntegrationTest


class GenerateNpcTest(BaseIntegrationTest):
    def setUp(self):
        super().setUp()

        self.npc_id = 123
        with patch('config.SQLITE_FILE', os.path.join(self.tempdir.name, 'mocked_file.sqlite')):
            self.repo = NpcRepository()

    def tearDown(self):
        self.repo.close()
        super().tearDown()

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('openai.ChatCompletion.create')
    @patch('jobs.download_image.download_image_job_async')
    def test_call_success(self, mock_generate_image_job, mock_create, mock_open):
        mock_gpt_create_npc = {'choices': [{'message': {'content': '\n'.join([f'{attr}: test' for attr in list(config.RELEVANT_ATTRIBUTES)])}}]}
        mock_gpt_translation = {'choices': [{'message': {'content': 'the person looks cool, man.'}}]}
        mock_create.side_effect = mock_gpt_create_npc, mock_gpt_translation

        npc = GenerateNpc('some prompt').call()
        mock_generate_image_job.assert_called_once()
        assert('the person looks cool, man', npc.image_generator_description)

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('openai.ChatCompletion.create', side_effect=Exception('Test Error'))
    @patch('jobs.download_image.download_image_job_async')
    def test_call_gpt_unavailable(self, mock_generate_image_job, mock_create, mock_open):
        npc = GenerateNpc('some prompt').call()
        mock_generate_image_job.assert_called_once()
        assert('the person looks cool, man', npc.image_generator_description)


