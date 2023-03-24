import initialState from "./initiaState"
import { INCREMENT, DECREMENT } from "./actionTypes";


const reducer = (state = initialState, action) => {
    switch (action.type) {
        case INCREMENT:
            return {
                ...state, initialValue: state.initialValue + 1
            }
        case DECREMENT:
            return {
                ...state, initialValue : state.initialValue - 1
            }

        default:
            return state;
    }

}


export default reducer