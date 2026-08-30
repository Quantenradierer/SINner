#!/usr/bin/env python3
"""Generate a German id -> name lookup for the SR6 reference data.

Run from anywhere:  python backend/npc_creator/reference/sr6/core/i18n/build_names.py
Writes de.json next to this script. Edit the translation dicts below and
re-run whenever the gear/rules JSON under sr6/core/ changes.

Best-effort: names that could not be mapped to a confident German GRW term are
prefixed with "TODO " so they are easy to grep and fix later.
"""
import json
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.normpath(os.path.join(HERE, ".."))          # .../sr6/core
OUT = os.path.join(HERE, "de.json")                        # .../sr6/core/i18n/de.json

SKILLS = {
    "astral": "Astralkampf",
    "athletics": "Athletik",
    "biotech": "Biotech",
    "close_combat": "Nahkampf",
    "con": "Überreden",
    "conjuring": "Beschwören",
    "cracking": "Cracken",
    "electronics": "Elektronik",
    "enchanting": "Verzaubern",
    "engineering": "Mechanik",
    "firearms": "Feuerwaffen",
    "influence": "Einfluss",
    "outdoors": "Natur",
    "perception": "Wahrnehmung",
    "piloting": "Steuern",
    "sorcery": "Hexerei",
    "stealth": "Heimlichkeit",
    "tasking": "Tasken",
}

