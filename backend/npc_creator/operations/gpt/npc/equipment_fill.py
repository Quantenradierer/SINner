from npc_creator.game_mechanics.manager import ALL_GEAR, GearManager
from npc_creator.game_mechanics.named_list_with_mods import (
    as_jsonable,
    get_minimal_gear_list,
)
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.operations.gpt import entity
import json


class EquipmentFill(entity.Fill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = f"""- Vervollständige einen NPC für ein Shadowrun Pen & Paper Rollenspiel
- Gib eine Menge von Ausrüstung des Charakters an
- Antworte nur die Ausrüstungsliste, gib dabei eine JSON Liste mit den IDs der Ausrüstung zurück 
- Die letzte Zahl in der ID steht für die Stufe der Ausrüstung
- Gib keine Cyberdecks in der Ausrüstung, es sei den der Charakter ist ein Decker (und hat Cracken)
- Gib eine Kleidung, mindestens eine Waffe und etwa 10 andere Gegenstände  

Verfügbare Ausrüstung: 
{self._equipment_json()}
"""

    def _equipment_json(self):
        gear_list = list(get_minimal_gear_list())
        return json.dumps(list(gear_list))

    def interpret_result(self, success):
        print('XXXX', success.data)
