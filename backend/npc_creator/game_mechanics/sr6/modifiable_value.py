from enum import IntEnum
from pydantic import BaseModel, Field, model_validator


class ModifiableValue(BaseModel):
    points: int = Field(default=0)
    mods: list["Rule"] = Field(default_factory=list)

    @property
    def mod(self) -> int:
        modified_value = self.points
        for mod in self.mods:
            modified_value = mod.calc(modified_value)

        return modified_value

    @model_validator(mode="before")
    @classmethod
    def convert_int(cls, value):
        if isinstance(value, int):
            return {"points": value}
        return value


class ModifiableValueStr(BaseModel):
    value: str | None = None
    mods: list["Rule"] = Field(default_factory=list)

    @property
    def mod(self) -> int:
        modified_value = self.value
        for mod in self.mods:
            modified_value = mod.calc(modified_value)

        return modified_value

    @model_validator(mode="before")
    @classmethod
    def convert_str(cls, value):
        if isinstance(value, str):
            return {"value": value}
        if value is None:
            return {"value": value}
        return value


from .rule import Rule
