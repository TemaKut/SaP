import {Route, Routes} from "react-router-dom"
import { createContext} from "react";

import "./index.css"
import {LoginPage} from "./pages/LoginPage/LoginPage"
import { NotFoundPage } from "./pages/NotFoundPage/NotFoundPage";
import { UsersMe } from "./pages/UsersMePage/UsersMePage";
import { ListOfUsersPage } from "./pages/ListOfUsersPage/ListOfUsersPage";



export const appContext = createContext()

export const urls = {
    auth: "/",
    usersMe: "/users/me",
    usersList: "/users/list"
}


function App() {
    /* Роутинг приложения */

    return (
        <appContext.Provider value={{}}>
            <Routes>
                <Route path={urls.auth} element={<LoginPage/>}/>
                <Route path={urls.usersMe} element={<UsersMe/>}/>
                <Route path={urls.usersList} element={<ListOfUsersPage/>} />
                <Route path="*" element={<NotFoundPage/>}/>
            </Routes>
        </appContext.Provider>
    );
}

export default App;
