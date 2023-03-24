import initialState from "./initiaState"
import { PUT_IMAGES_FROM_BACK_TO_FRONT } from "./actionTypes";


const reducer = (state = initialState, action) => {
    switch (action.type) {
        case PUT_IMAGES_FROM_BACK_TO_FRONT:
            return {
                ...state, 
                images : action.payload
            }

        default:
            return state;
    }

}


export default reducer