import React, {useState} from "react";
import LocationCard from "./location_card";
import CommentCard from "./comment_card";

import Prompt from "../entity/prompt";
import {useLoaderData} from "react-router";


const EXAMPLES = [
    'Generiere eine Bar',
    'Generiere eine Stadtbezirk',
    'Generiere eine geheime Unternehmensforschungsanlage',
    'Generiere eine hochsichere Bank',
    'Generiere eine städtische Bar oder ein Nachtclub',
    'Generiere eine dystopische Slum Region',
    'Generiere einen illegalen Cyberware-Markt',
    'Generiere eine verstohlene magische Bibliothek',
    'Generiere eine futuristische Wohnkomplexanlage',
    'Generiere ein verlassenes Industriesilo',
    'Generiere eine Gang-Hochburg',
    'Generiere einen geheimen Untergrundbunker',
    'Generiere ein von Konzernen kontrolliertes Stadtviertel',
    'Generiere ein High-Tech-Sicherheitsgefängnis',
    'Generiere einen verfallenen Amüsierungspark',
    'Generiere eine illegale Straßenrennstrecke',
    'Generiere ein überlaufenes Flüchtlingscamp',
    'Generiere eine hochrangige VIP-Residenz',
    'Generiere eine kontaminierte Strahlungszone',
    'Generiere einen versteckten Ort für Schwarzmagie-Rituale',
    'Generiere einen urbanen Dschungel aus technisch hochgerüsteten Bürogebäuden',
    'Generiere einen hochsicheren Datenzentrum',
    'Generiere einen rauen Hafenbereich',
    'Generiere ein futuristische Einkaufszentrum',
    'Generiere ein Spielcasino',
    'Generiere ein von organisierten Kriminellen kontrolliertes Stadtviertel',
    'Generiere eine verlassene Fabrik',
    'Generiere eine futuristische Krankenhausanlage',
    'Generiere eine Drohnenkampfarena',
    'Generiere ein Cybernetik-Labor',
    'Generiere einen Großstadtdschungel',
    'Generiere ein Bürogebäude',
    'Generiere ein Corp-Tower',
    'Generiere eine extraterritoriale Konzern-Enklave',
    'Generiere einen illegales Waffendepot',
    'Generiere ein Schmuggelhafen',
    'Generiere eine Gentech-Forschungseinrichtung',
    'Generiere eine Kontrollstelle der Lone Star Sicherheitsdienste',
    'Generiere einen Drogenpark',
    'Generiere ein noirhaftes Shadowrunner Safehouse',
    'Generiere eine futuristische Gangsterhöhle',
    'Generiere eine technisch hochmodernes Safehouse',
    'Generiere eine Untergrund-Kampfarena',
    'Generiere eine Neon-beleuchtete Nachtclub ',
    'Generiere eine geheime Schwarzmarkt-Basis',
    'Generiere eine Hightech-Hacker-Wohnung',
    'Generiere eine im Dschungel versteckte Forschungsstation',
    'Generiere eine zwielichtige Botschafts-Lounge',
    'Generiere ein Penthouse',
    'Generiere eine Penthouse-Wohnung in einem Wolkenkratzer',
    'Generiere eine Squatter-Siedlung',
    'Generiere eine verdeckte Schmuggler-Höhle',
    'Generiere eine geheime Street-Doc-Klinik',
    'Generiere eine dystopische Nomaden-Wohnsiedlung',
    'Generiere einen glamourösen Elfensalon',
    'Generiere ein Ramen-Laden',
    'Generiere eine Cocktailbar',
    'Generiere eine Bierstube',
    'Generiere eine Kneipe',
    'Generiere eine Diskothek',
    'Generiere einen Nachtclub',
    'Generiere eine Rooftop-Bar',
    'Generiere ein Lost Place',
    'Generiere eine Schattenklinik',
    'Generiere eine illegale Spielhölle',
    'Generiere eine hochtechnologisierte Archivbibliothek',
    'Generiere einen konzernfreien Drogen-Marktplatz',
    'Generiere ein paranormales Museum',
    'Generiere einen hochfrequentierten Flughafen',
    'Generiere eine futuristische Sport-Anlage',
    'Generiere ein urbanes Drogenlabor',
    'Generiere eine organisierte Verbrechersyndikat-HQ',
    'Generiere eine geheimnisvolle Abwasserkanäle',
    'Generiere eine Cyberpunk-Sikh-Tempel',
    'Generiere einen hochmodernen Kunstgalerien',
    'Generiere einen hochfrequentierten Schwarzmarkt',
    'Generiere eine moderne Medienproduktionsstätte',
    'Generiere eine abgelegene Ritualstätte',
    'Generiere einen futuristischen Konzertsaal',
    'Generiere einen gigantischen dystopischen Konzerncampus',
    'Generiere eine dystopische Massenwohnanlage',
    'Generiere eine illegale Implantatklinik',
    'Generiere einen belebten städtischen Markt',
    'Generiere eine technologisch erweiterte Raststätte',
    'Generiere eine exklusive Konzernschule',
    'Generiere eine zwielichtige Gefängniskolonie',
    'Generiere eine bestens ausgestattete Runner-Unterkunft',
    'Generiere ein futuristisches Straßenrennen',
    'Generiere eine unauffällige Schattenbar',
    'Generiere eine hochfrequentierte Waffenschmuggler-Werkstatt',
    'Generiere ein schillerndes Entertainment-Viertel',
    'Generiere eine gehobene Wohnanlage',
    'Generiere ein futuristisches Technologie-Museum',
    'Generiere ein paranormales Forschungslabor',
    'Generiere eine zwielichtige Hacker-Basis',
    'Generiere einen Cybernetik-Prothesenladen',
    'Generiere eine futuristische Sushi-Bar',
    'Generiere eine gut vernetzte Schmugglerbar',
]

const PromptLocation = props => {
    const default_entity = useLoaderData()

    const [entity, setEntity] = useState(default_entity);
    const [check, setCheck] = useState(false);
    const [editable, setEditable] = useState(true);

    return (<Prompt entityType={'location'} examples={EXAMPLES} entity={entity} setEntity={setEntity} setEditable={setEditable}
                    editableDisabled={props.disabled}
                    check={check} setCheck={setCheck}>
         <LocationCard entity={entity} editable={true} editableDisabled={!editable} check={check}/>
         <CommentCard key={'comments' + Math.random()} entity={entity}/>
    </Prompt>)
}


export default PromptLocation;
