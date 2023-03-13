import React from "react";
import {Blockquote, Card, List, Table, Text} from "@arwes/core";

class NPCCard extends React.Component {

    tableHeaders() {
        return [
            {id: 'K', data: 'K'},
            {id: 'G', data: 'G'},
            {id: 'R', data: 'R'},
            {id: 'S', data: 'S'},
            {id: 'W', data: 'W'},
            {id: 'L', data: 'L'},
            {id: 'I', data: 'I'},
            {id: 'C', data: 'C'},
            {id: 'E', data: 'E'}
        ];
    }

    tableDataset(npc) {
        return [{
            id: 0,
            columns: [
                {id: 'K', data: npc.attributes['Konstitution (von 1-6)']},
                {id: 'G', data: npc.attributes['Geschicklichkeit (von 1-6)']},
                {id: 'R', data: npc.attributes['Reaktion (von 1-6)']},
                {id: 'S', data: npc.attributes['Stärke (von 1-6)']},
                {id: 'W', data: npc.attributes['Konstitution (von 1-6)']},
                {id: 'L', data: npc.attributes['Logik (von 1-6)']},
                {id: 'I', data: npc.attributes['Intuition (von 1-6)']},
                {id: 'C', data: npc.attributes['Charisma (von 1-6)']},
                {id: 'E', data: npc.attributes['Glück (von 1-6)']}
            ]
        }]
    }

    render() {
        const relevantAttributes = ['Metatyp', 'Beruf', 'Ethnizität', 'Geschlecht', 'Alter', 'Detailliertes Aussehen',]
        const items = [];

        for (const attribute of relevantAttributes) {
            items.push(<li key={attribute}><Text><b>{attribute}:</b> {this.props.npc.attributes[attribute]} </Text>
            </li>);
        }

        return (
            <Card
                image={{
                    src: '../images/npcs/' + this.props.npc.image_url,
                    alt: this.props.npc.image_generator_description
                }}
                style={{width: 950, margin: 15}}
                title={this.props.npc.attributes['Name']}
                landscape
            >
                <div>
                    <Blockquote>
                        <Text>
                            {this.props.npc.attributes['Catchphrase']}
                        </Text>
                    </Blockquote>

                    <List>
                        <li><Text><b>SIN:</b> {this.props.npc.id}</Text></li>
                        {items}
                    </List>
                </div>
                <Table headers={this.tableHeaders()} dataset={this.tableDataset(this.props.npc)}>

                </Table>
            </Card>
        )
    }
}

export default NPCCard;
