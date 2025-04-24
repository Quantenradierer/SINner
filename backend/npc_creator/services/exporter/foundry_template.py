from typing import Any, Dict, List, Literal, Annotated
from pydantic import BaseModel, Field, BeforeValidator


def parse_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


ErrorProneInt = Annotated[int, BeforeValidator(lambda v: parse_int(value=v, default=0))]


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
    base: ErrorProneInt = 6
    mod: ErrorProneInt = 0
    pool: ErrorProneInt = 6


class Attributes(BaseModel):
    bod: Stat = Stat()
    agi: Stat = Stat()
    rea: Stat = Stat()
    str: Stat = Stat()
    wil: Stat = Stat()
    log: Stat = Stat()
    int: Stat = Stat()
    cha: Stat = Stat()
    mag: MagicAttr = MagicAttr()
    res: ResAttr = ResAttr()
    # edg: EdgAttr = EdgAttr()
    essence: EssenceAttr = EssenceAttr()


class AttributeTemplate(BaseModel):
    attributes: Attributes = Attributes()
    metatype: str = "human"
    type: str = "mundane"
    gender: str = ""


class ModWrapper(BaseModel):
    mod: ErrorProneInt = 0


class Derived(BaseModel):
    composure: ModWrapper = ModWrapper()
    judge_intentions: ModWrapper = ModWrapper()
    memory: ModWrapper = ModWrapper()
    lift_carry: ModWrapper = ModWrapper()
    matrix_perception: ModWrapper = ModWrapper()


class DerivedTemplate(BaseModel):
    derived: Derived = Derived()


class DefenseRating(BaseModel):
    physical: ModWrapper = ModWrapper()
    matrix: ModWrapper = ModWrapper()
    vehicle: ModWrapper = ModWrapper()
    astral: ModWrapper = ModWrapper()
    social: ModWrapper = ModWrapper()


class DefenseratingTemplate(BaseModel):
    defenserating: DefenseRating = DefenseRating()


class AttackRating(BaseModel):
    physical: ModWrapper = ModWrapper()
    astral: ModWrapper = ModWrapper()
    matrix: ModWrapper = ModWrapper()
    vehicle: ModWrapper = ModWrapper()
    social: ModWrapper = ModWrapper()


class AttackratingTemplate(BaseModel):
    attackrating: AttackRating = AttackRating()


class ResistPool(BaseModel):
    physical: ModWrapper = ModWrapper()
    astral: ModWrapper = ModWrapper()
    spells_direct: ModWrapper = ModWrapper()
    spells_indirect: ModWrapper = ModWrapper()
    spells_other: ModWrapper = ModWrapper()
    vehicle: ModWrapper = ModWrapper()
    toxin: ModWrapper = ModWrapper()
    damage_physical: ModWrapper = ModWrapper()
    damage_astral: ModWrapper = ModWrapper()


class ResistTemplate(BaseModel):
    defensepool: ResistPool = ResistPool()


class MonitoringStat(BaseModel):
    base: int = 9
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


class MonitorTemplate(BaseModel):
    physical: MonitoringStat = MonitoringStat()
    stun: MonitoringStat = MonitoringStat()
    overflow: OverflowStat = OverflowStat()
    edge: EdgeStat = EdgeStat()


class InitiativeDice(BaseModel):
    mod: int = 0
    dice: int = 1
    diceMod: int = 0


class InitiativeData(BaseModel):
    astral: InitiativeDice = InitiativeDice()
    matrix: InitiativeDice = InitiativeDice()
    physical: InitiativeDice = InitiativeDice()
    actions: int = 0


class InitiativeTemplate(BaseModel):
    initiative: InitiativeData = InitiativeData()


class MovementTemplate(BaseModel):
    walk: int = 5
    sprint: int = 10
    perHit: int = 1


class VehicleSkillStat(BaseModel):
    points: int = 0
    modifier: int = 0
    pool: int = 0


class VehicleSkills(BaseModel):
    piloting: VehicleSkillStat = VehicleSkillStat()
    evasion: VehicleSkillStat = VehicleSkillStat()
    perception: VehicleSkillStat = VehicleSkillStat()
    cracking: VehicleSkillStat = VehicleSkillStat()
    stealth: VehicleSkillStat = VehicleSkillStat()


class VehicleskillTemplate(BaseModel):
    skills: VehicleSkills = VehicleSkills()


class Skill(BaseModel):
    points: ErrorProneInt = 0
    specialization: str = ""
    expertise: str = ""
    modifier: ErrorProneInt = 0
    augment: ErrorProneInt = 0


class Skills(BaseModel):
    astral: Skill = Skill()
    athletics: Skill = Skill()
    biotech: Skill = Skill()
    close_combat: Skill = Skill()
    con: Skill = Skill()
    conjuring: Skill = Skill()
    cracking: Skill = Skill()
    electronics: Skill = Skill()
    enchanting: Skill = Skill()
    engineering: Skill = Skill()
    exotic_weapons: Skill = Skill()
    firearms: Skill = Skill()
    influence: Skill = Skill()
    outdoors: Skill = Skill()
    perception: Skill = Skill()
    piloting: Skill = Skill()
    sorcery: Skill = Skill()
    stealth: Skill = Skill()
    tasking: Skill = Skill()


