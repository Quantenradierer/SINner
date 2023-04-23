import React from "react";
import {Button, FrameBox, Text} from "@arwes/core";
import is_loggin_in from "../is_loggin_in";



const Header = props => {
    return (
        <FrameBox style={{width: '100%'}}>
            <div style={{justifyContent: 'center', display: 'flex'}}>
                <Button style={{display: 'flex', margin: '0px 15px 0px 15px'}} onClick={() => { window.location.href = '/npcs/' }}>
                    <Text>NPC Liste</Text>
                </Button>
                <Button style={{display: 'flex', margin: '0px 15px 0px 15px'}} onClick={() => { window.location.href = '/npcs/random' }}>
                    <Text>Zufälliger NPC</Text>
                </Button>
                <Button style={{display: 'flex', margin: '0px 15px 0px 15px'}} onClick={() => { window.location.href = '/prompt' }}>
                    <Text>NPC Erstellen</Text>
                </Button>
                <Button style={{display: is_loggin_in() ? 'none': 'none', margin: '0px 15px 0px 15px'}} onClick={() => { window.location.href = '/login' }}>
                    <Text>Login</Text>
                </Button>
                <Button style={{display: is_loggin_in() ? 'flex': 'none', margin: '0px 15px 0px 15px'}} onClick={() => { window.location.href = '/logout' }}>
                    <Text>Logout</Text>
                </Button>
            </div>
        </FrameBox>
    )
}

export default Header;
