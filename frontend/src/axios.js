import axios from "axios";
import {API_SERVER} from "./config";

const api = axios.create({
    baseURL: API_SERVER,
   // headers: {'Content-Type': 'application/json'},
    withCredentials: true
});


api.interceptors.request.use((config) => {
    const token = localStorage.getItem('auth_token');

    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }

    return config;
}, (error) => {
    return Promise.reject(error);
});

api.interceptors.response.use(
    (response) => {
      return response;
    },
    (error) => {
      if (error.response && error.response.status === 401) {
          localStorage.removeItem("auth_token");
          window.location.href = '/login';
      }

      return Promise.reject(error);
    }
);

export default api;