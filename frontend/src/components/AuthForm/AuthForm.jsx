import { useContext, useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

import { appContext } from "../../App"
import { urls } from "../../App"
import {Form} from "../Form/Form"
import { Input } from "../Input/Input"
import { userRegister, userLogin } from "../../api/users"
import styles from "./AuthForm.module.css"


export function AuthForm() {
    /* Форма для регистрации / входа пользователей */

    // Контекст приложения
    const context = useContext(appContext)

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

    // Нажата ли кнопка входа или регистрации
    const [isPressButton, setIsPressButton] = useState(false)

    // Редирект пользователя на другую страницу после успешной авторизации или регистрации
    const navigate = useNavigate()
    useEffect(
        () => {
            if (context.isAuthenticated && isPressButton) {
                navigate(urls.usersMe)
                setIsPressButton(false)
            }
        },
        [context.isAuthenticated, navigate, isPressButton],
    )

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
                <Form
                    buttonText="Register.."
                    formError={registerFormError}
                    onClickButton={() => {setIsPressButton(true); userRegister(registerData, setRegisterFormError, context)}}
                >
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
                <Form
                    buttonText="Login.."
                    formError={loginFormError}
                    onClickButton={() => {setIsPressButton(true); userLogin(loginData, setLoginFormError, context)}}
                >
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