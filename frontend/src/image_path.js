import {IMAGE_PATH} from "./config";


function image_path(entitytype, image_url) {
    if (image_url == undefined) {
        return ''
    }
    return IMAGE_PATH + entitytype + '/' + image_url
}

export default image_path;
