from unittest.mock import patch, Mock, mock_open

import requests

from npc_creator import config
from npc_creator.models.npc import Entity
from npc_creator.operations.pass_image_prompt import PassImagePrompt
from npc_creator.tests.operations.base_integration_test import BaseIntegrationTest


class TestPassImagePrompt(BaseIntegrationTest):
    def setUp(self):
        super().setUp()

        self.npc_id = 123

    @patch("openai.ChatCompletion.create")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="porn\ntied up\npetite\nass\n",
    )
    @patch("requests.post")
    def test_call_success(self, mock_post, _mock_open, mock_create):
        mock_create.return_value = {
            "choices": [{"message": {"content": "the person looks cool, man."}}]
        }

        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        npc = Entity(id=self.npc_id, attributes={config.VISUAL_APPEARANCE_ATTRIBUTE: ""})
        self.assertEqual("init", npc.image_generator_state)

        self.assertTrue(PassImagePrompt(npc).call())
        self.assertEqual("started", npc.image_generator_state)

    @patch("openai.ChatCompletion.create")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="porn\ntied up\npetite\nass\n",
    )
    @patch("requests.post")
    def test_call_when_the_npc_has_an_image_description(
        self, mock_post, _mock_open, mock_create
    ):
        mock_create.return_value = {
            "choices": [{"message": {"content": "the person looks cool, man."}}]
        }

        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        npc = Entity(id=self.npc_id, image_generator_description="someone with glasses")
        self.assertEqual("init", npc.image_generator_state)

        self.assertTrue(PassImagePrompt(npc).call())
        self.assertEqual("started", npc.image_generator_state)

    @patch("requests.post")
    def test_call_connection_error(self, mock_get):
        mock_get.side_effect = [requests.exceptions.RequestException()]

        npc = Entity(id=self.npc_id, image_generator_description="some description")
        self.assertEqual("init", npc.image_generator_state)

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual("sending_midjourney_prompt_was_unsuccessful", result.error)
        self.assertEqual("init", npc.image_generator_state)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("requests.get")
    def test_call_npc_already_has_image(self, mock_get, _mock_open):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        npc = Entity(id=self.npc_id, image_generator_description="someone with glasses")
        npc.add_image("example.png")

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual("image_generation_for_this_npc_already_started", result.error)
        self.assertEqual("done", npc.image_generator_state)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("requests.get")
    def test_call_image_generation_already_started(self, mock_get, _mock_open):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        npc = Entity(id=self.npc_id, image_generator_description="someone with glasses")
        npc.image_generation_started()

        result = PassImagePrompt(npc).call()
        self.assertFalse(result)
        self.assertEqual("image_generation_for_this_npc_already_started", result.error)
        self.assertEqual("started", npc.image_generator_state)
