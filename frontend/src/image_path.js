import {NPC_IMAGE_PATH} from "./config";


function image_path(image_url, pk, default_image_number) {
    if (image_url == undefined) {
        return ''
    }
    return NPC_IMAGE_PATH + image_url.replace('{pk}', pk, ).replace('{counter}', default_image_number)
}

export default image_path;