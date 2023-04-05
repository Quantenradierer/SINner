import React from "react";
import NPCCard from "./npc_card";
import NPCPrivate from "./npc_private";
import NPCSkills from "./npc_skills";
import api from "../axios";
import {useLoaderData} from "react-router";


class NPCCompleteWrapped extends React.Component {

    constructor(props) {
        super(props);

        //const npc = {id: this.props.id || 0, attributes: {'Name': 'LOADING'}}
        //this.state = {npc: npc};

        this.interval = null;

    }

    render() {
        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>

                <NPCCard npc={this.props.npc}/>
                <NPCPrivate npc={this.props.npc} />
                <NPCSkills npc={this.props.npc} />
            </div>
        )

    }
}


const NPCComplete = props => {
  const npc = useLoaderData()

  return <NPCCompleteWrapped npc={npc} {...props} />
}

export default NPCComplete;
