import {IMAGE_PATH} from "./config";


// `image` is an image object from the API (preferred), or a bare legacy uuid
// string for callers/rows that predate stored files.
function image_path(entitytype, image, thumbnail) {
    if (image == undefined) {
        return ''
    }

    if (typeof image === 'object') {
        return (thumbnail ? image.thumbnail_url : image.file_url) || ''
    }

    if (thumbnail) {
        return IMAGE_PATH + entitytype + '/jpgs/' + image + '.jpg'
    }
    return IMAGE_PATH + entitytype + '/' + image + '.png'
}

export default image_path;
