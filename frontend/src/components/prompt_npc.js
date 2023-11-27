import React from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, LoadingBars, Text} from "@arwes/core";
import {Animator} from "@arwes/animation";
import api from "../axios";
import i18next from "../i18n";
import NPCComplete from "./npc/npc_complete";
import NPCCard from "./npc/npc_card";
import NPCPrivate from "./npc/npc_private";
import NPCSkills from "./npc/npc_skills";
import {useLoaderData} from "react-router";
import {useNavigate, useNavigation} from "react-router-dom";

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

class PromptWrapped extends React.Component {
    constructor(props) {
        super(props)
        let url = new URL(window.location.href)
        const params = new URLSearchParams(url.search)
        let show = true

        let entity = props.entity
        entity["image_objects"] = [{id: 0, score: 0, name: 'creation_form.png'}]
        this.state = {
            show: show,
            prompt: random_prompt(),
            loadingState: 'prompt',
            activate: true,
            error: null,
            entity: entity,
            check: false
        }

        this.handleChange = this.handleChange.bind(this)
        this.handleClick = this.handleClick.bind(this)
        this.handleSave = this.handleSave.bind(this)
    }

    handleChange(event) {
        this.setState({prompt: event.target.value});
    }

    handleClick(event) {
        event.preventDefault();
        let self = this;
        self.setState({loadingState: 'waiting'});

        api.post('/api/npc_creator/npcs/prompt/', {prompt: this.state.prompt, values: this.state.entity.primary_values}, {timeout: 240000} )
            .then(function (response) {
                if (response.data.type === 'success') {
                    response.data.entity.image_objects = [{id: 0, score: 0, name: 'creation_form.png'}]
                    self.setState({ 'entity': response.data.entity })
                } else {
                    self.setState({ 'error': i18next.t(response.data.error) });
                    setTimeout(function(){
                        self.setState({'error': null })
                    },15000);
                }
            })
            .catch(function (error) {
                self.setState({ 'error': i18next.t('prompt_failed_connection') })
                setTimeout(function(){
                    self.setState({'error': null })
                },15000);
            })
            .finally(function () {
                self.setState({loadingState: 'prompt'})
            });
    }

    handleSave(event) {
        event.preventDefault()
        let self = this;
        self.setState({loadingState: 'waiting'})

        api.post('/api/npc_creator/npcs/save/', {values: this.state.entity.primary_values})
            .then(function (response) {
                if (response.data.type === 'success') {
                    window.location.href = '/npcs/' + response.data.entity.id
                } else {
                    if (response.data.error === 'custom') {
                        self.setState({'error': 'GPT: ' + response.data.message})
                    } else {
                        self.setState({'error': i18next.t(response.data.error),
                                            'check': true})
                    }
                    window.scrollTo(0, 0)

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
                    <ul style={{margin: 0}}>
                        <li className='fine-li'><Text>Beschreibe deinen NPC</Text></li>
                        <li className='fine-li'><Text>Klick auf "Ausfüllen" um die Werte von GPT ausfüllen zu lassen</Text></li>
                        <li className='fine-li'><Text>Kontrolliere und Korrigiere die Werte</Text></li>
                        <li className='fine-li'><Text>Speicher und lass ein Bild erzeugen</Text></li>
                    </ul>
                    <form onSubmit={this.handleClick}>
                        <div style={{display: 'flex', flexDirection: 'row'}}>
                            <input value={this.state.prompt} onChange={this.handleChange} maxLength="255"
                                   type="text"
                                   id="prompt"/>
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
                        <Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text>
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
            <div style={{display: 'flex', alignItems: 'right', justifyContent: 'right', margin: 15}}>
                <Button style={{margin: '3px 3px 3px 13px'}} FrameComponent={FramePentagon} onClick={this.handleClick} disabled={this.state.loadingState === 'waiting'}>
                    <Text>Ausfüllen</Text>
                </Button>
                <Button FrameComponent={FramePentagon} style={{margin: 3}} onClick={this.handleSave} disabled={this.state.loadingState === 'waiting'}>
                    <Text>NPC speichern und Bild generieren</Text>
                </Button>
            </div>
            <div>
                <NPCCard entity={this.state.entity} editable={true} editableDisabled={disabled} check={this.state.check}/>
                <NPCPrivate entity={this.state.entity} editable={true} editableDisabled={disabled} check={this.state.check}/>
                <NPCSkills entity={this.state.entity} editable={true} editableDisabled={disabled} check={this.state.check}/>
            </div>


        </div>)
    }
}




const Prompt_npc = props => {
  const default_entity = useLoaderData()
  const navigate = useNavigate()
  const { state } = useNavigation()

  if (state === 'loading') {
      return <LoadingBars></LoadingBars>
  } else {
      return <PromptWrapped entity={default_entity} {...props} />
  }
}

export default Prompt_npc;