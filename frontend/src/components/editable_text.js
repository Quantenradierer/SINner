import {Button, FrameLines, FramePentagon, Text} from "@arwes/core";
import React, {useEffect, useState} from "react";
import api from "../axios";




const EditableText = props => {
    const [value, setValue] = useState( props.npc.attributes[props.attribute] || '');

    useEffect(() => {
        setValue(props.npc.attributes[props.attribute] || '');
    }, [props.npc, props.attribute]);

    const handleChange = (event) => {
        props.npc.attributes[props.attribute] = event.target.value
        setValue(event.target.value);
    };

    async function handleAlternatives(event) {
        props.setAlternatives(props.attribute)
    }

    if (!props.editable) {
        return (
            <div style={{display: 'flex', width: '100%'}}>
                <Text style={{flexGrow: 1, flexBasis: '100%'}} key={props.attribute}>{value}</Text>
                <a onClick={handleAlternatives} style={{marginRight: '10px', cursor: 'pointer'}}>🎲</a>
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

        return (<textarea style={style} disabled={props.editableDisabled} rows={rows} key={props.attribute} value={value} onChange={handleChange} />);
    }
}

export default EditableText