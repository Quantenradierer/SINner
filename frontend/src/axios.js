import axios from "axios";
import {API_SERVER} from "./config";

const api = axios.create({
  baseURL: API_SERVER
});

export default api;