

import {
    Button,
    FrameBox,
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
import React, { useState } from 'react';
import {position} from "polished";
import {physicalCondition, stunCondition} from "./sr6Rules";
import {useEntity} from "../entityProvider";

const SkillTable = ({entity}) => {
    const skills = [
        "skill_astral", "skill_athletics", "skill_biotech", "skill_close_combat", "skill_con", "skill_conjuring",
        "skill_cracking", "skill_electronics", "skill_enchanting", "skill_engineering", "skill_exotic_weapons",
        "skill_firearms", "skill_influence", "skill_outdoors", "skill_perception", "skill_piloting", "skill_sorcery",
        "skill_stealth", "skill_tasking"
    ];
    const halfLength = Math.ceil(skills.length / 2);
    const firstHalfSkills = skills.slice(0, halfLength);
    const secondHalfSkills = skills.slice(halfLength);

    const tableHeaders = [
        {id: 'skill', data: 'Skill'},
        {id: 'value', data: 'Value'}
    ];

    const createTableContent = (skillSet) => {
        return skillSet.map(skill => ({
            id: skill,
            columns: [
                {id: 'skill', data: i18n.t('npc_' + skill)},
                {id: 'value', data: entity.values[skill] || 0}
            ]
        }));
    };

    const firstTableContent = createTableContent(firstHalfSkills);
    const secondTableContent = createTableContent(secondHalfSkills);

    return (
        <div className={"two-cols"}>
            <div style={{width: '195px', margin: 5}}>
                <Table className={"col1"} condensed headers={tableHeaders}
                       dataset={firstTableContent} columnWidths={['140px', '55px']}/>
            </div>
            <div style={{width: '195px', margin: 5}}>

                <Table className={"col2"} condensed headers={tableHeaders} dataset={secondTableContent}
                       columnWidths={['140px', '55px']}/>
            </div>
        </div>
    );
};

function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}

const ConditionTable = ({ amount, title }) => {
    if (!isNumeric(amount)) {
        return null;
    }
    const [activeStates, setActiveStates] = useState(Array(amount).fill(false));

    const buttonWidth = 42;
    const buttonHeight = 42;

    const toggleActiveState = (index) => {
        setActiveStates(prevStates => {
            const newStates = [...prevStates];
            newStates[index] = !newStates[index];
            return newStates;
        });
    };

    const buttons = [];
    for (let i = 0; i < amount; i++) {
        const malus = Math.floor((i + 1) / 3);
        buttons.push(
            <Button
                key={'ConditionTableButton' + i}
                style={{width: buttonWidth, height: buttonHeight}}
                FrameComponent={FrameBox}
                active={true}
                onClick={() => toggleActiveState(i)}
                palette={activeStates[i] ? 'error' : 'success'}
            >
                <Text>{malus > 0 && '-'}{malus}</Text>
            </Button>
        );
    }

    let pathData = '';
    for (let i = 0; i < amount / 3; i++) {
        const y = buttonHeight / 2 + i * buttonHeight;

        let end = 105
        if (i === Math.floor(amount / 3)) {
            end = (((amount - 1) % 3)) * buttonWidth + buttonWidth / 2
        }
        pathData += `${buttonWidth / 2} ${y} ${end} ${y} `;
    }

    return <FramePentagon style={{width: 'fit-content'}}>
        {title}

        <div style={{display: 'grid', width: 'fit-content', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0px'}}>
            {buttons}
            <div style={{position: 'absolute', opacity: '30%', pointerEvents: 'none'}}>
                <svg width="200" height="1000" xmlns="http://www.w3.org/2000/svg">
                    <path d={`M21 21 ${pathData}`} stroke="#00F8F8" stroke-width="3" fill="none"/>
                </svg>
            </div>
        </div>
    </FramePentagon>;

};

const CharArcSR6 = (props) => {
    const {entity, _} = useEntity();
    let activeImage = active_image(entity.image_objects) || {}

    const tableHeaders = [
        {id: 'bod', data: i18n.t('npc_attribute_bod')},
        {id: 'agi', data: i18n.t('npc_attribute_agi')},
        {id: 'rea', data: i18n.t('npc_attribute_rea')},
        {id: 'str', data: i18n.t('npc_attribute_str')},
        {id: 'wil', data: i18n.t('npc_attribute_wil')},
        {id: 'log', data: i18n.t('npc_attribute_log')},
        {id: 'int', data: i18n.t('npc_attribute_int')},
        {id: 'cha', data: i18n.t('npc_attribute_cha')},
        {id: 'edg', data: i18n.t('npc_attribute_edg')},
        {id: 'mag', data: i18n.t('npc_attribute_mag')},
        {id: 'res', data: i18n.t('npc_attribute_res')}
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
                <EditableText attributeName={attribute}
                              entity={entity}
                              check={false}
                />
        })
    )

    const tableContent = [{
        id: 0,
        columns: columns
    }]
    return (
        <div style={{display: 'flex', justifyContent: 'space-between'}}>

            <div style={{width: '100%'}}>

                <span><h2><u>Der Charakterbogen ist noch in Arbeit.</u></h2></span>
                <div style={{width: '100%'}}>
                    <FrameLines hideTopLines={true} style={{padding: 10, margin: 0, width: '100%'}}>
                        <h3 style={{margin: 0}}><Text>{entity.values['name']} </Text></h3>
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
                    <SkillTable entity={entity}/>
                    <ConditionTable title={'PhysicalCondition'} amount={physicalCondition(entity)}/>
                    <ConditionTable title={'StunCondition'} amount={stunCondition(entity)}/>
                    <br/>
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
    )
}

export default CharArcSR6;
