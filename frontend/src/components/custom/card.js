import React from "react";
import i18next from "../../i18n";
import Warning from "../warning";
import {Button, FramePentagon, Text} from "@arwes/core";
import EditableText from "../editable_text";
import CustomComplete from "./complete";
import image_path from "../../image_path";
import { Link } from "react-router-dom";



function CustomCard(props) {
    let items = []
    for (let image of props.entity?.image_objects || []) {
        items.push(
            <Link to={image_path('customs', image.name)}>
                <img style={{width: '24%'}} src={image_path('customs', image.name, true)}/>
            </Link>
        )
    }

    function RepeatImage(entity) {
        window.location.href = '/customs_prompt/?parameter=' + entity.values['Parameter'] + '&aussehen=' + entity.values['Aussehen']
    }

    return (
        <div style={{margin: 15}}>
            <FramePentagon style={{width: '100%'}}>
                <Text>{props.entity.values['Aussehen']}</Text>
                <Text>{props.entity.values['Parameter']}</Text>
                <div style={{margin: 15, width: '100%'}}>
                    {items}
                </div>
                <Button onClick={() => RepeatImage(props.entity)}>{i18next.t('Wiederholen')}</Button>
            </FramePentagon>
        </div>
    )
}







export default CustomCard;
