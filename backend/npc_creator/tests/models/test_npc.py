import unittest
from django.test import TestCase

from npc_creator import config
from npc_creator.models import Npc, Attribute


class TestNpcModel(TestCase):

    def test_has_image_description(self):
        npc = Npc(image_generator_description="Test description")
        self.assertEqual(npc.has_image_description(), True)

    def test_image_generation_started(self):
        npc = Npc()
        npc.image_generation_started()
        self.assertEqual(npc.image_generator_state, 'started')

    def test_add_image(self):
        npc = Npc()
        npc.add_image("http://test.invalid/image.jpg")
        self.assertEqual(npc.image_url, "http://test.invalid/image.jpg")
        self.assertEqual(npc.image_generator_state, 'done')

    def test_image_generation_failed(self):
        npc = Npc()
        npc.image_generation_failed()
        self.assertEqual(npc.image_generator_state, 'failed')

    def test_image_generation_used_banned_word(self):
        npc = Npc()
        npc.add_attributes({config.VISUAL_APPEARANCE_ATTRIBUTE: 'some banned word'})

        npc.image_generation_used_banned_word()
        self.assertEqual(npc.image_generator_state, 'banned')
        self.assertEqual(npc.image_generator_description, '')
        self.assertEqual(npc.attributes.get(config.VISUAL_APPEARANCE_ATTRIBUTE), '')

    def test_requires_image_generation(self):
        npc = Npc(image_generator_description="Test description")
        self.assertEqual(npc.requires_image_generation(), True)

    def test_requires_image_download(self):
        npc = Npc(image_generator_state='started')
        self.assertEqual(npc.requires_image_download(), True)

    def test_requires_new_image_generator_description(self):
        npc = Npc(image_generator_state='failed')
        self.assertEqual(npc.requires_new_image_generator_description(), True)


class TestAttributeModel(TestCase):
    def test_repr(self):
        npc = Npc.objects.create()
        attr = Attribute(npc=npc, key="test_key", value="test_value")
        self.assertEqual(repr(attr), f'<models.Attribute id={attr.id} key=test_key value=test_value npc_id={npc.id}>')


if __name__ == '__main__':
    unittest.main()