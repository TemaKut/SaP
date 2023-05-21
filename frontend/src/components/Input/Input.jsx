import styles from "./Input.module.css"


export function Input(props) {
    /* Строка ввода данных  */

    return <input className={styles.Input} {...props}/>
}