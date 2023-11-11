# Register your models here.

from django.contrib import admin
from npc_creator.models import Entity, TemplateImage
from npc_creator.models.gpt_request import GptRequest
from npc_creator.models.image import Image
from npc_creator.models.image_generation import ImageGeneration


@admin.register(Entity)
class NpcAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image_generator_description"
    )

    search_fields = ["image_generator_description"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("template", "npc", "created_at", "updated_at")
    search_fields = ["template", "npc", "created_at", "updated_at"]


@admin.register(ImageGeneration)
class ImageGenerationAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "retry_count",
        "url",
        "npc",
        "created_at",
        "updated_at",
    )
    search_fields = [
        "description",
        "retry_count",
        "url",
        "npc",
        "created_at",
        "updated_at",
    ]


@admin.register(GptRequest)
class GptRequestAdmin(admin.ModelAdmin):
    list_display = ("kind", "input", "output", "created_at")
    search_fields = ["kind", "input", "output", "created_at"]


@admin.register(TemplateImage)
class TemplateImageAdmin(admin.ModelAdmin):
    list_display = ("keyword", "url", "score", "created_at", "updated_at")
    search_fields = ["keyword", "url", "score", "created_at", "updated_at"]
