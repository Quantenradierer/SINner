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
            gpt_result_insufficient: 'GPT verweigerte ein vollständiges Ergebnis. Bitte versuch etwas anderes.'
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