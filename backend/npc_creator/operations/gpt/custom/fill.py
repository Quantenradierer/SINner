import json

from npc_creator.operations.gpt import entity


class Fill(entity.Fill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_json = True
        self.system_prompt = (
            "- Du bist ein Illustrator mit 100 Jahren Erfahrung\r\n"
            "- Antworte NUR als JSON in dem Format {'Aussehen': 'Eine gute Beschreibung für einen Bildgenerator'}\r\n"
            "- Das JSON darf nur diesen einen String und keine weiteren Objects/Vertiefungen enthalten\r\n"
            "- Frage nicht nach Details, sondern denke dir selbst Details aus\r\n"
            "- Fülle anhand der Eingabe das Aussehen aus \r\n"
            "- Gib immer etwas neues aus, statt die Eingabe zu wiederholen\r\n"
        )

    def prompt(self):
        return [self.user_prompt] + [
            f"Aussehen: {self.entity.primary_values['Aussehen']}"
        ]

    def json_format(self):
        return json.dumps(
            {
                (attr.name, attr.additional_data)
                for attr in self.entity.ATTRIBUTE_DEFINITION
            }
        )

    def interpret_result(self, success):
        values = json.loads(success.data)

        self.entity.add_values(values)
        return success
