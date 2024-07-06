import React from 'react';
import api from "./axios";


const UserContext = React.createContext();
class UserProvider extends React.Component {
    state = {
        user: null,
        error: null,
    };
    componentDidMount() {
        //this.fetchUserData();
    }

    fetchUserData = async () => {
        try {
            const response = await api.get('/api/npc_creator/collections');
            this.setState({ user: response.data });
        } catch (error) {
            console.error('Error fetching user data: ', error);
            this.setState({ error: error.toString() });
        }
    }

    render() {
        return (
            <UserContext.Provider value={this.state.user}>
                {this.props.children}
            </UserContext.Provider>
        );
    }
}

export default UserProvider;