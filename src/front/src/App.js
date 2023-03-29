import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import { Provider } from 'react-redux'
import Store from './redux/store'

import ExplorePage from "./pages/ExplorePage"
import FocusPage from "./pages/FocusPage"
import ConfigPage from "./pages/ConfigPage"


const App = () => {
    return (
        <Provider store={Store}>
            <Router>
                <Routes>
                    <Route path="/" element={<ExplorePage />} />
                    <Route path="/focus" element={<FocusPage />} />
                    <Route path="/config" element={<ConfigPage/>} />
                </Routes>
            </Router>
        </Provider>
        
        
    )
}


export default App