import React from "react";
import i18next from "../../i18n";
import Warning from "../warning";
import {FramePentagon, Text} from "@arwes/core";
import EditableText from "../editable_text";
import CustomComplete from "./complete";
import image_path from "../../image_path";




function CustomCard(props) {
    let items = []
    for (let image of props.entity?.image_objects || []) {
        items.push(
            <a href={image_path('customs', image.name)}>
                <img style={{width: '24%'}} src={image_path('customs', image.name, true)}/>
            </a>
        )
    }

    return (
        <div style={{margin: 15}}>
            <FramePentagon style={{width: '100%'}}>
                <Text>{props.entity.primary_values['Aussehen']}</Text>
                <div style={{margin: 15, width: '100%'}}>
                    {items}
                </div>
            </FramePentagon>
        </div>
    )
}







export default CustomCard;
