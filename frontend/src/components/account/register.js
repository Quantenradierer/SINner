import React, {useState} from "react";
import {Button, FrameCorners, FramePentagon, Text} from "@arwes/core";
import api from "../../axios";
import {math} from "polished";
import handleLogin from "../../loader/handle_login";
import i18n from "../../i18n";




function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [repassword, setRepassword] = useState('');
    const [usernameHint, setUsernameHint] = useState('');
    const [emailHint, setEmailHint] = useState('');
    const [passwordHint, setPasswordHint] = useState('');
    const [repasswordHint, setRepasswordHint] = useState('');

    const [error, setError] = useState('');

    function handleRegister(event) {
        event.preventDefault()
        api.defaults.xsrfCookieName = 'csrftoken'
        api.defaults.xsrfHeaderName = 'X-CSRFToken'

        const url = `auth/users/`;
        api.post(url, {
            username: username,
            email: username,
            password: password,
            re_password: repassword
        })
        .then((response) => {
            handleLogin(username, password)
        })
        .catch((error) => {
            setUsernameHint(error.response.data.username)
            setEmailHint(error.response.data.email)
            setPasswordHint(error.response.data.password)
            setRepasswordHint(error.response.data.re_password)
            setError(error.response.data.non_field_errors)
        });

    }

    const errorColor = '#3c2021'
    return (
        <FramePentagon key={error} style={{maxWidth: 400}}>
            <form>
                <div style={{display: 'flex', flexDirection: 'column'}}>
                    <div style={{margin: 5}}>
                        <input type="text" id="username" placeholder="E-Mail" onChange={(e) => setUsername(e.target.value)} value={username} style={{backgroundColor: emailHint? errorColor: ''}}/>
                        {usernameHint && <div>{usernameHint}</div>}
                        {emailHint && <div><text palette='secondary'>{emailHint}</text></div>}
                    </div>
                    <div style={{margin: 5}}>
                        <input type="password" id="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} value={password}  style={{backgroundColor: passwordHint? errorColor: ''}}/>
                        {passwordHint && <div><text palette='secondary'>{passwordHint}</text></div>}
                    </div>
                    <div style={{margin: 5}}>
                        <input type="password" id="repassword" placeholder="Password (wiederholt)" onChange={(e) => setRepassword(e.target.value)} value={repassword} style={{backgroundColor: repasswordHint? errorColor: ''}}/>
                        {repasswordHint && <div>{repasswordHint}</div>}
                    </div>
                    <div style={{margin: 5, display: 'flex', flexDirection: 'column'}}>
                        <Button style={{margin: 3}} FrameComponent={FrameCorners} onClick={handleRegister}>
                            <Text>{i18n.t('auth_signup')}</Text>
                        </Button>
                    </div>
                    {error && <FramePentagon  palette='secondary'>
                    <Text>{error}</Text>
                </FramePentagon>}
                </div>
            </form>
        </FramePentagon>
    )
}

export default Register;
