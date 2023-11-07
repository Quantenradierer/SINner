import {Button, FrameLines, List, Text} from "@arwes/core";
import React from "react";
import EditableText from "./editable_text";
import i18next from "../i18n";


const AttributeList = props => {
    const items = [];

    for (const attribute of props.attributes) {
        items.push(
            <li key={attribute} style={{padding: '7px 0 0 0', alignItems: 'top', display: 'flex'}}>
                <div>
                    <div style={{width: props.listItemWidth}}><Text><b>{i18next.t('attribute_' + attribute.replaceAll(' ', '_').toLowerCase())}:</b></Text></div>
                </div>
                <EditableText style={{margin: '-7px 0 0 0'}}
                              attribute={attribute}
                              npc={props.npc}
                              approxLineSize={props.approxLineSize}
                              editable={props.editable}
                              editableDisabled={props.editableDisabled}
                              check={props.check}
                              setAlternatives={props.setAlternatives}
                />



            </li>
        );
        items.push(<hr key={'hr' + items.length} style={{margin: '2px 0px 0px 2px'}}/>)
    }
    items.pop()

    return (<List>
        {items}
    </List>)
}

export default AttributeList