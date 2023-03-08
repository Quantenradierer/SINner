import React from "react";
import {Text} from "@arwes/core";
import {FramePentagon, List} from '@arwes/core';

class NPCDetails extends React.Component {

    render() {
        const relevantAttributes = ['Hintergrundgeschichte', 'Erfahrungen', 'Ressentiments', 'Motivationen', 'Ziele',
                                    'Stärken', 'Schwächen', 'Fertigkeiten', 'Ausrüstung']
        const items = [];

        for (const attribute of relevantAttributes) {
            items.push(<li key={attribute}><Text><b>{attribute}:</b> {this.props.npc.attributes[attribute]} </Text></li>);
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

export default NPCDetails;
