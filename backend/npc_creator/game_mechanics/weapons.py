import enum
import json
import os.path
from typing import Literal

from pydantic import BaseModel

from shadowrun.settings import BASE_DIR


class WeaponCategory(enum.Enum):
    """Weapon categories."""

    MELEE = "Melee"
    FIREARM = "Firearm"
    THROWN = "Thrown"
    PROJECTILE = "Projectile"


class WeaponSubtype(enum.Enum):
    HOLD_OUT = "Hold-Out"
    LIGHT_PISTOL = "Light Pistol"
    HEAVY_PISTOL = "Heavy Pistol"
    MACHINE_PISTOL = "Machine Pistol"
    SUBMACHINE_GUN = "Submachine Gun"
    SHOTGUN = "Shotgun"
    RIFLE = "Rifle"
    MACHINE_GUN = "Machine Gun"
    HEAVY_MACHINE_GUN = "Heavy Machine Gun"
    ASSAULT_CANNON = "Assault Cannon"
    EXOTIC = "Exotic"
    GRENADE_LAUNCHER = "Grenade Launcher"
    TASER = "Taser"
    BOW = "Bow"
    CROSSBOW = "Crossbow"
    THROWN = "Thrown"
    CLUB = "Club"
    SAP = "Sap"
    STUN_BATON = "Stun Baton"
    AXE = "Axe"
    KNIFE = "Knife"


class Source(BaseModel):
    page: int
    book: str


class Weapon(BaseModel):
    id: str
    kind: str
    subtype: str
    cnt: str | None
    rating: int | None
    avail: str | None
    price: int | None
    damage: str
    damage_type: Literal[None, "P", "S"]
    damage_note: str | None = None
    ss: bool
    sa: bool
    bf: bool
    fa: bool
    attack_rating: list[int | None]
    name: str
    source: Source
    skill: str


class WeaponLoader:

    def __init__(self):
        self.weapons = {}
        self._load_weapons()

    def _load_weapons(self):
        with open(
            os.path.join(BASE_DIR, "data", "weapons.json"),
            encoding="utf-8",
        ) as json_file:
            for key, weapon_def in json.load(json_file).items():
                self.weapons[key] = Weapon(id=key, **weapon_def)


weapon_loader = WeaponLoader()