# --- gear: keyed by the last meaningful slug (rating suffix stripped) ----------
GEAR = {
    # accessory
    "argloves": "AR-Handschuhe",
    "biometricreader": "Biometrieleser",
    "electronicpaper": "Elektronisches Papier",
    "printer": "Drucker",
    "satellitelink": "Satellitenverbindung",
    "simrig": "Sim-Rig",
    "subvocalmic": "Subvokalmikrofon",
    "tridprojector": "Trid-Projektor",
    "trodes": "Trodennetz",
    # armor
    "helmet": "Helm",
    "synthleather jacket": "Synthlederjacke",
    "actioneer business clothes": "Actioneer-Businesskleidung",
    "armor clothing": "Panzerkleidung",
    "armor jacket": "Panzerjacke",
    "armor vest": "Panzerweste",
    "chameleon suit": "Chamäleonanzug",
    "full body armor": "Ganzkörperpanzerung",
    "lined coat": "Gefütterter Mantel",
    "urban explorer jumpsuit": "Urban-Explorer-Overall",
    "ballistic shield": "Ballistischer Schild",
    "riot shield": "Aufruhrschild",
    # audio devices
    "directionalmic": "Richtmikrofon",
    "earbuds": "Ohrhörer",
    "headphones": "Kopfhörer",
    "lasermic": "Lasermikrofon",
    "omnimic": "Omnidirektionales Mikrofon",
    "audioenhancement": "Audioverbesserung",
    "selectsoundfilter": "Selektiver Geräuschfilter",
    "spatialrecognizer": "Raumklangerkennung",
    # biotech
    "biomonitor": "Biomonitor",
    "disposable_syringe": "Einwegspritze",
    "medkit": "Medkit",
    "medkit_supplies": "Medkit-Nachschub",
    "antidote_patch": "Antidot-Patch",
    "chem_patch": "Chemikalien-Patch",
    "stim_patch": "Stim-Patch",
    "tranq_patch": "Beruhigungs-Patch",
    "trauma_patch": "Trauma-Patch",
    "trauma_patch_alt": "Trauma-Patch",
    # breaking & entering
    "autopicker": "Autopicker",
    "cellularglovemolder": "Zellularer Handschuhformer",
    "chiselwreckingbar": "Meißel-Brecheisen",
    "keycardcopier": "Schlüsselkartenkopierer",
    "lockpickset": "Dietrichset",
    "maglockpasskey": "Maglock-Passkey",
    "miniwelder": "Minischweißgerät",
    "miniwelderfuelcanister": "Minischweißgerät-Brennstoffkanister",
    "monofilamentchainsaw": "Monofilament-Kettensäge",
    "sequencer": "Sequenzer",
    # chemical
    "chemicals_glue_solvent": "Klebstofflöser",
    "chemicals_glue_sprayer": "Klebstoffsprüher",
    "chemicals_thermite_burning_bar": "Thermit-Brennstab",
    # communication gear
    "commgear_bugscanner": "Wanzenscanner",
    "commgear_datatap": "Datentap",
    "commgear_headjammer": "Kopf-Störsender",
    "commgear_jammer_area": "Störsender (Fläche)",
    "commgear_jammer_directional": "Störsender (gerichtet)",
    "commgear_microtransceiver": "Mikrotransceiver",
    "commgear_tageraser": "Tag-Eraser",
    "commgear_whitenoise": "Weißrauschgenerator",
    # credstick
    "standard": "Standard",  # overridden per category below
    # cyberware bodyware
    "bone_lacing_plastic": "Knochenverstärkung (Kunststoff)",
    "bone_lacing_aluminum": "Knochenverstärkung (Aluminium)",
    "bone_lacing_titanium": "Knochenverstärkung (Titan)",
    "bodyware_dermal_plating": "Hautpanzerung",
    "bodyware_fingertip_compartment": "Fingerspitzenfach",
    "bodyware_grapple_gun": "Enterhaken (Implantat)",
    "bodyware_internal_air_tank": "Interner Lufttank",
    "bodyware_muscle_replacement": "Muskelersatz",
    "bodyware_reaction_enhancers": "Reaktionsverstärker",
    "bodyware_skillwires": "Skillwires",
    "bodyware_smuggling_compartment": "Schmuggelfach",
    "bodyware_wired_reflexes": "Verdrahtete Reflexe",
    "cyberjack": "Cyberjack",
    "cybereyes": "Cyberaugen",
    "headware_commlink": "Kommlink (Kopfware)",
    "headware_controlrig": "Steuerrig",
    "headware_cortexkinkbomb": "Kortexbombe (Kink)",
    "headware_cortexmicrobomb": "Kortexbombe (Mikro)",
    "headware_cortexareabomb": "Kortexbombe (Flächen)",
    "headware_cyberdeck": "Cyberdeck (Kopfware)",
    "headware_datajack": "Datenbuchse",
    "headware_datalock": "Datenschloss",
    "headware_olfactorybooster": "Geruchsverstärker",
    "headware_simrig": "Sim-Rig (Implantat)",
    "headware_skilljack": "Skilljack",
    # cyberware mods
    "cyberlimbaccessory_gyromount": "Cyberglied-Zubehör: Gyro-Halterung",
    "cyberlimbaccessory_slide": "Cyberglied-Zubehör: Gleitschiene",
    "cyberlimbaccessory_holster": "Cyberglied-Zubehör: Holster",
    "cyberlimbaccessory_hydraulicjacks": "Cyberglied-Zubehör: Hydraulikstelzen",
    "cyberlimbaccessory_smugglingcompartment": "Cyberglied-Zubehör: Schmuggelfach",
    "cyberjaw": "Cyberkiefer",
    "hardening": "Härtung",
    "shock_limb": "Schockglied",
    "handblade": "Handklinge",
    "retractable_handblade": "Einziehbare Handklinge",
    "hand_razors": "Handrasierer",
    "retractable_hand_razors": "Einziehbare Handrasierer",
    "spurs": "Sporen",
    "retractable_spurs": "Einziehbare Sporen",
    "holdout_pistol": "Holdout-Pistole (Implantat)",
    "light_pistol": "Leichte Pistole (Implantat)",
    "machine_pistol": "Maschinenpistole (Implantat)",
    "heavy_pistol": "Schwere Pistole (Implantat)",
    "smg": "Maschinenpistole/SMG (Implantat)",
    "shotgun": "Schrotflinte (Implantat)",
    "grenade_launcher": "Granatwerfer (Implantat)",
    "external_clip_port": "Externer Magazinanschluss",
    "laser_sight": "Laservisier",
    "silencer_suppressor": "Schalldämpfer",
    "flare_compensation": "Blendschutz",
    "image_link": "Bildverbindung",
    "low_light_vision": "Restlichtverstärkung",
    "ocular_drone": "Okulardrohne",
    "retinal_duplication": "Retina-Duplikation",
    "smartlink": "Smartlink",
    "thermographic_vision": "Thermografische Sicht",
    "vision_enhancement": "Sichtverbesserung",
    "vision_magnification": "Sichtvergrößerung",
    "headware_tastebooster": "Geschmacksverstärker",
    "headware_toothcompartment": "Zahnfach",
    "headware_ultrasoundsensor": "Ultraschallsensor",
    "headware_voicemodulator": "Stimmmodulator",
    # grapple
    "grapplegun": "Enterhaken-Gewehr",
    "grapplegun_microwire": "Enterhaken: Mikrodraht",
    "grapplegun_myomericrope": "Enterhaken: Myomerseil",
    "grapplegun_standardrope": "Enterhaken: Standardseil",
    "grapplegun_stealthrope": "Enterhaken: Tarnseil",
    "grapplegun_catalyststick": "Enterhaken: Katalysatorstab",
    # identification
    "identification_fake_license": "Gefälschte Lizenz",
    "identification_fake_sin": "Gefälschte SIN",
    # optical devices
    "optics_binoculars": "Fernglas",
    "optics_binoculars_optical": "Fernglas (rein optisch)",
    "optics_camera": "Kamera",
    "optics_microcamera": "Mikrokamera",
    "optics_contacts": "Kontaktlinsen",
    "optics_endoscope": "Endoskop",
    "optics_glasses": "Brille",
    "optics_goggles": "Schutzbrille",
    "optics_imaging_scope": "Bildgebendes Zielfernrohr",
    "optics_monocle": "Monokel",
    "optics_mage_sight_goggles": "Magiersicht-Brille",
    "optics_periscope": "Periskop",
    "opticsmod_flarecompensation": "Optik-Mod: Blendschutz",
    "opticsmod_imagelink": "Optik-Mod: Bildverbindung",
    "opticsmod_lowlightvision": "Optik-Mod: Restlichtverstärkung",
    "opticsmod_smartlink": "Optik-Mod: Smartlink",
    "opticsmod_thermographicvision": "Optik-Mod: Thermografische Sicht",
    "opticsmod_ultrasoundlink": "Optik-Mod: Ultraschallverbindung",
    "opticsmod_visionenhancement": "Optik-Mod: Sichtverbesserung",
    "opticsmod_visionmagnification": "Optik-Mod: Sichtvergrößerung",
    # rfid
    "datachip": "Datenchip",
    "security_stealth": "Sicherheits-/Stealth-Tag",
    "sensor": "Sensor-Tag",
    # security
    "containment_manacles": "Fesselungsschellen",
    "lock": "Schloss",
    "maglock": "Maglock",
    "keypad": "Zahlenfeld",
    "card_reader": "Kartenleser",
    "biometric_reader": "Biometrieleser",
    "metal_restraints": "Metallfesseln",
    "plasteel_restraints": "Plastahlfesseln",
    "plastic_straps": "Plastik-Kabelbinder",
    # sensor housings
    "sensor_handheldhousing": "Sensorgehäuse (Handgerät)",
    "sensor_wallmountedhousing": "Sensorgehäuse (wandmontiert)",
    "sensorarray": "Sensor-Array",
    "sensor_single": "Einzelsensor",
    "sensorfunction_atmosphere": "Sensorfunktion: Atmosphärensensor",
    "sensorfunction_cyberwarescanner": "Sensorfunktion: Cyberware-Scanner",
    "sensorfunction_geigercounter": "Sensorfunktion: Geigerzähler",
    "sensorfunction_laserrangefinder": "Sensorfunktion: Laser-Entfernungsmesser",
    "sensorfunction_madscanner": "Sensorfunktion: MAD-Scanner",
    "sensorfunction_motionsensor": "Sensorfunktion: Bewegungssensor",
    "sensorfunction_olfactoryscanner": "Sensorfunktion: Geruchsscanner",
    "sensorfunction_ultrasound": "Sensorfunktion: Ultraschall",
    # software
    "agents": "Agent",
    "autosoft": "Autosoft",
    "cyberprogram_basic": "Cyberprogramm (einfach)",
    "cyberprogram_hacking": "Cyberprogramm (Hacking)",
    "datasoft": "Datasoft",
    "mapsoft": "Mapsoft",
    "shopsoft": "Shopsoft",
    "activesoft": "Activesoft",
    "knowsoft": "Knowsoft",
    "linguasoft": "Linguasoft",
    "tutorsoft": "Tutorsoft",
    # survival gear
    "survival_chemsuit": "Chemieschutzanzug",
    "survival_climbinggear": "Kletterausrüstung",
    "survival_divinggear": "Tauchausrüstung",
    "survival_flashlight": "Taschenlampe",
    "survival_gasmask": "Gasmaske",
    "survival_geckotapegloves": "Gecko-Tape-Handschuhe",
    "survival_hazmatsuit": "Hazmat-Anzug",
    "survival_lightstick": "Knicklicht",
    "survival_magnesiumtorch": "Magnesiumfackel",
    "survival_microflarelauncher": "Mikro-Leuchtkugel-Werfer",
    "survival_microflares": "Mikro-Leuchtkugeln",
    "survival_rappellinggloves": "Abseilhandschuhe",
    "survival_respirator": "Atemschutzgerät",
    "survival_survivalkit": "Überlebensset",
    # tools
    "tools_kit": "Werkzeugkasten",
    "tools_shop": "Werkstatt",
    "tools_facility": "Werksanlage",
    # weapon mods
    "airburst_link": "Airburst-Link",
    "bipod": "Zweibein",
    "concealable_holster": "Verbergbares Holster",
    "gas_vent_system": "Gasabzugssystem",
    "gyro_mount": "Gyro-Stabilisator",
    "hidden_arm_slide": "Verstecktes Armgleitgestell",
    "imaging_scope": "Bildgebendes Zielfernrohr",
    "periscope": "Periskop",
    "quick_draw_holster": "Schnellziehholster",
    "shock_pad": "Schockdämpfer",
    "silencer": "Schalldämpfer",
    "smart_firing_platform": "Smart-Feuerplattform",
    "smartgun_system_internal": "Smartgun-System (intern)",
    "smartgun_system_external": "Smartgun-System (extern)",
    "spare_clip": "Ersatzmagazin",
    "speed_loader": "Speedloader",
    "tripod": "Dreibein",
    "gas_vent": "Gasabzugssystem",
}

