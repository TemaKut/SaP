import { Navigate } from "react-router-dom"
import { urls } from "../App"


export function ProtectedPage(props) {
    /* Надстройка над роутом. В случае если пользователь не авторизован - редирект */
    if (!localStorage.getItem('token') || !localStorage.getItem('isLoggedIn')) {
        return <Navigate to={urls.auth}/>
    }

    return <>{props.children}</>
}