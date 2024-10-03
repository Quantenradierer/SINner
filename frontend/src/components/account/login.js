import React, {useState} from "react";
import {Button, FrameBox, FrameCorners, FrameLines, FramePentagon, Text} from "@arwes/core";
import api from "../../axios";
import {math} from "polished";
import handleLogin from "../../loader/handle_login";
import {Link} from "react-router-dom";
import i18n from "../../i18n";
import {Helmet} from "react-helmet";


function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [usernameHint, setUsernameHint] = useState('');
    const [passwordHint, setPasswordHint] = useState('');

    const [error, setError] = useState('');

    function errorHandler(error) {
        setPasswordHint(error.response.data.password)
        setUsernameHint(error.response.data.username)
        setError(error.response.data.non_field_errors)
    }

    return (
        <FramePentagon key={error}  style={{maxWidth: 400, width: '100%', margin: 10}}>
            <Helmet>
                <title>{i18n.t(`page_login_title`)}</title>
            </Helmet>
            <form>
                {error && <FramePentagon  palette='secondary'>
                    <Text>{error}</Text>
                </FramePentagon>}
                <div style={{display: 'flex', flexDirection: 'column'}}>
                    <div style={{margin: 5}}>
                        <input type="text" id="username" placeholder="E-Mail" onChange={(e) => setUsername(e.target.value)} value={username}/>
                        {usernameHint && <Text>{usernameHint}</Text>}
                    </div>
                    <div style={{margin: 5}}>
                        <input type="password" id="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} value={password}/>
                        {passwordHint && <Text>{passwordHint}</Text>}
                    </div>
                    <Link style={{}} to={'/register'}>{i18n.t('auth_signup_description')}</Link>
                    <div style={{margin: 5, display: 'flex', flexDirection: 'column'}}>
                        <Button style={{margin: 3}} FrameComponent={FramePentagon} onClick={(event) => { event.preventDefault(); handleLogin(username, password, errorHandler)}}>
                            <Text>Anmelden</Text>
                        </Button>
                    </div>
                </div>
            </form>
        </FramePentagon>
    )
}

export default Login;
