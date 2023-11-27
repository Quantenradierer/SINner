import React, { useState, useEffect } from "react";

import i18next from "../../i18n";
import Warning from "../warning";
import CustomCard from "./card";
import {useLoaderData} from "react-router";
import {Text} from "@arwes/core";
import EntityLoader from "../../loader/entity_loader";


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

  useEffect(() => {
    const fetchData = async () => {
      let newEntity = await new EntityLoader('customs').entity({'params': {'id': entity.id}, undefined})

      if (newEntity.image_objects.length > 0) {
        clearInterval(interval);
        setEntity(newEntity);
      }
    };

    if (entity.image_objects.length == 0) {
        fetchData();
    }
    // Timer setzen für regelmäßige Aktualisierungen
    const interval = setInterval(fetchData, 5000); // Alle 5 Sekunden abfragen

    // Aufräumen wenn die Komponente unmountet
    return () => clearInterval(interval);

  }, []); // Nur beim initialen Rendering ausführen


  return <CustomCompleteWrapper entity={entity} {...props} />
}

export default CustomComplete;
