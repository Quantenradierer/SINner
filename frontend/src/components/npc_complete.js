import React from "react";
import {Blockquote, Button, Card, Text} from "@arwes/core";
import {FramePentagon, Figure, List} from '@arwes/core';
import NPCCard from "./npc_card";
import NPCDetails from "./npc_details";
import NPCPrivate from "./npc_private";

class NPCComplete extends React.Component {

   constructor(props) {
        super(props);
        this.state = { showDetails: true, showPrivate: true };
        this.toggleDetails = this.toggleDetails.bind(this)
        this.togglePrivate = this.togglePrivate.bind(this)
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
            <div style={{
                display: 'contents',
                alignContent: 'center'
            }}>
                <NPCCard npc={this.props.npc} toggleDetails={this.toggleDetails} togglePrivate={this.togglePrivate}/>
                <NPCDetails npc={this.props.npc} show={this.state.showDetails}/>
                <NPCPrivate npc={this.props.npc} show={this.state.showPrivate}/>
            </div>
        )

    }
}

export default NPCComplete;
