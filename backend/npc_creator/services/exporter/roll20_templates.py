from typing import List, Optional, Any
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


class R20Weapon(BaseModel):
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


class R20Item(BaseModel):
    name: str
    count: int
    rating: int
    type: str
    subType: str
    page: str
    accessories: List[Any]
    description: str


class R20Drone(BaseModel):
    name: str
    type: Optional[str]
    subtype: Optional[str]
    count: int
    handlOn: int
    handlOff: int
    accelOn: int
    accelOff: int
    speedIntOn: int
    speedIntOff: int
    speed: int
    body: int
    armor: int
    pilot: int
    sensor: int
    page: str
    accessories: Optional[Any]
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
    longRangeWeapons: List[Any]
    closeCombatWeapons: List[R20Weapon]
    armors: List[Any]
    items: List[R20Item]
    augmentations: List[Any]
    vehicles: List[Any]
    drones: List[R20Drone]
    lifestyles: List[Any]
    sins: List[Any]
    contacts: List[Any]
    licenses: List[Any]
    matrixItems: List[R20MatrixItem]
    martialArts: List[Any]
    signatureManeuvers: List[Any]
    notes: Optional[Any]
