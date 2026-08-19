import logging
from enum import StrEnum
from typing import Any, Literal, cast
from pydantic import BaseModel, ConfigDict, Field


from npc_creator.game_mechanics.sr6.eval_errors import NotExistingAttributeError
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.game_mechanics.sr6.source import Source
from simpleeval import EvalWithCompoundTypes, NameNotDefined, simple_eval


class ModifierType(StrEnum):
    BASE = "BASE"
    REPLACEMENT = "REPLACEMENT"
    ADD = "ADD"
    LIMIT = "LIMIT"


class Rule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    modifies: str
    modifier_type: Literal["BASE", "REPLACEMENT", "ADD", "LIMIT"]
    modification: str
    enable: str | None = None
    source: Source

    context: dict[str, Any] = Field(default_factory=dict)

    @property
    def modifies_types(self) -> ObjectType:
        return ObjectType(self.modifies.split(".")[0])

    def eval_modifies(
        self, context: dict[str, Any]
    ) -> list["ModifiableValue"]:  # pyright: ignore [reportExplicitAny]
        try:
            result = EvalWithCompoundTypes(names=context).eval(
                self.modifies
            )  # pyright: ignore [reportReturnType, reportUnknownMemberType)]
            if isinstance(result, list):
                return result
            return [result]
        except NameNotDefined:
            logging.error(f"Available context: {self.context}")
            raise

    def calc(self, value: int) -> int:
        try:
            result: int = cast(
                int,
                simple_eval(
                    self.modification,
                    names={"value": value, **self.context},
                    functions={"min": min, "max": max},
                ),
            )
        except NameNotDefined:
            logging.error(f"Available context: {self.context}")
            raise

        except NotExistingAttributeError:
            return value

        if self.modifier_type == ModifierType.BASE:
            return result
        elif self.modifier_type == ModifierType.REPLACEMENT:
            return result
        elif self.modifier_type == ModifierType.ADD:
            return value + result
        elif self.modifier_type == ModifierType.LIMIT:
            return result
        raise NotImplementedError(f"Unknown modifier type: {self.modifier_type}")


from .modifiable_value import ModifiableValue
