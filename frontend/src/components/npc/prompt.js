import React, {useState} from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, LoadingBars, Text} from "@arwes/core";
import {Animator} from "@arwes/animation";
import api from "../../axios";
import i18next from "../../i18n";
import NPCComplete from "./npc_complete";
import NPCCard from "./npc_card";
import NPCPrivate from "./npc_private";
import NPCSkills from "./npc_skills";
import {useLoaderData} from "react-router";
import {useNavigate, useNavigation} from "react-router-dom";
import AttributeList from "../attribute_list";
import Prompt from "../entity/prompt";

const EXAMPLES = [
    'Erstelle einen Werkstattbesitzer',
    'Erstelle eine widersprüchliche Person',
    'Erstelle einen Clubbesitzer',
    'Erstelle einen Buchhalter, der für einen der großen Konzern arbeitet.',
    'Erstelle einen Straßendoc',
    'Erstelle einen Büroangestellten',
    'Erstelle einen Magietheoretiker',
    'Erstelle einen NPC, der mal Runner werden will',
    'Erstelle einen erfolglosen Restaurantbesitzer',
    'Erstelle einen Schmuggler, der ein Fahrrad nutzt',
    'Erstelle einen Drogendealer',
    'Erstelle ein Gangmitglied',
    'Erstelle einen Straßenmusiker',
    'Erstelle einen Reporter',
    'Erstelle einen Barkeeper',
    'Erstelle einen Ökoterrorist',
    'Erstelle einen Büroangestellten, der gerne ein Ökoterrorist wäre',
    'Erstelle eine künstliche Intelligenz',
    'Erstelle einen NPC aus Hamburg',
    'Erstelle einen ausgebrannten Magier',
    'Erstelle einen Magier',
    'Erstelle einen Anarchisten',
    'Erstelle einen Verschwörungstheoretiker',
    'Erstelle einen korrupten Polizisten',
    'Erstelle einen korrupten Politiker',
    'Erstelle ein Vorstandsmitglied eines großen Konzerns',
    'Erstelle einen Fabrikarbeiter',
    'Erstelle einen Runner',
    'Erstelle einen Schieber',
    'Erstelle eine Babuschka',
    'Erstelle einen Zwerg',
    'Erstelle einen Taxifahrer',
    'Erstelle einen Kultisten',
    'Erstelle einen exzentrischen Artefaktsammler',
    'Erstelle einen Fährmann',
    'Erstelle einen Bodyguard',
    'Erstelle einen Türsteher',
    'Erstelle einen Obdachlosen',
    'Erstelle einen Troll',
    'Erstelle einen Ork',
    'Erstelle einen Sicherheitsberater',
    'Erstelle einen Wissenschaftler, der für einen der großen Konzern arbeitet.',
    'Erstelle einen Elfen',
    'Erstelle einen Frachterpiloten',
    'Erstelle einen kriminellen Hacker',
    'Erstelle einen Privatdetektiv',
    'Erstelle einen paranormalen Forscher',
    'Erstelle einen NPC, der ein pensionierter Shadowrunner ist',
    'Erstelle einen Konzernspion',
    'Erstelle eine professionelle Attentäterin',
    'Erstelle einen Illegalen Waffenhändler',
    'Erstelle einen Söldner',
    'Erstelle einen Guerillakämpfer',
    'Erstelle einen Bürgerrechtler',
    'Erstelle einen Graffiti-Künstler',
    'Erstelle einen paranormalen Kreaturenjäger',
    'Erstelle einen Kriegsveteranen',
    'Erstelle einen religiösen Fanatiker',
    'Erstelle einen NPC aus Berlin',
    'Erstelle einen Cyberkriminellen',
    'Erstelle einen Arzt, der im Heimlichen Experimente durchführt',
    'Erstelle einen Kriminellen Unterweltboss',
    'Erstelle einen flüchtigen Kriegsverbrecher',
    'Erstelle einen privaten Sicherheitsdienstmitarbeiter',
    'Erstelle einen paranormale Kreaturenexperten',
    'Erstelle einen berühmte Rockstar',
    'Erstelle einen reichen Philanthrop',
    'Erstelle einen schizophrenen Matrixentwickler',
    'Erstelle einen Magielehrer aus der Magierschule',
    'Erstelle einen sadistischen Gangführer',
    'Erstelle einen überzeugten Transhumanisten',
    'Erstelle einen Feuerwehrmann, der Angst vor Feuer hat',
    'Erstelle einen Friedensbotschafter, der gerne Streit anfängt',
    'Erstelle einen hochgebildeten Trottel',
    'Erstelle einen philosophischen Söldner',
    'Erstelle einen enthusiastischen Pessimisten',
    'Erstelle einen Umweltaktivist, der in einer Ölgesellschaft arbeitet',
    'Erstelle einen zynischen Motivationsredner',
    'Erstelle einen reisenden Einsiedler',
    'Erstelle einen paranoischen Sicherheitsberater',
    'Erstelle einen Architekten mit Platzangst',
    'Erstelle einen zwielichtigen Anwalt',
    'Erstelle einen hochrangigen Militäroffizier',
    'Erstelle einen drogenabhängigen Künstler',
    'Erstelle einen ehemaligen Runner, der jetzt zum Gesetz geworden ist',
    'Erstelle einen Zuhälter',
    'Erstelle einen verdeckten Ermittler',
    'Erstelle einen GreenWar-Aktivisten',
    'Erstelle einen Nachbarschaftswächter',
    'Erstelle einen ausgemusterten Soldaten',
    'Erstelle einen humanitären Ladenbesitzer',
    'Erstelle einen Barmann mit einer kriminellen Vergangenheit',
    'Erstelle einen Konzernspion',
    'Erstelle einen kleinen MegaKonzern-Informanten',
    'Erstelle einen Bewährungshelfer',
    'Erstelle einen Dronenhändler',
    'Erstelle einen Cyberware-Ingenieur',
    'Erstelle einen Informanten, der ein Informant ist, weil er seine Schulden abbezahlen muss.',
    'Erstelle einen Schrotthändler',
    'Erstelle einen Security-Angestellten',
    'Erstelle einen Sprengstoffexperten',
    'Erstelle einen schattigen Anwalt',
    'Erstelle einen Betreiber eines illegalen Cybercafés',
    'Erstelle einen Spion eines konkurrierenden Konzerns'
]


const NPCPrompt = props => {
    const default_entity = useLoaderData()

    const [entity, setEntity] = useState(default_entity);
    const [check, setCheck] = useState(false);
    const [editable, setEditable] = useState(true);

    const relevantAttributes = ['Aussehen', 'Parameter']

    return (
        <Prompt entityType={'npc'} examples={EXAMPLES} entity={entity} setEntity={setEntity}
                setEditable={setEditable}
                check={check} setCheck={setCheck}>
            <div>
                <NPCCard entity={entity}  editable={true} editableDisabled={!editable}  check={check}/>
                <NPCPrivate entity={entity}  editable={true} editableDisabled={!editable}  check={check}/>
                <NPCSkills entity={entity}  editable={true} editableDisabled={!editable}  check={check}/>
            </div>

        </Prompt>)
}




export default NPCPrompt;
