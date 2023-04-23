import React from "react";
import {Blockquote, Button, Card, List, Table, Text} from "@arwes/core";
import image_path from "../image_path";
import is_loggin_in from "../is_loggin_in";
import is_logged_in from "../is_loggin_in";

class NPCCard extends React.Component {
    constructor(props) {
        super(props);
    }

    tableHeaders() {
        return [
            {id: 'Ko', data: 'Kon'},
            {id: 'G', data: 'Ges'},
            {id: 'R', data: 'Rea'},
            {id: 'S', data: 'Str'},
            {id: 'W', data: 'Wil'},
            {id: 'L', data: 'Log'},
            {id: 'I', data: 'Int'},
            {id: 'C', data: 'Cha'},
            {id: 'Edg', data: 'Edg'},
            {id: 'Mag', data: 'Mag'},
            {id: 'Res', data: 'Res'}
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
                {id: 'Edg', data: npc.attributes['Glück (von 1-6)']},
                {id: 'Mag', data: npc.attributes['Magie (von 0-6)']},
                {id: 'Res', data: npc.attributes['Resonanz (von 0-6)']}
            ]
        }]
    }

    render() {
        const relevantAttributes = ['Metatyp', 'Beruf', 'Ethnizität', 'Geschlecht', 'Alter', 'Eigenarten', 'Detailliertes Aussehen']
        const items = [];

        for (const attribute of relevantAttributes) {
            items.push(<li key={attribute}><Text><b>{attribute}:</b> {this.props.npc.attributes[attribute]} </Text>
            </li>);
        }

        return (
            <Card
                image={{
                    src: image_path(this.props.npc.image_url, this.props.npc.id, this.props.npc.default_image_number),
                    alt: this.props.npc.image_generator_description,

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
                <Table headers={this.tableHeaders()} dataset={this.tableDataset(this.props.npc)}/>
                <div className={is_logged_in()? '': 'hidden'}>
                    <a href={"/npcs/" + this.props.npc.id + "/gallery"}>
                        <Button>Galerie</Button>
                    </a>
                </div>
            </Card>
        )
    }
}

export default NPCCard;
