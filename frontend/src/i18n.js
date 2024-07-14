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
            image_generation_in_progress: 'Das Bild wird noch erzeugt. Bitte aktualisiere diese Seite in ein paar Minuten erneut.',

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

            page_list_title_npcs: 'Schattenakte - NPC Liste',
            page_list_description_npcs: 'Liste aller generierten NPCs',
            page_list_title_locations: 'Schattenakte - Location Liste',
            page_list_description_locations: 'Liste aller generierten Locations',

            create_explanation_npc: 'Beschreibe den NPC',
            create_explanation_location: 'Beschreibe den Ort',
            create_explanation_custom: 'Beschreibe etwas grobes und lass GPT ausfüllen - oder gib unten direkt das Aussehen an',

            attribute_metatyp: 'Metatyp',
            attribute_beruf: 'Beruf',
            attribute_ethnizität: 'Ethnizität',
            attribute_geschlecht: 'Geschlecht',
            attribute_alter: 'Alter',
            attribute_eigenarten: 'Eigenarten',
            attribute_detailliertes_aussehen: 'Aussehen',

            attribute_hintergrundgeschichte: 'Hintergrund',
            attribute_erfahrungen: 'Erfahrung',
            attribute_ressentiments: 'Abneigung',
            attribute_motivationen: 'Motivation',
            attribute_ziele: 'Ziele',
            attribute_hobbys_und_interessen: 'Hobbys',
            attribute_familie: 'Familie',
            attribute_kontakte: 'Kontakte',
            attribute_wohnort: 'Wohnort',
            attribute_konzernzugehörigkeit: 'Konzern',

            attribute_stärken: 'Stärken',
            attribute_schwächen: 'Schwächen',
            attribute_fertigkeiten: 'Fertigkeiten',
            attribute_ausrüstung: 'Ausrüstung',
            attribute_lootbare_gegenstände: 'Loot',
            attribute_geheimnis: 'Geheimnis',

            attribute_name: 'Name',
            attribute_typ: 'Typ',
            attribute_aussehen: 'Aussehen',
            attribute_stadtteil_zone: 'Gebiet',
            attribute_zugehörige_gruppe_corp_fraktion: 'Zugehörigkeit',
            attribute_besonderheiten: 'Besonderheiten',
            attribute_hinweise: 'Hinweise',
            attribute_verfügbarkeit_von_sicherheitssystemen: 'Sicherheit',
            attribute_aktuelle_aktionen_events: 'Aktionen',
            attribute_gerüchte_und_geschichten_über_die_location: 'Gerüchte',

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
        },
    },
    en: {
        translation: {
            app_name: "SINer - Shadowrun NPC Generator",
            prompt_failed_connection: "Connection issues. Please try again later.",
            input_was_flagged_by_gpt: 'Input was filtered out by GPT moderation. Please insert something less extreme.',
            npc_was_flagged_by_gpt: 'NPC was flagged as inappropriate. Please insert something less extreme.',
            gpt_raised_an_error: 'GPT raised an error. Please try again later.',
            gpt_result_insufficient: 'GPT denied this request. Please try something else.'
        },
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