
from pydantic import BaseModel


from npc_creator.operations.gpt.npc.equipment_fill import EquipmentFill
from npc_creator.operations.gpt.npc.generic_fill import GenericFill


class Fill:
    def __init__(self, entity, schema: str = "default"):
        self.entity = entity
        self.schema = schema

    def call(self):
        if self.schema == "sr6equipment":
            return EquipmentFill(entity=self.entity, schema=self.schema).call()

        result = GenericFill(entity=self.entity, schema=self.schema).call()

        # The SR6 sheet shows an "Ausrüstung" box, but equipment lives in its
        # own schema with a dedicated prompt. Fill it alongside the sr6 request
        # so the box is populated without a separate client call.
        if self.schema == "sr6":
            EquipmentFill(entity=self.entity, schema="sr6equipment").call()

        return result
