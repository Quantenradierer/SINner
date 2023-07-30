import i18next from "i18next";
import {initReactI18next} from "react-i18next";
// "Inline" English and Arabic translations.
// We can localize to any language and any number of languages.
const resources = {
    de: {
        translation: {
            app_name: "SINer - Shadowrun NPC Generator",
            prompt_failed_connection: "Verbindungsprobleme. Bitte versuche es später erneut.",
            input_was_flagged_by_gpt: 'Die Eingabe wurde von der GPT Moderation ausgefiltert. Bitte gib etwas weniger extremes ein.',
            npc_was_flagged_by_gpt: 'Der NPC wurde von GPT als unangemessen eingeschätzt. Bitte gib etwas weniger extremes ein.',
            gpt_raised_an_error: 'GPT hat einen Fehler geworfen. Bitte versuche es später erneut.',
            gpt_result_insufficient: 'GPT verweigerte ein vollständiges Ergebnis. Bitte versuch etwas anderes.',
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
            attribute_geheimnis: 'Geheimnis'
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