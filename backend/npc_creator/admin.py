# Register your models here.

from django.contrib import admin
from npc_creator.models import Entity, TemplateImage
from npc_creator.models.collection import Collection
from npc_creator.models.favorite import Favorite
from npc_creator.models.feedback import Feedback
from npc_creator.models.gpt_request import GptRequest
from npc_creator.models.image import Image
from npc_creator.models.image_generation import ImageGeneration


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ("id", "kind", "image_generator_description")

    search_fields = ["image_generator_description"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "score", "template", "entity", "created_at", "updated_at")
    search_fields = ["name", "score", "template", "entity", "created_at", "updated_at"]


@admin.register(ImageGeneration)
class ImageGenerationAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "template",
        "retry_count",
        "url",
        "entity",
        "created_at",
        "updated_at",
    )
    search_fields = [
        "description",
        "template",
        "retry_count",
        "url",
        "entity",
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


@admin.register(Feedback)
class TemplateImageAdmin(admin.ModelAdmin):
    list_display = ("comment", "email")
    search_fields = ["comment", "email"]


class FavoriteInline(admin.TabularInline):
    model = Favorite
    extra = 0


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

    inlines = [FavoriteInline]
