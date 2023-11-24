import React from "react";
import {Blockquote, Button, Card, FrameLines, FramePentagon, List, Table, Text} from "@arwes/core";
import image_path from "../../image_path";
import is_logged_in from "../../is_loggin_in";
import {Link} from "react-router-dom";
import api from "../../axios";
import i18next from "../../i18n";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";
import ImageGallery from "../image_gallery";
import active_image from "../../active_image";
import Comment from "./comment";


class LocationCard extends React.Component {
    render() {
        let state_label = ''
        let activeImage = active_image(this.props.entity.image_objects) || {}

        const relevantAttributes = ['Typ', 'Aussehen', 'Besonderheiten', 'Hinweise', 'Verfügbarkeit von Sicherheitssystemen', 'Aktuelle Aktionen/Events', 'Gerüchte und Geschichten über die Location']

        return (
            <div>
                {state_label}
                <Card
                    hover
                    image={{
                        src: image_path('locations', activeImage.name),
                        alt: this.props.entity.image_generator_description
                    }}
                    style={{width: 950, margin: 15}}
                    title={<div><EditableText style={{width: '910px'}}
                                          attribute='Name'
                                          entity={this.props.entity}
                                          approxLineSize={58}
                                          editable={this.props.editable}
                                          editableDisabled={this.props.editableDisabled}
                                          check={this.props.check}
                                          setAlternatives={this.props.setAlternatives}

                    /> </div>}
                >

                    <div>
                          <AttributeList listItemWidth={130}
                                       entity={this.props.entity}
                                       attributes={relevantAttributes}
                                       approxLineSize={90}
                                       editable={this.props.editable}
                                       editableDisabled={this.props.editableDisabled}
                                       check={this.props.check}
                                       setAlternatives={this.props.setAlternatives}
                        />
                    </div>

                    <div className={this.props.entity.id? '': 'hidden'}>
                        <a href={"/locations/" + this.props.entity.id + "/gallery"}>
                            <Button>Galerie</Button>
                        </a>
                    </div>
                </Card>
            </div>

        )
    }
}

export default LocationCard;