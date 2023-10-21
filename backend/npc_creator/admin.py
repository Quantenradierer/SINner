# Register your models here.

from django.contrib import admin
from npc_creator.models import Npc, Attribute, TemplateImage
from npc_creator.models.gpt_request import GptRequest
from npc_creator.models.panel_image import PanelImage


class InlineAttributeAdmin(admin.TabularInline):
    model = Attribute


@admin.register(Npc)
class NpcAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_url', 'image_generator_description', 'user_prompt', 'state', 'default_image_number')
    inlines = [
        InlineAttributeAdmin,
    ]

    search_fields = ['image_url', 'image_generator_description', 'user_prompt']


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('npc', 'key', 'value')
    search_fields = ['key', 'value']


@admin.register(TemplateImage)
class PanelImageAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'url')
    search_fields = ['keyword', 'url']


@admin.register(GptRequest)
class GptRequestAdmin(admin.ModelAdmin):
    list_display = ('input', 'output', 'created_at')
    search_fields = ['input', 'output']
