from npc_creator.operations.gpt.npc.generic_fill import GenericFill
from npc_creator.operations.jev.equipment_fill import JevEquipmentFill
from npc_creator.operations.jev.sr5_fill import JevSr5Fill
from npc_creator.operations.jev.sr6_fill import JevSr6Fill


class Fill:
    def __init__(self, entity, schema: str = "default"):
        self.entity = entity
        self.schema = schema

    def call(self):
        if self.schema == "sr6equipment":
            return JevEquipmentFill(entity=self.entity, schema=self.schema).call()
        if self.schema == "sr5":
            return JevSr5Fill(entity=self.entity, schema=self.schema).call()
        if self.schema == "sr6":
            result = JevSr6Fill(entity=self.entity, schema=self.schema).call()
            # The SR6 sheet shows an "Ausrüstung" box, but equipment lives in
            # its own schema. Fill it alongside the sr6 request so the box is
            # populated without a separate client call.
            JevEquipmentFill(entity=self.entity, schema="sr6equipment").call()
            return result

        return GenericFill(entity=self.entity, schema=self.schema).call()
