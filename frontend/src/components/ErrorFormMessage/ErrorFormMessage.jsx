import styles from "./ErrorFormMessage.module.css"


export function ErrorFormMessage(props) {
    /* Сообщение об ошибке валидации (Для форм) */
    const {response} = props
    const {data} = response

    return (
        <div className={styles.ErrorFormMessage_}>
            <hr className={styles.Hr_}/>
            <p className={styles.P_}>error = {JSON.stringify(data)}</p>
        </div>
    )
}