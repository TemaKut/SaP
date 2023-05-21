import axios from "axios"


// Объект клиента, через который следует делать запросы на backend
const client = axios.create(
    {
        baseURL: 'http://localhost:8000/api',
    }
)

// Добавить в клиент автодобавление токена в каждый запрос
client.interceptors.request.use(
    (config) => {
        // config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`

        return config
    }
)


export {client}
