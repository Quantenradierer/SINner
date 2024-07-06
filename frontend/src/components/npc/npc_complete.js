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
import { Helmet } from 'react-helmet'
import image_path from "../../image_path";
import active_image from "../../active_image";

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
        let activeImage = active_image(this.props.entity.image_objects) || {}

        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>
                <Helmet>
                  <title>Schattenakte - {this.props.entity.values['Name']}</title>
                  <meta name="description" content={this.props.entity.values['Catchphrase']} />
                  <meta property="og:title" content="Schattenakte - {this.props.entity.values['Name']}" />
                  <meta property="og:description" content={this.props.entity.values['Catchphrase']} />
                  <meta property="og:image" content={image_path('npcs', activeImage.name, true)} />
                </Helmet>

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
