import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import { Provider } from 'react-redux'
import Store from './redux/store'

import ExplorePage from "./pages/ExplorePage"
import FocusPage from "./pages/FocusPage"


const App = () => {
    return (
        <Provider store={Store}>
            <Router>
                <Routes>
                    <Route path="/" element={<ExplorePage />} />
                    <Route path="/focus" element={<FocusPage />} />
                </Routes>
            </Router>
        </Provider>
        
        
    )
}


export default App