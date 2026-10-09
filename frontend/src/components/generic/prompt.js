import React, {useState} from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, List, Text} from "@arwes/core";
import api from "../../axios";
import i18next from "../../i18n";
import {useNavigate, useNavigation} from "react-router-dom";
import LoadingBar from "../loading_bar";
import {TabsHeader} from "../cyberpunk/tabsHeader";
import {Helmet} from "react-helmet";
import i18n from "../../i18n";


function pick(examples, n) {
    return [...examples].sort(() => Math.random() - 0.5).slice(0, n)
}

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
            prompt: '',
            chips: pick(props.examples, 4)
        }

        this.handleGenerate = this.handleGenerate.bind(this)
        this.handleChange = this.handleChange.bind(this)
        this.handleShuffle = () => this.setState({prompt: random_prompt(props.examples), chips: pick(props.examples, 4)})
        this.handleKeyDown = (e) => {
            if (e.key === 'Enter' && !e.shiftKey) this.handleGenerate(e)
        }
    }


    handleGenerate = async (event) => {
        event.preventDefault();
        const self = this;
        this.setState({loadingState: 'waiting'});
        const prompt = this.state.prompt

        const response = await api.post(`/api/npc_creator/entities/prompt/`, {kind: this.props.entityType, prompt: prompt, language: i18next.language}, {timeout: 180000})
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

        let disabled = this.state.loadingState === 'waiting'

        const chips = this.state.chips
        const empty = this.state.prompt.trim() === ''

        return (<div style={{width: '100%', maxWidth: 900, margin: '0 auto'}}>
            <Helmet>
                <title>{i18n.t(`page_prompt_title`)}</title>
            </Helmet>
            <FrameLines style={{width: '100%'}}>
                <div style={{padding: '10px 20px'}}>
                    <Text style={{display: 'block', opacity: 0.75, marginBottom: 18, lineHeight: 1.5}}>{translation}</Text>
                    <form onSubmit={this.handleGenerate}>
                        <textarea value={this.state.prompt} onChange={this.handleChange}
                                  onKeyDown={this.handleKeyDown}
                                  maxLength="255" rows={3} id="prompt" disabled={disabled}
                                  style={{
                                      width: '100%', boxSizing: 'border-box', resize: 'none', padding: 12,
                                      fontSize: '1.1em', lineHeight: 1.4, fontFamily: 'inherit',
                                      background: 'rgba(0,0,0,0.35)', color: 'inherit',
                                      border: '1px solid rgba(2,238,238,0.35)', outline: 'none'
                                  }}/>
                        <div style={{textAlign: 'right', opacity: 0.5, fontSize: '0.8em', marginTop: 4}}>
                            {this.state.prompt.length}/255
                        </div>
                    </form>

                    <div style={{display: 'flex', flexWrap: 'wrap', gap: 8, alignItems: 'center', margin: '8px 0 20px'}}>
                        <span style={{opacity: 0.6, fontSize: '0.85em'}}>{i18n.t('prompt_examples')}</span>
                        {chips.map(c => <button key={c} type="button" disabled={disabled}
                                                onClick={() => this.setState({prompt: c})}
                                                style={{
                                                    cursor: 'pointer', color: 'inherit', fontFamily: 'inherit',
                                                    background: 'transparent', padding: '4px 10px', fontSize: '0.85em',
                                                    border: '1px solid rgba(2,238,238,0.3)', borderRadius: 999
                                                }}>{c}</button>)}
                        <button type="button" disabled={disabled} onClick={this.handleShuffle}
                                style={{
                                    cursor: 'pointer', color: 'inherit', fontFamily: 'inherit',
                                    background: 'transparent', padding: '4px 10px', fontSize: '0.85em',
                                    border: '1px dashed rgba(2,238,238,0.5)', borderRadius: 999
                                }}>🎲 {i18n.t('prompt_random')}</button>
                    </div>

                    <div style={{display: 'flex', justifyContent: 'center'}}>
                        <Button FrameComponent={FramePentagon} style={{width: 260}}
                                onClick={this.handleGenerate}
                                disabled={disabled || empty}>
                            <Text>{i18next.t("prompt_generate")}</Text>
                        </Button>
                    </div>
                </div>
            </FrameLines>
            {errorDialog && <div style={{margin: '15px 0'}}>{errorDialog}</div>}
            {disabled && <div style={{margin: '15px 0'}}>
                <LoadingBar estimated_time={8000} steps={50} title={i18n.t("prompt_wait")}/>
            </div>}
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
        },
        'floorplans': {
            url: `/floorplans/create`,
            name: i18next.t('tab_header_floorplans_create'),
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
