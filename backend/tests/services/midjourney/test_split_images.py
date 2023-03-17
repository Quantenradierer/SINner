import os
import tempfile
import unittest
from PIL import Image

from services.midjourney.split_images import split_image


class TestSplitImage(unittest.TestCase):

    def setUp(self):
        # Create a test output directory.
        self.tempdir = tempfile.TemporaryDirectory()

        # Create a test image file.
        self.test_image_path = os.path.join(self.tempdir.name, "test_image.png")
        im = Image.new("RGB", (50, 50), color=(255, 0, 0))
        im.save(self.test_image_path)

    def tearDown(self):
        self.tempdir.cleanup()

    def test_split_image(self):
        # Test splitting the test image.
        split_filenames = split_image(self.test_image_path, self.tempdir.name)

        # Check that 4 files were created.
        self.assertEqual(len(list(split_filenames)), 4)

        # Check that each split file has the expected dimensions.
        for i, split_filename in enumerate(split_filenames):
            split_file_path = os.path.join(self.test_output_path, split_filename)
            with Image.open(split_file_path) as splitted_image:
                self.assertEqual(splitted_image.size, (25, 25))
