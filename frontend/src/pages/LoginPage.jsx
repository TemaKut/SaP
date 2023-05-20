import { BigSiteLogo } from "../components/BigSiteLogo/BigSiteLogo"
import { AuthForm } from "../components/AuthForm/AuthForm"


function LoginPage() {
    /* Страница Входа / Регистрации пользователей. */

    return (
        <div className="loginPage">
            <BigSiteLogo />
            <AuthForm />
        </div>
    )
}


export {LoginPage}
