from npc_creator.models import Entity
from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import entity_prompt
from npc_creator.services.exporter.foundry import foundry_json
from npc_creator.services.interpret_gpt import dict_from_text
from npc_creator.operations.gpt import entity


class Export:
    def __init__(self, entity: Entity, format: str):
        self.entity = entity
        self.format = format

    def call(self):
        raise RuntimeError("Unsupported export format.")
