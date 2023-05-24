import {client} from "./axiosConfig.js"
import { BACKEND_BASE_URL } from "../settings.js"


export async function userRegister(data, setError, context) {
    /* Регистрация пользоваеля */
    try {
        const response = await client.post('api/v1/users/register', data)
        setError(false)
        context.setIsAuthenticated(true)

        localStorage.setItem('token', response.data.token)

    } catch (error) {
        console.log(error)
        setError(error.response)
        context.setUserData(null)
        context.setIsAuthenticated(false)
    }
}

export async function userLogin(data, setError, context) {
    /* Вход пользоваеля */
    try {
        const response = await client.post('api/v1/users/get-token', data)
        setError(false)
        context.setIsAuthenticated(true)

        localStorage.setItem('token', response.data.token)

    } catch (error) {
        console.log(error)
        setError(error.response)
        context.setUserData(null)
        context.setIsAuthenticated(false)
    }
}

export async function userMe(context) {
    /* Получить информацию о пользователе, сделавшем запрос */
    try {
        const response = await client.get('api/v1/users/me')
        // Заменить uri фотографии на url
        response.data.logo = `${BACKEND_BASE_URL}${response.data.logo}`

        context.setIsAuthenticated(true)
        context.setUserData(response.data)

    } catch (error) {
        console.log(error)
        context.setUserData(null)
        context.setIsAuthenticated(false)
    }
}