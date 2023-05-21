import {client} from "./axiosConfig.js"


export async function userRegister (data, setError) {
    /* Регистрация пользоваеля */
    try {
        const response = await client.post('/v1/users/register', data)

        return response.data

    } catch (error) {
        setError(error.response)
    }
}
