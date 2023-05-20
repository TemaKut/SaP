import styles from "./Button.module.css"


export function Button(props) {
    /* Кнопка */
    const {text, id} = props

    return <button className={styles.Button} id={id}>{text}</button>
}