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
        <Link to={props.to} onClick={() => {props.setShow(false) }}>
            <FrameLines hideTopLines={true}
                style={{width: 200, margin: '5px', padding: '5px'}}>{props.children}</FrameLines>
        </Link>
    );
}

const MenuHeader = props => {
    return (
        <div style={{width: '100%', maxWidth: 320, textAlign: 'center', margin: '10px'}}>
            <FrameLines>

                <Link to={props.to} onClick={() => {
                    props.setShow(false)
                }}>
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

    const [show, setShow] = useState(false);

    const toggleShow = () => {
        setShow(!show);
    }

    const header = <Header key='header' toggleBurger={toggleShow}/>

    let nav = props.children
    if (show) {
        scroll(0, 0);
        nav = (
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
                zIndex: 1000,

            }}>
                <MenuHeader setShow={setShow} to="/npcs/" headerTitle={'NPC'}>
                    <MenuLink setShow={setShow} to="/npcs/create">Erstellen</MenuLink>
                    <MenuLink setShow={setShow} to="/npcs/">Liste</MenuLink>
                    <MenuLink setShow={setShow} to="/npcs/random">Zufall</MenuLink>
                </MenuHeader>


                <MenuHeader setShow={setShow} to="locations" headerTitle={'Location'}>
                    <MenuLink setShow={setShow} to="/locations/create">Erstellen</MenuLink>
                    <MenuLink setShow={setShow} to="/locations/">Liste</MenuLink>
                    <MenuLink setShow={setShow} to="/locations/random">Zufall</MenuLink>
                </MenuHeader>

                <MenuHeader setShow={setShow} headerTitle={'Sonstiges'}>
                    {!is_logged_in() && <MenuLink setShow={setShow} to="/login">{i18next.t('menu_login')}</MenuLink>}
                    {is_logged_in() && <MenuLink setShow={setShow} to="/login">{i18next.t('menu_logout')}</MenuLink>}
                    <MenuLink setShow={setShow} to="/impressum">{i18next.t('menu_impressum')}</MenuLink>
                    <MenuLink setShow={setShow} to="/feedback">{i18next.t('menu_feedback')}</MenuLink>
                </MenuHeader>
            </div>
        )
    }

     return <div>
            {header}
            {nav}
         <Footer/>
        </div>
}

export default Navigation;


