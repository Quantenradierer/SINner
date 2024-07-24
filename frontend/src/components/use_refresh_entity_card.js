
import { useEffect, useState } from 'react';
import EntityLoader from "../loader/entity_loader";

const useRefreshEntityCard = (entityType, entity, reloadCallback, interval = 5000) => {
    useEffect(() => {
      const fetchData = async () => {
        let newEntity = await new EntityLoader(entityType).entity({'params': {'id': entity.id}, undefined})

        if (newEntity.image_objects.length > 0) {
          clearInterval(timer);
          reloadCallback();
        }
      };

      var timer = undefined;
      if (entity.image_objects.length == 0) {
        const timer = setInterval(fetchData, interval);
        return () => clearInterval(timer);
      }
    }, []);


};

export default useRefreshEntityCard;