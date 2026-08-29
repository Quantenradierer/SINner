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
    @patch("npc_creator.operations.download_image.split_image_to_bytes")
    def test_call_success_stores_one_image_per_quadrant(
        self, mock_split, mock_download
    ):
        mock_download.return_value = True
        mock_split.return_value = [b"q1", b"q2"]

        with patch(
            "npc_creator.operations.download_image.store_entity_image"
        ) as mock_store:
            mock_store.side_effect = lambda data, entity, generation: Image.objects.create(
                entity=entity, generation=generation, name=data.decode()
            )
            result = DownloadImage(self.generation).call()

        self.assertTrue(result)
        self.assertEqual(2, len(result.data))
        self.generation.refresh_from_db()
        self.assertEqual(ImageGeneration.State.DOWNLOADED, self.generation.state)
        self.assertEqual(2, Image.objects.filter(entity=self.entity).count())

    @patch("npc_creator.operations.download_image.download_midjourney_image")
    def test_call_failure_on_download(self, mock_download):
        mock_download.return_value = False

        result = DownloadImage(self.generation).call()

        self.assertFalse(result)
        self.assertEqual("download of midjourney image failed", result.error)

    @patch("npc_creator.operations.download_image.download_midjourney_image")
    @patch("npc_creator.operations.download_image.split_image_to_bytes")
    def test_call_failure_when_split_yields_nothing(self, mock_split, mock_download):
        mock_download.return_value = True
        mock_split.return_value = []

        result = DownloadImage(self.generation).call()

        self.assertFalse(result)
        self.assertEqual("splitting the midjourney image failed", result.error)
