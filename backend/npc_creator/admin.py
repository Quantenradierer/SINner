# Register your models here.

from django.contrib import admin
from npc_creator.models import Npc, Attribute


class InlineAttributeAdmin(admin.TabularInline):
    model = Attribute


@admin.register(Npc)
class NpcAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_url', 'image_generator_state', 'image_generator_description')
    inlines = [
        InlineAttributeAdmin,
    ]


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value', 'npc')
