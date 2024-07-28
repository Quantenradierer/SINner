import React, {useState} from "react";
import {Blockquote, Button, Card, FrameBox, FrameHexagon, FrameLines, FramePentagon, Text} from "@arwes/core";
import image_path from "../../image_path";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";
import active_image from "../../active_image";
   import { css } from '@emotion/react';
import {Animator} from "@arwes/animation";
import './charDefault.css';
import {Frame} from "@arwes/core/lib/utils/Frame";
import SimpleAttributeList from "../simpleAttributeList";

function charDefault(props) {
    const entity = props.entity
    let activeImage = active_image(entity.image_objects) || {}

    const relevantAttributesMain = ['metatype', 'profession', 'ethnicity', 'gender', 'age',]
    const relevantAttributesHistory = ['backstory', 'experiences', 'family', 'resentments', 'secret']
    const relevantAttributesActivities = ['quirks', 'motivations', 'goals', 'hobbies_and_interests', 'contacts', 'strengths', 'weaknesses']


    return (
        <FramePentagon style={{padding: 0, margin: 0}}>
            <div style={{width: '100%'}}>
                <FrameLines hideTopLines={true} style={{padding: 10, margin: 0, width: '100%'}}>
                    <h3 style={{margin: 0}}><Text>{entity.values['name']}</Text></h3>
            </FrameLines>
            </div>
            <div className="container">
                <Animator animator={{
                    combine: true, manager: 'stagger',
                    duration: {stagger: 250}
                }}>
                    <div className='left-container'>
                        <div style={{margin: '5px'}}>
                            <div>
                                <div style={{
                                    maxWidth: '600px',
                                    maxHeight: '400px',
                                    overflow: 'hidden'
                                }}>
                                    <a href={image_path('npcs', activeImage.name)} target="_blank">
                                    <img className='growing-img'
                                        src={image_path('npcs', activeImage.name)}
                                        alt={entity.image_generator_description}
                                        style={{
                                            objectFit: 'cover',
                                            objectPosition: 'center',
                                        }}
                                    />
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div style={{margin: '5px'}}>
                            <FramePentagon style={{margin: 0, padding: 0, width: '100%'}}>
                                <SimpleAttributeList
                                    entity={entity}
                                    attributes={relevantAttributesMain}
                                />
                            </FramePentagon></div>

                    </div>
                    <div className='right-container'>
                        <div style={{margin: '5px'}}>
                            <FramePentagon style={{margin: 0, padding: 0}}>
                                <SimpleAttributeList
                                    entity={props.entity}
                                    attributes={relevantAttributesHistory}
                                />
                            </FramePentagon>
                        </div>
                        <div style={{height: '1px'}}></div>
                        <div style={{margin: '5px'}}>
                            <FramePentagon style={{margin: 0, padding: 0}}>
                                <SimpleAttributeList
                                    entity={props.entity}
                                    attributes={relevantAttributesActivities}
                                />
                            </FramePentagon>
                        </div>
                    </div>
                </Animator>

            </div>
        </FramePentagon>
    );
}

export default charDefault;
