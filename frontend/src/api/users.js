import {client} from "./axiosConfig.js"


export async function userRegister(data, setError, context) {
    /* Регистрация пользоваеля */
    try {
        const response = await client.post('/v1/users/register', data)
        setError(false)
        context.setIsAuthenticated(true)

        localStorage.setItem('token', response.data.token)

    } catch (error) {
        setError(error.response)
        context.setIsAuthenticated(false)
    }
}

export async function userLogin(data, setError, context) {
    /* Вход пользоваеля */
    try {
        const response = await client.post('/v1/users/get-token', data)
        setError(false)
        context.setIsAuthenticated(true)

        localStorage.setItem('token', response.data.token)

    } catch (error) {
        setError(error.response)
        context.setIsAuthenticated(false)
    }
}