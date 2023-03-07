import React, {FC, useState} from 'react';
import ReactDOM from 'react-dom';
import {AnimatorGeneralProvider} from '@arwes/animation';
import {ArwesThemeProvider, StylesBaseline} from '@arwes/core';
import './index.css';
import NPCCard from "./components/npc_card";
import Npc from "./models/npc";
import axios from 'axios';
import NPCDetails from "./components/npc_details";
import NPCPrivate from "./components/npc_private";
import Prompt from "./components/prompt";

// For the font-family to work, you would have to setup the Google Fonts link:
// <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300;400;600&display=swap" />
const ROOT_FONT_FAMILY = '"Titillium Web", sans-serif';

const generalAnimator = {duration: {enter: 500, exit: 500}};


class Root extends React.Component {
    render() {
        return (
            <ArwesThemeProvider>
                <StylesBaseline styles={{
                    body: {fontFamily: ROOT_FONT_FAMILY},
                    'ul li::marker': {
                        content: '""'
                    }
                }}/>
                <AnimatorGeneralProvider animator={generalAnimator}>
                    <div style={{justifyContent: 'center', display: 'flex', margin: 15}}>
                        <Content/>
                    </div>

                </AnimatorGeneralProvider>
            </ArwesThemeProvider>
        )
    }
}

class Content extends React.Component {
    constructor(props) {
        super(props);
        const npc = new Npc('LOADING ...', 'LOADING ... ', './images/loading.png', '', {'Please stand by': '...'})
        this.state = { npc: npc, showDetails: false, showPrivate: false };
        this.toggleDetails = this.toggleDetails.bind(this)
        this.togglePrivate = this.togglePrivate.bind(this)
        this.changeNpc = this.changeNpc.bind(this)
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

    changeNpc(npc) {
        console.log(npc)
        this.setState({npc: npc})
    }

    toggleDetails() {
        this.setState((state, props) => {
            return {showDetails: !state.showDetails}
        });
    }

    togglePrivate() {
        this.setState((state, props) => {
            return {showPrivate: !state.showPrivate}
        });
    }

    render() {
        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>
                <Prompt changeNpc={this.changeNpc}/>

                <NPCCard npc={this.state.npc} toggleDetails={this.toggleDetails} togglePrivate={this.togglePrivate}/>
                <NPCDetails npc={this.state.npc} show={this.state.showDetails}/>
                <NPCPrivate npc={this.state.npc} show={this.state.showPrivate}/>
            </div>
        )
    }
}



// Assuming there is a HTML element with id "root".
ReactDOM.render(<Root/>, document.querySelector('#root'));
//CreationPriorityList.render(document.querySelector('#root'))