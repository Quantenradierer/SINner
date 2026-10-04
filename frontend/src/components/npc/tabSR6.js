

import {
    FrameCorners,
    FrameHexagon,
    FrameLines,
    FramePentagon,
    FrameUnderline,
    Table,
    Text
} from '@arwes/core';
import EditableText from "../editableText";
import image_path from "../../image_path";
import active_image from "../../active_image";
import i18n from "../../i18n";
import React from 'react';
import {physicalCondition, stunCondition} from "./sr6Rules";
import {AttributeTable, ConditionTable} from "./sheetParts";
import {useEntity} from "../entityProvider";
import ImageFrame from "../cyberpunk/imageFrame";
import {Animator} from "@arwes/animation";
import Tabs from "../entity/tabs";

// The backend resolves equipment ids to readable names in `entity.equipment_display`
// ([{id, name}, ...]). Fall back to whatever is in entity.values['equipment']
// (legacy comma-separated string, or a list of ids / {id, mods} objects).
const equipmentText = (entity) => {
    const resolved = entity.equipment_display;
    if (Array.isArray(resolved) && resolved.length) {
        return resolved.map(item => item.name || item.id).join(', ');
    }
    const raw = entity.values && entity.values['equipment'];
    if (!raw) return '';
    if (typeof raw === 'string') return raw;
    if (Array.isArray(raw)) {
        return raw
            .map(item => (typeof item === 'string' ? item : item && item.id))
            .filter(Boolean)
            .join(', ');
    }
    return String(raw);
};

const SkillTable = ({entity}) => {
    const skills = [
        "skill_astral", "skill_athletics", "skill_biotech", "skill_close_combat", "skill_con", "skill_conjuring",
        "skill_cracking", "skill_electronics", "skill_enchanting", "skill_engineering",
        "skill_firearms", "skill_influence", "skill_outdoors", "skill_perception", "skill_piloting", "skill_sorcery",
        "skill_stealth", "skill_tasking", "skill_exotic_weapons"
    ];
    const halfLength = Math.ceil(skills.length / 2);
    const firstHalfSkills = skills.slice(0, halfLength);
    const secondHalfSkills = skills.slice(halfLength);

    const tableHeaders = [
        {id: 'skill', data: i18n.t('npc_skill')},
        {id: 'value', data: i18n.t('npc_skill_value')}
    ];

    const createTableContent = (skillSet) => {
        return skillSet.map(skill => ({
            id: skill,
            columns: [
                {id: 'skill', data: i18n.t('npc_' + skill)},
                {id: 'value', data: <EditableText attributeName={skill}/>}
            ]
        }));
    };

    const firstTableContent = createTableContent(firstHalfSkills);
    const secondTableContent = createTableContent(secondHalfSkills);

    return (
        <div className="two-cols">
            <div style={{width: '175px', margin: 5}}>
                <Table className={"col1"} condensed headers={tableHeaders}
                       dataset={firstTableContent} columnWidths={['120px', '55px']}/>
            </div>
            <div style={{width: '175px', margin: 5}}>
                <Table className={"col2"} condensed headers={tableHeaders} dataset={secondTableContent}
                       columnWidths={['120px', '55px']}/>
            </div>
        </div>
    );
};

const WeaponTable = ({entity}) => {
        const tableHeaders = [
        {id: 'weapon', data: i18n.t('Waffe')},
        {id: 'pool', data: i18n.t('Pool')},
        {id: 'schaden', data: i18n.t('Schaden')},
        {id: 'aw', data: i18n.t('AW')},
        {id: 'mode', data: i18n.t('Modus')},
        {id: 'ammo', data: i18n.t('Muni')},
    ]
    let columns = [{
        id: 'weapon',
        data: 'TBD Pistole'
    },
        {
            id: 'pool',
            data: 'TBD'
        },
        {
            id: 'schaden',
            data: 'TBD'
        },
        {
            id: 'aw',
            data: 'TBD'
        },
        {
            id: 'mode',
            data: 'TBD'
        },
        {
            id: 'ammo',
            data: 'TBD'
        }]


    const tableContent = [{
        id: 0,
        columns: columns
    }]

    return <Table condensed headers={tableHeaders} dataset={tableContent}/>

}

const TabSR6 = (props) => {
    const {entity, _} = useEntity();
    let activeImage = active_image(entity.image_objects) || {}

    return (
        <div>
            <Animator animator={{
                combine: true, manager: 'stagger',
                duration: {stagger: 250}
            }}>
                <div className="tab-sr6-content">
                    <div className='left-container' style={{width: '100%', flexDirection: 'column'}}>
                        <div className="tab-sr6-container">
                            <FramePentagon style={{padding: 0}}>
                                <FrameLines hideTopLines={true} style={{padding: 10, margin: 0, width: '100%'}}>
                                    <h3 style={{margin: 0}}><Text>{entity.values['name']} </Text></h3>
                                </FrameLines>
                                <div style={{margin: '10px'}}>
                                    <AttributeTable entity={entity}/>
                                    <SkillTable entity={entity}/>
                                </div>
                            </FramePentagon>
                        </div>
                        <div className="tab-sr6-container">
                            <FramePentagon>
                                <div style={{}}>
                                    <span><b>{i18n.t("attribute_equipment")}:</b> <Text>{equipmentText(entity)}</Text></span>
                                    <br/>
                                </div>
                            </FramePentagon>
                        </div>
                    </div>
                    <div className='right-container'>

                        <div style={{width: 'min-content'}}>
                            <div className="tab-sr6-container">
                                <ImageFrame style={{
                                    maxWidth: '600px',
                                    maxHeight: '400px',
                                    minHeight: '150px',
                                    overflow: 'hidden'
                                }}/>
                            </div>
                            <div style={{display: 'flex'}}>
                                <div className="tab-sr6-container">
                                    <ConditionTable title={i18n.t('npc_physical_condition')}
                                                    amount={physicalCondition(entity)}/>
                                </div>
                                <div className="tab-sr6-container">
                                    <ConditionTable title={i18n.t('npc_stun_condition')}
                                                    amount={stunCondition(entity)}/>
                                </div>
                            </div>
                        </div>
                        <br/>
                    </div>
                </div>
            </Animator>
        </div>
    )
}

export default TabSR6;
