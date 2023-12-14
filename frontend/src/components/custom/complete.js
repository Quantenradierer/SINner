import React, { useState, useEffect } from "react";

import i18next from "../../i18n";
import Warning from "../warning";
import CustomCard from "./card";
import {useLoaderData} from "react-router";
import {Text} from "@arwes/core";
import EntityLoader from "../../loader/entity_loader";
import useRefreshEntityCard from "../use_refresh_entity_card";


const  CustomCompleteWrapper = props => {
    let warning = ''
    if (props.entity.image_objects.length == 0) {
        warning = <Warning text={i18next.t('image_generation_in_progress')}/>
    }

    return (
        <div>
            {warning}
            <CustomCard entity={props.entity} key={props.entity.id}/>
        </div>
    )

}


const CustomComplete = props => {
  const loaded_entity = useLoaderData()
  const [entity, setEntity] = useState(loaded_entity);
  useRefreshEntityCard('customs', entity, setEntity)

  return <CustomCompleteWrapper entity={entity} {...props} />
}

export default CustomComplete;
