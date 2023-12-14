
import { useEffect, useState } from 'react';
import EntityLoader from "../loader/entity_loader";

const useRefreshEntityCard = (entityType, entity, setEntity, interval = 5000) => {
  useEffect(() => {
    const fetchData = async () => {
      let newEntity = await new EntityLoader(entityType).entity({'params': {'id': entity.id}, undefined})

      if (newEntity.image_objects.length > 0) {
        clearInterval(timer);
        setEntity(newEntity);
      }
    };

    const timer = setInterval(fetchData, interval);

    return () => clearInterval(timer);
  }, []);
};

export default useRefreshEntityCard;