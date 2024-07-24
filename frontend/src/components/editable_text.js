import {Button, FrameLines, FramePentagon, Text} from "@arwes/core";
import React, {useEffect, useState} from "react";
import api from "../axios";




const EditableText = props => {
    let attributes = props.entity.values[props.attribute]
    let attribute = ''
    if (attributes != undefined && attributes instanceof Array) {
        attribute = attributes[0]
    } else {
        attribute = attributes
    }

    let definition = props.entity.attribute_definition&[props.attribute]
    const [value, setValue] = useState( attribute || '');

    useEffect(() => {
        setValue(attribute?.toString() || '');
    }, [props.entity, props.attribute]);

    const handleChange = (event) => {
        props.entity.values[props.attribute] = event.target.value
        setValue(event.target.value?.toString());
    };

    if (!props.editable) {
        return (
            <div style={{display: 'flex', width: '100%'}}>
                <Text style={{flexGrow: 1, flexBasis: '100%'}} key={props.attribute}>{value}</Text>
            </div>);
    } else {
        let rows = 1;
        let backgroundColor = ''

        if (value) {
            rows = Math.ceil(value.length / props.approxLineSize);
        }
        if (!value.trim() && props.check) {
            backgroundColor = '#3c2021'
        }

        rows = Math.min(4, rows);
        let style = { padding: '2px', height: 4 + rows * 32 + 'px', width: '100%', backgroundColor: backgroundColor };

        Object.assign(style, props.style);
        if (definition.length == 0) {
            return (<textarea style={style} disabled={props.editableDisabled} rows={rows} key={props.attribute} value={value} onChange={handleChange} />);
        } else {
            return (<div style={style}><input style={{height: '100%'}} type={"text"} maxLength={definition.length} disabled={props.editableDisabled} rows={rows} key={props.attribute} value={value} onChange={handleChange} /> </div>);
        }
    }
}

export default EditableText