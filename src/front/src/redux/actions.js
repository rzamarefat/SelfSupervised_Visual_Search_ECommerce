import { PUT_IMAGES_FROM_BACK_TO_FRONT, SET_EXPLORE_OR_FOCUS, SET_FOCUSED_ITEM, SET_RECOMS } from "./actionTypes"


export const putImages = (images) => {
    return {
        type: PUT_IMAGES_FROM_BACK_TO_FRONT,
        payload: images
    }
}

export const setFocusedImage = (productID) => {
    return {
        type: SET_FOCUSED_ITEM,
        payload: productID
    }
}


export const setRecoms = (recoms) => {
    return {
        type: SET_RECOMS,
        payload: recoms
    }
}


export const setExploreOrFocus = (n) => {
    return {
        type: SET_EXPLORE_OR_FOCUS,
        payload: n
    }
}