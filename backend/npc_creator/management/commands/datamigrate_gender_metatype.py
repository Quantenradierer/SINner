from django.core.management import BaseCommand

from npc_creator.game_mechanics.sr6.character import Metatype, Gender
from npc_creator.models import Npc


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        genders = set()
        metatypes = set()
        for npc in Npc.objects.all():
            metatypes.add(npc.values["metatype"])
            genders.add(npc.values["gender"])

            translation_gender = {
                "Weiblich ": Gender.FEMALE,
                " Männlich ": Gender.MALE,
                "Keines": Gender.OTHER,
                "Männlich ": Gender.MALE,
                "m": Gender.MALE,
                "Weiblich": Gender.FEMALE,
                "Divers": Gender.DIVERS,
                " weiblich ": Gender.FEMALE,
                "Female": Gender.FEMALE,
                "männlich ": Gender.MALE,
                "Maskulin": Gender.MALE,
                "Keins": Gender.OTHER,
                "male": Gender.MALE,
                "Mann": Gender.MALE,
                "weiblich ": Gender.FEMALE,
                "Frau": Gender.FEMALE,
                " Männlich": Gender.MALE,
                "Männer": Gender.MALE,
                "weiblich": Gender.FEMALE,
                " weiblich": Gender.FEMALE,
                "Männlich": Gender.MALE,
                "männlich": Gender.MALE,
                " männlich": Gender.MALE,
                " Weiblich": Gender.FEMALE,
                "Male": Gender.MALE,
                "N/A (elementarwesen)": Gender.OTHER,
                "Androgyn": Gender.OTHER,
                "N/A (Wassergeist)": Gender.OTHER,
                "Mänlich": Gender.MALE,
                "N/A": Gender.OTHER,
            }

            translation_metatype = {
                "human": Metatype.HUMAN,
                "Hauskatze": Metatype.OTHER,
                "Hobgoblin": Metatype.HOBGOBLIN,
                "Oni": Metatype.ONI,
                "Drake": Metatype.DRAKE,
                "Gnom": Metatype.DWARF,
                "Saugroboter": Metatype.AI,
                "Zwerg": Metatype.DWARF,
                "Fuchs-Gestaltwandler": Metatype.OTHER,
                "Drako": Metatype.DRAKE,
                "Oger": Metatype.OGRE,
                "Mensch (Norm)": Metatype.HUMAN,
                "Gestaltwandler (Wildkatze)": Metatype.OTHER,
                "Orkin": Metatype.ORK,
                "Ghul": Metatype.OTHER,
                "Geist": Metatype.SPIRIT,
                "Elfe": Metatype.ELF,
                "Künstliche Intelligenz": Metatype.AI,
                "Z elf": Metatype.ELF,
                "mensch": Metatype.HUMAN,
                "Mensch": Metatype.HUMAN,
                "Elf": Metatype.ELF,
                "Dryade": Metatype.DRYAD,
                "Menschen": Metatype.HUMAN,
                "Troll": Metatype.TROLL,
                "Wassergeist": Metatype.SPIRIT,
                "Human": Metatype.HUMAN,
                "Zwergin": Metatype.DWARF,
                "Luftgeist": Metatype.SPIRIT,
                "Elf (Wakyambi-Variante)": Metatype.WAKYAMBI,
                "Surge Mutant": Metatype.OTHER,
                "KI (künstliche Intelligenz)": Metatype.AI,
                "Maschine": Metatype.AI,
                "Dunkelelf": Metatype.NOCTURNE,
                "Geistwesen": Metatype.SPIRIT,
                "Goblin (infizierte Ork-Unterart, in Shadowrun beka": Metatype.HOBGOBLIN,
                "Elf\nElf": Metatype.ELF,
                "Robbe": Metatype.OTHER,
                "Ork": Metatype.ORK,
                "Zwerge": Metatype.DWARF,
                "Mensch (Erwachter Gestaltwandler)": Metatype.HUMAN,
                "troll": Metatype.TROLL,
            }

            if "gender_enum" not in npc.values:
                npc.values["gender_enum"] = translation_gender.get(
                    npc.values["gender"], Gender.OTHER
                )

            if "metatype_enum" not in npc.values:
                npc.values["gender_enum"] = translation_metatype.get(
                    npc.values["metatype"], Metatype.OTHER
                )

            npc.save()
        print(genders)
        print(metatypes)
