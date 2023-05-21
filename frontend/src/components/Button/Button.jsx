import styles from "./Button.module.css"


export function Button(props) {
    /* Кнопка */
    const {text, id, onClickButton} = props

    return <button className={styles.Button} id={id} onClick={onClickButton}>{text}</button>
}