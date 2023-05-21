import {client} from "./axiosConfig.js"


export async function userRegister(data, setError) {
    /* Регистрация пользоваеля */
    try {
        const response = await client.post('/v1/users/register', data)
        setError(false)

        return response.data

    } catch (error) {
        setError(error.response)
    }
}

export async function userLogin(data, setError) {
    /* Вход пользоваеля */
    try {
        const response = await client.post('/v1/users/get-token', data)
        setError(false)
        console.log(response.data)

        return response.data

    } catch (error) {
        setError(error.response)
    }
}