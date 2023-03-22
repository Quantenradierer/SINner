import React from 'react';
import ReactDOM from 'react-dom';
import {AnimatorGeneralProvider} from '@arwes/animation';
import {ArwesThemeProvider, StylesBaseline} from '@arwes/core';
import './index.css';
import Prompt from "./components/prompt";
import NPCComplete from "./components/npc_complete";
import Footer from "./components/footer";
import api from "./axios";
import ReloadButton from "./components/reload_button";

// For the font-family to work, you would have to setup the Google Fonts link:
// <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300;400;600&display=swap" />
const ROOT_FONT_FAMILY = '"Titillium Web", sans-serif';

const generalAnimator = {duration: {enter: 300, exit: 300}};


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
        const npc = {id: npc_id || 0, image_url: 'images/loading.png', attributes: {'Name': 'LOADING'}}
        this.state = {npc: npc, loadNpc: null};
        this.changeNpc = this.changeNpc.bind(this)
        this.interval = null;

        this.loadNpc = this.loadNpc.bind(this)
    }

    componentDidMount() {
        this.loadNpc(this.state.npc.id)

        this.interval = setInterval(this.checkImageUpdate, 3 * 60 * 1000);
    }

    componentWillUnmount() {
        clearInterval(this.interval)
    }

     componentDidUpdate(prevProps) {
         if (this.state.loadNpc) {
             this.setState((prevState) => {
                 return {
                     npc: prevState.loadNpc,
                     loadNpc: null
                 }
             })
         }
     }

    checkImageUpdate() {
        if (this.state.npc.image_url == null) {
            this.loadNpc(this.state.npc.id)
        }
    }

    loadNpc(id) {
        let self = this;

        let npc = {};
        api.get('/api/npc_creator/npc/' + id)
            .then(function (response) {
                npc = response.data
            })
            .catch(function (error) {
                npc = {id: id, image_url: 'npc_load_error.png', attributes: {'Name': 'ERROR'}}
            })
            .finally(function () {
                    self.changeNpc(npc)
                }
            );
    }


    changeNpc(npc) {
        if (npc !== this.state.npc) {
            const url = "/npc/" + npc.id
            //window.history.replaceState(null, '', url)
            window.history.pushState({}, "", url)
            this.setState({npc: null, loadNpc: npc})
        }
    }

    render() {
        if (this.state.npc == null) {
            return (
                <div style={{display: 'flex', flexDirection: 'column'}}>
                    <Prompt changeNpc={this.changeNpc}/>
                    <div style={{margin: 15}}></div>
                    <ReloadButton changeNpc={this.changeNpc} npc={this.state.npc}/>
                    <Footer/>
                </div>
            )
        } else {
            //return (<div></div>)
            return (
                <div style={{display: 'flex', flexDirection: 'column'}}>
                    <Prompt changeNpc={this.changeNpc}/>
                    <div style={{margin: 15}}></div>
                    <ReloadButton changeNpc={this.changeNpc} npc={this.state.npc}/>
                    <NPCComplete npc={this.state.npc}/>

                    <Footer/>
                </div>
            )
        }
    }
}

ReactDOM.render(<Root/>, document.querySelector('#root'));
//CreationPriorityList.render(document.querySelector('#root'))