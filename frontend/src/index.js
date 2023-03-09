import React, {FC, useState} from 'react';
import ReactDOM from 'react-dom';
import {AnimatorGeneralProvider} from '@arwes/animation';
import {ArwesThemeProvider, StylesBaseline} from '@arwes/core';
import './index.css';
import NPCCard from "./components/npc_card";
import axios from 'axios';
import NPCDetails from "./components/npc_details";
import NPCPrivate from "./components/npc_private";
import Prompt from "./components/prompt";
import NPCComplete from "./components/npc_complete";

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

        const path = window.location.pathname.split('/')
        const npc_id = path[path.length - 1]
        console.log(npc_id)
        const npc = {id: npc_id, image_url: 'images/loading.png', attributes: {'Name': 'LOADING'}}
        this.state = { npc: npc };
        this.changeNpc = this.changeNpc.bind(this)
    }

    componentDidMount() {
        let npc = {};
        let self = this;
        axios.get('http://localhost:5000/npc/' + this.state.npc.id)
          .then(function (response) {
              npc = response.data
          })
          .catch(function (error) {
              npc = {id: 'ERROR', image_url: 'images/npc_load_error.png', attributes: {'Name': 'ERROR'}}
          })
          .finally(function () {
            self.changeNpc(npc)
          });
    }

    changeNpc(npc) {
        window.history.replaceState(null, "SINner: " + npc.name, "/npc/" + npc.id)
        this.setState({npc: npc})
    }

    render() {
        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>
                <Prompt changeNpc={this.changeNpc}/>

                <NPCComplete npc={this.state.npc}/>
            </div>
        )
    }
}



// Assuming there is a HTML element with id "root".
ReactDOM.render(<Root/>, document.querySelector('#root'));
//CreationPriorityList.render(document.querySelector('#root'))