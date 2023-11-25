import React, { useState } from 'react';
import {Button, FrameBox, FrameCorners, FrameLines, FramePentagon, FrameUnderline, Text} from "@arwes/core";
import i18next from "../i18n";

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
                    <a href={`/${kind}`} className="neon-link">
                        <span>Liste</span>
                    </a>
                    /
                    <a href={`/${kind}_prompt`} className="neon-link">
                        <span>Erstellen</span>
                    </a>/
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
        return (
            <div className="menu-container">
                <MenuItems kind={'npcs'}/>
                <MenuItems kind={'locations'}/>
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
