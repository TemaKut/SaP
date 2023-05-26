import { useEffect, useState } from "react"

import { allUsers } from "../api/users"

export function useAllUsers() {
    /* Получить список всех пользователей */
    const [users, setUsers] = useState([])
    
    useEffect(
        () => {
            async function getAllUsers() {
                
                setUsers(await allUsers())
            }

            getAllUsers()
        },
        []
    )

    return users
}