# credstick names differ per colour
CREDSTICK = {
    "standard": "Credstick (Standard)",
    "silver": "Credstick (Silber)",
    "gold": "Credstick (Gold)",
    "platinum": "Credstick (Platin)",
    "ebony": "Credstick (Ebenholz)",
}

RFID = {
    "standard": "RFID-Tag (Standard)",
}

# device-rating gear that the GRW lists by model name
COMMLINK = {
    "1": "Meta Link",
    "2": "Sony Emperor",
    "3": "Renraku Sensei",
    "4": "Erika Elite",
    "5": "Hermes Ikon",
    "6": "Transys Avalon",
}
CYBERDECK = {
    "1": "Erika MCD-1",
    "2": "Microdeck Summit",
    "3": "Microtrónica Azteca 200",
    "4": "Hermes Chariot",
    "5": "Novatech Navigator",
    "6": "Fairlight Excalibur",
}

# weapons: only the non-brand (translatable) entries; brand/model names are kept
WEAPON = {
    "light crossbow": "Leichte Armbrust",
    "standard crossbow": "Standardarmbrust",
    "heavy crossbow": "Schwere Armbrust",
    "bike chain": "Fahrradkette",
    "telescoping staff": "Teleskopstab",
    "staff": "Stab",
    "extendable baton": "Teleskopschlagstock",
    "sap": "Totschläger",
    "stun baton": "Betäubungsschlagstock",
    "combat axe": "Kampfaxt",
    "knife": "Messer",
    "combat/survival knife": "Kampf-/Überlebensmesser",
    "survival knife": "Überlebensmesser",
    "forearm snap blades": "Unterarm-Klappklingen",
    "katana": "Katana",
    "sword": "Schwert",
    "polearm": "Stangenwaffe",
    "knucks": "Schlagring",
    "shock gloves": "Schockhandschuhe",
    "bullwhip": "Bullenpeitsche",
    "monofilament whip": "Monofilamentpeitsche",
    "throwing knives": "Wurfmesser",
    "throwing stars": "Wurfsterne",
    "unarmed": "Unbewaffnet",
    "parashield dart pistol": "Parashield Dartpistole",
    "parashield dart rifle": "Parashield Dartgewehr",
    # brand / model names (explicit casing)
    "fichetti tiffani needler": "Fichetti Tiffani Needler",
    "streetline special": "Streetline Special",
    "walther palm pistol": "Walther Palm Pistol",
    "ares light fire 70": "Ares Light Fire 70",
    "ares light fire 75": "Ares Light Fire 75",
    "beretta 101t": "Beretta 101T",
    "beretta 201t": "Beretta 201T",
    "colt america l36": "Colt America L36",
    "fichetti security 600": "Fichetti Security 600",
    "ruger redhawk": "Ruger Redhawk",
    "ares predator vi": "Ares Predator VI",
    "ares viper slivergun": "Ares Viper Slivergun",
    "browning ultra power": "Browning Ultra-Power",
    "colt government 2076": "Colt Government 2076",
    "colt manhunter": "Colt Manhunter",
    "ruger super warhawk": "Ruger Super Warhawk",
    "ares crusader ii": "Ares Crusader II",
    "ceska black scorpion": "Ceska Black Scorpion",
    "steyr tmp": "Steyr TMP",
    "colt cobra tz-100": "Colt Cobra TZ-100",
    "colt cobra tz-110": "Colt Cobra TZ-110",
    "colt cobra tz-120": "Colt Cobra TZ-120",
    "fn p93 praetor": "FN P93 Praetor",
    "hk-227": "HK-227",
    "ingram smartgun xi": "Ingram Smartgun X1",
    "sck model 100": "SCK Model 100",
    "uzi iv": "Uzi IV",
    "defiance t-250": "Defiance T-250",
    "mossberg cmdt": "Mossberg CMDT",
    "pjss model 55": "PJSS Model 55",
    "remington roomsweeper": "Remington Roomsweeper",
    "ak-97": "AK-97",
    "ares alpha": "Ares Alpha",
    "colt m23": "Colt M23",
    "fn-har": "FN HAR",
    "yamaha raiden": "Yamaha Raiden",
    "ares desert strike": "Ares Desert Strike",
    "cavalier arms crockett ebr": "Cavalier Arms Crockett EBR",
    "ranger arms sm-5": "Ranger Arms SM-5",
    "remington 900": "Remington 900",
    "ruger 101": "Ruger 101",
    "barret model 122": "Barret Model 122",
    "ingram valiant": "Ingram Valiant",
    "stoner-ares m202": "Stoner-Ares M202",
    "rpk hmg": "RPK HMG",
    "panther xxl": "Panther XXL",
    "ares super squirt": "Ares Super Squirt",
    "yamaha pulsar i/ii": "Yamaha Pulsar I/II",
    "yamaha pulsar ii": "Yamaha Pulsar II",
    "colt cobra": "Colt Cobra",
}
CYBER_IMPLANT_WEAPON = {
    "hardening": "Cyberimplantat-Waffe: Härtung",
    "shock_limb": "Cyberimplantat-Waffe: Schockglied",
    "handblade": "Cyberimplantat-Waffe: Handklinge",
    "hand_razors": "Cyberimplantat-Waffe: Handrasierer",
    "spurs": "Cyberimplantat-Waffe: Sporen",
    "cyberjaw": "Cyberimplantat-Waffe: Cyberkiefer",
}

