import React from "react";
import {Button, FrameBox, Text} from "@arwes/core";



const Header = props => {
    return (
        <FrameBox style={{width: '100%'}}>
            <div style={{justifyContent: 'center', display: 'flex'}}>
                <Button style={{width: 200}} onClick={() => { window.location.href = '/npcs' }}>
                    <Text>NPC Liste</Text>
                </Button>
                <div style={{width: 50}}/>
                <Button style={{width: 200}} onClick={() => { window.location.href = '/npcs/random' }}>
                    <Text>Zufälliger NPC</Text>
                </Button>
                <div style={{width: 50}}/>
                <Button style={{width: 200}} onClick={() => { window.location.href = '/prompt' }}>
                    <Text>NPC Erstellen</Text>
                </Button>
            </div>
        </FrameBox>
    )
}

export default Header;
