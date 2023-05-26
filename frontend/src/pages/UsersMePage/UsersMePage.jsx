import styles from "./UsersMePage.module.css"
import { SideBar } from "../../components/SideBar/SideBar"
import { useCurrentUser } from "../../hooks/UseCurrentUser"



export function UsersMe() {
    /* Страница с информацией о пользователе. */
    const user = useCurrentUser()

    return (
        <div>
            <SideBar/>
            <div className={styles.UserPageBody}>
                <div className={styles.UserCard}>
                    <img src={user.logo} alt="Userlogo"/>
                    <h2>{user.username}</h2>
                </div>
            </div>
        </div>
    )
}