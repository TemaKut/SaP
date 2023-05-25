import {client} from "./axiosConfig.js"
import { BACKEND_BASE_URL } from "../settings.js"


export async function userRegister(data, setError) {
    /* Регистрация пользоваеля */
    try {
        const response = await client.post('api/v1/users/register', data)
        setError(false)

        localStorage.setItem('token', response.data.token)
        localStorage.setItem('isLoggedIn', true)

    } catch (error) {
        localStorage.removeItem('token')
        localStorage.removeItem('isLoggedIn')
        setError(error.response)
    }
}

export async function userLogin(data, setError) {
    /* Вход пользоваеля */
    try {
        const response = await client.post('api/v1/users/get-token', data)
        setError(false)

        localStorage.setItem('token', response.data.token)
        localStorage.setItem('isLoggedIn', true)

    } catch (error) {
        localStorage.removeItem('token')
        localStorage.removeItem('isLoggedIn')
        setError(error.response)
    }
}

export async function userMe() {
    /* Получить информацию о пользователе, сделавшем запрос */
    try {
        const response = await client.get('api/v1/users/me')

        // Заменить uri фотографии на url
        response.data.logo = `${BACKEND_BASE_URL}${response.data.logo}`

        localStorage.setItem('isLoggedIn', true)

        return response.data

    } catch (error) {
        localStorage.removeItem('isLoggedIn')

        return {}
    }
}