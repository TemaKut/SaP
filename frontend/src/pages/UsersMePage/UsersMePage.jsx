import styles from "./UsersMePage.module.css"
import { SideBar } from "../../components/SideBar/SideBar"
import userLogo from "../../images/DefaultUserLogo.png"


export function UsersMe() {
    /* Страница с информацией о пользователе. */
    const userData = {
        id: 0,
        logo: userLogo,  // На бэке пока нет
        username: "Artem",
        email: "tema.kutuzzzov@yandex.ru",
        registred_at: "2023-05-23T18:20:42.486Z",
        is_active: true
    }

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