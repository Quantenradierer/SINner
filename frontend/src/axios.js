import axios from "axios";
import {API_SERVER} from "./config";

const api = axios.create({
    baseURL: API_SERVER,
   // headers: {'Content-Type': 'application/json'},
    withCredentials: true
});

let refresh = false;
export default api;