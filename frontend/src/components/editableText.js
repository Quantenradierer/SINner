import {Button, FrameLines, FramePentagon, Text} from "@arwes/core";
import React, {useEffect, useState} from "react";
import api from "../axios";
import {useEntity} from "./entityProvider";




const EditableText = ({attributeName}) => {
    const {entity, _} = useEntity();

    let attribute = entity.values[attributeName]
    const [value, setValue] = useState( attribute || '');

    useEffect(() => {
        setValue(attribute?.toString() || '');
    }, [entity, attributeName]);

    const handleChange = (event) => {
        entity.values[attributeName] = event.target.value
        setValue(event.target.value?.toString());
    };

    if (!entity.editable) {
        return (
            <div style={{width: '100%'}}>
                <Text key={attribute}>{value}</Text>
            </div>);
    } else {
        let rows = 1;
        if (value) {
            rows = Math.ceil(value.length / 80);
        }

        return (<textarea style={{width: '100%'}} rows={rows} key={'textarea' + attributeName} value={value} onChange={handleChange} />);
    }
}

export default EditableText