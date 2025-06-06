import os
import tempfile
import unittest
from unittest.mock import patch

from requests.exceptions import RequestException

from npc_creator.services.image_generation.download_midjourney_image import (
    download_midjourney_image,
)


class DownloadMidjourneyImageTest(unittest.TestCase):
    def setUp(self):
        self.url = "https://example.com/image.jpg"
        self.content = b"\x89PNG\r\n\x1a\n\x00"
        self.tempdir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tempdir.cleanup()

    @patch("requests.get")
    def test_download_successful(self, mock_get):
        mock_get.return_value = type(
            "MockResponse", (object,), {"content": self.content}
        )
        local_path = download_midjourney_image(self.tempdir.name, self.url)
        self.assertTrue(os.path.exists(local_path))
        with open(local_path, "rb") as f:
            self.assertEqual(f.read(), self.content)

    @patch("requests.get")
    def test_request_error(self, mock_get):
        mock_get.side_effect = RequestException
        self.assertIsNone(download_midjourney_image(self.tempdir.name, self.url))
