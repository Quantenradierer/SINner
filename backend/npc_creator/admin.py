# Register your models here.

from django.contrib import admin
from npc_creator.models import Npc, Attribute


class InlineAttributeAdmin(admin.TabularInline):
    model = Attribute


@admin.register(Npc)
class NpcAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_url', 'image_generator_state', 'image_generator_description', 'user_prompt', 'state')
    inlines = [
        InlineAttributeAdmin,
    ]

    search_fields = ['image_url', 'image_generator_state', 'image_generator_description', 'user_prompt']


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('npc', 'key', 'value')

    search_fields = ['key', 'value']
