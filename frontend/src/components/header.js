import React from 'react';
import {Button, FrameBox, FrameCorners, FrameHexagon, FrameLines, Text} from "@arwes/core";
import GlitchEffect from "./cyberpunk/glitchEffect";
import { ReactComponent as BurgerMenu } from '../icons/burger.svg';
import {Link, useLocation, useNavigate} from 'react-router-dom';
import is_logged_in from "../is_loggin_in";
import {ProfileButton} from "../icons/profileButton";

const Header = (props) => {
    const navigate = useNavigate();
    const location = useLocation();

    const handleClick = (event) => {
        event.preventDefault();
        navigate(-1);
    }

    const is_navi = location.pathname === '/navi'

    return (
        <div className="no-print">
            <div style={{position: 'fixed', top: 0, left: 0, width: '100%', zIndex: 1000}}>
                <FrameLines style={{width: '100%', paddingTop: 5, paddingBottom: 0}} hideTopLines={true}>
                    <div style={{display: 'flex', justifyContent: 'center'}}>
                        <div style={{
                            display: 'flex',
                            maxWidth: 1380,
                            width: '100%',
                            alignItems: 'center',
                            position: 'relative'
                        }}>
                            <div style={{
                                position: 'absolute',
                                left: '50%',
                                transform: 'translateX(-50%)',
                                textAlign: 'center'
                            }}>
                                <Link to={'/'}>
                                    <h1 style={{padding: 0, margin: 0}}><GlitchEffect>SCHATTENAKTE</GlitchEffect></h1>
                                </Link>
                            </div>

                            <div style={{
                                display: 'flex',
                                flexDirection: 'row',
                                justifyContent: 'flex-end',
                                flexGrow: 1
                            }}>
                                <div style={{
                                    display: 'flex',
                                    flexDirection: 'column',
                                    justifyContent: 'center',
                                    marginRight: 15
                                }}>
                                    {!is_logged_in() && <Link to={'/login'}><FrameLines style={{margin: 0, padding: 5}}><Text>Anmelden</Text></FrameLines></Link>}
                                    {is_logged_in() && <ProfileButton/>}
                                </div>
                                <div>
                                    {is_navi ?
                                        <a href="#" onClick={handleClick}
                                           style={{display: 'flex', flexDirection: 'column', justifyContent: 'center'}}><BurgerMenu/></a> :
                                        <Link to={'navi'} style={{
                                            display: 'flex',
                                            flexDirection: 'column',
                                            justifyContent: 'center'
                                        }}><BurgerMenu/></Link>}
                                </div>
                            </div>
                        </div>
                    </div>
                </FrameLines>
            </div>
            <div style={{height: 55}}></div>
        </div>
    );
};

export default Header;