
from pydantic import BaseModel


from npc_creator.operations.gpt.npc.equipment_fill import EquipmentFill
from npc_creator.operations.gpt.npc.generic_fill import GenericFill


class Fill:
    def __init__(self, entity, schema: str = "default"):
        self.entity = entity
        self.schema = schema

    def call(self):
        if self.schema == "sr6equipment":
            result = EquipmentFill(entity=self.entity, schema=self.schema).call()
        else:
            result = GenericFill(entity=self.entity, schema=self.schema).call()

        return result
