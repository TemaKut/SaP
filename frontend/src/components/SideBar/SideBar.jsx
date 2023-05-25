import { Link } from "react-router-dom"

import styles from "./SideBar.module.css"
import { urls } from "../../App"
import { useCurrentUser } from "../../hooks/UseCurrentUser"

export function SideBar() {
    /* Боковая навигация */
    const user = useCurrentUser()

    return (
        <div className={styles.SideBar}>
            <Link to={urls.usersMe} className={styles.Link_}>
                <img className={styles.UserLogo} src={user.logo} alt="User logo"/>
            </Link>
            <p className={styles.Title}>{user.username}</p>
            <hr className={`${styles.Hr_} ${styles.Title}`}/>

            <Link to={urls.usersList}>
                <h5>Список пользователей</h5>
            </Link>

            <div className={styles.DownElement}>
                <hr className={styles.Hr_}/>
                <Link
                    to={urls.auth}
                    className={styles.Link_}
                    onClick={() => {
                            localStorage.removeItem('token')
                            localStorage.removeItem('isLoggedIn')
                        }
                    }
                >
                    Exit
                </Link>
            </div>
        </div>
    )
}