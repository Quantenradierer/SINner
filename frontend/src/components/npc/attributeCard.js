import {FrameHexagon, FramePentagon, Text} from "@arwes/core";
import SimpleAttributeList from "../simpleAttributeList";
import React from "react";
import styled from 'styled-components';

const AttributeCard = ({ title, attributes }) => {
    return (
        <div className={'attribute-card'} style={{padding: '5px'}}>
            <FramePentagon style={{width: '100%', padding: '0px'}} squareSize={35}>
                <div style={{padding: '5px 0px 5px 10px'}}>
                    <h6 style={{margin: 0}}><Text>{title}</Text></h6>
                </div>
                <hr style={{padding: 0, margin: 0, width: '100%'}}/>
                <div>
                    <SimpleAttributeList attributes={attributes}/>
                </div>
            </FramePentagon>
        </div>
    );
}

export default AttributeCard;