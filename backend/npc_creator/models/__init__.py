"""
Django models for Schattenakte
"""

# Import all models to make them available to Django
from .entity import Entity
from .image import Image
from .image_generation import ImageGeneration
from .gpt_request import GptRequest
from .collection import Collection
from .favorite import Favorite
from .feedback import Feedback
from .template_image import TemplateImage
from .floorplan import FloorplanFile, FloorplanGeneration

__all__ = [
    "Entity",
    "Image",
    "ImageGeneration",
    "GptRequest",
    "Collection",
    "Favorite",
    "Feedback",
    "TemplateImage",
    "FloorplanFile",
    "FloorplanGeneration",
]