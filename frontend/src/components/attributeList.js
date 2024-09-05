import {Button, FrameLines, List, Text} from "@arwes/core";
import React from "react";
import EditableText from "./editableText";
import i18next from "../i18n";
import './dividerAttributeList.css'
import Divider from "./cyberpunk/divider";


const AttributeList = ({ attributes, firstColumnSize }) => {
    const items = [];

    for (const attribute of attributes) {
        items.push(
            <div key={'div' + attribute} style={{width: '100%', display: 'flex'}}>
                <b style={{display: 'flex', alignItems: 'center', width: firstColumnSize}}><Text>{i18next.t('attribute_' + attribute.replaceAll(' ', '_').replaceAll('/', '_').toLowerCase())}:&nbsp;</Text></b>
                <EditableText attributeName={attribute}/>
            </div>
        );
        items.push(<div key={'divider' + attribute} style={{margin: '7px 0 7px 0', padding: 0}}><Divider></Divider></div>)
    }

    return (<div style={{width: '100%', padding: '0px 10px 0px 10px'}}>
        {items}
    </div>)
}

export default AttributeList