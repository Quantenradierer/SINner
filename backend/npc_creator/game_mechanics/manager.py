from collections import UserDict
import logging
from typing import Self
from npc_creator.game_mechanics.sr6.books import Rulebook
from npc_creator.game_mechanics.sr6.gear import Gear
from npc_creator.game_mechanics.sr6.gear_collection import GearCollection
from npc_creator.game_mechanics.sr6.modifiable_object import ModifiableObject
from npc_creator.game_mechanics.sr6.modifiable_value import ModifiableValue
from npc_creator.game_mechanics.sr6.object_type import ObjectType
from npc_creator.game_mechanics.sr6.rule import ModifierType, Rule

_ = ModifiableValue.model_rebuild()
_ = ModifiableObject.model_rebuild()
_ = Gear.model_rebuild()
_ = GearCollection.model_rebuild()
_ = Rule.model_rebuild()


class GearManager(UserDict[str, Gear]):
    def add(self, gear: Gear) -> None:
        if gear.id in self.data:
            logging.warning(f"Duplicate gear {gear.id}")
        self.data[gear.id] = gear

    def only(self, object_type: ObjectType) -> Self:
        return self.__class__(
            **{k: g for k, g in self.data.items() if g.type == object_type}
        )

    def _fits_mod_requirements(self, gear: Gear, mod: Gear):
        # is no mod for other gear
        if mod.mod_for is None:
            return False

        result = []
        for key, values in mod.mod_for.items():
            requirements: str | list[str] = getattr(gear, key)
            if requirements is None:
                return False

            if isinstance(requirements, str):
                requirements = [requirements]
            if isinstance(values, str):
                values = [values]
            fits = bool(set(requirements).intersection(set(values)))
            result.append(fits)
        return all(result)

    def mods_for(self, gear: Gear):
        for mod in self.values():
            if self._fits_mod_requirements(gear, mod):
                yield mod


class RulesManager(UserDict[str, Rule]):
    def add(self, rule: Rule):
        if rule.id in self.data:
            logging.warning(f"Duplicate rule {rule.id}")
        self.data[rule.id] = rule

    def only_rulebooks(self, rulebooks: list[Rulebook]) -> Self:
        return self.__class__(
            {k: v for k, v in self.data.items() if v.source.book in rulebooks}
        )

    def only_modifier_type(self, type: ModifierType) -> Self:
        return self.__class__(
            {k: v for k, v in self.data.items() if v.modifier_type == type}
        )

    def filter(self, rulenames: list[str]) -> Self:
        return self.__class__({name: self.data[name] for name in rulenames})


ALL_GEAR = GearManager()
ALL_RULES = RulesManager()
