import React, { useEffect, useState } from 'react';
import {Button, FrameLines} from "@arwes/core";
import GlitchEffect from "./cyberpunk/glitchEffect";
import { ReactComponent as BurgerMenu } from '../icons/burger.svg';
import {Link} from "react-router-dom";



function getScrollbarWidth() {
    const outer = document.createElement("div");
    outer.style.visibility = "hidden";
    outer.style.width = "100px";
    outer.style.msOverflowStyle = "scrollbar";

    document.body.appendChild(outer);

    const widthNoScroll = outer.offsetWidth;

    outer.style.overflow = "scroll";

    const inner = document.createElement("div");
    inner.style.width = "100%";
    outer.appendChild(inner);

    const widthWithScroll = inner.offsetWidth;

    outer.parentNode.removeChild(outer);

    return widthNoScroll - widthWithScroll;
}

function isScrollbarPresent() {
    return document.body.scrollHeight > document.body.clientHeight;
}

const Header = props => {
    const [scrollbarWidth, setScrollbarWidth] = useState(getScrollbarWidth());


    return <div>
        <div style={{position: 'fixed', top: 0, left: 0, width: '100%', zIndex: 1000}}>
            <FrameLines style={{width: '100%'}} hideTopLines={true}>
                <div style={{display: 'flex', justifyContent: 'center'}}>

                    <div style={{
                        display: 'flex',
                        maxWidth: 1380,
                        width: '100%',
                        flexDirection: 'row',
                        justifyContent: 'space-between'
                    }}>
                        <div style={{width: 40}}></div>
                        <h1 style={{margin: 0, display: 'flex', flexDirection: 'column', justifyContent: 'center'}}>
                            <GlitchEffect>SCHATTENAKTE</GlitchEffect>
                        </h1>
                        <Link><div onClick={props.toggleBurger}><BurgerMenu/></div></Link>
                    </div>

                </div>
            </FrameLines>
        </div>
        <div style={{height: 80}}></div>
    </div>
}

export default Header;
