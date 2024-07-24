

import React from 'react';
import {
    FrameBox,
    FrameCorners,
    FrameHexagon,
    FrameLines,
    FramePentagon,
    FrameUnderline,
    Table,
    Text
} from '@arwes/core';
import EditableText from "../editable_text";
import image_path from "../../image_path";
import active_image from "../../active_image";
import i18n from "../../i18n";

const CharArcSR6 = (props) => {
    const entity = props.entity
    let activeImage = active_image(entity.image_objects) || {}


    const tableHeaders = [
        {id: 'Kon', data: 'Kon'},
        {id: 'Ges', data: 'Ges'},
        {id: 'Rea', data: 'Rea'},
        {id: 'Str', data: 'Str'},
        {id: 'Wil', data: 'Wil'},
        {id: 'Log', data: 'Log'},
        {id: 'Int', data: 'Int'},
        {id: 'Cha', data: 'Cha'},
        {id: 'Edg', data: 'Edg'},
        {id: 'Mag', data: 'Mag'},
        {id: 'Res', data: 'Res'}
    ]


    let attributes = [
        'constitution',
        'agility',
        'reaction',
        'strength',
        'willpower',
        'logic',
        'intuition',
        'charisma',
        'edge',
        'magic',
        'resonance'
    ]
    let columns = attributes.map(attribute => new Object({
            id: attribute.substring(0, 3),
            data:
                <EditableText attribute={attribute}
                              entity={entity}
                              approxLineSize={58}
                              editable={false}
                              editableDisabled={false}
                              check={false}
                />
        })
    )

    const tableContent = [{
        id: 0,
        columns: columns
    }]

    return (
        <div key={entity.id}>
            <FramePentagon style={{margin: 0, padding: 0, width: '100%'}}>
                <div style={{display: 'flex', justifyContent: 'space-between'}}>
                    <div style={{width: '100%'}}>
                        <div style={{width: '100%'}}>
                            <FrameLines hideTopLines={true} style={{padding: 10, margin: 0, width: '100%'}}>
                                <Text><h3 style={{margin: 0}}>{entity.values['name']} </h3></Text>
                            </FrameLines>
                        </div>
                        <div style={{width: '100%', padding: 10}}>
                            <Table condensed headers={tableHeaders} dataset={tableContent}/>
                            <span><b>{i18n.t("attribute_skills")}:</b> <Text>{entity.values['skills']}</Text></span>
                            <br/>
                            <span><b>{i18n.t("attribute_equipment")}:</b> <Text>{entity.values['equipment']}</Text></span>
                            <br/>
                            <span><b>{i18n.t("attribute_lootable_items")}:</b> <Text>{entity.values['lootable_items']}</Text></span>
                            <br/>
                            <br/>
                            <br/>
                            <span><b>Der Charakterbogen ist noch in Arbeit.</b></span>
                        </div>
                    </div>
                    <div style={{maxWidth: '200px', padding: '1px 1px 1px 0px'}}>
                        <div>
                            <img style={{padding: 5, overflow: 'hidden'}}
                                 src={image_path('npcs', activeImage.name, true)}
                                 alt={entity.values['image_generator_description']}/>
                        </div>
                    </div>
                </div>
            </FramePentagon>
        </div>
    )
}

export default CharArcSR6;