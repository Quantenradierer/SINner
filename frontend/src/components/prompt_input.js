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


class PromptInput extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            prompt: this.props.prompt
        }

        this.handleChange = this.handleChange.bind(this)
        this.handleFill = this.handleFill.bind(this)
    }

    handleChange(event) {
        event.preventDefault();
        this.setState({prompt: event.target.value});
    }

    handleFill(event) {
        event.preventDefault();
        this.props.handleFill(this.state.prompt)
    }

    render() {
        let translation = i18next.t(`create_explanation_${this.props.entityType}`)
        return <FrameLines style={{width: '100%'}}>
            <ul style={{margin: 0}}>
                <li className='fine-li'><Text>{translation}</Text></li>
                <li className='fine-li'><Text>Klick auf "Ausfüllen" um die Werte von GPT ausfüllen zu lassen</Text></li>
                <li className='fine-li'><Text>Kontrolliere und Korrigiere die Werte</Text></li>
                <li className='fine-li'><Text>Speicher und lass ein Bild erzeugen</Text></li>
            </ul>
            <form onSubmit={this.handleFill}>
                <div style={{display: 'flex', flexDirection: 'row'}}>
                    <input value={this.state.prompt} onChange={this.handleChange} maxLength="255"
                           type="text"
                           id="prompt"/>
                </div>
            </form>

             <div style={{display: 'flex', alignItems: 'right', justifyContent: 'right', margin: '10px 0px 0px 0px'}}>
            <Button style={{margin: '3px 3px 3px 13px'}} FrameComponent={FramePentagon} onClick={this.handleFill}>
                <Text>Ausfüllen</Text>
            </Button>
            <Button FrameComponent={FramePentagon} style={{margin: 3}} onClick={this.props.handleSave}>
                <Text>Speichern und Bild generieren</Text>
            </Button>
        </div>
        </FrameLines>


    }
}


export default PromptInput;
