import { Link } from "react-router-dom"

import styles from "./SideBar.module.css"
import { urls } from "../../App"
import { useContext } from "react"
import { appContext } from "../../App"


export function SideBar() {
    /* Боковая навигация */
    const context = useContext(appContext)
    const {userData} = context

    return (
        <div className={styles.SideBar}>
            <Link to={urls.usersMe} className={styles.Link_}>
                <img className={styles.UserLogo} src={userData.logo} alt="User logo"/>
            </Link>
            <p className={styles.Title}>{userData.username}</p>
            <hr className={`${styles.Hr_} ${styles.Title}`}/>

            <div className={styles.DownElement}>
                <hr className={styles.Hr_}/>
                <Link to={urls.auth} className={styles.Link_}>
                    Exit
                </Link>
            </div>
        </div>
    )
}