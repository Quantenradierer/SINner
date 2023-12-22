import React, {useState} from "react";
import {Button, FrameCorners, FramePentagon, Text} from "@arwes/core";
import api from "../../axios";
import {math} from "polished";




function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [repassword, setRepassword] = useState('');
    const [usernameHint, setUsernameHint] = useState('');
    const [emailHint, setEmailHint] = useState('');
    const [passwordHint, setPasswordHint] = useState('');
    const [repasswordHint, setRepasswordHint] = useState('');

    const [error, setError] = useState('');

    function handleLogin(event) {
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
            console.log(response)

        })
        .catch((exception) => {
            console.log(exception)
            setUsernameHint(exception.response.data.username)
            setEmailHint(exception.response.data.email)
            setPasswordHint(exception.response.data.password)
            setRepasswordHint(exception.response.data.re_password)
            setError(exception.response.data.non_field_errors)
        });

    }

    return (
        <FramePentagon key={error}>
            <form>
                {error && <FramePentagon  palette='secondary'>
                    <Text>{error}</Text>
                </FramePentagon>}
                <div style={{display: 'flex', flexDirection: 'column'}}>
                    <div style={{margin: 5}}>
                        <input type="text" id="username" placeholder="E-Mail" onChange={(e) => setUsername(e.target.value)} value={username}/>
                        {usernameHint && <div>{usernameHint}</div>}
                        {emailHint && <div>{emailHint}</div>}
                    </div>
                    <div style={{margin: 5}}>
                        <input type="password" id="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} value={password}/>
                        {passwordHint && <div>{passwordHint}</div>}
                    </div>
                    <div style={{margin: 5}}>
                        <input type="password" id="repassword" placeholder="Password (wiederholt)" onChange={(e) => setRepassword(e.target.value)} value={repassword}/>
                        {repasswordHint && <div>{repasswordHint}</div>}
                    </div>
                    <div style={{margin: 5, display: 'flex', flexDirection: 'column'}}>
                        <Button style={{margin: 3}} FrameComponent={FrameCorners} onClick={handleLogin}>
                            <Text>Register</Text>
                        </Button>
                    </div>
                </div>
            </form>
        </FramePentagon>
    )
}

export default Register;
