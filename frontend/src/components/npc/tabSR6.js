

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
import ImageFrame from "../cyberpunk/imageFrame";
import {Animator} from "@arwes/animation";
import Tabs from "../entity/tabs";

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

        let end = buttonWidth * 2 + buttonWidth / 2;
        if (i === Math.floor(amount / 3)) {
            end = (((amount - 1) % 3)) * buttonWidth + buttonWidth / 2
        }
        pathData += `${buttonWidth / 2} ${y} ${end} ${y} `;
    }

    return <FramePentagon style={{width: 'fit-content', paddingBottom: 15}} squareSize={35}>
        <Text style={{marginBottom: 5}}>{title}</Text>

        <div style={{display: 'grid', width: 'fit-content', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0px'}}>
            {buttons}
            <div style={{position: 'absolute', opacity: '30%', pointerEvents: 'none'}}>
                <svg width={buttonWidth*3} height={buttonHeight*(amount / 3 + 1)} xmlns="http://www.w3.org/2000/svg">
                    <path d={`M${buttonWidth/2} ${buttonHeight/2} ${pathData}`} stroke="#00F8F8" stroke-width="3" fill="none"/>
                </svg>
            </div>
        </div>
    </FramePentagon>;

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
                                    <Table condensed headers={tableHeaders} dataset={tableContent}/>
                                    <SkillTable entity={entity}/>
                                </div>
                            </FramePentagon>
                        </div>
                        <div className="tab-sr6-container">
                            <FramePentagon>
                                <div style={{}}>
                                    <span><b>{i18n.t("attribute_equipment")}:</b> <Text>{entity.values['equipment']}</Text></span>
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
