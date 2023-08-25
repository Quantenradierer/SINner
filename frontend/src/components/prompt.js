import React from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, Text} from "@arwes/core";
import {Animator} from "@arwes/animation";
import api from "../axios";
import i18next from "../i18n";

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
    'Erstelle einen Freizeitdrogenanwender',
    'Erstelle einen flüchtigen Kriegsverbrecher',
    'Erstelle einen privaten Sicherheitsdienstmitarbeiter',
    'Erstelle einen paranormale Kreaturenexperten',
    'Erstelle eine berühmte Rockstar',
    'Erstelle einen reichen Philanthrop',
    'Erstelle einen schizophrenen Matrixentwickler',
    'Erstelle einen ghulfizierten Politiker',
    'Erstelle einen Magielehrer aus der Magierschule',
    'Erstelle einen sadistischen Gangführer',
    'Erstelle einen überzeugten Transhumanisten',
    'Erstelle einen Feuerwehrmann, der Angst vor Feuer hat',
    'Erstelle einen veganen Metzger',
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
    'Erstelle einen jungen Technomancer',
    'Erstelle einen verdeckten Ermittler',
    'Erstelle einen GreenPeace-Aktivisten',
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
        this.state = {show: show, prompt: random_prompt(), loadingState: 'prompt', activate: true, error: null}

        this.handleChange = this.handleChange.bind(this)
        this.handleClick = this.handleClick.bind(this)
    }

    handleChange(event) {
        this.setState({prompt: event.target.value});
    }

    handleClick() {
        let self = this;
        self.setState({loadingState: 'waiting'})

        api.post('/api/npc_creator/npcs/prompt/', {prompt: this.state.prompt})
            .then(function (response) {
                if (response.data.type === 'success') {
                    window.location.href = '/npcs/' + response.data.id
                } else {
                    self.setState({'error': i18next.t(response.data.error)})
                }
            })
            .catch(function (error) {
                self.setState({'error': i18next.t('prompt_failed_connection')})
                //window.location.href = '/npcs/error'
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
                    style={{ margin: '15px 0px 15px 0px', display: 'flex'}}
                    palette='secondary'
                    lineWidth={1}
                >
                    <Text>{this.state.error}</Text>
                </FramePentagon>
            </div>
        }

        if (!this.state.show) {
            return (<div key='nothing'></div>)
        } else if (this.state.loadingState === 'prompt') {
            return (
                <div key='prompt'>
                    {errorDialog}
                    <FrameLines style={{width: '100%'}}>
                        <form>
                            <Text> Beschreibe deinen NPC. Gib keine persönlichen Informationen
                                von dir an, da diese öffentlich zugänglich sein werden!</Text>
                            <div style={{display: 'flex', flexDirection: 'row'}}>
                                <input value={this.state.prompt} onChange={this.handleChange} maxLength="255"
                                       type="text"
                                       id="prompt"/>
                                <Button style={{margin: 3}} FrameComponent={FrameCorners} onClick={this.handleClick}>
                                    <Text>Erstellen</Text>
                                </Button>
                            </div>
                        </form>
                    </FrameLines>
                </div>
            )
        } else if (this.state.loadingState === 'waiting') {
            return (
                <div key='waiting' style={{width: '100%'}}>
                    <FrameLines style={{width: '100%'}}>
                        <Animator animator={{
                            activate: this.state.activate,
                            manager: 'stagger',
                            duration: {stagger: 300}
                        }}>
                            <Text>Bitte warten. Erstelle NPC. Das Bild wird in einigen Minuten nachgeladen.</Text><br/>
                            <Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text>
                            <Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text>
                        </Animator>
                    </FrameLines>
                </div>
            )
        }

    }
}

export default Prompt;
