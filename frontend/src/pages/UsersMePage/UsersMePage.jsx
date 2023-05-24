import { useContext } from "react"

import styles from "./UsersMePage.module.css"
import { SideBar } from "../../components/SideBar/SideBar"
import { appContext } from "../../App"


export function UsersMe() {
    /* Страница с информацией о пользователе. */
    const context = useContext(appContext)
    const {userData} = context

    return (
        <div>
            <SideBar/>
            <div className={styles.UserPageBody}>
                <div className={styles.UserCard}>
                    <img src={userData.logo} alt="Userlogo"/>
                    <h2>{userData.username}</h2>
                </div>
                <hr className={styles.Hr_}/>
            </div>
        </div>
    )
}