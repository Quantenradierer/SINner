import i18next from "i18next";
import {initReactI18next} from "react-i18next";
// "Inline" English and Arabic translations.
// We can localize to any language and any number of languages.
const resources = {
    de: {
        translation: {
            app_name: "Schattenakte - Shadowrun NPC Generator",
            prompt_failed_connection: "Verbindungsprobleme. Bitte versuche es später erneut.",
            input_was_flagged_by_gpt: 'Die Eingabe wurde von der GPT Moderation ausgefiltert. Versuche es erneut oder gib etwas anderes ein.',
            npc_was_flagged_by_gpt: 'Der NPC wurde von GPT als unangemessen eingeschätzt. Versuche es erneut oder gib etwas anderes ein.',
            gpt_raised_an_error: 'GPT hat einen Fehler geworfen. Bitte versuche es später erneut.',
            npc_incomplete: 'Der NPC ist unvollständig. Bitte fülle alle Felder aus bevor du speicherst.',
            image_generation_in_progress: 'Das Bild wird derzeit erstellt und in Kürze angezeigt.',
            prompt_wait: "Wird generiert... bitte warten...",

            header_profile: "Account",

            page_prompt_title: "Schattenakte - Generator",
            page_impressum_title: "Schattenakte - Impressum",
            page_login_title: "Schattenakte - Login",
            page_profile_title: "Schattenakte - Account",
            page_list_title: "Schattenakte - Liste",
            page_list_description: "Liste aller Akteneinträge",

            favorite_list_empty_text: "Du hast noch keine Favoriten hinzugefügt. Klicke auf das Sternsymbol in einem Eintrag, um ihn zu deinen Favoriten hinzuzufügen.",
            search_list_empty_text: "Deine Suche ergab keine Ergebnisse. Versuche es mit einem anderen Suchbegriff.",
            npc_list_empty_text: "Das sollte nie passieren. Entweder ist dein Internet oder der Server down. Versuche es später erneut.",
            location_list_empty_text: "Das sollte nie passieren. Entweder ist dein Internet oder der Server down. Versuche es später erneut.",




            menu_npcs: 'NPCs',
            menu_locations: 'Locations',
            menu_critters: 'Critters',
            menu_vehicles: 'Vehicles',
            menu_customs: "Bildgenerator",
            menu_feedback: "Feedback",
            menu_impressum: "Impressum",

            menu_login: 'Login',
            menu_register: 'Register',
            menu_logout: 'Logout',



            tab_header_npc_list: "NPCs",
            tab_header_npc_create: "NPCs",
            tab_header_locations_list: "Orte",
            tab_header_locations_create: "Orte",
            tab_header_customs_list: "Bildgenerator",
            tab_header_customs_create: "Bildgenerator",
            tab_header_favorites_list: "Favoriten",

            tab_header_npcs_default: 'NPC',
            tab_header_npcs_sr6: 'SR6',
            tab_header_npcs_gallery: 'Galerie',
            tab_header_locations_default: 'Location',
            tab_header_locations_reviews: 'Reviews',
            tab_header_locations_gallery: 'Galerie',

            create_explanation_npc: 'Beschreibe deinen NPC. Du kannst Aussehen, Beruf, den Hintergrund oder sogar Werte angeben, GPT erzeugt dann den Rest. Du kannst ihn danach noch abändern.',
            create_explanation_location: 'Beschreibe den Ort. Du kannst das Gebiet oder eine grobe Beschreibung dazuschreiben. GPT erzeugt dann den Rest. Du kannst ihn danach noch abändern.',
            create_explanation_custom: 'Beschreibe etwas grobes und lass GPT ausfüllen - oder gib unten direkt das Aussehen an',

            entity_create: 'Erstellen',
            entity_save: 'Veröffentlichen',
            entity_favorite: 'Favorisieren',

            attribute_metatype: 'Metatyp',
            attribute_profession: 'Beruf',
            attribute_ethnicity: 'Ethnizität',
            attribute_gender: 'Geschlecht',
            attribute_age: 'Alter',
            attribute_quirks: 'Eigenarten',
            attribute_appearance: 'Aussehen',

            attribute_backstory: 'Geschichte',
            attribute_experiences: 'Erfahrung',
            attribute_resentments: 'Abneigung',
            attribute_motivations: 'Motivation',
            attribute_hobbies_and_interests: 'Hobbys',
            attribute_family: 'Familie',
            attribute_contacts: 'Kontakte',

            attribute_strengths: 'Stärken',
            attribute_weaknesses: 'Schwächen',
            attribute_skills: 'Fertigkeiten',
            attribute_equipment: 'Ausrüstung',
            attribute_secret: 'Geheimnis',

            attribute_name: 'Name',
            attribute_type: 'Typ',
            attribute_aussehen: 'Aussehen',
            attribute_special_features: 'Besonderheiten',
            attribute_besonderheiten: 'Besonderheiten',
            attribute_remarks: 'Hinweise',
            attribute_security_systems: 'Sicherheit',
            attribute_events: 'Aktionen',
            attribute_rumors_and_stories: 'Gerüchte',

            attribute_parameter: 'Parameter',

            "--s 50": "stylize low",
            "--s 100": "stylize medium",
            "--s 250": "stylize high",
            "--s 750": "stylize very high",

            "--ar 1:1": "Quadratisch (1:1)",
            "--ar 2:3": "Hoch (2:3)",
            "--ar 4:7": "Portrait (4:7)",
            "--ar 3:2": "Breit (3:2)",
            "--ar 7:4": "Landschaft (7:4)",

            "--chaos 0": "Kein Chaos",
            "--chaos 7": "Wenig Chaos",
            "--chaos 25": "Mittleres Chaos",
            "--chaos 50": "Hohes Chaos",
            "--chaos 100": "Maximales Chaos",

            tab_loading_text: "Daten werden generiert...",


            npc_card_title_background: 'Hintergrund',
            npc_card_title_social: 'Soziales',
            npc_card_title_personality: 'Persönlichkeit',
            npc_card_title_skills_and_traits: 'Eigenschaften',

            npc_attribute_bod: 'Kon',
            npc_attribute_agi: 'Agi',
            npc_attribute_rea: 'Rea',
            npc_attribute_str: 'Str',
            npc_attribute_wil: 'Wil',
            npc_attribute_log: 'Log',
            npc_attribute_int: 'Int',
            npc_attribute_cha: 'Cha',
            npc_attribute_edg: 'Edg',
            npc_attribute_mag: 'Mag',
            npc_attribute_res: 'Res',

            npc_skill_astral: 'Astral',
            npc_skill_athletics: 'Athletik',
            npc_skill_biotech: 'Biotech',
            npc_skill_close_combat: 'Nahkampf',
            npc_skill_con: 'Überreden',
            npc_skill_conjuring: 'Beschwören',
            npc_skill_cracking: 'Cracken',
            npc_skill_electronics: 'Elektronik',
            npc_skill_enchanting: 'Verzaubern',
            npc_skill_engineering: 'Mechanik',
            npc_skill_exotic_weapons: 'Exotische Waffen',
            npc_skill_firearms: 'Feuerwaffen',
            npc_skill_influence: 'Einfluss',
            npc_skill_outdoors: 'Natur',
            npc_skill_perception: 'Wahrnehmung',
            npc_skill_piloting: 'Steuern',
            npc_skill_sorcery: 'Hexerei',
            npc_skill_stealth: 'Heimlichkeit',
            npc_skill_tasking: 'Tasken',

            npc_entity_is_not_published: 'Dieser NPC wurde noch nicht veröffentlicht und kann nur durch die exakte URL aufgerufen werden. Speichere den Link, um später darauf zugreifen zu können.',

            npc_skill: 'Fertigkeit',
            npc_skill_value: 'Wert',

            npc_physical_condition: 'Körperlich',
            npc_stun_condition: 'Geistig',


            location_entity_is_not_published: 'Diese Location wurde noch nicht veröffentlicht und kann nur durch die exakte URL aufgerufen werden. Speichere den Link, um später darauf zugreifen zu können.',


            auth_signup: 'Registrieren',
            auth_signup_description: 'Noch keinen Account? Hier registrieren',
        },
    },
    en: {
        translation: {
            "app_name": "Shadow File - Shadowrun NPC Generator",
            "prompt_failed_connection": "Connection issues. Please try again later.",
            "input_was_flagged_by_gpt": "The input was filtered by GPT moderation. Try again or enter something else.",
            "npc_was_flagged_by_gpt": "The NPC was considered inappropriate by GPT. Try again or enter something else.",
            "gpt_raised_an_error": "GPT encountered an error. Please try again later.",
            "npc_incomplete": "The NPC is incomplete. Please fill out all fields before saving.",
            "image_generation_in_progress": "The image is still being generated. Please refresh this page again in a few minutes.",
            "prompt_wait": "Generating... please wait...",

            "menu_npcs": "NPCs",
            "menu_locations": "Locations",
            "menu_critters": "Critters",
            "menu_vehicles": "Vehicles",
            "menu_customs": "Image Generator",
            "menu_feedback": "Feedback",
            "menu_impressum": "Impressum",
            "menu_login": "Login",
            "menu_register": "Register",
            "menu_logout": "Logout",
            "page_list_title_npcs": "Schattenakte - NPC List",
            "page_list_description_npcs": "List of all generated NPCs",
            "page_list_title_locations": "Schattenakte - Location List",
            "page_list_description_locations": "List of all generated locations",
            "page_list_title_customs": "Schattenakte - NPC List",
            "page_list_description_customs": "List of all generated custom images",
            "create_explanation_npc": "Describe your NPC. You can specify appearance, profession, background, or even stats, and GPT will generate the rest. You can modify it later.",
            "create_explanation_location": "Describe the location. You can add the area or a rough description. GPT will generate the rest. You can modify it later.",
            "create_explanation_custom": "Describe something roughly and let GPT fill it in - or directly specify the appearance below",
            "attribute_metatype": "Metatype",
            "attribute_profession": "Profession",
            "attribute_ethnicity": "Ethnicity",
            "attribute_gender": "Gender",
            "attribute_age": "Age",
            "attribute_quirks": "Quirks",
            "attribute_appearance": "Appearance",
            "attribute_backstory": "Backstory",
            "attribute_experiences": "Experiences",
            "attribute_resentments": "Resentments",
            "attribute_motivations": "Motivation",
            "attribute_hobbies_and_interests": "Hobbies",
            "attribute_family": "Family",
            "attribute_contacts": "Contacts",
            "attribute_konzernzugehörigkeit": "Corporation",
            "attribute_strengths": "Strengths",
            "attribute_weaknesses": "Weaknesses",
            "attribute_skills": "Skills",
            "attribute_equipment": "Equipment",
            "attribute_secret": "Secret",
            "attribute_name": "Name",
            "attribute_typ": "Type",
            "attribute_aussehen": "Appearance",
            "attribute_stadtteil_zone": "Area",
            "attribute_zugehörige_gruppe_corp_fraktion": "Affiliation",
            "attribute_besonderheiten": "Special Features",
            "attribute_hinweise": "Hints",
            "attribute_verfügbarkeit_von_sicherheitssystemen": "Security",
            "attribute_aktuelle_aktionen_events": "Actions",
            "attribute_gerüchte_und_geschichten_über_die_location": "Rumors",
            "attribute_parameter": "Parameter",
            "--s 50": "stylize low",
            "--s 100": "stylize medium",
            "--s 250": "stylize high",
            "--s 750": "stylize very high",
            "--ar 1:1": "Square (1:1)",
            "--ar 2:3": "Tall (2:3)",
            "--ar 4:7": "Portrait (4:7)",
            "--ar 3:2": "Wide (3:2)",
            "--ar 7:4": "Landscape (7:4)",
            "--chaos 0": "No Chaos",
            "--chaos 7": "Low Chaos",
            "--chaos 25": "Medium Chaos",
            "--chaos 50": "High Chaos",
            "--chaos 100": "Maximum Chaos"
        }
    },
};

i18next
    .use(initReactI18next)
    .init({
        resources,
        lng: "de",
        interpolation: {
            escapeValue: false,
        },
        debug: true
    });
export default i18next;