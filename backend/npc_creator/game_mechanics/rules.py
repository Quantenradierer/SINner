class RuleBooks(enum.Enum):
    SR6CORE = "Shadowrun 6D - Core Rulebook"


def source(*, rule_book: RuleBooks, page: int):
    """
    does nothing, just contains the location of the rule for now
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


@source(rule_book=RuleBooks.SR6CORE, page=39)
def physical_initiative(*, reaction, intuition, modifier=0):
    return reaction + intuition + modifier


@source(rule_book=RuleBooks.SR6CORE, page=161)
def astral_initiative(*, logic, intuition, modifier=0):
    return logic + intuition + modifier


@source(rule_book=RuleBooks.SR6CORE, page=179)
def matrix_vr_initiative(*, inituition, data_processing, modifier=0):
    return inituition + data_processing + modifier


@source(rule_book=RuleBooks.SR6CORE, page=39)
def defense_rating(*, body, armor):
    return body + armor


@source(rule_book=RuleBooks.SR6CORE, page=109)
def defense_test(*, reaction, intuition):
    return reaction + intuition


@source(rule_book=RuleBooks.SR6CORE, page=161)
def defense_astral(*, intuition, logic):
    return intuition + logic


@source(rule_book=RuleBooks.SR6CORE, page=130)
def defense_direct_spell(*, willpower):
    return willpower


@source(rule_book=RuleBooks.SR6CORE, page=132)
def defense_indirect_spell(*, reaction, intuition):
    return reaction + intuition


@source(rule_book=RuleBooks.SR6CORE, page=123)
def resist_toxin(*, body, willpower):
    return body + willpower


@source(rule_book=RuleBooks.SR6CORE, page=109)
def resist_physical_damage(*, body, armor=0):
    return body + armor


@source(rule_book=RuleBooks.SR6CORE, page=161)
def resist_astral_damage(*, willpower):
    return willpower
