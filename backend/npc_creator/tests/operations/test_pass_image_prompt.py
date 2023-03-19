from unittest.mock import patch, Mock, mock_open

import requests

from npc_creator.models.npc import Npc
from npc_creator.operations.pass_image_prompt import PassImagePrompt
from npc_creator.tests.operations.base_integration_test import BaseIntegrationTest


class TestPassImagePrompt(BaseIntegrationTest):
    def setUp(self):
        super().setUp()

        self.npc_id = 123

    @patch('builtins.open', new_callable=mock_open, read_data="porn\ntied up\npetite\nass\n")
    @patch('requests.post')
    def test_call_success(self, mock_post, _mock_open):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        npc = Npc(id=self.npc_id, image_generator_description='someone with glasses')
        self.assertEqual('', npc.image_generator_state)

        self.assertTrue(PassImagePrompt(npc).call())
        self.assertEqual('started', npc.image_generator_state)

    @patch('builtins.open', new_callable=mock_open, read_data="porn\ntied up\npetite\n")
    def test_call_banned_word(self, _mock_open):
        npc = Npc(id=self.npc_id, image_generator_description='tied up hair')
        self.assertEqual('', npc.image_generator_state)

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual('contains banned word', result.error)
        self.assertEqual('banned', npc.image_generator_state)

    @patch('requests.post')
    def test_call_connection_error(self, mock_get):
        mock_get.side_effect = [requests.exceptions.RequestException()]

        npc = Npc(id=self.npc_id, image_generator_description='some description')
        self.assertEqual('', npc.image_generator_state)

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual('sending midjourney prompt was unsuccessful', result.error)
        self.assertEqual('', npc.image_generator_state)

    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('requests.get')
    def test_call_npc_already_has_image(self, mock_get, _mock_open):
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
    def test_call_image_generation_already_started(self, mock_get, _mock_open):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        npc = Npc(id=self.npc_id, image_generator_description='someone with glasses')
        npc.image_generation_started()

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual('image generation for this npc already started', result.error)
        self.assertEqual('started', npc.image_generator_state)