CYBERLIMB = {
    "cyberlimb_skull": "Cyberschädel",
    "cyberlimb_torso": "Cybertorso",
    "cyberlimb_arm": "Cyberarm",
    "cyberlimb_forearm": "Cyberunterarm",
    "cyberlimb_hand": "Cyberhand",
    "cyberlimb_leg": "Cyberbein",
    "cyberlimb_lowerleg": "Cyberunterschenkel",
    "cyberlimb_foot": "Cyberfuß",
}
QUALITY = {"synthetic": "synthetisch", "obvious": "offensichtlich"}
SIDE = {"right": "rechts", "left": "links"}

DOCWAGON = {
    "docwagon_contract_basic": "DocWagon-Vertrag (Basis)",
    "docwagon_contract_gold": "DocWagon-Vertrag (Gold)",
    "docwagon_contract_platinum": "DocWagon-Vertrag (Platin)",
    "docwagon_contract_superplatinum": "DocWagon-Vertrag (Superplatin)",
}
PERIOD = {"month": "Monat", "year": "Jahr"}

TITLED = re.compile(r"[a-z]")


def brandcase(s: str) -> str:
    """Title-case a brand/model weapon name, keeping roman numerals upper."""
    out = []
    for w in s.split():
        if re.fullmatch(r"[ivx]+", w):
            out.append(w.upper())
        elif re.fullmatch(r"[a-z]{1,3}-?\d+.*", w) or "-" in w:
            out.append(w.upper())
        else:
            out.append(w[:1].upper() + w[1:])
    return " ".join(out)


