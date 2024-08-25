import {Button, FrameLines, List, Text} from "@arwes/core";
import React from "react";
import EditableText from "./editableText";
import i18next from "../i18n";


const styles = {
    container: {
        width: 'auto',
        margin: '20px auto',
        fontFamily: 'Arial, sans-serif'
    },
    listItem: {
        display: 'flex',
        justifyContent: 'flex-start',
        padding: '7px 7px 0px 0px',
        alignItems: 'top',
    },
    label: {
        minWidth: 'max-content',
    },
    value: {
        flex: 1
    }
};

const AttributeList = props => {
    const items = [];

    for (const attribute of props.attributes) {
        items.push(
            <div key={'div' + attribute} style={styles.listItem}>
                <div style={styles.label}>
                    <div style={{width: props.listItemWidth}}><Text><b>{i18next.t('attribute_' + attribute.replaceAll(' ', '_').replaceAll('/', '_').toLowerCase())}:</b></Text></div>
                </div>
                <EditableText style={{margin: '-7px 0 0 0'}}
                              attributeName={attribute}
                              editable={props.editable}
                />



            </div>
        );
        items.push(<hr key={'hr' + items.length} style={{width: '97%', margin: '2px 0px 0px 2px'}}/>)
    }
    items.pop()

    return (<div style={{width: '100%', margin: '0px 0px 7px 7px'}}>
        {items}
    </div>)
}

export default AttributeList