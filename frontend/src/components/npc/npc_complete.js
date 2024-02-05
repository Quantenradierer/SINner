import React, {useState} from "react";
import NPCCard from "./npc_card";
import NPCPrivate from "./npc_private";
import NPCSkills from "./npc_skills";
import api from "../../axios";
import {useLoaderData} from "react-router";
import {FramePentagon, Text} from "@arwes/core";
import i18next from "../../i18n";
import AlternativeDialog from "../alternative_dialog";
import {random} from "animejs";
import Warning from "../warning";
import useRefreshEntityCard from "../use_refresh_entity_card";


class NPCCompleteWrapped extends React.Component {
    constructor(props) {
        super(props);

        this.interval = null;

    }

    render() {
        let warning = ''
        if (this.props.entity.image_objects.length == 0) {
            warning = <Warning text={i18next.t('image_generation_in_progress')}/>
        }

        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>
                {warning}

                <NPCCard entity={this.props.entity}/>
                <NPCPrivate entity={this.props.entity}/>
                <NPCSkills entity={this.props.entity}/>
            </div>
        )

    }
}


const NPCComplete = props => {
  const loaded_entity = useLoaderData()
  const [entity, setEntity] = useState(loaded_entity);
  useRefreshEntityCard('npcs', entity, setEntity)
  return <NPCCompleteWrapped entity={entity} {...props} />
}

export default NPCComplete;
