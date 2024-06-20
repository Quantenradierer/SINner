from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import entity_prompt
from npc_creator.operations.return_types import Failure


class Check(GptInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = (
            "- Antworte als JSON leeres object, wenn alles in Ordnung ist. Ansonsten beschreibe das Problem in der Form: {'attribute': 'problem'}"
            "- Prüf ob die Daten inhaltlich passen"
            "- Verwirf Urheberrechtsverletzungen oder zu extreme Namen oder Beschreibungen"
            "- Es sollte eine gewisse Qualität haben"
        )

    @property
    def entity(self):
        return self.kwargs["entity"]

    def prompt(self):
        return entity_prompt(self.entity)

    def interpret_result(self, success):
        if not success.data:
            return success
        return Failure(success.data)
