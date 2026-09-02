"""Pydantic models mirroring the Foundry VTT ``shadowrun6-eden`` data model.

These describe the JSON that the eden system's native *Import Data* action
expects for an Actor of type ``npc`` (Foundry v10+ data model, so the actor
payload lives under ``system``, not the legacy ``data`` key).

The shapes are transcribed from the system's ``template.json``:
https://bitbucket.org/rpgframework-cloud/shadowrun6-eden/src/master/template.json

Only what the exporter actually fills is modelled with intent (attributes,
skills, gear items, tradition); the remaining sub-templates (condition
monitors, initiative, defense ratings, movement, ...) are emitted at their
eden defaults because the eden NPC sheet derives them from the attributes on
import.
"""

from typing import Annotated, Any, Dict, List, Literal

from pydantic import BaseModel, BeforeValidator, Field


def parse_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


ErrorProneInt = Annotated[int, BeforeValidator(lambda v: parse_int(value=v, default=0))]


# --------------------------------------------------------------------------- #
# attribute-template
# --------------------------------------------------------------------------- #
class Stat(BaseModel):
    base: ErrorProneInt = 2
    mod: ErrorProneInt = 0
    modString: str = ""
    augment: ErrorProneInt = 0
    pool: ErrorProneInt = 2


class MagicAttr(BaseModel):
    base: ErrorProneInt = 0
    mod: ErrorProneInt = 0
    pool: ErrorProneInt = 0
    min: ErrorProneInt = 0


class ResAttr(BaseModel):
    base: ErrorProneInt = 0
    mod: ErrorProneInt = 0
    pool: ErrorProneInt = 0


class EdgAttr(BaseModel):
    current: ErrorProneInt = 0
    max: ErrorProneInt = 1


class EssenceAttr(BaseModel):
    base: float = 6
    mod: float = 0
    pool: float = 6


class Attributes(BaseModel):
    bod: Stat = Field(default_factory=Stat)
    agi: Stat = Field(default_factory=Stat)
    rea: Stat = Field(default_factory=Stat)
    str: Stat = Field(default_factory=Stat)
    wil: Stat = Field(default_factory=Stat)
    log: Stat = Field(default_factory=Stat)
    int: Stat = Field(default_factory=Stat)
    cha: Stat = Field(default_factory=Stat)
    mag: MagicAttr = Field(default_factory=MagicAttr)
    res: ResAttr = Field(default_factory=ResAttr)
    edg: EdgAttr = Field(default_factory=EdgAttr)
    essence: EssenceAttr = Field(default_factory=EssenceAttr)


# --------------------------------------------------------------------------- #
# derived / defense / resist templates (emitted at defaults)
# --------------------------------------------------------------------------- #
class ModWrapper(BaseModel):
    mod: ErrorProneInt = 0


class Derived(BaseModel):
    composure: ModWrapper = Field(default_factory=ModWrapper)
    judge_intentions: ModWrapper = Field(default_factory=ModWrapper)
    memory: ModWrapper = Field(default_factory=ModWrapper)
    lift_carry: ModWrapper = Field(default_factory=ModWrapper)
    matrix_perception: ModWrapper = Field(default_factory=ModWrapper)


class DefenseRating(BaseModel):
    physical: ModWrapper = Field(default_factory=ModWrapper)
    matrix: ModWrapper = Field(default_factory=ModWrapper)
    vehicle: ModWrapper = Field(default_factory=ModWrapper)
    astral: ModWrapper = Field(default_factory=ModWrapper)
    social: ModWrapper = Field(default_factory=ModWrapper)


class ResistPool(BaseModel):
    physical: ModWrapper = Field(default_factory=ModWrapper)
    astral: ModWrapper = Field(default_factory=ModWrapper)
    spells_direct: ModWrapper = Field(default_factory=ModWrapper)
    spells_indirect: ModWrapper = Field(default_factory=ModWrapper)
    spells_other: ModWrapper = Field(default_factory=ModWrapper)
    vehicle: ModWrapper = Field(default_factory=ModWrapper)
    toxin: ModWrapper = Field(default_factory=ModWrapper)
    damage_physical: ModWrapper = Field(default_factory=ModWrapper)
    damage_astral: ModWrapper = Field(default_factory=ModWrapper)


