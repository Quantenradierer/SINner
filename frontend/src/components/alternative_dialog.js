import React from 'react';
import {Text, FramePentagon} from "@arwes/core";
import api from "../axios";

class AlternativeDialog extends React.Component {
    state = {
        state: 'exit',
        alternatives: []
    }

    componentDidMount() {
        if (this.props.attributeAlternative != null) {
            this.retrieveAlternatives();
        }
    }

    retrieveAlternatives = async () => {
        console.log(this.props.npc.id)

        this.setState({state: 'loading', alternatives: []});

        try {
            const response = await api.post( `/api/npc_creator/npcs/${this.props.npc.id}/alternatives/`, {
                attribute: this.props.attributeAlternative
            }, {timeout: 60000});

            if (response.status === 200) {
                this.setState({
                    state: response.data.type === 'success' ? 'success' : 'loading',
                    alternatives: response.data.alternatives || []
                });
            } else {
                this.setState({state: 'failed', alternatives: []});
            }
        } catch (error) {
            this.setState({state: 'failed', alternatives: []});
        }
    }

    onExit = () => {
        this.props.setAlternatives(null);
    }

    render() {
        if (this.state.state === 'exit') {
            return (<div/>)
        }

        let items = []
        for (let item of this.state.alternatives) {
            items.push(<Text key={'text' + items.length} style={{whiteSpace: 'pre-wrap'}}>{item}</Text>)
            items.push(<hr key={'hr' + items.length} style={{margin: '2px 0px 0px 2px'}}/>)
        }
        items.pop()

        return <div key={this.state.state} style={{position: 'fixed', zIndex: 100, width: '100%', height: '100%', left: 0, top: 0, justifyContent: 'center', display: 'flex', padding: '10 10 10 10', margin: '10 10 10 10', backgroundColor: 'rgba(0,0,0,.75)'}} onClick={this.onExit}>
            <div style={{ minHeight: 270, maxHeight: 600, minWidth: 300, maxWidth: 900, padding: '10 10 10 10', margin: '10 10 10 10'}}>
            <FramePentagon style={{backgroundColor: 'black', top: 100, padding: '10 10 10 10', margin: '10 10 10 10'}}>
                <div style={{overflow: 'auto'}}>
                    {this.state.state === 'loading' && <div>Alternativen werden erzeugt...</div>}
                    {this.state.state === 'failed' && <div><Text>Technische Probleme :(</Text></div>}
                    {this.state.state === 'success' && <div style={{display: 'flex', minHeight: 270, maxHeight: 570, flexDirection: 'column', overflow: 'auto'}}>{items}</div>}
                </div>

            </FramePentagon>
                </div>
        </div>
    }

}

export default AlternativeDialog;