import {FrameLines, FramePentagon, Table, Text} from '@arwes/core';
import EditableText from "../editableText";
import active_image from "../../active_image";
import i18n from "../../i18n";
import React from 'react';
import {physicalCondition, stunCondition} from "./sr6Rules";
import {AttributeTable, ConditionTable} from "./sheetParts";
import {categories, skillKey} from "./sr5Skills";
import {useEntity} from "../entityProvider";
import ImageFrame from "../cyberpunk/imageFrame";
import {Animator} from "@arwes/animation";

const tableHeaders = [
    {id: 'skill', data: i18n.t('npc_skill')},
    {id: 'value', data: i18n.t('npc_skill_value')}
];

// Only skills above 0 are shown; categories without any are left out.
const SkillTable = ({entity}) => {
    const tables = Object.entries(categories).map(([category, names]) => {
        const dataset = names
            .map(skillKey)
            .filter(key => Number(entity.values[key]) > 0)
            .map(key => ({
                id: key,
                columns: [
                    {id: 'skill', data: i18n.t('npc_' + key)},
                    {id: 'value', data: <EditableText attributeName={key}/>}
                ]
            }));
        if (!dataset.length) {
            return null;
        }
        return (
            <div key={category} style={{width: '175px', margin: 5}}>
                <Text>{i18n.t('npc_sr5_category_' + category)}</Text>
                <Table condensed headers={tableHeaders} dataset={dataset} columnWidths={['120px', '55px']}/>
            </div>
        );
    });
    return <div className="two-cols" style={{flexWrap: 'wrap'}}>{tables}</div>;
};

const TabSR5 = (props) => {
    const {entity, _} = useEntity();

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

export default TabSR5;
