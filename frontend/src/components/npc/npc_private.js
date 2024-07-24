import React from "react";
import {FramePentagon, List, Text} from "@arwes/core";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";

class NPCPrivate extends React.Component {

    render() {
        const relevantAttributes = ['backstory', 'experiences', 'resentments', 'motivations', 'goals', 'hobbies_and_interests',
            'family', 'contacts', 'strengths', 'weaknesses', 'secret']

        return (
            <FramePentagon>
                <AttributeList listItemWidth={105} entity={this.props.entity} attributes={relevantAttributes} approxLineSize={100} editable={this.props.editable} check={this.props.check}
                                       editableDisabled={this.props.editableDisabled} setAlternatives={this.props.setAlternatives}/>
            </FramePentagon>
        )
    }
}

export default NPCPrivate;
