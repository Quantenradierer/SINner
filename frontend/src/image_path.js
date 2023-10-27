import {NPC_IMAGE_PATH} from "./config";


function image_path(image_url, pk, default_image_number) {
    if (image_url == undefined) {
        return ''
    }
    return NPC_IMAGE_PATH + image_url
}

export default image_path;