class SkillTemplate(BaseModel):
    skills: Skills = Field(default_factory=lambda: Skills())


class Tradition(BaseModel):
    genesisID: str = ""
    name: str = ""
    attribute: str = "log"


class MagicTemplate(BaseModel):
    tradition: Tradition = Tradition()


class DeviceMod(BaseModel):
    a: int = 0
    s: int = 0
    d: int = 0
    f: int = 0


class ModContainer(BaseModel):
    mod: DeviceMod = DeviceMod()


class Used(BaseModel):
    a: int = 0
    s: int = 0
    d: int = 0
    f: int = 0


class PersonaData(BaseModel):
    device: ModContainer = Field(default_factory=lambda: ModContainer())
    living: ModContainer = Field(default_factory=lambda: ModContainer())
    used: Used = Used()


class PersonaTemplate(BaseModel):
    persona: PersonaData = PersonaData()


class KnowledgeTemplate(BaseModel):
    pass


class ActorPlayer(
    AttributeTemplate,
    MonitorTemplate,
    DerivedTemplate,
    # DefenseratingTemplate,
    ResistTemplate,
    # InitiativeTemplate,
    MovementTemplate,
    SkillTemplate,
    KnowledgeTemplate,
    MagicTemplate,
    PersonaTemplate,
):
    name: str = ""
    metatype: str = ""
    mortype: str = "mundane"
    matrixIni: str = "vrcold"
    gender: str = ""
    nuyen: int = 0
    overwatch: int = 0
    notes: str = ""
    karma: int = 0
    karma_total: int = 0
    heat: int = 0
    reputation: int = 0


class ActorNPC(
    AttributeTemplate,
    MonitorTemplate,
    DerivedTemplate,
    # DefenseratingTemplate,
    ResistTemplate,
    # InitiativeTemplate,
    MovementTemplate,
    SkillTemplate,
    KnowledgeTemplate,
    MagicTemplate,
    PersonaTemplate,
):
    name: str = ""
    type: str = "mundane"
    mortype: str = "mundane"
    matrixIni: str = "vrcold"
    rating: int = 1
    gruntmeta: str = ""
    editmode: bool = False


class ActorCritter(
    AttributeTemplate,
    MonitorTemplate,
    # InitiativeTemplate,
    SkillTemplate,
    KnowledgeTemplate,
):
    name: str = ""
    editmode: bool = False


class ActorSpirit(
    AttributeTemplate,
    MonitorTemplate,
    # InitiativeTemplate,
    SkillTemplate,
    KnowledgeTemplate,
):
    name: str = ""
    rating: int = 1
    spiritType: str = ""
    editmode: bool = False


class ActorVehicleVehicle(BaseModel):
    belongs: str = ""
    opMode: str = "manual"
    offRoad: bool = False
    speed: int = 0


class ActorVehicle(MonitorTemplate, VehicleskillTemplate):
    handlOn: int = 1
    handlOff: int = 2
    accOn: int = 3
    accOff: int = 4
    spdiOn: int = 5
    spdiOff: int = 0
    tspd: int = 0
    bod: int = 0
    arm: int = 0
    pil: int = 0
    sen: int = 0
    sea: int = 0
    vtype: str = ""
    vehicle: ActorVehicleVehicle = ActorVehicleVehicle()
    notes: str = ""


class GenesisTemplate(BaseModel):
    genesisID: str = "-"
    description: str = ""


class SkillValueTemplate(BaseModel):
    points: int = 0
    modifier: int = 0


class DicePoolTemplate(BaseModel):
    modifier: int = 0
    wild: bool = False
    pool: int = 0


class QualityValueTemplate(BaseModel):
    value: int = 0
    explain: str = ""
    modifier: list[int] = Field(default_factory=list)


class AdeptPower(BaseModel):
    hasLevel: bool = False
    level: int = 0
    choice: str = ""
    cost: float = 0.0
    activation: str = ""
    templates: list[str] = Field(default_factory=lambda: ["genesis"])


class ComplexForm(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])
    duration: str = "sustained"
    fading: int = 3
    skill: str = ""
    skillSpec: str = ""
    attrib: str = "res"
    threshold: int = 0
    oppAttr1: str = ""
    oppAttr2: str = ""


class Contact(BaseModel):
    name: str = "Someone"
    rating: int = 1
    loyalty: int = 1
    favors: int = 0
    type: str = ""
    description: str = ""


class CritterPower(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])
    duration: str = "instantaneous"
    action: str = ""
    type: str = "physical"
    range: str = "self"


class Echo(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])


class Focus(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])
    rating: int = 1


class GearVehicle(BaseModel):
    opMode: str = "manual"


