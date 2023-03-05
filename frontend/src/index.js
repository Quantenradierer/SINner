import React, {FC, useState} from 'react';
import ReactDOM from 'react-dom';
import {AnimatorGeneralProvider} from '@arwes/animation';
import {BleepsProvider} from '@arwes/sounds';
import {ArwesThemeProvider, StylesBaseline} from '@arwes/core';
import './index.css';
import NPCCard from "./components/npc_card";
import Npc from "./models/npc";
import axios from 'axios';

// For the font-family to work, you would have to setup the Google Fonts link:
// <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300;400;600&display=swap" />
const ROOT_FONT_FAMILY = '"Titillium Web", sans-serif';
const IMAGE_URL = 'https://playground.arwes.dev/assets/images/wallpaper.jpg';
const SOUND_OBJECT_URL = 'https://playground.arwes.dev/assets/sounds/object.mp3';
const SOUND_TYPE_URL = 'https://playground.arwes.dev/assets/sounds/type.mp3';
const audioSettings = {common: {volume: 0.25}};
const playersSettings = {
    object: {src: [SOUND_OBJECT_URL]},
    type: {src: [SOUND_TYPE_URL], loop: true}
};
const bleepsSettings = {
    object: {player: 'object'},
    type: {player: 'type'}
};
const generalAnimator = {duration: {enter: 500, exit: 500}};


class Root extends React.Component {
    render() {
        return (
            <ArwesThemeProvider>
                <StylesBaseline styles={{body: {fontFamily: ROOT_FONT_FAMILY}}}/>
                <BleepsProvider
                    audioSettings={audioSettings}
                    playersSettings={playersSettings}
                    bleepsSettings={bleepsSettings}
                >
                    <AnimatorGeneralProvider animator={generalAnimator}>
                        <div style={{display: 'flex', justifyContent: 'center', margin: 25}}>
                            <Content/>
                        </div>

                    </AnimatorGeneralProvider>
                </BleepsProvider>
            </ArwesThemeProvider>
        )
    }
}

class Content extends React.Component {
    constructor(props) {
        super(props);
        const npc = new Npc('LOADING ...', 'LOADING ... ', './images/loading.png', '', {'Please stand by': '...'})
        this.state = { npc: npc };
    }

    componentDidMount() {
        let npc;
        let self = this;
        axios.get('http://localhost:5000/random_npc')
          .then(function (response) {
              npc = response.data
          })
          .catch(function (error) {
            npc = new Npc('ERROR', 'ERROR', './images/npc_load_error.png', 'Image could not be loaded.',{error: error.message})
          })
          .finally(function () {
            self.setState({npc: npc})
          });


    }

    render() {
        console.log(this.state.npc)
        return (
            <NPCCard npc={this.state.npc}>
            </NPCCard>
        )
    }
}



// Assuming there is a HTML element with id "root".
ReactDOM.render(<Root/>, document.querySelector('#root'));
//CreationPriorityList.render(document.querySelector('#root'))