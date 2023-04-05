import React from "react";
import {FramePentagon, List, Text} from "@arwes/core";

class NPCSkills extends React.Component {
    render() {
        const relevantAttributes = ['Stärken', 'Schwächen', 'Fertigkeiten', 'Ausrüstung', 'Lootbare Gegenstände', 'Geheimnis']
        const items = [];

        for (const attribute of relevantAttributes) {
            items.push(<li key={attribute}><Text><b>{attribute}:</b> {this.props.npc.attributes[attribute]} </Text>
            </li>);
        }

        return (
            <FramePentagon style={{width: 950, margin: 15}}>
                <List>
                    {items}
                </List>
            </FramePentagon>
        )
    }
}

export default NPCSkills;
