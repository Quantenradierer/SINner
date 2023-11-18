import json

from npc_creator.operations.gpt import entity


class Fill(entity.Fill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_json = True
        self.system_prompt = """- Vervollständige eine Location für ein Shadowrun Pen & Paper Rollenspiel
- Wenn keine Informationen gegeben sind, denke dir welche aus
- Achte darauf, den NPC in die Shadowrun-Welt zu integrieren und ihn für die Spieler ansprechend zu gestalten
- Antworte als JSON, wobei nur strings erlaubt sind
"""

    def interpret_result(self, success):
        values = json.loads(success.data)

        self.entity.add_values(values)
        return success
