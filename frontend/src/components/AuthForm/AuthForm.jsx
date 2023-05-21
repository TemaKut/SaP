import { userRegister, userLogin } from "../../api/users"
import styles from "./AuthForm.module.css"
import {Form} from "../Form/Form"
import { Input } from "../Input/Input"
import { useState } from "react"


export function AuthForm() {
    /* Форма для регистрации / входа пользователей */

    // Переключатель между формой регистрации и входа
    const [isRegister, setIsRegister] = useState(false)

    // Состояние введённых данных из формы регистрации
    const [registerData, setRegisterData] = useState(
        {
            username: '',
            email: '',
            password: '',
        }
    )

    // Состояние введённых данных из формы логина
    const [loginData, setLoginData] = useState(
        {
            email: '',
            password: '',
        }
    )

    // Ошибки валидации формы регистрации
    const [registerFormError, setRegisterFormError] = useState(false)

    // Ошибки валидации формы логина
    const [loginFormError, setLoginFormError] = useState(false)

    return (
        <div className={styles.AuthForm}>

            <div id={styles.chooseLoginOrRegister}>
                <button id={styles.buttonChoose}onClick={() => {setIsRegister(false)}}>
                    Login
                </button>
                <button id={styles.buttonChoose}onClick={() => {setIsRegister(true)}}>
                    Register
                </button>
            </div>

            {
                isRegister
                ?
                <Form buttonText="Register.." formError={registerFormError} onClickButton={() => userRegister(registerData, setRegisterFormError)}>
                    <Input
                        fieldname='"username"'
                        value={registerData.username}
                        onChange={(event) => setRegisterData({...registerData, username:event.target.value})}
                    />
                    <Input
                        fieldname='"email"'
                        value={registerData.email}
                        onChange={(event) => setRegisterData({...registerData, email:event.target.value})}
                    />
                    <Input
                        fieldname='"password"'
                        value={registerData.password}
                        onChange={(event) => setRegisterData({...registerData, password:event.target.value})}
                        type="password"
                    />
                </Form>
                :
                <Form buttonText="Login.." formError={loginFormError} onClickButton={() => userLogin(loginData, setLoginFormError)}>
                    <Input
                        fieldname='"email"'
                        value={loginData.email}
                        onChange={(event) => setLoginData({...loginData, email:event.target.value})}
                    />
                    <Input
                        fieldname='"password"'
                        type="password"
                        value={loginData.password}
                        onChange={(event) => setLoginData({...loginData, password:event.target.value})}
                    />
                </Form>
            }
        </div>
    )
}