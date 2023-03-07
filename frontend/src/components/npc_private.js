import React from "react";
import {Button, Card, Text} from "@arwes/core";
import {FramePentagon, Figure, List} from '@arwes/core';

class NPCPrivate extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        const relevantAttributes = ['Hobbys und Interessen', 'Eigenarten', 'Familienstand', 'Familie', 'Kinder',
                                    'Kontakte', 'Wohnort', 'Nationalität', 'Konzernzugehörigkeit', 'Geheimnis']
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

export default NPCPrivate;
