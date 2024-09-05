import {useEntity} from "../entityProvider";
import active_image from "../../active_image";
import {FramePentagon, Text} from "@arwes/core";
import image_path from "../../image_path";
import React, {useState, useEffect, useCallback} from "react";
import i18n from "../../i18n";
import useEntitySchema from "../../loader/useEntitySchema";



const useImageWithPolling = (entityType, id, pollInterval = 10000) => {
  const { entity, loading, error, refetch } = useEntitySchema(entityType, id, 'gallery');
  const [polling, setPolling] = useState(null);

  useEffect(() => {
    const intervalId = setInterval(() => {
      refetch();
    }, pollInterval);

    setPolling(intervalId);

    return () => clearInterval(intervalId);
  }, []);

  useEffect(() => {
      console.log(polling, entity)
    if (polling && entity && entity.image_objects && entity.image_objects.length > 0) {
      clearInterval(polling);
      setPolling(null);
    }
  }, [polling, entity]);

  return { polledEntity: entity, loading, error };
};


function ImageFrame({style}) {
    const {entity, setEntity} = useEntity();
    const {polledEntity} = useImageWithPolling(entity.entityType, entity.id);

    useEffect(() => {
        if (polledEntity && polledEntity.image_objects && polledEntity.image_objects.length > 0) {
            setEntity(prevEntity => ({...prevEntity, image_objects: polledEntity.image_objects}));
        }
    }, [polledEntity]);

    let activeImage = active_image(entity.image_objects) || null;

    return <FramePentagon className='growing-img' style={{padding: 5, margin: 0}} squareSize={35}>
        <div className='pentagonframe-image' style={{'--squareSize': '35px'}}>
            {activeImage && <a href={image_path(entity.entityType, activeImage.name)} target="_blank">
                <div style={style}>
                    <img
                        src={image_path(entity.entityType, activeImage.name)}
                        alt={entity.image_generator_description}
                        style={{
                            display: 'block',
                        }}
                    />
                </div>
            </a>}
            {activeImage === null && <div style={style}><Text>{i18n.t('image_generation_in_progress')}</Text></div>}
        </div>
    </FramePentagon>
}


export default ImageFrame;