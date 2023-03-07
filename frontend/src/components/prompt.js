import React from "react";
import {Blockquote, Button, Card, FrameCorners, FrameLines, LoadingBars, Text} from "@arwes/core";
import {FramePentagon, Figure, List} from '@arwes/core';
import axios from "axios";
import Npc from "../models/npc";
import {Animator} from "@arwes/animation";

const EXAMPLES = [
    'Der NPC arbeitet als Techniker und ist spezialisiert auf Cyberware',
    'Der NPC ist ein einfacher Ladenbesitzer und betreibt einen Waffenladen in der Stadt',
    'Der NPC ist ein beliebter Clubbesitzer',
    'Der NPC ist ein Buchhalter und arbeitet für einen der großen Konzerne',
    'Der NPC ist ein Straßendoc',
    'Der NPC ist ein Büroangestellter',
    'Der NPC ist ein Magietheoretiker',
    'Der NPC will mal ein Runner werden',
    'Der NPC ist ein erfolgloser Restaurantbesitzer',
    'Der NPC ist ein Schmuggler auf einem Fahrrad',
    'Der NPC ist ein Verkäufer von illegalen Drogen',
    'Der NPC ist ein Gangmitglied und bietet Schutz vor anderen Gangs in der Stadt',
    'Der NPC ist ein Straßenmusiker',
    'Der NPC ist ein Reporter',
    'Der NPC ist ein Barkeeper',
    'Der NPC ist ein Ökoterrorist',
    'Der NPC ist ein Büroangestellter der gerne ein Ökoterrorist wäre',
    'Der NPC ist eine künstliche Intelligenz',
    'Der NPC ist Friedhofswärter',
    'Der NPC kommt aus Hamburg',
    'Der NPC kommt aus der Sonderverwaltungszone SOX',
    'Der NPC hat irgendwas mit Keksen zu tun',
    'Der NPC ist magisch begabt',
    'Der NPC ist ein anarchist',
    'Der NPC ist ein Politiker',
    'Der NPC ist ein Mafia-Mitglied',
    'Der NPC ist ein ausgebrannter Magier',
    'Der NPC ist stark vercybert'
]

function random_prompt() {
    return EXAMPLES[Math.floor(Math.random()*EXAMPLES.length)];
}

class Prompt extends React.Component {

    constructor(props) {
        super(props)

        this.state = {prompt: random_prompt(), loadingState: 'prompt', activate: true}

        this.handleChange = this.handleChange.bind(this)
        this.handleClick = this.handleClick.bind(this)
    }

    handleChange(event) {
      this.setState({prompt: event.target.value});
    }

    handleClick() {
        let self = this;
        self.setState({loadingState: 'waiting'})

        axios.post('http://localhost:5000/npc', {prompt: this.state.prompt})
            .then(function (response) {
                self.props.changeNpc(response.data)
            })
            .catch(function (error) {
            })
            .finally(function () {
                self.setState({loadingState: 'prompt'})
            });
    }

    render() {

        if (this.state.loadingState == 'prompt') {
            return (
                <FrameLines style={{width: 950, margin: 15}}>
                    <form>
                        <Text> Erstelle einen NPC und beschreibe seine Ausrichtung. Gib keine persönlichen Informationen
                               von dir an, da diese öffentlich zugänglich sein werden!</Text>
                        <div style={{display: 'flex', flexDirection: 'row'}}>
                            <input value={this.state.prompt} onChange={this.handleChange} maxLength="255" type="text"
                                   id="prompt"/>
                            <Button FrameComponent={FrameCorners} onClick={this.handleClick}>
                                <Text>Erstellen</Text>
                            </Button>
                        </div>
                    </form>
                </FrameLines>
            )
        }
        else if (this.state.loadingState == 'waiting') {
            return (
                <div>
                    <FrameLines style={{width: 950, margin: 15}}>
                        <Animator animator={{
                            activate: this.state.activate,
                            manager: 'stagger',
                            duration: { stagger: 210 }
                        }}>
                            <Text>Bitte warten. Erstelle NPC. Die Bildgenerierung ist aktuell noch deaktiviert.</Text><br/>
                            <Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text>
                            <Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text>
                        </Animator>
                    </FrameLines>
                </div>
            )
        }

    }
}

export default Prompt;
