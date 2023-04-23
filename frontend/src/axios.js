import axios from "axios";
import {API_SERVER} from "./config";

const api = axios.create({
    baseURL: API_SERVER
});

api.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`;


let refresh = false;
api.interceptors.response.use(resp => resp, async error => {
    if (error.response.status === 401 && !refresh) {
        refresh = true;
        const response = await
            api.post('token/refresh/', {
                refresh: localStorage.getItem('refresh_token')
            }, {
                headers:
                    {'Content-Type': 'application/json'}
            }, {withCredentials: true});
        if (response.status === 200) {
            const newToken = `Bearer ${response.data['access']}`;
            api.defaults.headers.common['Authorization'] = newToken;
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);

            // Aktualisieren des Tokens in der error.config-Instanz
            error.config.headers['Authorization'] = newToken;
            return api(error.config);
        }
    }
    refresh = false;
    return Promise.reject(error);
});

export default api;