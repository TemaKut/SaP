import logo from "../../images/MainLogo.png"
import styles from "./BigSiteLogo.module.css"

export function BigSiteLogo() {
    /* Большой логотип сайта */

    return (
        <div className={styles.BigSiteLogo}>
            <img src={logo} alt="MainLogo" id={styles.mainLogo}/>
            <hr id={styles.lineUnderLogo}/>
            <h2 id={styles.slogan}>Share a Project</h2>
        </div>
    )
}