def load_ids(kind):
    out = []
    for f in sorted(glob.glob(f"{REF}/{kind}/**/*.json", recursive=True)):
        for o in json.load(open(f)):
            if "id" in o:
                out.append(o["id"])
    return out


def split_rating(parts):
    """If the last segment is an int, pop it as rating."""
    if parts and re.fullmatch(r"\d+", parts[-1]):
        return parts[:-1], parts[-1]
    return parts, None


def gear_name(gid):
    parts = gid.split("/")
    assert parts[0] == "sr6core"
    cat = parts[1]
    rest = parts[2:]
    rest, rating = split_rating(rest)
    slug = "/".join(rest)
    suffix = f" {rating}" if rating else ""

    if cat == "commlink" and rating:
        return COMMLINK.get(rating, f"TODO Kommlink (Gerätestufe {rating})")
    if cat == "cyberdeck" and rating:
        return CYBERDECK.get(rating, f"TODO Cyberdeck (Gerätestufe {rating})")
    if cat == "credstick":
        return CREDSTICK.get(slug, f"TODO Credstick {slug}")
    if cat == "rfid":
        return RFID.get(slug) or GEAR.get(slug) or f"TODO RFID {slug}"
    if cat == "biotech" and slug in DOCWAGON:
        return DOCWAGON[slug]
    if cat == "biotech" and rest and rest[0] in DOCWAGON:
        base = DOCWAGON[rest[0]]
        per = PERIOD.get(rest[1], rest[1]) if len(rest) > 1 else ""
        return f"{base} – {per}" if per else base
    if cat == "weapon":
        if rest[:1] == ["cyber_implant_weapon"]:
            return CYBER_IMPLANT_WEAPON.get(rest[1], f"TODO {rest[1]}")
        if slug in WEAPON:
            return WEAPON[slug]
        # brand / model name -> keep, just cased
        return brandcase(slug)
    if cat == "cyberwaremod" and rest[:2] == ["cyberlimb", "defense_rating"]:
        return f"Cyberglied-Panzerung{suffix}"
    if cat == "cyberwaremod" and rest[:1] == ["{limb}"]:
        return f"Cyberglied-Attributssteigerung{suffix}"
    if cat == "cyberware" and rest and rest[0] in CYBERLIMB:
        # cyberlimb_arm / synthetic / right
        limb = CYBERLIMB[rest[0]]
        q = QUALITY.get(rest[1], rest[1]) if len(rest) > 1 else ""
        s = SIDE.get(rest[2], "") if len(rest) > 2 else ""
        extra = ", ".join(x for x in (q, s) if x)
        return f"{limb} ({extra})" if extra else limb
    if "{" in slug:
        return f"TODO {cat}: {slug}"

    if slug in GEAR:
        return GEAR[slug] + suffix
    # last-ditch: prettify the slug
    pretty = slug.replace("_", " ").replace("/", " ").strip()
    return f"TODO {pretty}{suffix}"


