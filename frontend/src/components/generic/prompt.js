import React, {useState} from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, List, Text} from "@arwes/core";
import api from "../../axios";
import i18next from "../../i18n";
import {useNavigate, useNavigation} from "react-router-dom";
import LoadingBar from "../loading_bar";
import {TabsHeader} from "../cyberpunk/tabsHeader";
import {Helmet} from "react-helmet";
import i18n from "../../i18n";


function random_prompt(examples) {
    return examples[Math.floor(Math.random() * examples.length)];
}

class PromptWrapped extends React.Component {



    constructor(props) {
        super(props)
        let url = new URL(window.location.href)
        const params = new URLSearchParams(url.search)

        this.state = {
            loadingState: 'prompt',
            error: null,
            prompt: random_prompt(props.examples)
        }

        this.handleGenerate = this.handleGenerate.bind(this)
        this.handleChange = this.handleChange.bind(this)
    }


    handleGenerate = async (event) => {
        event.preventDefault();
        const self = this;
        this.setState({loadingState: 'waiting'});
        const prompt = this.state.prompt

        const response = await api.post(`/api/npc_creator/entities/prompt/`, {kind: this.props.entityType, prompt: prompt}, {timeout: 180000})
        if (response.status === 200) {
            if (response.data.type === 'success') {
                window.location.href = `/${self.props.entityType}s/${response.data.entity.id}`
            } else {
                this.setState({'error': i18next.t(response.data.error)});
            }
            this.setState({loadingState: 'prompt'})
        } else {
            this.setState({'error': i18next.t('prompt_failed_connection')})
            this.setState({loadingState: 'prompt'})
        }
    }

    handleChange(event) {
        event.preventDefault()
        this.setState({prompt: event.target.value})
    }

    render() {
        let translation = i18next.t(`create_explanation_${this.props.entityType}`);
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

        let loadingBar = <div/>
        if (this.state.loadingState === 'waiting') {
            loadingBar = <div key='waiting' style={{width: '100%'}}>
                <LoadingBar/>
            </div>
        }

        let disabled = this.state.loadingState === 'waiting'

        return (<div style={{width: '100%'}}>
            <Helmet>
                <title>{i18n.t(`page_prompt_title`)}</title>
            </Helmet>
            <div style={{flex: 1}}>
                <FrameLines style={{width: '100%'}}>
                    <Text>{translation}</Text>
                    <form onSubmit={this.handleGenerate}>
                        <div style={{display: 'flex', flexDirection: 'row'}}>
                            <input value={this.state.prompt} onChange={this.handleChange} maxLength="255"
                                   type="text"
                                   id="prompt"
                                   disabled={disabled}/>
                        </div>
                    </form>

                    <div style={{
                        display: 'flex',
                        alignItems: 'right',
                        justifyContent: 'right',
                        margin: '10px 0px 0px 0px'
                    }}>
                        <Button FrameComponent={FramePentagon} style={{margin: 3, width: 150}}
                                onClick={this.handleGenerate}
                                disabled={disabled}>
                            <Text>Generieren</Text>
                        </Button>
                    </div>
                </FrameLines>
            </div>
            <div style={{margin: 15}}>
                {errorDialog}
            </div>
            <div style={{margin: '15px 0px 15px 0px'}}>
                {disabled && <LoadingBar/>}
            </div>
        </div>)
    }
}


const Prompt = props => {
    const navigate = useNavigate()
    const {state} = useNavigation()

  const tabs = {
        'npcs': {
            url: `/npcs/create`,
            name: i18next.t('tab_header_npc_create'),
            element: <></>
        },
        'locations': {
            url: `/locations/create`,
            name: i18next.t('tab_header_locations_create'),
            element: <></>
        }
    };


    if (state === 'loading') {
        return <LoadingBars></LoadingBars>
    } else {
        return <div style={{width: '100%', position: 'relative'}}>
            <TabsHeader tabs={tabs}/>
            <PromptWrapped {...props} />
        </div>
    }
}

export default Prompt;
