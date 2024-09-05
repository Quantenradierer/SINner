import {Button, FrameLines, List, Text} from "@arwes/core";
import React, {useState} from "react";
import EditableText from "./editableText";
import i18next from "../i18n";
import Divider from "./cyberpunk/divider";
import './dividerAttributeList.css'





const DividerAttributeList = ({ attributes }) => {
    const items = [];

    for (const attribute of attributes) {
        items.push(
            <div key={'div' + attribute} style={{width: '100%'}}>
                <Divider title={i18next.t('attribute_' + attribute.replaceAll(' ', '_').replaceAll('/', '_').toLowerCase())}/>

                <EditableText attributeName={attribute}></EditableText>
            </div>
        );
    }

    return (<div style={{width: '100%', padding: '0px 7px 0px 7px'}}>
        {items}
    </div>)
}

export default DividerAttributeList