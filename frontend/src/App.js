import {Route, Routes} from "react-router-dom"

import "./index.css"
import {LoginPage} from "./pages/LoginPage"
import { NotFoundPage } from "./pages/NotFoundPage";
import { UsersMe } from "./pages/UsersMe";
import { createContext} from "react";


export const appContext = createContext({isAuthenticated: false})


function App() {
    /* Роутинг приложения */

    return (
        <appContext.Provider>
            <Routes>
                <Route path="/auth" element={<LoginPage/>}/>
                <Route path="/users/me" element={<UsersMe/>}/>
                <Route path="*" element={<NotFoundPage/>}/>
            </Routes>
        </appContext.Provider>
    );
}

export default App;
