import {IMAGE_PATH} from "./config";


function image_path(entitytype, image_url, thumbnail) {
    if (image_url == undefined) {
        return ''
    }

    if (thumbnail) {
        return IMAGE_PATH + entitytype + '/jpgs/' + image_url + '.jpg'
    } else {
        return IMAGE_PATH + entitytype + '/' + image_url + '.png'
    }
}

export default image_path;
