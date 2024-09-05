import React from "react";
import { Blockquote, Button, Card, FrameLines, FramePentagon, List, Table, Text } from "@arwes/core";
import image_path from "../../image_path";
import EditableText from "../editableText";
import active_image from "../../active_image";
import { Link } from "react-router-dom";
import { useEntity } from "../entityProvider";
import DividerAttributeList from "../dividerAttributeList";
import AttributeList from "../attributeList";
import {Animator} from "@arwes/animation";
import ImageFrame from "../cyberpunk/imageFrame";
import {Frame} from "@arwes/core/lib/utils/Frame";
import Comment from "./comment";

const TabDefault = (props) => {
    const {entity, _} = useEntity();
    let state_label = '';
    let activeImage = active_image(entity.image_objects) || {};
    const relevantAttributes = ['type', 'appearance', 'special_features', 'remarks', 'security_systems', 'events', 'rumors_and_stories'];

    let comments = entity?.values?.reviews
    if (comments == undefined || comments.length == 0) {
        return <div/>
    }

    const comment_data = comments || []
    let comments_components = []

    for (let nr = 0; nr < comment_data.length; nr++) {
        comments_components.push(<Blockquote key={nr}><Comment rating={comment_data[nr]['rating']}
                                                               comment={comment_data[nr]['comment']}
                                                               name={comment_data[nr]['name']}/></Blockquote>)
    }

    return (
        <div style={{}}>
            <div style={{margin: '10px 10px 0px 10px'}}>
                <ImageFrame style={{
                    overflow: 'hidden',
                    minHeight: '200px'
                }}/>
            </div>
            <div style={{padding: 5, display: 'flex', flexWrap: 'wrap'}}>
                <div style={{
                    padding: 5,
                    minWidth: '300px',
                    flex: 1,
                    boxSizing: 'border-box'
                }}>
                    <FramePentagon style={{padding: 0}} squareSize={35}>
                        <FrameLines hideTopLines={true} style={{padding: 10, margin: 0, width: '100%'}}>
                            <h3 style={{margin: 0}}>
                                <EditableText attributeName="name"/>
                            </h3>
                        </FrameLines>
                        <div style={{padding: 5}}>
                            <DividerAttributeList attributes={relevantAttributes}/>
                        </div>
                    </FramePentagon>
                </div>
                <div style={{
                    padding: 5,
                    minWidth: '300px',
                    flex: 1,
                    boxSizing: 'border-box'
                }}>
                    <FramePentagon style={{padding: 0}} squareSize={35}>
                        <div style={{padding: 5}}>
                            {comments_components}
                        </div>
                    </FramePentagon>
                </div>
            </div>
        </div>
    );
};

export default TabDefault;