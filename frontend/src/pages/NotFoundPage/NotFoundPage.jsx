import { Link } from "react-router-dom"

import { urls } from "../../App"

export function NotFoundPage() {
    /* Страница Входа / Регистрации пользователей. */

    return (
        <div className="notFoundPage">
            <h1>Страница 404</h1>
            <Link to={urls.auth}>login or register</Link>
        </div>
    )
}
