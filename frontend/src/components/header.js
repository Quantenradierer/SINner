import React, { useState } from 'react';
import {Button, FrameBox, FrameCorners, FrameLines, FramePentagon, FrameUnderline, Text} from "@arwes/core";
import i18next from "../i18n";
import is_logged_in from "../is_loggin_in";
import { Link } from "react-router-dom";

class MenuItems extends React.Component {
    render() {
        const kind = this.props.kind;
        return (
            <div className="menu-item-container">
                <div className="menu-item-title">
                    <Link to={`/${kind}`}>
                        <Text className="neon-text">{i18next.t('menu_' + kind)}</Text>
                    </Link>
                </div>

                <div className="menu-submenu">
                    <Link to={`/${kind}_prompt`} className="neon-link">
                        <span>Erstellen</span>
                    </Link>
                    /
                    <Link to={`/${kind}`} className="neon-link">
                        <span>Liste</span>
                    </Link>
                    /
                    <Link to={`/${kind}/random`} className="neon-link">
                        <span>Zufall</span>
                    </Link>
                </div>
            </div>
        );
    }
}




class Menu extends React.Component {
    render() {
        let custom_prompts = localStorage.getItem('custom_prompt') === 'true';


        return (
            <div className="menu-container">
                <MenuItems kind={'npcs'}/>
                <MenuItems kind={'locations'}/>
                {custom_prompts && <MenuItems kind='customs'/>}
                {!is_logged_in() && false && <div className="menu-item-container">
                    <div className="menu-item-title">
                        <Link to={`/login`}>
                            <Text className="neon-text">{i18next.t('menu_login')}</Text>
                        </Link>
                    </div>
                </div>}
                {!is_logged_in() && false && <div className="menu-item-container">
                    <div className="menu-item-title">
                        <Link to={`/register`}>
                            <Text className="neon-text">{i18next.t('menu_register')}</Text>
                        </Link>
                    </div>
                </div>}
                {is_logged_in() && <div className="menu-item-container">
                    <div className="menu-item-title">
                        <Link to={`/logout`}>
                            <Text className="neon-text">{i18next.t('menu_logout')}</Text>
                        </Link>
                    </div>
                </div>}
                <div className="menu-item-container">
                    <div className="menu-item-title">
                        <Link to={`/feedback`}>
                            <Text className="neon-text">{i18next.t('menu_feedback')}</Text>
                        </Link>
                    </div>
                </div>
            </div>
        );
    }
}


const Header = props => {
    return (
        <FrameBox style={{width: '100%'}}>
            <Menu/>
        </FrameBox>
    )
}

export default Header;