# --------------------------------------------------------------------------- #
# monitor-template (fields sit at the system root)
# --------------------------------------------------------------------------- #
class MonitoringStat(BaseModel):
    mod: int = 0
    modString: str = ""
    value: int = 9
    dmg: int = 0
    max: int = 18


class OverflowStat(BaseModel):
    mod: int = 0
    modString: str = ""
    value: int = 0
    dmg: int = 0
    max: int = 32


class EdgeStat(BaseModel):
    value: ErrorProneInt = 0
    max: ErrorProneInt = 1


# --------------------------------------------------------------------------- #
# initiative-template
# --------------------------------------------------------------------------- #
class InitiativeDice(BaseModel):
    mod: int = 0
    dice: int = 1
    diceMod: int = 0


class InitiativeData(BaseModel):
    astral: InitiativeDice = Field(default_factory=InitiativeDice)
    matrix: InitiativeDice = Field(default_factory=InitiativeDice)
    physical: InitiativeDice = Field(default_factory=InitiativeDice)
    actions: int = 0


# --------------------------------------------------------------------------- #
# skill-template
# --------------------------------------------------------------------------- #
class Skill(BaseModel):
    points: ErrorProneInt = 0
    specialization: str = ""
    expertise: str = ""
    modifier: ErrorProneInt = 0
    augment: ErrorProneInt = 0


SKILL_NAMES = (
    "astral",
    "athletics",
    "biotech",
    "close_combat",
    "con",
    "conjuring",
    "cracking",
    "electronics",
    "enchanting",
    "engineering",
    "exotic_weapons",
    "firearms",
    "influence",
    "outdoors",
    "perception",
    "piloting",
    "sorcery",
    "stealth",
    "tasking",
)


class Skills(BaseModel):
    astral: Skill = Field(default_factory=Skill)
    athletics: Skill = Field(default_factory=Skill)
    biotech: Skill = Field(default_factory=Skill)
    close_combat: Skill = Field(default_factory=Skill)
    con: Skill = Field(default_factory=Skill)
    conjuring: Skill = Field(default_factory=Skill)
    cracking: Skill = Field(default_factory=Skill)
    electronics: Skill = Field(default_factory=Skill)
    enchanting: Skill = Field(default_factory=Skill)
    engineering: Skill = Field(default_factory=Skill)
    exotic_weapons: Skill = Field(default_factory=Skill)
    firearms: Skill = Field(default_factory=Skill)
    influence: Skill = Field(default_factory=Skill)
    outdoors: Skill = Field(default_factory=Skill)
    perception: Skill = Field(default_factory=Skill)
    piloting: Skill = Field(default_factory=Skill)
    sorcery: Skill = Field(default_factory=Skill)
    stealth: Skill = Field(default_factory=Skill)
    tasking: Skill = Field(default_factory=Skill)


# --------------------------------------------------------------------------- #
# magic-template
# --------------------------------------------------------------------------- #
class Tradition(BaseModel):
    genesisID: str = ""
    name: str = ""
    attribute: str = "log"


