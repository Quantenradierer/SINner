import React from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, LoadingBars, Text} from "@arwes/core";
import {Animator} from "@arwes/animation";
import api from "../axios";
import i18next from "../i18n";
import {useLoaderData} from "react-router";
import {useNavigate, useNavigation} from "react-router-dom";
import LocationCard from "./location/location_card";

const EXAMPLES = [
    'Erstelle eine Bar'
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

        api.post('/api/npc_creator/locations/prompt/', {prompt: this.state.prompt, values: this.state.entity.primary_values}, {timeout: 240000} )
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

        api.post('/api/npc_creator/locations/save/', {values: this.state.entity.primary_values})
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
                <FrameLines style={{width: '100%'}}>
                    <ul style={{margin: 0}}>
                        <li className='fine-li'><Text>Beschreibe den Ort</Text></li>
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
                    <Text>Ort speichern und Bild generieren</Text>
                </Button>
            </div>
            <div>
                <LocationCard entity={this.state.entity} editable={true} editableDisabled={disabled} check={this.state.check}/>
            </div>


        </div>)
    }
}




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
