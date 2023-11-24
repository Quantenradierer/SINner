import React from "react";
import {FramePentagon, List, Text} from "@arwes/core";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";

class NPCPrivate extends React.Component {

    render() {
        const relevantAttributes = ['Hintergrundgeschichte', 'Erfahrungen', 'Ressentiments', 'Motivationen', 'Ziele', 'Hobbys und Interessen',
            'Familie', 'Kontakte']

        return (
            <FramePentagon style={{width: 950, margin: 15}}>
                <AttributeList listItemWidth={105} entity={this.props.entity} attributes={relevantAttributes} approxLineSize={100} editable={this.props.editable} check={this.props.check}
                                       editableDisabled={this.props.editableDisabled} setAlternatives={this.props.setAlternatives}/>
            </FramePentagon>
        )
    }
}

export default NPCPrivate;
