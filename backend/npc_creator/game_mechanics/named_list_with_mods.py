import json
import logging
from typing import Self
from typing_extensions import Generator

from pydantic import BaseModel
from npc_creator.game_mechanics.manager import ALL_GEAR, ALL_RULES
from npc_creator.game_mechanics.sr6.gear import Gear
from npc_creator.game_mechanics.startup import startup


class MinimalGear(BaseModel):
    id: str
    mods: list[Self]

    @classmethod
    def from_gear(cls, gear: Gear) -> Self:
        mods = ALL_GEAR.mods_for(gear)
        return cls(id=gear.id, mods=[cls.from_gear(mod) for mod in mods])


def get_minimal_gear_list() -> Generator[str]:
    for gear in ALL_GEAR.values():
        if gear.is_mod:
            continue
        yield gear.id


def as_jsonable(gear):
    d = gear.model_dump()
    if "mods" in d:
        d["mods"] = [as_jsonable(m) for m in gear.mods]
        if not d["mods"]:
            d.pop("mods")
    return d


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    startup()
    gear_list = list(get_minimal_gear_list())
    json_str = json.dumps([as_jsonable(g) for g in gear_list])
    print(json_str)
