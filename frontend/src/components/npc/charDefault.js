import React from "react";
import {Blockquote, Button, Card, Text} from "@arwes/core";
import image_path from "../../image_path";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";
import active_image from "../../active_image";
import NPCPrivate from "./npc_private";
import {useLoaderData} from "react-router";
import {useNavigation, useParams} from "react-router-dom";
import NpcTabsHeader from "./npcTabsHeader";
import useEntitySchema from "../../loader/useEntitySchema";


function charDefault(props) {
    const entity = props.entity
    let activeImage = active_image(entity.image_objects) || {}

    const relevantAttributes = ['metatype', 'profession', 'ethnicity', 'gender', 'age', 'quirks']
    return (
        <div>
            <Card
                image={{
                    src: image_path('npcs', activeImage.name),
                    alt: entity.image_generator_description,
                }}
                title={<EditableText style={{width: '630px'}}
                                     attribute='name'
                                     entity={entity}
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
                                              attribute='catchphrase'
                                              entity={entity}
                                              approxLineSize={58}
                                              editable={props.editable}
                                              editableDisabled={props.editableDisabled}
                                              check={props.check}
                                /></div>
                        </Text>
                    </Blockquote>

                    <AttributeList listItemWidth={100}
                                   entity={entity}
                                   attributes={relevantAttributes}
                                   approxLineSize={58}
                                   editable={props.editable}
                                   editableDisabled={props.editableDisabled}
                                   check={props.check}
                    />
                </div>
            </Card>
            <NPCPrivate entity={entity}/>
        </div>

    )
}

export default charDefault;
