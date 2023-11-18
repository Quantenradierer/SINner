from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import entity_prompt
from npc_creator.operations.return_types import Failure


class Check:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = (
            "- Antworte NUR mit 'Ok' oder mit einer Erklärung abgelehnt wurde"
            "- Die Attribute sollten einen NPC einen Shadowrun darstellen"
            "- Prüf ob die Daten inhaltlich passen"
            "- Verwirf Urheberrechtsverletzungen oder zu extreme Namen oder Beschreibungen"
            "- Der NPC sollte eine gewisse Qualität haben"
        )
        self.gpt = GptInterface.GptVersion.GPT4_TURBO

    @property
    def entity(self):
        return self.kwargs["entity"]

    def prompt(self):
        return [self.user_prompt] + entity_prompt(self.entity)

    def interpret_result(self, success):
        if (
            success.data.lower().strip() == "ok"
            or success.data.lower().strip() == "ok."
        ):
            return success
        return Failure(success.data)
