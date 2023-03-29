import initialState from "./initiaState"
import { PUT_IMAGES_FROM_BACK_TO_FRONT, SET_EMBEDDING_APPROACH, SET_EXPLORE_OR_FOCUS, SET_FOCUSED_ITEM, SET_RECOMS } from "./actionTypes";


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
                focusedItem: action.payload.id,
                focusedItemImage: action.payload.image
            }

        case SET_RECOMS:
            return {
                ...state,
                recoms: action.payload
            }
        case SET_EXPLORE_OR_FOCUS:
            return {
                ...state,
                exploreOrFocus: action.payload
            }
        case SET_EMBEDDING_APPROACH:
            return {
                ...state,
                embApproach: action.payload,
                images: [],
            }

        default:
            return state;
    }

}


export default reducer