import json

from npc_creator.operations.gpt.gpt_interface import GptInterface
from npc_creator.operations.gpt.helper import entity_prompt
from npc_creator.operations.return_types import Success
from npc_creator.services.interpret_gpt import dict_from_text
from filelock import FileLock


class Fill(GptInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_prompt = ""

    @property
    def entity(self):
        return self.kwargs["entity"]

    @property
    def schema(self):
        return self.kwargs.get("schema", "default")

    def prompt(self):
        return (
            [self.entity.prompt]
            + [entity_prompt(self.entity, "default", filled_values=True)]
            + [entity_prompt(self.entity, self.schema, filled_values=False)]
        )

    def interpret_result(self, success):
        attributes = success.data
        self.entity.add_values(attributes)
        self.entity.save()
        return success

    def call(self):
        lock = FileLock(f"lock-{self.entity.uuid}.lock")
        with lock:
            if self.entity.id:
                self.entity.refresh_from_db()
            if self.entity.schema_complete(self.schema):
                return Success()

            return super().call()
