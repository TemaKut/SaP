import styles from "./ListUsers.module.css"


export function ListUsers(props) {
    /* Списком вывести пользователей */
    let {users} = props
    users = users.concat(users).concat(users) // На время тестирования утрен список
    return (
        <div className={styles.list}>
            <p>{`[`}</p>
                {
                users.map(
                    (user) => {
                        return(
                            <div>
                                <p className={styles.SpasesBefore}>{`{`}</p>
                                    <img className={styles.user_logo} src={user.logo} alt="User Logo"/>
                                    <br/>
                                    <span className={styles.MoreSpasesBefore}>"username": {user.username}</span>
                                    <br/>
                                    <span className={styles.MoreSpasesBefore}>"registred_at": {user.registred_at}</span>
                                <p className={styles.SpasesBefore}>{`},`}</p>
                            </div>
                        )
                    }
                )
                }
            <p>{`]`}</p>
        </div>
    )
}