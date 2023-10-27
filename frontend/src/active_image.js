
function active_image(image_objects) {
    let highest_image = image_objects[0]
    for (let image of image_objects) {
        if (image.score > highest_image.score) {
            highest_image = image
        }
    }

    return highest_image
}

export default active_image;
