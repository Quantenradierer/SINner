from django.apps import AppConfig

from npc_creator.game_mechanics.startup import startup


class NpcCreatorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "npc_creator"

    def ready(self):
        startup()
