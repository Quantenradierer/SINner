import React from "react";
import NPCCard from "./npc_card";
import NPCPrivate from "./npc_private";
import NPCSkills from "./npc_skills";
import api from "../axios";
import {useLoaderData} from "react-router";
import {FramePentagon, Text} from "@arwes/core";
import i18next from "../i18n";


const Warning = props => {
    return (<div key='error'  style={{width: 950, margin: 15}}>
                <FramePentagon
                    style={{margin: '15px 0px 15px 0px', display: 'flex'}}
                    palette='secondary'
                    lineWidth={1}
                >
                    <Text>{props.text}</Text>
                </FramePentagon>
            </div>)
}

class NPCCompleteWrapped extends React.Component {

    constructor(props) {
        super(props);

        this.interval = null;

    }

    render() {
        let warning = ''
        if (this.props.npc.image_objects.length == 0) {
            warning = <Warning text={i18next.t('image_generation_in_progress')}/>
        }

        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>
                {warning}

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
