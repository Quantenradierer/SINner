import React from "react";
import {Button, FrameBox, Text} from "@arwes/core";



const Header = props => {
    const logged_in = localStorage.getItem('access_token') !== null && localStorage.getItem('refresh_token') !== null
    console.log(logged_in)

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
                <Button style={{display: logged_in ? 'none': 'flex', margin: '0px 15px 0px 15px'}} onClick={() => { window.location.href = '/login' }}>
                    <Text>Login</Text>
                </Button>
                <Button style={{display: logged_in ? 'flex': 'none', margin: '0px 15px 0px 15px'}} onClick={() => { window.location.href = '/logout' }}>
                    <Text>Logout</Text>
                </Button>
            </div>
        </FrameBox>
    )
}

export default Header;
