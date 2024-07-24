import React, {useState} from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, List, Text} from "@arwes/core";
import api from "../../axios";
import i18next from "../../i18n";
import {useNavigate, useNavigation} from "react-router-dom";
import LoadingBar from "../loading_bar";


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


    handleGenerate = async () => {
        const self = this;
        this.setState({loadingState: 'waiting'});
        const prompt = this.state.prompt

        const response = await api.post(`/api/npc_creator/${this.props.entityType}s/prompt/`, {prompt: prompt}, {timeout: 240000})
        console.log(response)
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

        return (<div>
            <div style={{margin: 15}}>
                {errorDialog}
            </div>
            <div style={{margin: 15}}>
                <div key='prompt'>
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
                            <Button FrameComponent={FramePentagon} style={{margin: 3}} onClick={this.handleGenerate}
                                    disabled={disabled}>
                                <Text>Generieren</Text>
                            </Button>
                        </div>
                    </FrameLines>
                </div>
                <div style={{margin: '15px 0px 15px 0px'}}>
                    {disabled && <LoadingBar/>}
                </div>
            </div>
        </div>)
    }
}


const Prompt = props => {
    const navigate = useNavigate()
    const {state} = useNavigation()

    if (state === 'loading') {
        return <LoadingBars></LoadingBars>
    } else {
        return <div style={{maxWidth: 980, width: '100%', position: 'relative'}}>
            <PromptWrapped {...props} />
        </div>
    }
}

export default Prompt;
