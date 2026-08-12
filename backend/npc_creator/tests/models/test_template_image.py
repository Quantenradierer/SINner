import unittest

from django.test import TestCase
from django.contrib.auth import get_user_model

from npc_creator.models.template_image import TemplateImage

User = get_user_model()


class TestTemplateImage(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )

    def test_template_image_creation(self):
        """Test that a template image can be created successfully."""
        template_image = TemplateImage.objects.create(
            name="Test Template",
            user=self.user,
            image_url="https://example.com/test.jpg"
        )
        
        self.assertEqual(template_image.name, "Test Template")
        self.assertEqual(template_image.user, self.user)
        self.assertEqual(template_image.image_url, "https://example.com/test.jpg")
        self.assertIsNotNone(template_image.created_at)

    def test_template_image_str_representation(self):
        """Test that the string representation is correct."""
        template_image = TemplateImage.objects.create(
            name="Test Template",
            user=self.user,
            image_url="https://example.com/test.jpg"
        )
        expected_str = f"TemplateImage: {template_image.name}"
        self.assertEqual(str(template_image), expected_str)