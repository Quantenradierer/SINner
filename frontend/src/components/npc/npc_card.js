import React from "react";
import {Blockquote, Button, Card, Text} from "@arwes/core";
import image_path from "../../image_path";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";
import active_image from "../../active_image";
import NPCPrivate from "./npc_private";


function NPCCard(props) {
    let state_label = ''
    let activeImage = active_image(props.entity.image_objects) || {}

    const relevantAttributes = ['Metatyp', 'Beruf', 'Ethnizität', 'Geschlecht', 'Alter', 'Eigenarten']
    return (
        <div>
            {state_label}
            <Card
                image={{
                    src: image_path('npcs', activeImage.name),
                    alt: props.entity.image_generator_description,
                }}
                title={<EditableText style={{width: '630px'}}
                                     attribute='Name'
                                     entity={props.entity}
                                     approxLineSize={58}
                                     editable={props.editable}
                                     editableDisabled={props.editableDisabled}
                                     check={props.check}

                />}
                landscape
            >

                <div>
                    <Blockquote>
                        <Text>
                            <div>
                                <EditableText style={{margin: '1 0 0 0', width: '580px'}}
                                              attribute='Catchphrase'
                                              entity={props.entity}
                                              approxLineSize={58}
                                              editable={props.editable}
                                              editableDisabled={props.editableDisabled}
                                              check={props.check}
                                /></div>
                        </Text>
                    </Blockquote>

                    <AttributeList listItemWidth={100}
                                   entity={props.entity}
                                   attributes={relevantAttributes}
                                   approxLineSize={58}
                                   editable={props.editable}
                                   editableDisabled={props.editableDisabled}
                                   check={props.check}
                    />
                </div>
            </Card>
            <NPCPrivate entity={props.entity}/>
        </div>

    )
}

export default NPCCard;
