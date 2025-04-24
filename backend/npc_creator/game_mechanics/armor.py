import enum
import json
import os.path
from typing import Literal

from pydantic import BaseModel

from shadowrun.settings import BASE_DIR


class Source(BaseModel):
    page: int
    book: str


class Armor(BaseModel):
    id: str
    type: str
    subtype: str
    name: str
    defense_rating: int
    capacity: int
    availability: int
    cost: int
    source: Source


class ArmorLoader:

    def __init__(self):
        self.armors = {}
        self._load_armors()

    def _load_armors(self):
        with open(
            os.path.join(BASE_DIR, "data", "armors.json"),
            encoding="utf-8",
        ) as json_file:
            for key, armor_def in json.load(json_file).items():
                self.armors[key] = Armor(id=key, **armor_def)


armor_loader = ArmorLoader()
