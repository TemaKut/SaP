import styles from "./ErrorFormMessage.module.css"


export function ErrorFormMessage(props) {
    /* Сообщение об ошибке валидации (Для форм) */
    const {response} = props
    const {status, statusText, data} = response

    return (
        <div className={styles.ErrorFormMessage_}>
            <hr className={styles.Hr_}/>

            <p>error = {`{`}</p>
                <p className={styles.WithTab}>status_code: {status},</p>
                <p className={styles.WithTab}>status_text: "{statusText}",</p>
                <p className={styles.WithTab}>data: {JSON.stringify(data)},</p>
            <p>{`}`}</p>
        </div>
    )
}