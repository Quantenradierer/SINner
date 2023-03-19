import unittest
from unittest.mock import patch, Mock
import os

from npc_creator.services.midjourney.retrieve_latest_messages import retrieve_latest_messages

SERVER_ID = os.getenv('MJ_SERVER_ID')
CHANNEL_ID = os.getenv('MJ_CHANNEL_ID')
PRIVATE_DISCORD_TOKEN = os.getenv('MJ_PRIVATE_DISCORD_TOKEN')

class TestRetrieveLatestMessages(unittest.TestCase):

    @patch('requests.get')
    def test_returns_list_of_messages(self, mock_get):
        expected_messages = [
            {"id": 1, "content": "Message 1"},
            {"id": 2, "content": "Message 2"}
        ]
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_messages
        mock_get.return_value = mock_response

        result = retrieve_latest_messages()

        self.assertEqual(result, expected_messages)

    @patch('requests.get')
    def test_correct_discord_channel(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        retrieve_latest_messages()

        mock_get.assert_called_once_with(
            f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages',
            headers={
                "Authorization": PRIVATE_DISCORD_TOKEN,
                "Content-Type": "application/json"
            },
            params={"limit": 50}
        )


    @patch('requests.get')
    def test_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'id': '1', 'content': 'Hello'}, {'id': '2', 'content': 'World'}]

        result = retrieve_latest_messages()

        self.assertEqual(result, [{'id': '1', 'content': 'Hello'}, {'id': '2', 'content': 'World'}])
        mock_get.assert_called_once_with(
            f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages',
            headers={
                "Authorization": PRIVATE_DISCORD_TOKEN,
                "Content-Type": "application/json"
            },
            params={
                "limit": 50
            }
        )

    @patch('requests.get')
    def test_http_error(self, mock_get):
        mock_get.return_value.status_code = 404

        result = retrieve_latest_messages()

        self.assertListEqual([], result)
        mock_get.assert_called_once_with(
            f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages',
            headers={
                "Authorization": PRIVATE_DISCORD_TOKEN,
                "Content-Type": "application/json"
            },
            params={
                "limit": 50
            }
        )
