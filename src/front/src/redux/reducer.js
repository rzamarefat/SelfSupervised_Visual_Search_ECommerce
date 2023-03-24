import initialState from "./initiaState"
import { PUT_IMAGES_FROM_BACK_TO_FRONT, SET_FOCUSED_ITEM } from "./actionTypes";


const reducer = (state = initialState, action) => {
    switch (action.type) {
        case PUT_IMAGES_FROM_BACK_TO_FRONT:
            return {
                ...state, 
                images : action.payload
            }

        case SET_FOCUSED_ITEM:
            return {
                ...state,
                focusedItem: action.payload
            }

        default:
            return state;
    }

}


export default reducer