import React from "react";
import NPCCard from "./npc_card";
import NPCPrivate from "./npc_private";
import NPCSkills from "./npc_skills";
import api from "../axios";
import {useLoaderData} from "react-router";
import {FramePentagon, Text} from "@arwes/core";
import i18next from "../i18n";
import AlternativeDialog from "./alternative_dialog";
import {random} from "animejs";


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

        this.state = {attributeAlternative: null}
        this.interval = null;

        this.setAlternatives = this.setAlternatives.bind(this);
    }

    setAlternatives(attribute) {
        this.setState({attributeAlternative: attribute})
    }

    render() {
        let warning = ''
        if (this.props.npc.image_objects.length == 0) {
            warning = <Warning text={i18next.t('image_generation_in_progress')}/>
        }

        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>
                {warning}

                {this.state.attributeAlternative && <AlternativeDialog npc={this.props.npc} attributeAlternative={this.state.attributeAlternative} setAlternatives={this.setAlternatives}/>}
                <NPCCard npc={this.props.npc} setAlternatives={this.setAlternatives}/>
                <NPCPrivate npc={this.props.npc} setAlternatives={this.setAlternatives}/>
                <NPCSkills npc={this.props.npc} setAlternatives={this.setAlternatives}/>
            </div>
        )

    }
}


const NPCComplete = props => {
  const npc = useLoaderData()

  return <NPCCompleteWrapped npc={npc} {...props} />
}

export default NPCComplete;
