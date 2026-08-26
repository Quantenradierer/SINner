from enum import StrEnum
from typing import Literal

from pydantic import ConfigDict, Field


from npc_creator.game_mechanics.sr6.modifiable_object import ModifiableObject
from npc_creator.game_mechanics.sr6.modifiable_value import (
    ModifiableValue,
    ModifiableValueStr,
)
from npc_creator.game_mechanics.sr6.source import Source


class WeaponCategory(StrEnum):
    MELEE = "Melee"
    FIREARM = "Firearm"
    THROWN = "Thrown"
    PROJECTILE = "Projectile"


class WeaponSubtype(StrEnum):
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


class Gear(ModifiableObject):
    model_config = ConfigDict(extra="forbid")

    id: str
    subtype: str = ""

    mod_for: dict[str, str | list[str]] | None = None
    replacement: list[str] | None = None
    add_gears: list[str] | None = None

    source: Source

    cost: int
    avail: str

    capacity: int | None = None

    max_value: int | None = None  # credsticks

    # technical devices
    device_rating: int | None = None

    # cyberdeck/commlink
    active_program_slots: ModifiableValue = Field(default_factory=ModifiableValue)
    A: ModifiableValue = Field(default_factory=ModifiableValue)
    S: ModifiableValue = Field(default_factory=ModifiableValue)
    D: ModifiableValue = Field(default_factory=ModifiableValue)
    F: ModifiableValue = Field(default_factory=ModifiableValue)

    # armor
    defense_rating: int | None = None

    # weapon
    cnt: str | None = None
    rating: int | None = None
    damage: ModifiableValue = Field(default_factory=ModifiableValue)
    damage_type: ModifiableValueStr = Field(
        default_factory=ModifiableValueStr
    )  # Literal[None, "P", "S"] = None
    damage_note: str | None = None
    ss: bool | None = None
    sa: bool | None = None
    bf: bool | None = None
    fa: bool | None = None
    attack_rating_0: ModifiableValue = Field(default_factory=ModifiableValue)
    attack_rating_1: ModifiableValue = Field(default_factory=ModifiableValue)
    attack_rating_2: ModifiableValue = Field(default_factory=ModifiableValue)
    attack_rating_3: ModifiableValue = Field(default_factory=ModifiableValue)
    attack_rating_4: ModifiableValue = Field(default_factory=ModifiableValue)
    skill: str | None = None
    attack_dices: ModifiableValue = Field(default_factory=ModifiableValue)

    # bodyware
    essence: float | None = None

    mount: str | None = None
    rule: str | None = None

    @property
    def is_mod(self):
        return bool(self.mod_for)

    def __repr__(self):
        return f"<Gear: {self.id}>"
