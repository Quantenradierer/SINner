import copy
import logging
from typing import Self
from pydantic import BaseModel, Field, model_validator

from npc_creator.game_mechanics.sr6.object_type import ObjectType


class ModifiableObject(BaseModel):
    type: ObjectType

    gear: "GearCollection"

    context: dict[str, "ModifiableObject"] = Field(default_factory=dict)
    apply_rules_str: list[str] = Field(default_factory=list, alias="wear_rules")
    apply_rules: list["Rule"] = Field(default_factory=list)
    enabled: bool = True

    @model_validator(mode="after")
    def add_self_context(self) -> Self:
        self.context[str(self.type)] = self
        return self

    @model_validator(mode="after")
    def validate_rules_exist(self) -> Self:
        from npc_creator.game_mechanics.manager import ALL_RULES

        for rulename in self.apply_rules_str:
            if rulename not in ALL_RULES:
                raise AttributeError(f"Rule '{rulename}' does not exist")
        return self

    def add_gear(self, gear: "ModifiableObject") -> None:
        from npc_creator.game_mechanics.manager import ALL_RULES

        gear.context.update({str(self.type): self, **self.context})
        self.gear.append(gear)

        for rulename in gear.apply_rules_str:
            rule = ALL_RULES[rulename]
            gear.apply_rule(rule)

    def apply_rule(self, org_rule: "Rule"):

        modifies_list = org_rule.eval_modifies(self.context)
        for modifies in modifies_list:
            rule = copy.deepcopy(org_rule)
            rule.context = self.context
            modifies.mods.append(rule)

            order = ["BASE", "REPLACEMENT", "ADD", "LIMIT"]
            order_map = {v: i for i, v in enumerate(order)}
            modifies.mods.sort(key=lambda obj: order_map[obj.modifier_type])

            self.apply_rules.append(rule)


from .rule import Rule
from .gear_collection import GearCollection