# --- rules -------------------------------------------------------------------
RULE_EXACT = {
    "armor defense rating": "Verteidigungswert durch Rüstung",
    "audio device modification - aural enhancement": "Audiogerät-Mod: Gehörverbesserung",
    "autopicker +1 lockpicking": "Autopicker: +1 auf Schlösser knacken",
    "base physical initiative dices": "Körperliche Initiative: Würfel (Basis)",
    "base physical initiative limit dices": "Körperliche Initiative: Würfellimit",
    "base physical initiative base": "Körperliche Initiative: Basiswert",
    "base astral initiative dices": "Astrale Initiative: Würfel (Basis)",
    "base astral initiative limit dices": "Astrale Initiative: Würfellimit",
    "base astral initiative base": "Astrale Initiative: Basiswert",
    "base initiative matrix ar dices": "Matrix-Initiative (AR): Würfel (Basis)",
    "base initiative matrix ar limit dices": "Matrix-Initiative (AR): Würfellimit",
    "base initiative matrix ar base": "Matrix-Initiative (AR): Basiswert",
    "base initiative matrix vr cold dices": "Matrix-Initiative (VR, kalt): Würfel (Basis)",
    "base initiative matrix vr cold limit dices": "Matrix-Initiative (VR, kalt): Würfellimit",
    "base initiative matrix vr cold base": "Matrix-Initiative (VR, kalt): Basiswert",
    "base initiative matrix vr hot dices": "Matrix-Initiative (VR, heiß): Würfel (Basis)",
    "base initiative matrix vr hot limit dices": "Matrix-Initiative (VR, heiß): Würfellimit",
    "base initiative matrix vr hot base": "Matrix-Initiative (VR, heiß): Basiswert",
    "base defense rating": "Verteidigungswert (Basis)",
    "base defense pool physical": "Verteidigungspool (körperlich)",
    "base defense astral": "Verteidigung (astral)",
    "base defense direct spell": "Verteidigung gegen direkte Zauber",
    "base defense indirect spell": "Verteidigung gegen indirekte Zauber",
    "base resist toxin": "Toxinwiderstand",
    "base resist physical damage": "Widerstand gegen körperlichen Schaden",
    "base resist astral damage": "Widerstand gegen astralen Schaden",
    "base physical condition monitor": "Körperlicher Zustandsmonitor",
    "base stun condition monitor": "Geistiger Zustandsmonitor",
    "base composure": "Fassung",
    "base judge intentions": "Menschenkenntnis",
    "base memory": "Erinnerungsvermögen",
    "base lift carry": "Heben und Tragen",
    "cyberjack +1 matrix initiative dice vr": "Cyberjack: +1 Matrix-Initiativewürfel (VR)",
    "cyberjack +2 matrix initiative dice vr": "Cyberjack: +2 Matrix-Initiativewürfel (VR)",
    "cybereye vision enhancement +1 visual perception": "Cyberauge: Sichtverbesserung +1 auf visuelle Wahrnehmung",
    "optical device modification - smartlink": "Optikgerät-Mod: Smartlink",
    "optical device modification - vision enhancement": "Optikgerät-Mod: Sichtverbesserung",
    "unarmed attack rating": "Unbewaffneter Angriffswert",
    "melee weapon strength to attack rating": "Nahkampfwaffe: Stärke auf Angriffswert",
}

