import React, { useState } from 'react';
import {Button, FrameBox, FrameCorners, FrameLines, FramePentagon, FrameUnderline, Text} from "@arwes/core";
import i18next from "../i18n";
import is_logged_in from "../is_loggin_in";

class MenuItems extends React.Component {
    render() {
        const kind = this.props.kind;
        return (
            <div className="menu-item-container">
                <div className="menu-item-title">
                    <a href={`/${kind}`}>
                        <Text className="neon-text">{i18next.t('menu_' + kind)}</Text>
                    </a>
                </div>

                <div className="menu-submenu">
                    <a href={`/${kind}_prompt`} className="neon-link">
                        <span>Erstellen</span>
                    </a>
                    /
                    <a href={`/${kind}`} className="neon-link">
                        <span>Liste</span>
                    </a>
                    /
                    <a href={`/${kind}/random`} className="neon-link">
                        <span>Zufall</span>
                    </a>

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
                        <a href={`/login`}>
                            <Text className="neon-text">{i18next.t('menu_login')}</Text>
                        </a>
                    </div>
                </div>}
                {!is_logged_in() && false && <div className="menu-item-container">
                    <div className="menu-item-title">
                        <a href={`/register`}>
                            <Text className="neon-text">{i18next.t('menu_register')}</Text>
                        </a>
                    </div>
                </div>}
                {is_logged_in() && <div className="menu-item-container">
                    <div className="menu-item-title">
                        <a href={`/logout`}>
                            <Text className="neon-text">{i18next.t('menu_logout')}</Text>
                        </a>
                    </div>
                </div>}
                <div className="menu-item-container">
                    <div className="menu-item-title">
                        <a href={`/feedback`}>
                            <Text className="neon-text">{i18next.t('menu_feedback')}</Text>
                        </a>
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
