import {SideBar} from "../../components/SideBar/SideBar"
import { useAllUsers } from "../../hooks/UseAllUsers"


export function ListOfUsersPage() {
    /* Страница со списком всех пользователей */
    const users = useAllUsers()

    console.log(users)
    return (
        <div>
            <SideBar/>
            <p>{`{`}</p>
        </div>
    )
}