RULE_TOKENS = [
    ("cyberware/bone lacing/", "Knochenverstärkung: "),
    ("cyberware/dermal plating/", "Hautpanzerung: "),
    ("cyberware/muscle replacement/", "Muskelersatz: "),
    ("cyberware/reaction enhancers/", "Reaktionsverstärker: "),
    ("cyberware/wired reflexes/", "Verdrahtete Reflexe: "),
    ("cyberware/cyberlimb/", "Cyberglied: "),
    ("cyberware/limb/", "Cyberglied: "),
    ("cyberware olfactorybooster ", "Geruchsverstärker: "),
    ("cyberware tastebooster ", "Geschmacksverstärker: "),
    ("cyberware voice modulator ", "Stimmmodulator: "),
    ("cyberware/cybereye/smartlink/", "Cyberauge-Smartlink: "),
    ("cyberware/", "Cyberware: "),
]
RULE_WORDS = {
    "body": "Konstitution",
    "agility": "Agilität",
    "strength": "Stärke",
    "reaction": "Reaktion",
    "defense rating": "Verteidigungswert",
    "defense": "Verteidigung",
    "initiative dices": "Initiativewürfel",
    "unarmed damage": "unbewaffneter Schaden",
    "unarmed physical damage": "unbewaffneter körperlicher Schaden",
    "unarmed attack rating": "unbewaffneter Angriffswert",
    "physical condition monitor": "körperlicher Zustandsmonitor",
    "olfactory perception": "Geruchswahrnehmung",
    "taste perception": "Geschmackswahrnehmung",
    "soundbased con": "klangbasiertes Überreden",
    "attack rating close": "Angriffswert (Nah)",
    "attack rating near": "Angriffswert (Kurz)",
    "attack rating medium": "Angriffswert (Mittel)",
    "attack rating far": "Angriffswert (Weit)",
    "attack rating very far": "Angriffswert (Sehr weit)",
    "arm replacement": "Armersatz",
    "forearm replacement": "Unterarmersatz",
    "hand replacement": "Handersatz",
    "leg replacement": "Beinersatz",
    "lower leg replacement": "Unterschenkelersatz",
    "foot replacement": "Fußersatz",
    "right": "rechts",
    "left": "links",
}


