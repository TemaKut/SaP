import {Route, Routes} from "react-router-dom"

import "./index.css"
import {LoginPage} from "./pages/LoginPage"
import { NotFoundPage } from "./pages/NotFoundPage";


function App() {
    /* Роутинг приложения */

    return (
        <Routes>
            <Route path="/auth" element={<LoginPage/>}/>
            <Route path="*" element={<NotFoundPage/>}/>
        </Routes>
    );
}

export default App;
