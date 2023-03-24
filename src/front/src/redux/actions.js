import { PUT_IMAGES_FROM_BACK_TO_FRONT, SET_FOCUSED_ITEM } from "./actionTypes"


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