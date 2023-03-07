import React from "react";
import {Blockquote, Button, Card, Text} from "@arwes/core";
import {FramePentagon, Figure, List} from '@arwes/core';

class NPCCard extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        const relevantAttributes = ['Metatyp', 'Beruf', 'Ethnizität', 'Geschlecht', 'Alter', 'Geruch', 'Detailliertes Aussehen', ]
        const items = [];

        for (const attribute of relevantAttributes) {
            items.push(<li key={attribute}><Text><b>{attribute}:</b> {this.props.npc.attributes[attribute]} </Text></li>);
        }

        return (
            <Card
                image={{
                    src: this.props.npc.image_url,
                    alt: this.props.npc.image_generator_description
                }}
                options={
                <div>
                  <Button onClick={this.props.toggleDetails}>
                    <Text>Hintergrund</Text>
                  </Button>
                  <Button onClick={this.props.togglePrivate}>
                    <Text>Privates</Text>
                  </Button>
                </div>
                }
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
            </Card>
        )
    }
}

export default NPCCard;
