import {client} from "./axiosConfig.js"


export async function userRegister (data) {
    /* Регистрация пользоваеля */
    try {
        const response = await client.post('/v1/users/register', data)

        return response.data

    } catch (error) {
        return error.response.data
    }
}
