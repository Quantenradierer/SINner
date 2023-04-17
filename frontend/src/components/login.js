import React from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, Text} from "@arwes/core";
import api from "../axios";


class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {username: '', password: ''};

        this.handleLogin = this.handleLogin.bind(this);
        this.handleUsernameChange = this.handleUsernameChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
    }

    async handleLogin(event) {
        event.preventDefault();

        const user = {
            username: this.state.username,
            password: this.state.password
        };
        const {data} = await api.post('token/',
            user, {
                headers:
                    {'Content-Type': 'application/json'}},
                {withCredentials: true}
        );

        localStorage.clear();
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);
        api.defaults.headers.common['Authorization'] = `Bearer ${data['access']}`;
        window.location.href = '/'
    }

    handleUsernameChange(event) {
        this.setState({username: event.target.value});
    }

    handlePasswordChange(event) {
        this.setState({password: event.target.value});
    }

    render() {
        return (
            <FramePentagon>
                <form>
                    <div style={{display: 'flex', flexDirection: 'column'}}>
                        <div style={{margin: 5}}>
                            <input type="text" id="username" placeholder="Name" onChange={this.handleUsernameChange}/>
                        </div>
                        <div style={{margin: 5}}>
                            <input type="password" id="password" placeholder="Password"
                                   onChange={this.handlePasswordChange}/>
                        </div>
                        <div style={{margin: 5, display: 'flex', flexDirection: 'column'}}>
                            <Button style={{margin: 3}} FrameComponent={FrameCorners} onClick={this.handleLogin}>
                                <Text>Login</Text>
                            </Button>
                        </div>
                    </div>
                </form>
            </FramePentagon>
        )
    }
}

export default Login;
