import React from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, List, LoadingBars, Text} from "@arwes/core";
import api from "../../axios";
import i18next from "../../i18n";
import {useLoaderData} from "react-router";
import {useNavigate, useNavigation} from "react-router-dom";
import PromptInput from "../prompt_input";
import LoadingBar from "../loading_bar";

function random_prompt(examples) {
    return examples[Math.floor(Math.random() * examples.length)];
}




class PromptWrapped extends React.Component {
    constructor(props) {
        super(props)
        let url = new URL(window.location.href)
        const params = new URLSearchParams(url.search)
        let show = true

        let entity = props.entity
        entity["image_objects"] = [{id: 0, score: 0, name: 'creation_form'}]
        this.state = {
            show: show,
            loadingState: 'prompt',
            error: null,
            entity: this.props.entity,
            check: this.props.check,
            prompt: random_prompt(this.props.examples)
        }

        this.handleFill = this.handleFill.bind(this)
        this.handleSave = this.handleSave.bind(this)
    }



    handleFill(prompt) {
        let self = this;
        self.setState({loadingState: 'waiting', prompt: prompt});
        self.props.setEditable(false)

        api.post(`/api/npc_creator/${this.props.entityType}s/prompt/`, {prompt: prompt, values: this.state.entity.values}, {timeout: 240000} )
            .then(function (response) {
                if (response.data.type === 'success') {
                    response.data.entity.image_objects = [{id: 0, score: 0, name: 'creation_form'}]

                    self.setState({ entity: response.data.entity})
                    self.props.setEntity(response.data.entity)
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
                self.props.setEditable(true)
            });
    }

    handleSave(event) {
        event.preventDefault()
        let self = this;
        self.setState({loadingState: 'waiting'})

        api.post(`/api/npc_creator/${this.props.entityType}s/save/`, {values: this.state.entity.values})
            .then(function (response) {
                if (response.data.type === 'success') {
                    window.location.href = `/${self.props.entityType}s/${response.data.entity.id}`
                } else {
                    if (response.data.error === 'custom') {
                        self.setState({'error': 'GPT: ' + response.data.message})
                    } else {
                        self.props.setCheck(true)
                        self.setState({'error': i18next.t(response.data.error)})
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
                <PromptInput entityType={this.props.entityType} prompt={this.state.prompt} handleSave={this.handleSave} handleFill={this.handleFill}></PromptInput>
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
                {this.props.children}
            </div>


        </div>)
    }
} //





const Prompt = props => {
  const navigate = useNavigate()
  const { state } = useNavigation()

  if (state === 'loading') {
      return <LoadingBars></LoadingBars>
  } else {
      return <PromptWrapped {...props} />
  }
}

export default Prompt;
