import io
import os
import tempfile
import unittest

from PIL import Image

from npc_creator.services.image_generation.split_images import split_image_to_bytes


class TestSplitImage(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.test_image_path = os.path.join(self.tempdir.name, "test_image.png")
        Image.new("RGB", (50, 50), color=(255, 0, 0)).save(self.test_image_path)

    def tearDown(self):
        self.tempdir.cleanup()

    def test_split_image_returns_four_quadrants_as_bytes(self):
        quadrants = split_image_to_bytes(self.test_image_path)

        self.assertEqual(4, len(quadrants))
        for data in quadrants:
            with Image.open(io.BytesIO(data)) as quadrant:
                self.assertEqual((25, 25), quadrant.size)

    def test_source_file_is_removed(self):
        split_image_to_bytes(self.test_image_path)
        self.assertFalse(os.path.exists(self.test_image_path))

    def test_unreadable_source_returns_empty_list(self):
        bad_path = os.path.join(self.tempdir.name, "not_an_image.png")
        with open(bad_path, "w") as f:
            f.write("nope")
        self.assertEqual([], split_image_to_bytes(bad_path))
