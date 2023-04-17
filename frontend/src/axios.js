import axios from "axios";
import {API_SERVER} from "./config";

const api = axios.create({
    baseURL: API_SERVER
});

api.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`;


let refresh = false;
axios.interceptors.response.use(resp => resp, async error => {
    if (error.response.status === 401 && !refresh) {
        refresh = true;
        console.log(localStorage.getItem('refresh_token'))
        const response = await
            api.post('refresh/', {
                refresh: localStorage.getItem('refresh_token')
            }, {
                headers:
                    {'Content-Type': 'application/json'}
            }, {withCredentials: true});
        if (response.status === 200) {
            axios.defaults.headers.common['Authorization'] = `Bearer 
       ${response.data['access']}`;
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            return axios(error.config);
        }
    }
    refresh = false;
    return error;
});

export default api;