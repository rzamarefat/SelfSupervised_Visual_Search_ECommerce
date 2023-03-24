import { PUT_IMAGES_FROM_BACK_TO_FRONT } from "./actionTypes"


export const putImages = (images) => {
    return {
        type: PUT_IMAGES_FROM_BACK_TO_FRONT,
        payload: images
    }
}