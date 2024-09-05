import {FrameHexagon, FrameLines, FramePentagon, Text} from "@arwes/core";
import DividerAttributeList from "../dividerAttributeList";
import React from "react";
import styled from 'styled-components';

const AttributeCard = ({ title, attributes }) => {
    return (
        <div className='attribute-card' style={{padding: '5px'}}>
            <FramePentagon style={{width: '100%', padding: '0px 0px 5px 0px'}} squareSize={35}>
                <FrameLines hideTopLines  style={{width: '100%', padding: '5px 0px 5px 10px'}}>
                    <h6 style={{margin: 0}}><Text>{title}</Text></h6>
                </FrameLines>
                <div style={{padding: 5}}>
                    <DividerAttributeList attributes={attributes}/>
                </div>
            </FramePentagon>
        </div>
    );
}

export default AttributeCard;