import React from "react";
import {Text} from "@arwes/core";
import {FramePentagon, Figure, List} from '@arwes/core';

class NPCCard extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        const items = [];
        for (const property in this.props.npc.attributes) {
            items.push(<li key={property}><Text> {property}: {this.props.npc.attributes[property]} </Text></li>);
        }

        return (
            <FramePentagon hover squareSize={155} style={{width: 1200, height: 555}}>
                <div>
                    <div style={{float:'left'}}>
                        <Figure src={this.props.npc.image_url} alt={this.props.npc.image_generator_description} />
                    </div>
                    <div style={{float:'left', width: 620}}>
                        <List>
                            <li><Text>SIN: {this.props.npc.id}</Text></li>
                            {items}
                        </List>
                    </div>
                </div>
            </FramePentagon>
        )
    }
}

export default NPCCard;
