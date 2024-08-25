import React, {useState} from "react";
import {FrameLines, FramePentagon, Text} from "@arwes/core";
import image_path from "../../image_path";
import EditableText from "../editableText";
import AttributeList from "../attribute_list";
import active_image from "../../active_image";
   import { css } from '@emotion/react';
import {Animator} from "@arwes/animation";
import './charDefault.css';
import {Frame} from "@arwes/core/lib/utils/Frame";
import SimpleAttributeList from "../simpleAttributeList";
import AttributeCard from "./attributeCard";
import i18next from "i18next";
import {useEntity} from "../entityProvider";
import Blockquote from "../cyberpunk/blockquote";
import GlitchEffect from "../cyberpunk/glitchEffect";
import {CustomFrame} from "../cyberpunk/CustomFrame";
import imageFrame from "../cyberpunk/imageFrame";
import ImageFrame from "../cyberpunk/imageFrame";





function TabDefault(props) {
    const {entity, _} = useEntity();

    const relevantAttributesMain = ['metatype', 'profession', 'ethnicity', 'gender', 'age',]

    return (
                <div className="container">
                    <Animator animator={{
                        combine: true, manager: 'stagger',
                        duration: {stagger: 250}
                    }}>
                        <div className='left-container'>
                            <div style={{margin: '5px'}}>
                                <ImageFrame/>
                            </div>
                            <FramePentagon style={{margin: '5px', padding: '0px', width: '100%'}} squareSize={35}>
                                <FrameLines hideTopLines={true} style={{padding: 10, margin: 0, width: '100%'}}>
                                    <h3 style={{margin: 0}}><EditableText attributeName="name"/></h3>
                                </FrameLines>
                                <div style={{margin: '7px'}}>
                                    <Blockquote style={{margin: '0px'}}><EditableText attributeName="catchphrase"/></Blockquote>

                                    <hr style={{padding: 0, margin: 0}}/>
                                </div>
                                <SimpleAttributeList
                                    attributes={relevantAttributesMain}
                                />
                            </FramePentagon>
                        </div>
                        <div className='attribute-cards-container'>
                            <div className={'two-cols'}>
                                <div className={'col1'}>
                                    <AttributeCard title={i18next.t('npc_card_title_background')} attributes={['backstory', 'secret', 'experiences']}/>
                                    <AttributeCard title={i18next.t('npc_card_title_social')} attributes={['family', 'contacts']}/>
                                </div>
                                <div className={'col2'}>
                                    <AttributeCard title={i18next.t('npc_card_title_personality')} attributes={['quirks', 'motivations', 'resentments']}/>
                                    <AttributeCard title={i18next.t('npc_card_title_skills_and_traits')} attributes={['strengths', 'weaknesses', 'hobbies_and_interests']}/>
                                </div>
                            </div>
                        </div>
                    </Animator>
                </div>
    );
}

export default TabDefault;
