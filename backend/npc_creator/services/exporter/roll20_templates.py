"""Pydantic models for the Genesis / Roll20 Shadowrun 6E character JSON.

The target is the ``"system": "SHADOWRUN6"`` export format (currently
``version`` ``3.2.0``) that the Roll20 SR6 character sheet's *Import* button
consumes. Field names and casing mirror that schema exactly; unknown sections
are still emitted (as empty lists / ``null``) because the importer expects the
full set of keys.
"""

from typing import Any, List, Optional

from pydantic import BaseModel


class R20Attribute(BaseModel):
    name: str
    id: str
    points: int
    modifiedValue: int


class R20Initiative(BaseModel):
    name: str
    id: str
    value: int
    dice: str


class R20Quality(BaseModel):
    name: str
    id: str
    choice: str
    positive: bool
    rating: int
    page: str
    description: str


class R20Skill(BaseModel):
    name: str
    id: str
    attribute: str
    rating: int
    pool: int
    specializations: List[Any]
    influencedBy: List[Any]
    description: str


class R20CloseCombatWeapon(BaseModel):
    name: str
    type: str
    subtype: str
    skill: Optional[str]
    pool: int
    damage: str
    attackRating: str
    wifi: List[Any]
    accessories: List[Any]
    page: str
    description: str
    primary: bool


class R20LongRangeWeapon(BaseModel):
    name: str
    type: str
    subtype: str
    skill: Optional[str]
    pool: int
    damage: str
    attackRating: str
    mode: Optional[str]
    ammunition: str
    wifi: List[Any]
    accessories: List[Any]
    page: str
    description: str
    primary: bool


class R20Armor(BaseModel):
    name: str
    rating: int
    socialrating: int
    accessories: List[Any]
    isIgnored: bool
    page: str
    description: str
    primary: bool


class R20Augmentation(BaseModel):
    name: str
    level: Optional[int]
    essence: float
    page: str
    quality: Optional[str]
    description: str
    accessories: List[Any]


class R20Item(BaseModel):
    name: str
    count: int
    rating: int
    type: str
    subType: str
    page: str
    accessories: List[Any]
    description: str


class R20MatrixItem(BaseModel):
    name: str
    dataProcessing: int
    firewall: int
    attack: int
    sleaze: int
    deviceRating: int
    type: str
    subType: str
    page: str
    concurrentPrograms: int
    accessories: List[Any]
    programs: List[Any]
    description: str


class R20Sin(BaseModel):
    name: str
    description: Optional[str]
    quality: int


class R20License(BaseModel):
    name: str
    sin: str
    type: Optional[str]
    rating: str


class R20Character(BaseModel):
    system: str
    version: str
    name: Optional[str]
    streetName: str
    metaType: str
    size: int
    weight: int
    age: Optional[int]
    gender: str
    heat: int
    reputation: int
    karma: int
    freeKarma: int
    nuyen: int
    initiation: int
    submersion: int
    attributes: List[R20Attribute]
    initiatives: List[R20Initiative]
    qualities: List[R20Quality]
    skills: List[R20Skill]
    spells: List[Any]
    rituals: List[Any]
    metamagic: Optional[Any]
    echoes: Optional[Any]
    complexForms: List[Any]
    adeptPowers: List[Any]
    longRangeWeapons: List[R20LongRangeWeapon]
    closeCombatWeapons: List[R20CloseCombatWeapon]
    armors: List[R20Armor]
    items: List[R20Item]
    augmentations: List[R20Augmentation]
    vehicles: List[Any]
    drones: List[Any]
    lifestyles: List[Any]
    sins: List[R20Sin]
    contacts: List[Any]
    licenses: List[R20License]
    matrixItems: List[R20MatrixItem]
    martialArts: List[Any]
    signatureManeuvers: List[Any]
    notes: Optional[Any]
