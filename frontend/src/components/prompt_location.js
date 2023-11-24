import React from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, List, LoadingBars, Text} from "@arwes/core";
import {Animator} from "@arwes/animation";
import api from "../axios";
import i18next from "../i18n";
import {useLoaderData} from "react-router";
import {useNavigate, useNavigation} from "react-router-dom";
import LocationCard from "./location/location_card";
import CommentCard from "./location/comment_card";
import Comment from "./location/comment";
import PromptInput from "./prompt_input";
import LoadingBar from "./loading_bar";
import {random} from "animejs";


const EXAMPLES = [
    'Generiere eine Bar',
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
    'Generiere eine hochsichere Yakuza-Villa',
    'Generiere eine geheime Street-Doc-Klinik',
    'Generiere eine dystopische Nomaden-Wohnsiedlung',
    'Generiere einen glamourösen Elfensalon',
    'Generiere ein Ramen-Laden',
    'Generiere ein Ramen-Restaurant',
    'Generiere eine Cocktailbar',
    'Generiere eine Bierstube',
    'Generiere eine Kneipe',
    'Generiere eine Diskothek',
    'Generiere einen Nachtclub',
    'Generiere eine Rooftop-Bar',
    'Generiere ein Aquarium',
    'Generiere ein Lost Place',
    'Generiere eine Schatten Klinik'

    
]


function random_prompt() {
    return EXAMPLES[Math.floor(Math.random() * EXAMPLES.length)];
}

class PromptLocationWrapped extends React.Component {
    constructor(props) {
        super(props)
        let url = new URL(window.location.href)
        const params = new URLSearchParams(url.search)
        let show = true

        let entity = props.entity
        entity["image_objects"] = [{id: 0, score: 0, name: 'creation_form.png'}]
        this.state = {
            show: show,
            loadingState: 'prompt',
            error: null,
            entity: entity,
            comments: [],
            check: false,
            prompt: random_prompt()
        }

        this.handleFill = this.handleFill.bind(this)
        this.handleSave = this.handleSave.bind(this)
    }



    handleFill(prompt) {
        let self = this;
        self.setState({loadingState: 'waiting', prompt: prompt});
        api.post('/api/npc_creator/locations/prompt/', {prompt: prompt, values: this.state.entity.values}, {timeout: 240000} )
            .then(function (response) {
                if (response.data.type === 'success') {
                    response.data.entity.image_objects = [{id: 0, score: 0, name: 'creation_form.png'}]
                    let comments = response.data.entity.values['Bewertungen']

                    self.setState({ entity: response.data.entity, comments: comments})
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

        console.log({values: this.state.entity.values});
        api.post('/api/npc_creator/locations/save/', {values: this.state.entity.values})
            .then(function (response) {
                if (response.data.type === 'success') {
                    window.location.href = '/locations/' + response.data.entity.id
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
                <PromptInput entityType='Ort' prompt={this.state.prompt} handleSave={this.handleSave} handleFill={this.handleFill}></PromptInput>
            </div>
        } else if (this.state.loadingState === 'waiting') {
            prompt = <div key='waiting' style={{width: '100%'}}>
                <LoadingBar/>
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
            <div key={'cards'}>
                <LocationCard entity={this.state.entity} editable={true} editableDisabled={disabled} check={this.state.check}/>
                 <CommentCard key={'comments' + Math.random()} comments={this.state.comments}/>
            </div>


        </div>)
    }
} //





const PromptLocation = props => {
  const default_entity = useLoaderData()
  const navigate = useNavigate()
  const { state } = useNavigation()

  if (state === 'loading') {
      return <LoadingBars></LoadingBars>
  } else {
      return <PromptLocationWrapped entity={default_entity} {...props} />
  }
}

export default PromptLocation;
