import {Button, FrameLines, Text} from "@arwes/core";
import React, {useEffect, useState} from "react";


const EditableText = props => {
    const [value, setValue] = useState( props.npc.attributes[props.attribute] || ' ');

    useEffect(() => {
        setValue(props.npc.attributes[props.attribute] || ' ');
    }, [props.npc, props.attribute]);

    const handleChange = (event) => {
        props.npc.attributes[props.attribute] = event.target.value
        setValue(event.target.value);
    };

    if (!props.editable) {
        return (<Text key={props.attribute}>{value}</Text>);
    } else {
        let rows = 1;
        if (value) {
            rows = Math.ceil(value.length / props.approxLineSize);
        }
        rows = Math.min(4, rows);
        let style = { padding: '2px' };
        Object.assign(style, props.style);

        return (<textarea style={style} disabled={props.editableDisabled} rows={rows} key={props.attribute} value={value} onChange={handleChange} />);
    }
}

export default EditableText