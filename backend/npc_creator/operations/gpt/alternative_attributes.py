from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import entity_prompt
from npc_creator.operations.return_types import Success


class AlternativeAttributes(GptInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gpt = GptInterface.GptVersion.GPT4_TURBO
        self.system_prompt = """
- Es handelt sich um das Pen&Paper Rollenspiel Shadowrun
- Für einen NPC-Generator werden anderen Ideen und Vorschläge für ein Attribute benötigt
- Denke dir stimmige Antworten aus
- Beginne jede Antwort mit "###", ohne Durchnummerierung oder Strich 
- Wiederhole nicht das Attribute
"""

    @property
    def npc(self):
        return self.kwargs["npc"]

    @property
    def attribute(self):
        return self.kwargs.get("attribute", "")

    def prompt(self):
        self.npc.primary_values[self.attribute] = ""
        return entity_prompt(self.npc) + [
            f"Erstelle andere Vorschläge für {self.attribute}:",
        ]

    def interpret_result(self, success):
        return Success(
            [answer.strip() for answer in success.data.split("###") if answer.strip()]
        )
