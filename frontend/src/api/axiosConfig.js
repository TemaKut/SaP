import axios from "axios"
import { BACKEND_BASE_URL } from "../settings"


// Объект клиента, через который следует делать запросы на backend
const client = axios.create(
    {
        baseURL: BACKEND_BASE_URL,
    }
)

// Добавить в клиент автодобавление токена в каждый запрос
client.interceptors.request.use(
    (config) => {
        config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`

        return config
    }
)



export {client}
