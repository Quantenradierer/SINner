from django.test import TestCase

from npc_creator.models.template_image import TemplateImage


class TestTemplateImage(TestCase):
    def test_template_image_creation(self):
        template_image = TemplateImage.objects.create(
            keyword="troll", url="https://example.com/test.jpg"
        )

        self.assertEqual(template_image.keyword, "troll")
        self.assertEqual(template_image.url, "https://example.com/test.jpg")
        self.assertEqual(template_image.score, 100)
        self.assertIsNotNone(template_image.created_at)

    def test_upvote_increases_score(self):
        template_image = TemplateImage.objects.create(
            keyword="troll", url="https://example.com/test.jpg"
        )

        template_image.upvote()

        self.assertEqual(101, template_image.score)

    def test_downvote_decreases_score(self):
        template_image = TemplateImage.objects.create(
            keyword="troll", url="https://example.com/test.jpg"
        )

        template_image.downvote()

        self.assertEqual(99, template_image.score)

    def test_downvote_does_not_go_below_zero(self):
        template_image = TemplateImage.objects.create(
            keyword="troll", url="https://example.com/test.jpg", score=0
        )

        template_image.downvote()

        self.assertEqual(0, template_image.score)
