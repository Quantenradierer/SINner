from unittest.mock import patch

from django.test import TestCase

from npc_creator.models.entity import Entity
from npc_creator.models.image import Image
from npc_creator.models.image_generation import ImageGeneration
from npc_creator.operations.download_image import DownloadImage


class TestDownloadImage(TestCase):
    def setUp(self):
        self.entity = Entity.objects.create(
            kind=Entity.Kinds.NPC,
            attributes={"name": "Test NPC"},
        )

        self.generation = ImageGeneration.objects.create(
            entity=self.entity,
            url="https://example.com/test_image.png",
            state=ImageGeneration.State.CREATED,
        )

    @patch("npc_creator.operations.download_image.download_midjourney_image")
    @patch("npc_creator.operations.download_image.split_image")
    @patch("npc_creator.operations.download_image.create_thumbnail")
    def test_call_success(
        self, mock_create_thumbnail, mock_split_image, mock_download
    ):
        mock_download.return_value = True
        mock_split_image.return_value = ["test_image_1", "test_image_2"]
        mock_create_thumbnail.return_value = True

        result = DownloadImage(self.generation).call()

        self.assertTrue(result)
        self.assertEqual(["test_image_1", "test_image_2"], result.data)
        self.generation.refresh_from_db()
        self.assertEqual(ImageGeneration.State.DOWNLOADED, self.generation.state)
        image_names = list(
            Image.objects.filter(entity=self.entity).values_list("name", flat=True)
        )
        self.assertEqual(["test_image_1", "test_image_2"], image_names)

    @patch("npc_creator.operations.download_image.download_midjourney_image")
    def test_call_failure_on_download(self, mock_download):
        mock_download.return_value = False

        result = DownloadImage(self.generation).call()

        self.assertFalse(result)
        self.assertEqual("download of midjourney image failed", result.error)

    @patch("npc_creator.operations.download_image.download_midjourney_image")
    @patch("npc_creator.operations.download_image.split_image")
    @patch("npc_creator.operations.download_image.create_thumbnail")
    def test_call_failure_on_thumbnail(
        self, mock_create_thumbnail, mock_split_image, mock_download
    ):
        mock_download.return_value = True
        mock_split_image.return_value = ["test_image_1"]
        mock_create_thumbnail.return_value = False

        result = DownloadImage(self.generation).call()

        self.assertFalse(result)
        self.assertEqual("thumbnail creation failed", result.error)

    def test_add_images_creates_an_image_per_path(self):
        downloader = DownloadImage(self.generation)
        downloader.add_images(["test1.jpg", "test2.jpg"])

        created_images = Image.objects.filter(generation=self.generation)
        self.assertEqual(2, created_images.count())
        image_names = [img.name for img in created_images]
        self.assertIn("test1.jpg", image_names)
        self.assertIn("test2.jpg", image_names)
