import React, {useState} from "react";
import {Button, FrameCorners, FramePentagon, Text} from "@arwes/core";
import api from "../../axios";
import {math} from "polished";




function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [usernameHint, setUsernameHint] = useState('');
    const [passwordHint, setPasswordHint] = useState('');

    const [error, setError] = useState('');

    function handleLogin(event) {
        event.preventDefault()
        api.defaults.xsrfCookieName = 'csrftoken'
        api.defaults.xsrfHeaderName = 'X-CSRFToken'

        const url = `http://localhost:8000/auth/token/login/`;
        api.post(url, {
            username: username,
            password: password
        })
        .then((response) => {
            console.log(response.data.auth_token)
        })
        .catch((exception) => {
            console.log(exception)
            setPasswordHint(exception.response.data.password)
            setUsernameHint(exception.response.data.username)
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
                        {usernameHint && <Text>{usernameHint}</Text>}
                    </div>
                    <div style={{margin: 5}}>
                        <input type="password" id="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} value={password}/>
                        {passwordHint && <Text>{passwordHint}</Text>}
                    </div>
                    <div style={{margin: 5, display: 'flex', flexDirection: 'column'}}>
                        <Button style={{margin: 3}} FrameComponent={FrameCorners} onClick={handleLogin}>
                            <Text>Login</Text>
                        </Button>
                    </div>
                </div>
            </form>
        </FramePentagon>
    )
}

export default Login;
