import React, {useEffect, useRef, useState} from "react";
import {Link} from "react-router-dom";
import {Text, Button, FrameBox, FrameCorners, FrameHexagon, FrameLines, FramePentagon, FrameUnderline} from "@arwes/core";
import is_logged_in from "./is_loggin_in";
import i18next from "./i18n";
import GlitchEffect from "./components/cyberpunk/glitchEffect";
import Header from "./components/header";
import Footer from "./components/footer";




const MenuLink = props => {
    return (
        <Link to={props.to}>
            <FrameLines hideTopLines={true}
                style={{width: 200, margin: '5px', padding: '5px'}}>{props.children}</FrameLines>
        </Link>
    );
}

const MenuHeader = props => {
    return (
        <div style={{width: '100%', maxWidth: 320, textAlign: 'center', margin: '10px'}}>
            <FrameLines>

                <Link to={props.to}>
                    <Text><h3 style={{margin: '0 0 15px 0'}}>{props.headerTitle}</h3></Text>
                </Link>
                <div style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                }}>
                    <h4>
                        {props.children}
                    </h4>
                </div>
            </FrameLines>

        </div>
    )
}



const Navigation = props => {
    let custom_prompts = localStorage.getItem('custom_prompt') === 'true';
    scroll(0, 0)
    return (
        <div style={{
            position: 'absolute',
            width: '100%',
            height: '100% - 64px',
            top: 70,
            left: 0,
            right: 0,
            bottom: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            zIndex: 100,

        }}>
            <MenuHeader to="/npcs/" headerTitle={'NPC'}>
                <MenuLink to="/npcs/create">Erstellen</MenuLink>
                <MenuLink to="/npcs/">Liste</MenuLink>
                <MenuLink to="/npcs/random">Zufall</MenuLink>
            </MenuHeader>


            <MenuHeader to="/locations" headerTitle={'Location'}>
                <MenuLink to="/locations/create">Erstellen</MenuLink>
                <MenuLink to="/locations/">Liste</MenuLink>
                <MenuLink to="/locations/random">Zufall</MenuLink>
            </MenuHeader>

            {custom_prompts && <MenuHeader to="/customs" headerTitle={'Customs'}>
                <MenuLink to="/customs/create">Erstellen</MenuLink>
                <MenuLink to="/customs/">Liste</MenuLink>
                <MenuLink to="/customs/random">Zufall</MenuLink>
            </MenuHeader>}

            <MenuHeader headerTitle={'Sonstiges'}>
                {!is_logged_in() && <MenuLink to="/login">{i18next.t('menu_login')}</MenuLink>}
                {is_logged_in() && <MenuLink to="/login">{i18next.t('menu_logout')}</MenuLink>}
                <MenuLink to="/impressum">{i18next.t('menu_impressum')}</MenuLink>
                <MenuLink to="/feedback">{i18next.t('menu_feedback')}</MenuLink>
            </MenuHeader>
        </div>
    )
}

export default Navigation;


