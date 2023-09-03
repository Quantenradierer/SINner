import React from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, Text} from "@arwes/core";
import {Animator} from "@arwes/animation";
import api from "../axios";
import i18next from "../i18n";
import NPCComplete from "./npc_complete";
import NPCCard from "./npc_card";
import NPCPrivate from "./npc_private";
import NPCSkills from "./npc_skills";

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

function random_prompt() {
    return EXAMPLES[Math.floor(Math.random() * EXAMPLES.length)];
}

class Prompt extends React.Component {
    constructor(props) {
        super(props)
        let url = new URL(window.location.href)
        const params = new URLSearchParams(url.search)
        let show = true
        this.state = {
            show: show,
            prompt: random_prompt(),
            loadingState: 'prompt',
            activate: true,
            error: null,
            npc: {attributes: {}}
        }

        this.handleChange = this.handleChange.bind(this)
        this.handleClick = this.handleClick.bind(this)
        this.handleSave = this.handleSave.bind(this)
    }

    handleChange(event) {
        this.setState({prompt: event.target.value});
    }

    handleClick(event) {
        event.preventDefault()
        let self = this;
        self.setState({loadingState: 'waiting'})

        api.post('/api/npc_creator/npcs/prompt/', {prompt: this.state.prompt, npc: this.state.npc})
            .then(function (response) {
                if (response.data.type === 'success') {
                    self.setState({'npc': response.data.npc})
                } else {
                    self.setState({'error': i18next.t(response.data.error)})
                }
            })
            .catch(function (error) {
                self.setState({'error': i18next.t('prompt_failed_connection')})
            })
            .finally(function () {
                self.setState({loadingState: 'prompt'})
            });
    }

    handleSave(event) {
        event.preventDefault()
        let self = this;
        self.setState({loadingState: 'waiting'})

        api.post('/api/npc_creator/npcs/save/', {npc: this.state.npc})
            .then(function (response) {
                console.log(response.data.npc)
                if (response.data.type === 'success') {
                    window.location.href = '/npcs/' + response.data.npc.id
                } else {
                    self.setState({'error': i18next.t(response.data.error)})
                }
            })
            .catch(function (error) {
                self.setState({'error': i18next.t('prompt_failed_connection')})
            })
            .finally(function () {
                self.setState({loadingState: 'prompt'})
            });
    }


    render() {
        let errorDialog = ''
        if (this.state.error !== null) {
            errorDialog = <div key='error' style={{width: '100%'}}>
                <FramePentagon
                    style={{margin: '15px 0px 15px 0px', display: 'flex'}}
                    palette='secondary'
                    lineWidth={1}
                >
                    <Text>{this.state.error}</Text>
                </FramePentagon>
            </div>
        }


        let prompt = <div></div>

        if (!this.state.show) {
            return (<div key='nothing'></div>)
        } else if (this.state.loadingState === 'prompt') {
            prompt = <div key='prompt'>
                <FrameLines style={{width: '100%'}}>
                    <form>
                        <Text> Beschreibe deinen NPC. Gib keine persönlichen Informationen
                            von dir an, da diese öffentlich zugänglich sein werden!

                            <br/>Das Bild wird erst nach dem Speichern des NPCs erzeugt.
                        </Text>
                        <div style={{display: 'flex', flexDirection: 'row'}}>
                            <input value={this.state.prompt} onChange={this.handleChange} maxLength="255"
                                   type="text"
                                   id="prompt"/>
                            <Button style={{margin: '3px 3px 3px 13px'}} FrameComponent={FrameCorners} onClick={this.handleClick}>
                                <Text>Ausfüllen</Text>
                            </Button>
                        </div>
                    </form>
                </FrameLines>
            </div>
        } else if (this.state.loadingState === 'waiting') {
            prompt = <div key='waiting' style={{width: '100%'}}>
                <FrameLines style={{width: '100%'}}>
                    <Animator animator={{
                        activate: this.state.activate,
                        manager: 'stagger',
                        duration: {stagger: 300}
                    }}>
                        <Text>Bitte warten...</Text><br/>
                        <Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text>
                        <Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text>
                    </Animator>
                </FrameLines>
            </div>
        }

        let disabled = this.state.loadingState === 'waiting'

        return (<div>
            <div style={{margin: 15}}>
                {errorDialog}
            </div>
            <div style={{margin: 15}}>
                {prompt}
            </div>

            <div style={{display: 'flex', alignItems: 'center', justifyContent: 'flex-end', margin: 15}}>
                <Button style={{margin: 3}} onClick={this.handleSave}>
                    <Text>NPC speichern und Bild generieren</Text>
                </Button>
            </div>
            <div>
                <NPCCard npc={this.state.npc} editable={true} editableDisabled={disabled}/>
                <NPCPrivate npc={this.state.npc} editable={true} editableDisabled={disabled}/>
                <NPCSkills npc={this.state.npc} editable={true} editableDisabled={disabled}/>
            </div>

        </div>)
    }
}

export default Prompt;
