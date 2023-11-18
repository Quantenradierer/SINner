import {FramePentagon, Text} from "@arwes/core";
import React from "react";
import NPCComplete from "./location/location_complete";

const Warning = props => {
    return (<div key='error'  style={{width: 950, margin: 15}}>
                <FramePentagon
                    style={{margin: '15px 0px 15px 0px', display: 'flex'}}
                    palette='secondary'
                    lineWidth={1}
                >
                    <Text>{props.text}</Text>
                </FramePentagon>
            </div>)
}


export default Warning;