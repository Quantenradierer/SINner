import React from "react";
import {FramePentagon, List, Text} from "@arwes/core";

class NPCPrivate extends React.Component {
    render() {
        const relevantAttributes = ['Hobbys und Interessen', 'Eigenarten', 'Familie',
            'Kontakte', 'Wohnort', 'Konzernzugehörigkeit', 'Geheimnis']
        const items = [];

        for (const attribute of relevantAttributes) {
            items.push(<li key={attribute}><Text><b>{attribute}:</b> {this.props.npc.attributes[attribute]} </Text>
            </li>);
        }
        if (!this.props.show) {
            return (<div></div>)
        } else {
            return (
                <FramePentagon style={{width: 950, margin: 15}}>
                    <List>
                        {items}
                    </List>
                </FramePentagon>
            )
        }
    }
}

export default NPCPrivate;
