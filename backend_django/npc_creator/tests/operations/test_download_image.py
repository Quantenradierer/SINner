import os
from unittest.mock import patch

import requests

from npc_creator.models.npc import Npc
from npc_creator.operations.download_image import DownloadImage
from npc_creator.tests.mocks.mock_return_discord_messages import mock_return_discord_messages
from npc_creator.tests.mocks.mock_download_image import mock_download_image
from npc_creator.tests.operations.base_integration_test import BaseIntegrationTest


class TestDownloadImage(BaseIntegrationTest):
    def setUp(self):
        super().setUp()

        self.npc_id = 123

    def tearDown(self):
        super().tearDown()

    @patch('requests.get')
    def test_call_success(self, get_mock):
        get_mock.side_effect = [mock_return_discord_messages(), mock_download_image()]
        npc = Npc(id=self.npc_id, image_generator_description='with a PNG attachment')
        npc.image_generation_started()

        with patch('config.PUBLIC_NPC_IMAGE_PATH', self.tempdir.name):
            self.assertTrue(DownloadImage(npc, self.tempdir.name).call())

        self.assertIsNotNone(npc.image_url)
        with open(os.path.join(self.tempdir.name, npc.image_url), "rb") as f:
            self.assertTrue(f.readable())

    @patch('requests.get')
    def test_call_cant_find_message(self, get_mock):
        get_mock.side_effect = [mock_return_discord_messages(), mock_download_image()]
        npc = Npc(id=self.npc_id, image_generator_description='No useful description')
        npc.image_generation_started()

        result = DownloadImage(npc, self.tempdir.name).call()

        self.assertFalse(result)
        self.assertEqual('could not find the correlated response or a OVERRIDE response', result.error)

    @patch('requests.get')
    def test_call_image_unreadable(self, get_mock):
        image_request_mock = mock_download_image()
        image_request_mock.content = b'invalid_data'
        get_mock.side_effect = [mock_return_discord_messages(), image_request_mock]
        npc = Npc(id=self.npc_id, image_generator_description='with a PNG attachment')
        npc.image_generation_started()

        result = DownloadImage(npc, self.tempdir.name).call()

        self.assertFalse(result)
        self.assertEqual('no image could be extracted', result.error)

    @patch('requests.get')
    def test_call_npc_has_already_image(self, get_mock):
        get_mock.side_effect = [mock_return_discord_messages(), mock_download_image()]
        npc = Npc(id=self.npc_id, image_generator_description='with a PNG attachment')
        npc.image_generation_started()
        npc.add_image('example.png')

        result = DownloadImage(npc, self.tempdir.name).call()
        self.assertFalse(result)
        self.assertEqual('npc does not require an image download', result.error)

    @patch('requests.get')
    def test_call_no_discord_messages(self, get_mock):
        discord_mock = mock_return_discord_messages()
        discord_mock.json.return_value  = []
        get_mock.side_effect = [discord_mock, mock_download_image()]
        npc = Npc(id=self.npc_id, image_generator_description='with a PNG attachment')
        npc.image_generation_started()

        npc.image_generation_started()

        result = DownloadImage(npc, self.tempdir.name).call()
        self.assertFalse(result)
        self.assertEqual('could not find the correlated response or a OVERRIDE response', result.error)

    @patch('requests.get')
    def test_call_no_discord_messages(self, get_mock):
        discord_mock = mock_return_discord_messages()
        discord_mock.json.return_value = []
        get_mock.side_effect = [discord_mock, mock_download_image()]
        npc = Npc(id=self.npc_id, image_generator_description='with a PNG attachment')
        npc.image_generation_started()

        result = DownloadImage(npc, self.tempdir.name).call()
        self.assertFalse(result)
        self.assertEqual('could not find the correlated response or a OVERRIDE response', result.error)


    @patch('requests.get')
    def test_call_success(self, get_mock):
        get_mock.side_effect = [mock_return_discord_messages(), requests.exceptions.RequestException()]
        npc = Npc(id=self.npc_id, image_generator_description='with a PNG attachment')
        npc.image_generation_started()

        result = DownloadImage(npc, self.tempdir.name).call()
        self.assertFalse(result)
        self.assertEqual('download of midjourney image failed', result.error)

    @patch('requests.get')
    def test_call_success(self, get_mock):
        get_mock.side_effect = [mock_return_discord_messages(), requests.exceptions.RequestException()]
        npc = Npc(id=self.npc_id, image_generator_description='with a PNG attachment')
        npc.image_generation_started()

        result = DownloadImage(npc, self.tempdir.name).call()
        self.assertFalse(result)
        self.assertEqual('download of midjourney image failed', result.error)

    @patch('requests.get')
    def test_call_discord_unavailable(self, get_mock):
        get_mock.side_effect = [requests.exceptions.RequestException()]
        npc = Npc(id=self.npc_id, image_generator_description='with a PNG attachment')
        npc.image_generation_started()

        result = DownloadImage(npc, self.tempdir.name).call()
        self.assertFalse(result)
        self.assertEqual('could not find the correlated response or a OVERRIDE response', result.error)
