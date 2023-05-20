import styles from "./AuthForm.module.css"
import {Form} from "../Form/Form"
import { Input } from "../Input/Input"


export function AuthForm() {
    /* Форма для регистрации пользователей */

    return (
        <div className={styles.AuthForm}>
            <div id={styles.chooseLoginOrRegister}>
                <button id={styles.buttonChoose} autofocused={true}>Login</button>
                <button id={styles.buttonChoose}>Register</button>
            </div>
            <Form>
                <Input fieldName="username"/>
                <Input fieldName="enami"/>
                <Input fieldName="password" type="password"/>
            </Form>
        </div>
    )
}