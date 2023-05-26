import {SideBar} from "../../components/SideBar/SideBar"
import { ListUsers } from "../../components/ListUsers/ListUsers"
import { useAllUsers } from "../../hooks/UseAllUsers"
import { Search } from "../../components/Search/Search"


export function ListOfUsersPage() {
    /* Страница со списком всех пользователей */
    const users = useAllUsers()

    console.log(users)
    return (
        <div>
            <SideBar/>
            <Search/>
            <ListUsers users={users}/>
        </div>
    )
}