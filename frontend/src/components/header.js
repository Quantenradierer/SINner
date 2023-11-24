import React, { useState } from 'react';
import {Button, FrameBox, FrameCorners, FrameLines, FramePentagon, FrameUnderline, Text} from "@arwes/core";
import i18next from "../i18n";

class MenuItems extends React.Component {
    render() {
        const kind = this.props.kind;
        return (
            <div className='menuItem'>
                <a href={`/${kind}`}><FrameLines style={{minWidth: '140px', textAlign: 'center'}}>{i18next.t('menu_' + kind)}</FrameLines></a>
                <div className='subMenu'>
                    <a href={`/${kind}`}>
                        <div style={{margin: '10px 5px 0px 5px'}}>Liste</div>
                    </a>
                    <a href={`/${kind}_prompt`}>
                        <div style={{margin: '10px 5px 0px 5px'}}>Erstellen</div>
                    </a>
                    <a href={`/${kind}/random`}>
                        <div style={{margin: '10px 5px 0px 5px'}}>Zufall</div>
                    </a>
                </div>

            </div>
        );
    }
}

class Menu extends React.Component {
    render() {
        return (
            <div className='menu'>
                <MenuItems kind={'npcs'}/>
                <MenuItems kind={'locations'}/>
                <MenuItems kind={'critters'}/>
                <MenuItems kind={'vehicles'}/>
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