# --------------------------------------------------------------------------- #
# Actor: npc
# --------------------------------------------------------------------------- #
class ActorNPC(BaseModel):
    # attribute-template
    attributes: Attributes = Field(default_factory=Attributes)
    metatype: str = "human"
    # eden's template.json fixes ``system.type`` to "npc" for the NPC actor;
    # the awakened/mundane distinction lives in ``mortype``.
    type: str = "npc"
    gender: str = ""
    # derived / defense / resist templates
    derived: Derived = Field(default_factory=Derived)
    defenserating: DefenseRating = Field(default_factory=DefenseRating)
    defensepool: ResistPool = Field(default_factory=ResistPool)
    # monitor-template (flat at the system root)
    physical: MonitoringStat = Field(default_factory=MonitoringStat)
    stun: MonitoringStat = Field(default_factory=MonitoringStat)
    overflow: OverflowStat = Field(default_factory=OverflowStat)
    edge: EdgeStat = Field(default_factory=EdgeStat)
    # initiative-template
    initiative: InitiativeData = Field(default_factory=InitiativeData)
    # movement-template (flat at the system root)
    walk: int = 5
    sprint: int = 10
    perHit: int = 1
    # skill-template
    skills: Skills = Field(default_factory=Skills)
    # magic-template
    tradition: Tradition = Field(default_factory=Tradition)
    # npc actor fields
    mortype: str = "mundane"
    matrixIni: str = "vrcold"
    rating: int = 1
    gruntmeta: str = ""
    editmode: bool = False


# --------------------------------------------------------------------------- #
# Item: gear  (system.type is the eden ITEMTYPE enum; the document type stays
# "gear")
# --------------------------------------------------------------------------- #
class GearVehicle(BaseModel):
    opMode: str = "manual"


class FoundryGear(BaseModel):
    # genesis template
    genesisID: str = ""
    description: str = ""
    # dice-pool template
    modifier: int = 0
    wild: bool = False
    pool: int = 0
    # gear
    type: str = "ACCESSORY"
    subtype: str = ""
    count: int = 1
    countable: bool = True
    availDef: str = ""
    avail: ErrorProneInt = 0
    ammocap: int = 0
    ammocount: int = 0
    priceDef: str = ""
    price: ErrorProneInt = 0
    customName: str = ""
    usedForPool: bool = False
    notes: str = ""
    accessories: str = ""
    needsRating: bool = False
    rating: ErrorProneInt = 0
    skill: str = ""
    skillSpec: str = ""
    dmg: ErrorProneInt = 0
    stun: bool = False
    dmgDef: str = ""
    attackRating: List[int | None] = Field(default_factory=lambda: [0, 0, 0, 0, 0])
    modes: Dict[str, bool] = Field(
        default_factory=lambda: {"BF": False, "FA": False, "SA": False, "SS": False}
    )
    defense: int = 0
    social: int = 0
    essence: float = 0
    capacity: int = 0
    natural: bool = False
    devRating: int = 0
    a: int = 0
    s: int = 0
    d: int = 0
    f: int = 0
    progSlots: int = 0
    handlOn: int = 0
    handlOff: int = 0
    accOn: int = 0
    accOff: int = 0
    spdiOn: int = 0
    spdiOff: int = 0
    tspd: int = 0
    bod: int = 0
    arm: int = 0
    pil: int = 0
    sen: int = 0
    sea: int = 0
    vtype: str = ""
    vehicle: GearVehicle = Field(default_factory=GearVehicle)
    strWeapon: bool = False
    dualHand: bool = False


class Item(BaseModel):
    name: str = "Unnamed"
    type: Literal["gear"] = "gear"
    img: str | None = None
    system: FoundryGear = Field(default_factory=FoundryGear)
    effects: list = Field(default_factory=list)


# --------------------------------------------------------------------------- #
# Root actor document
# --------------------------------------------------------------------------- #
class ExportSource(BaseModel):
    npc_uuid: str = ""
    world: str = ""
    system: str = "schattenakte.de"
    coreVersion: str = ""
    systemVersion: str = ""


class Flags(BaseModel):
    exportSource: ExportSource = Field(default_factory=ExportSource)


class RootNPC(BaseModel):
    name: str
    type: Literal["NPC"] = "NPC"
    img: str | None = None
    system: ActorNPC = Field(default_factory=ActorNPC)
    items: list[Item] = Field(default_factory=list)
    effects: list = Field(default_factory=list)
    flags: Flags = Field(default_factory=Flags)
    sort: int = 0
