import React from "react";
import {Blockquote, Button, Card, FrameLines, FramePentagon, List, Table, Text} from "@arwes/core";
import image_path from "../../image_path";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";
import active_image from "../../active_image";
import useRefreshEntityCard from "../use_refresh_entity_card";
import { Link } from "react-router-dom";


class LocationCard extends React.Component {
    render() {
        let state_label = ''
        let activeImage = active_image(this.props.entity.image_objects) || {}

        const relevantAttributes = ['type', 'appearance', 'special_features', 'remarks', 'security_systems', 'events', 'rumors_and_stories']

        return (
            <div>
                {state_label}
                <Card
                    hover
                    image={{
                        src: image_path('locations', activeImage.name),
                        alt: this.props.entity.image_generator_description
                    }}
                    title={<div><EditableText style={{width: '910px'}}
                                          attribute='name'
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
                </Card>
            </div>

        )
    }
}

export default LocationCard;