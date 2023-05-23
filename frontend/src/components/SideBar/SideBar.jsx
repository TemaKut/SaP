import { Link } from "react-router-dom"

import styles from "./SideBar.module.css"
import defaultUserLogo from "../../images/DefaultUserLogo.png"


export function SideBar() {
    /* Боковая навигация */
    return (
        <div className={styles.SideBar}>
            <Link to="/users/me" className={styles.Link_}>
                <img className={styles.UserLogo} src={defaultUserLogo} alt="User logo"></img>
                <p className={styles.Title}>Artem</p>
            </Link>

            <hr className={`${styles.Hr_} ${styles.Title}`}/>
            <div className={styles.DownElement}>
                <hr className={styles.Hr_}/>
                <Link to="/auth" className={styles.Link_}>
                    Exit
                </Link>
            </div>
        </div>
    )
}