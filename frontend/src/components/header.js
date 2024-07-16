import React from 'react';
import { Button, FrameLines } from "@arwes/core";
import GlitchEffect from "./cyberpunk/glitchEffect";
import { ReactComponent as BurgerMenu } from '../icons/burger.svg';
import {Link, useLocation, useNavigate} from 'react-router-dom';

const Header = (props) => {
    const navigate = useNavigate();
    const location = useLocation();

    const handleClick = (event) => {
        event.preventDefault();
        navigate(-1);
    }

    const is_navi = location.pathname === '/navi'

    return (
        <div>
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
                            <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'center'}}>
                                {is_navi && <a href="#" onClick={handleClick}>
                                    <h1 style={{margin: 0}}>
                                        <GlitchEffect>SCHATTENAKTE</GlitchEffect>
                                    </h1>
                                </a>}
                                {!is_navi && <Link to={'navi'}><h1
                                    style={{margin: 0}}>
                                    <GlitchEffect>SCHATTENAKTE</GlitchEffect>
                                </h1></Link>}
                            </div>
                            <div>
                                {is_navi && <a href="#" onClick={handleClick} style={{display: 'flex', flexDirection: 'column', justifyContent: 'center'}}><BurgerMenu/></a>}
                                {!is_navi && <Link to={'navi'} style={{display: 'flex', flexDirection: 'column', justifyContent: 'center'}}><BurgerMenu/></Link>}
                            </div>
                        </div>
                    </div>
                </FrameLines>
            </div>
            <div style={{height: 80}}></div>
        </div>
    );
};

export default Header;