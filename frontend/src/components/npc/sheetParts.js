import {Button, FrameBox, FramePentagon, Table, Text} from '@arwes/core';
import React, {useState} from 'react';
import i18n from "../../i18n";
import EditableText from "../editableText";

// [value key, i18n abbreviation]
const attributes = [
    ['constitution', 'bod'], ['agility', 'agi'], ['reaction', 'rea'], ['strength', 'str'],
    ['willpower', 'wil'], ['logic', 'log'], ['intuition', 'int'], ['charisma', 'cha'],
    ['edge', 'edg'], ['magic', 'mag'], ['resonance', 'res']
];

// The attributes Shadowrun 5 and 6 share.
const AttributeTable = ({entity}) => {
    const tableHeaders = attributes.map(([_, abbreviation]) => ({
        id: abbreviation,
        data: i18n.t('npc_attribute_' + abbreviation)
    }));
    const columns = attributes.map(([attribute, abbreviation]) => ({
        id: abbreviation,
        data: <EditableText attributeName={attribute} entity={entity} check={false}/>
    }));
    return <Table condensed headers={tableHeaders} dataset={[{id: 0, columns: columns}]}/>;
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

export {AttributeTable, ConditionTable};
