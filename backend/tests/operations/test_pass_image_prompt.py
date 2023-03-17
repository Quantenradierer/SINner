import os
import unittest
from unittest.mock import patch, Mock, mock_open

import requests

from models.npc import Npc
from operations.pass_image_prompt import PassImagePrompt
from repositories.npc import NpcRepository
from tests.operations.base_integration_test import BaseIntegrationTest


class TestPassImagePrompt(BaseIntegrationTest):
    def setUp(self):
        super().setUp()

        self.npc_id = 123
        with patch('config.SQLITE_FILE', os.path.join(self.tempdir.name, 'mocked_file.sqlite')):
            self.repo = NpcRepository()

    def tearDown(self):
        self.repo.close()
        super().tearDown()

    @patch('builtins.open', new_callable=mock_open, read_data="porn\ntied up\npetite\nass\n")
    @patch('requests.post')
    def test_call_success(self, mock_post, mock_open):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        npc = Npc(id=self.npc_id, image_generator_description='someone with glasses')
        self.assertIsNone(npc.image_generator_state)

        self.assertTrue(PassImagePrompt(npc).call())
        self.assertEqual('started', npc.image_generator_state)

    @patch('builtins.open', new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_call_banned_word(self, mock_open):
        npc = Npc(id=self.npc_id, image_generator_description='tied up hair')
        self.assertIsNone(npc.image_generator_state)

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual('contains banned word', result.error)
        self.assertEqual('banned', npc.image_generator_state)

    @patch('requests.post')
    def test_call_connection_error(self, mock_get):
        mock_get.side_effect = [requests.exceptions.RequestException()]

        npc = Npc(id=self.npc_id, image_generator_description='some description')
        self.assertIsNone(npc.image_generator_state)

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual('sending midjourney prompt was unsuccessful', result.error)
        self.assertIsNone(npc.image_generator_state)

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('requests.get')
    def test_call_npc_already_has_image(self, mock_get, mock_open):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        npc = Npc(id=self.npc_id, image_generator_description='someone with glasses')
        npc.add_image('example.png')

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual('image generation for this npc already started', result.error)
        self.assertEqual('done', npc.image_generator_state)

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('requests.get')
    def test_call_image_generation_already_started(self, mock_get, mock_open):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        npc = Npc(id=self.npc_id, image_generator_description='someone with glasses')
        npc.image_generation_started()

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual('image generation for this npc already started', result.error)
        self.assertEqual('started', npc.image_generator_state)