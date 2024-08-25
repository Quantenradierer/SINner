import {Button, FrameLines, List, Text} from "@arwes/core";
import React from "react";
import EditableText from "./editableText";
import i18next from "../i18n";
import './simpleAttributeList.css'

const SimpleAttributeList = ({ attributes }) => {
    const items = [];

    for (const attribute of attributes) {
        items.push(
            <div key={'div' + attribute} style={{width: '100%'}}>
                <div>
                    <Text className='attr-list-item' style={{width: '100%', margin: '5px 5px 0px 5px'}}>
                        <span>
                            <b>{i18next.t('attribute_' + attribute.replaceAll(' ', '_').replaceAll('/', '_').toLowerCase())}</b>
                        </span></Text>
                </div>
                <EditableText attributeName={attribute} style={{margin: '5px 5px 5px 5px'}}></EditableText>
            </div>
        );
        items.push(<hr key={'hr' + items.length} style={{width: '100%', margin: '0px'}}/>)
    }
    items.pop()

    return (<div style={{width: '100%', padding: '0px 7px 0px 7px'}}>
        {items}
    </div>)
}

export default SimpleAttributeList