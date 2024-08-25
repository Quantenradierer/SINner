import {FrameBox, FrameHexagon, FrameLines, FramePentagon, FrameUnderline, Text} from "@arwes/core";
import React from "react";

const Warning = props => {
    return (<div key='error'  style={{width: '100%', padding: 0}}>
                <FrameBox
                    style={{display: 'flex', margin: '0px 0px 15px 0px'}}
                    palette='secondary'
                    lineWidth={1}
                >
                    <Text>{props.text}</Text>
                </FrameBox>
            </div>)
}


export default Warning;