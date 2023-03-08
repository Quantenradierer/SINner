import React from "react";
import {Button, FrameCorners, FrameLines, Text} from "@arwes/core";
import axios from "axios";
import {Animator} from "@arwes/animation";

const EXAMPLES = [
    'Erstelle einen Ladenbesitzer',
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
    'Erstelle einen Friedhofswärter',
    'Erstelle einen NPC aus Hamburg',
    'Erstelle einen ausgebrannten Magier',
    'Erstelle einen Anarchisten',
    'Erstelle einen Verschwörungstheoretiker',
    'Erstelle einen korrupten Polizisten',
    'Erstelle einen korrupten Politiker',
    'Erstelle einen NPC mit viel Cyberware',
    'Erstelle ein Vorstandsmitglied eines großen Konzerns',
    'Erstelle einen NPC mit Bezug auf die ADL, Allianz Deutscher Länder',
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
                let npc = {id: 'ERROR', image_url: 'images/npc_load_error.png', attributes: {'Name': 'ERROR'}}
                self.props.changeNpc(npc)
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
