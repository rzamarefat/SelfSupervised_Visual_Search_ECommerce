import { createStore, applyMiddleware } from 'redux'
import { composeWithDevTools } from 'redux-devtools-extension'
import logger from 'redux-logger'
import reducer from './reducer'


const Store = createStore(reducer, composeWithDevTools(applyMiddleware(logger)))

export default Store