def rule_name(rid):
    body = rid[len("sr6core/"):] if rid.startswith("sr6core/") else rid

    if body in RULE_EXACT:
        return RULE_EXACT[body]

    m = re.fullmatch(r"specialisation of (\w+)", body)
    if m:
        sk = SKILLS.get(m.group(1), m.group(1))
        return f"Spezialisierung: {sk}"

    RULE_TEMPLATE = {
        "character/{limb}/{attribute}": "Cyberglied-Attribut (Basiswert)",
        "character/{limb}/limit/{attribute}": "Cyberglied-Attributslimit",
        "character/{direction}_forearm/{attribute}": "Cyberunterarm-Attribut (Basiswert)",
        "character/{direction}_hand/{attribute}": "Cyberhand-Attribut (Basiswert)",
        "character/{direction}_lower_leg/{attribute}": "Cyberunterschenkel-Attribut (Basiswert)",
        "character/{direction}_foot/{attribute}": "Cyberfuß-Attribut (Basiswert)",
        "cyberware/cyberlimb/defense_rating/{rating}": "Cyberglied-Panzerung (nach Stufe)",
        "cyberware/{limb}/{attribute}/{rating}": "Cyberglied-Attribut (nach Stufe)",
    }
    if body in RULE_TEMPLATE:
        return RULE_TEMPLATE[body]
    if "{" in body:
        return f"TODO Regel: {body}"

    LIMB_ERSATZ = {
        "arm": "Armersatz",
        "forearm": "Unterarmersatz",
        "hand": "Handersatz",
        "leg": "Beinersatz",
        "lower leg": "Unterschenkelersatz",
        "foot": "Fußersatz",
    }
    m = re.fullmatch(
        r"cyberware/(right|left) (.+) replacement/(agility|strength)", body
    )
    if m:
        side = "rechts" if m.group(1) == "right" else "links"
        ersatz = LIMB_ERSATZ.get(m.group(2), m.group(2) + "ersatz")
        attr = "Agilität" if m.group(3) == "agility" else "Stärke"
        return f"{ersatz} ({side}): {attr}"

    for pre, repl in RULE_TOKENS:
        if body.startswith(pre):
            tail = body[len(pre):]
            for en, de in sorted(RULE_WORDS.items(), key=lambda x: -len(x[0])):
                tail = re.sub(rf"\b{re.escape(en)}\b", de, tail)
                tail = tail.replace("/", " ")
            tail = re.sub(r"\b(\d+)p\b", r"\1K", tail)
            return repl + tail.strip()

    # generic word replacement
    tail = body
    hit = False
    for en, de in sorted(RULE_WORDS.items(), key=lambda x: -len(x[0])):
        new = re.sub(rf"\b{re.escape(en)}\b", de, tail)
        if new != tail:
            hit = True
        tail = new
    if hit:
        return tail
    return f"TODO Regel: {body}"


def main():
    result = {}
    for gid in load_ids("gear"):
        result[gid] = gear_name(gid)
    for rid in load_ids("rules"):
        result[rid] = rule_name(rid)

    result = dict(sorted(result.items()))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

    todos = [k for k, v in result.items() if v.startswith("TODO ")]
    print(f"wrote {len(result)} entries to {OUT}")
    print(f"  {len(todos)} still marked TODO ({100 * len(todos) // len(result)}%)")
    for k in todos:
        print(f"  {k}  ->  {result[k]}")


if __name__ == "__main__":
    main()
