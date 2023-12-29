import React from "react";
import {Blockquote, Button, Card, FrameLines, List, Table, Text} from "@arwes/core";
import image_path from "../../image_path";
import is_logged_in from "../../is_loggin_in";
import {Link} from "react-router-dom";
import api from "../../axios";
import i18next from "../../i18n";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";
import ImageGallery from "../image_gallery";
import active_image from "../../active_image";
import {AddToListMenu} from "../scene/add_to_list_menu";


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
                data: <div><EditableText attribute={attribute}
                                         entity={this.props.entity}
                                         approxLineSize={58}
                                         editable={this.props.editable}
                                         editableDisabled={this.props.editableDisabled}
                                         check={this.props.check}
                                         setAlternatives={this.props.setAlternatives}
                /></div>
            })
        )


        return [{
            id: 0,
            columns: columns
        }]
    }

    render() {
        let state_label = ''
        let activeImage = active_image(this.props.entity.image_objects) || {}

        const relevantAttributes = ['Metatyp', 'Beruf', 'Ethnizität', 'Geschlecht', 'Alter', 'Eigenarten', 'Detailliertes Aussehen']
        return (
            <div>
                {state_label}
                <Card
                    image={{
                        src: image_path('npcs', activeImage.name),
                        alt: this.props.entity.image_generator_description
                    }}
                    style={{width: 950, margin: 15}}
                    title={<div style={{display: 'flex', flexDirection: 'row', justifyContent: 'space-between'}}>
                        <div>
                            <EditableText style={{width: '630px'}}
                                          attribute='Name'
                                          entity={this.props.entity}
                                          approxLineSize={58}
                                          editable={this.props.editable}
                                          editableDisabled={this.props.editableDisabled}
                                          check={this.props.check}
                                          setAlternatives={this.props.setAlternatives}

                            /></div>
                        <div>
                            <AddToListMenu show={!this.props.editable} entity_id={this.props.entity.id}/></div>
                    </div>}
                    landscape
                >

                    <div>
                        <Blockquote>
                            <Text>
                                <div>
                                    <EditableText style={{margin: '1 0 0 0', width: '580px'}}
                                                  attribute='Catchphrase'
                                                  entity={this.props.entity}
                                                  approxLineSize={58}
                                                  editable={this.props.editable}
                                                  editableDisabled={this.props.editableDisabled}
                                                  check={this.props.check}
                                                  setAlternatives={this.props.setAlternatives}
                                    /></div>
                            </Text>
                        </Blockquote>

                        <AttributeList listItemWidth={100}
                                       entity={this.props.entity}
                                       attributes={relevantAttributes}
                                       approxLineSize={58}
                                       editable={this.props.editable}
                                       editableDisabled={this.props.editableDisabled}
                                       check={this.props.check}
                                       setAlternatives={this.props.setAlternatives}
                        />
                    </div>

                    <Table headers={this.tableHeaders()} dataset={this.tableDataset(this.props.entity)}/>

                    <div className={this.props.entity.id ? '' : 'hidden'}>
                        <a href={"/npcs/" + this.props.entity.id + "/gallery"}>
                            <Button>Galerie</Button>
                        </a>
                    </div>
                </Card>
            </div>

        )
    }
}

export default NPCCard;
