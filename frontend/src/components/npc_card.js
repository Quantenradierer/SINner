import React from "react";
import {Button, Card, Text} from "@arwes/core";
import {FramePentagon, Figure, List} from '@arwes/core';

class NPCCard extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        const relevantAttributes = ['Catchphrase', 'Metatyp', 'Beruf', 'Ethnizität', 'Geschlecht', 'Alter', 'Geruch', 'Detailliertes Aussehen', ]
        const items = [];

        for (const attribute of relevantAttributes) {
            items.push(<li style={{  position: 'relative' }} key={attribute}><Text> {attribute}: {this.props.npc.attributes[attribute]} </Text></li>);
            //items.push(<Text> {attribute}: {this.props.npc.attributes[attribute]} </Text>);
        }

        return (
            <Card
                image={{
                    src: this.props.npc.image_url,
                    alt: this.props.npc.image_generator_description
                }}
                options={
                  <Button palette='secondary'>
                    <Text>Details</Text>
                  </Button>
                }
                style={{width: 1000}}
                title={this.props.npc.attributes['Name']}
                landscape
            >
                <div>
                    <List>
                        <li><Text>SIN: {this.props.npc.id}</Text></li>
                        {items}
                    </List>
                </div>
            </Card>
        )
    }
}

export default NPCCard;
