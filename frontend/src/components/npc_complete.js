import React from "react";
import NPCCard from "./npc_card";
import NPCPrivate from "./npc_private";
import NPCSkills from "./npc_skills";

class NPCComplete extends React.Component {

    constructor(props) {
        super(props);
        this.state = {showDetails: true, showPrivate: true};
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
                <NPCPrivate npc={this.props.npc} show={this.state.showDetails}/>
                <NPCSkills npc={this.props.npc} show={this.state.showPrivate}/>
            </div>
        )

    }
}

export default NPCComplete;
