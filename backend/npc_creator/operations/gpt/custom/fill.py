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

        if self.entity.language == self.entity.Languages.ENGLISH:
            self.system_prompt = (
                "- You are an illustrator with 100 years of experience\r\n"
                "- Answer ONLY as JSON in the format {'appearance': 'A good description for an image generator'}\r\n"
                "- The JSON may only contain this one string and no further objects/nesting\r\n"
                "- Do not ask for details, make up details yourself\r\n"
                "- Fill in the appearance based on the input\r\n"
                "- Always output something new instead of repeating the input\r\n"
            )

    def prompt(self):
        return [
            self.entity.prompt,
        ]

    def interpret_result(self, success):
        values = success.data

        self.entity.add_values(values)
        return success
