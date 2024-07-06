import {Button, FrameLines, List, Text} from "@arwes/core";
import React from "react";
import EditableText from "./editable_text";
import i18next from "../i18n";


const AttributeList = props => {
    const items = [];

    for (const attribute of props.attributes) {
        items.push(
            <li key={'LI' + attribute} style={{padding: '7px 0 0 0', alignItems: 'top', display: 'flex'}}>
                <div>
                    <div style={{width: props.listItemWidth}}><Text><b>{i18next.t('attribute_' + attribute.replaceAll(' ', '_').replaceAll('/', '_').toLowerCase())}:</b></Text></div>
                </div>
                <EditableText style={{margin: '-7px 0 0 0'}}
                              attribute={attribute}
                              entity={props.entity}
                              approxLineSize={props.approxLineSize}
                              editable={props.editable}
                              editableDisabled={props.editableDisabled}
                              check={props.check}
                />



            </li>
        );
        items.push(<hr key={'hr' + items.length} style={{margin: '2px 0px 0px 2px'}}/>)
    }
    items.pop()

    return (<List style={{width: '100%'}}>
        {items}
    </List>)
}

export default AttributeList