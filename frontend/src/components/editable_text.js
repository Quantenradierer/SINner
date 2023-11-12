import {Button, FrameLines, FramePentagon, Text} from "@arwes/core";
import React, {useEffect, useState} from "react";
import api from "../axios";




const EditableText = props => {
    let attribute = props.entity.primary_values[props.attribute]
    console.log(attribute)
    let definition = props.entity.attribute_definition[props.attribute]
    const [value, setValue] = useState( attribute || '');

    useEffect(() => {
        setValue(attribute || '');
    }, [props.entity, props.attribute]);

    const handleChange = (event) => {
        props.entity.primary_values[props.attribute] = event.target.value
        setValue(event.target.value);
    };

    async function handleAlternatives(event) {
        props.setAlternatives(props.attribute)
    }

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
        let style = { padding: '2px', height: 4 + rows * 32 + 'px', backgroundColor: backgroundColor };

        Object.assign(style, props.style);

        console.log(definition.length)
        if (definition.length == 0) {
            return (<textarea style={style} disabled={props.editableDisabled} rows={rows} key={props.attribute} value={value} onChange={handleChange} />);
        } else {
            return (<input type={"text"} maxLength={definition.length} style={style} disabled={props.editableDisabled} rows={rows} key={props.attribute} value={value} onChange={handleChange} />);
        }
    }
}

export default EditableText