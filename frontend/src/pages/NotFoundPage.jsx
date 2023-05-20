import { Link } from "react-router-dom"

function NotFoundPage() {
    /* Страница Входа / Регистрации пользователей. */

    return (
        <div className="notFoundPage">
            <h1>Страница 404</h1>
            <Link to="/auth">login</Link>
        </div>
    )
}


export {NotFoundPage}
