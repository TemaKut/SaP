import {client} from "./axiosConfig.js"


export async function userRegister (data) {
    /* Регистрация пользоваеля */
    console.log(111111)
    try {
        const response = await client.post('/v1/users/register', data)

        return response.data

    } catch (error) {
        console.log(error.response.data)
    }
}