class Gear(BaseModel):
    type: str = ""
    subtype: str = ""
    ammocap: int = 0
    ammocount: int = 0
    skill: str = ""
    skillSpec: str = ""
    dmg: int = 0
    dmgDef: str = ""
    stun: bool = False
    attackRating: list[int | None] = Field(default_factory=lambda: [0, 0, 0, 0, 0])
    modes: Dict[str, bool] = Field(
        default_factory=lambda: {"BF": False, "FA": False, "SA": False, "SS": False}
    )
    usedForPool: bool = False
    notes: str = ""
    accessories: str = ""
    needsRating: bool = False
    rating: int = 0
    skill: str = ""
    skillSpec: str = ""

    defense: int = 0
    social: int = 0
    essence: int = 0
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
    vehicle: GearVehicle = GearVehicle()
    strWeapon: bool = False
    dualHand: bool = False
    templates: list[str] = Field(default_factory=lambda: ["genesis", "dice-pool"])


class Lifestyle(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])
    type: str = "low"
    paid: int = 1
    cost: int = 2000
    sin: str = ""


class MartialArtStyle(BaseModel):
    category: Dict[str, bool] = Field(
        default_factory=lambda: {
            "grappling": False,
            "mobility": False,
            "ranged": False,
            "striking": False,
            "weapon": False,
        }
    )
    templates: list[str] = Field(default_factory=lambda: ["genesis"])


class MartialArtTech(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])
    style: str = ""
    choice: str = ""


class Metamagic(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])
    level: bool = False
    adepts: bool = False
    mages: bool = False


class Quality(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis", "quality-value"])
    category: str = ""
    level: bool = False


class RitualFeatures(BaseModel):
    anchored: bool = False
    material_link: bool = False
    minion: bool = False
    spell: bool = False
    spotter: bool = False


class Ritual(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])
    threshold: int = 5
    features: RitualFeatures = RitualFeatures()


class Sin(BaseModel):
    name: str = "Someone"
    quality: str = "REAL_SIN"
    description: str = ""


class ItemSkill(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis", "skill-value"])
    genesisID: str = ""
    description: str = ""
    points: int = 0
    modifier: int = 0


class Software(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])
    type: str = "SOFTWARE"
    subtype: str = "AUTOSOFT"
    category: str = ""
    rating: int = 1


class Spell(BaseModel):
    templates: list[str] = Field(default_factory=lambda: ["genesis"])
    category: str = "health"
    duration: str = "instantaneous"
    drain: int = 1
    type: str = "physical"
    range: str = "self"
    damage: str = "physical"
    alchemic: bool = False
    multiSense: bool = False
    isOpposed: bool = True
    withEssence: bool = False
    wildDie: bool = False
    isSustained: bool = False


class Item(BaseModel):
    type: Literal[
        "complexform",
        "contact",
        "critterpower",
        "echo",
        "gear",
        "lifestyle",
        "martialartstyle",
        "martialarttech",
        "metamagic",
        "quality",
        "sin",
        "skill",
        "adeptpower",
        "spell",
        "ritual",
        "focus",
        "software",
    ]
    name: str = "Unnamed"
    adeptpower: AdeptPower = AdeptPower()
    complexform: ComplexForm = ComplexForm()
    contact: Contact = Contact()
    critterpower: CritterPower = CritterPower()
    echo: Echo = Echo()
    focus: Focus = Focus()
    system: Gear = Gear()
    lifestyle: Lifestyle = Lifestyle()
    martialartstyle: MartialArtStyle = MartialArtStyle()
    martialarttech: MartialArtTech = MartialArtTech()
    metamagic: Metamagic = Metamagic()
    quality: Quality = Quality()
    ritual: Ritual = Ritual()
    sin: Sin = Sin()
    skill: ItemSkill = ItemSkill()
    software: Software = Software()
    spell: Spell = Spell()


class ExportSource(BaseModel):
    world: str = ""
    system: str = "Schattenakte"
    coreVersion: str = ""
    systemVersion: str = ""


class FlagsUNDOCUMENTED(BaseModel):
    exportSource: ExportSource = Field(default_factory=ExportSource)


class RootUNDOCUMENTED(BaseModel):
    img: str | None = None
    flags: FlagsUNDOCUMENTED = Field(default_factory=FlagsUNDOCUMENTED)


class RootBase(RootUNDOCUMENTED):
    items: list[Item] = []
    name: str
    sort: int = 0

    # effects: list[???]
    # token: ???


class RootPlayer(RootBase):
    type: Literal["Player"] = "Player"
    data: ActorPlayer = Field(default_factory=ActorPlayer)


class RootNPC(RootBase):
    type: Literal["NPC"] = "NPC"
    data: ActorNPC = Field(default_factory=ActorNPC)


class RootCritter(RootBase):
    type: Literal["Critter"] = "Critter"
    data: ActorCritter = Field(default_factory=ActorCritter)


class RootSpirit(RootBase):
    type: Literal["Spirit"] = "Spirit"
    data: ActorSpirit = Field(default_factory=ActorSpirit)


class RootVehicle(RootBase):
    type: Literal["Vehicle"] = "Vehicle"
    data: ActorVehicle = Field(default_factory=ActorVehicle)
