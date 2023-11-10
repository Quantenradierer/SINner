from npc_creator.operations.gpt.fill_npc import FillNpc

from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.return_types import Failure


class CheckNpc(FillNpc):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = "- Antworte NUR mit 'Ok' oder mit einer Erklärung warum der NPC abgelehnt wurde \n- Die Attribute sollten einen NPC einen Shadowrun darstellen\n- Prüf ob die Daten inhaltlich passen\n- Verwirf Urheberrechtsverletzungen oder zu extreme Namen oder Beschreibungen\n- Der NPC sollte eine gewisse Qualität haben"
        self.gpt = GptInterface.GptVersion.GPT4_TURBO

    def interpret_result(self, success):
        if success.data.lower() == "ok":
            return success
        return Failure(success.data)
