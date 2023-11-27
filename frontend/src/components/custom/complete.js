import React from "react";
import i18next from "../../i18n";
import Warning from "../warning";
import CustomCard from "./card";
import {useLoaderData} from "react-router";
import {Text} from "@arwes/core";


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
  const entity = useLoaderData()

  return <CustomCompleteWrapper entity={entity} {...props} />
}

export default CustomComplete;
