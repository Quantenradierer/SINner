import React, {useState} from "react";

import Prompt from "../entity/prompt";
import {useLoaderData} from "react-router";
import CustomComplete from "./complete";
import {FramePentagon, Text} from "@arwes/core";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";


const EXAMPLES = []

const CustomCard = props => {

}


const CustomPrompt = props => {
    localStorage.setItem('custom_prompt', 'true');

    const default_entity = useLoaderData()

    const [entity, setEntity] = useState(default_entity);
    const [check, setCheck] = useState(false);
    const [editable, setEditable] = useState(true);

    const relevantAttributes = ['Aussehen', 'Parameter']

    return (
        <Prompt entityType={'custom'} examples={EXAMPLES} entity={entity} setEntity={setEntity}
                setEditable={setEditable}
                check={check} setCheck={setCheck}>

            <FramePentagon style={{width: 950, margin: 15}}>
                <div style={{display: 'flex', width: '100%'}}>

                    <AttributeList listItemWidth={100}
                                   entity={entity}
                                   attributes={relevantAttributes}
                                   approxLineSize={98}
                                   editable={true}
                                   editableDisabled={!editable}
                                   check={check}/>
                </div>

            </FramePentagon>

        </Prompt>)
}


export default CustomPrompt;
