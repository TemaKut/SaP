import {Route, Routes} from "react-router-dom"

import "./index.css"
import {LoginPage} from "./pages/LoginPage/LoginPage"
import { NotFoundPage } from "./pages/NotFoundPage/NotFoundPage";
import { UsersMe } from "./pages/UsersMePage/UsersMePage";
import { createContext, useEffect, useState} from "react";


export const appContext = createContext()

export const urls = {
    auth: "/",
    usersMe: "/users/me",
}


function App() {
    /* Роутинг приложения */
    const [userData, setUserData] = useState(null)
    const [isAuthenticated, setIsAuthenticated] = useState(false)

    return (
        <appContext.Provider value={
            {isAuthenticated, setIsAuthenticated, userData, setUserData}
        }>
            <Routes>
                <Route path={urls.auth} element={<LoginPage/>}/>
                <Route path={urls.usersMe} element={<UsersMe/>}/>
                <Route path="*" element={<NotFoundPage/>}/>
            </Routes>
        </appContext.Provider>
    );
}

export default App;
