import { useState, useEffect } from "react"

import { userMe } from "../api/users"


export function useCurrentUser(){
    const [user, setUser] = useState({})
    useEffect(
        () => {
            async function getUser() {
                setUser(await userMe())
            }
            getUser()
        },
        []
    )

    return user
}
