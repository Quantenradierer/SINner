import {useEntity} from "../entityProvider";
import active_image from "../../active_image";
import {FramePentagon} from "@arwes/core";
import image_path from "../../image_path";
import React from "react";

function ImageFrame(props) {
    const {entity, _} = useEntity();

    let activeImage = active_image(entity.image_objects) || {}

    return <FramePentagon className='growing-img' style={{padding: 5, margin: 0}} squareSize={35}>
        <div className='pentagonframe-image' style={{'--squareSize': '35px'}}>
            <div style={{
                maxWidth: '600px',
                maxHeight: '400px',
                overflow: 'hidden'
            }}>
                <a href={image_path('npcs', activeImage.name)} target="_blank">
                    <img
                        src={image_path('npcs', activeImage.name)}
                        alt={entity.image_generator_description}
                        style={{
                            objectFit: 'cover',
                            objectPosition: 'center',
                        }}
                    />
                </a>
            </div>
        </div>
    </FramePentagon>
}


export default ImageFrame;