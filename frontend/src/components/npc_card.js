import React from "react";
import {Blockquote, Button, Card, FrameLines, List, Table, Text} from "@arwes/core";
import image_path from "../image_path";
import is_logged_in from "../is_loggin_in";
import {Link} from "react-router-dom";
import api from "../axios";
import i18next from "../i18n";
import EditableText from "./editable_text";
import AttributeList from "./attribute_list";


function allows_edit(npc) {
  const queryParameters = new URLSearchParams(window.location.search)
  return !!queryParameters.get("access_key")
}


class NPCCard extends React.Component {
    constructor(props) {
        super(props);
    }

    tableHeaders() {
        return [
            {id: 'Kon', data: 'Kon'},
            {id: 'Ges', data: 'Ges'},
            {id: 'Rea', data: 'Rea'},
            {id: 'Str', data: 'Str'},
            {id: 'Wil', data: 'Wil'},
            {id: 'Log', data: 'Log'},
            {id: 'Int', data: 'Int'},
            {id: 'Cha', data: 'Cha'},
            {id: 'Edg', data: 'Edg'},
            {id: 'Mag', data: 'Mag'},
            {id: 'Res', data: 'Res'}
        ];
    }

    tableDataset(npc) {
        let attributes = [
            'Konstitution (von 1-6)',
            'Geschicklichkeit (von 1-6)',
            'Reaktion (von 1-6)',
            'Stärke (von 1-6)',
            'Willenskraft (von 1-6)',
            'Logik (von 1-6)',
            'Intuition (von 1-6)',
            'Charisma (von 1-6)',
            'Glück (von 1-6)',
            'Magie (von 0-6)',
            'Resonanz (von 0-6)'
        ]
        let columns = attributes.map(attribute => new Object({
                id: attribute.substring(0, 3),
                data: <EditableText attribute={attribute}
                                    npc={this.props.npc}
                                    approxLineSize={58}
                                    editable={this.props.editable}
                                    editableDisabled={this.props.editableDisabled}/>
            })
        )


        return [{
            id: 0,
            columns: columns
        }]
    }

    render() {
        let state_label = ''

        const relevantAttributes = ['Metatyp', 'Beruf', 'Ethnizität', 'Geschlecht', 'Alter', 'Eigenarten', 'Detailliertes Aussehen']
        const items = [];

        for (const attribute of relevantAttributes) {
            items.push(<li key={attribute}><Text><b>{attribute}:</b> {this.props.npc.attributes[attribute]} </Text>
            </li>);
        }

        return (
            <div>
                {state_label}
                <Card
                    image={{
                        src: image_path(this.props.npc.image_url, this.props.npc.id, this.props.npc.default_image_number),
                        alt: this.props.npc.image_generator_description
                    }}
                    style={{width: 950, margin: 15}}
                    title={(<EditableText style={{width: '630px'}}
                                          attribute='Name'
                                          npc={this.props.npc}
                                          approxLineSize={58}
                                          editable={this.props.editable}
                                          editableDisabled={this.props.editableDisabled}
                    />)}
                    landscape
                >

                    <div>
                        <Blockquote>
                            <Text>
                                <EditableText style={{width: '580px'}}
                                              attribute='Catchphrase'
                                              npc={this.props.npc}
                                              approxLineSize={58}
                                              editable={this.props.editable}
                                              editableDisabled={this.props.editableDisabled}
                                />
                            </Text>
                        </Blockquote>

                        <AttributeList listItemWidth={100}
                                       npc={this.props.npc}
                                       attributes={relevantAttributes}
                                       approxLineSize={58}
                                       editable={this.props.editable}
                                       editableDisabled={this.props.editableDisabled}/>
                    </div>
                    <Table headers={this.tableHeaders()} dataset={this.tableDataset(this.props.npc)}/>


                </Card>
            </div>

        )
    }
}

export default NPCCard;
