import React, {createContext, useContext, useEffect, useState} from 'react';
import useEntitySchema from "../loader/useEntitySchema";
import {useParams} from "react-router-dom";

const EntityContext = createContext();

const EntityProvider = ({ entityType, selectedTab, children }) => {
  const {id} = useParams();
  const {entity: fetchedEntity, loading, error} = useEntitySchema(entityType, id, selectedTab);
  const [entity, setEntity] = useState({values: {name: ''}, image_objects: []});

  entity.entityType = entityType;
  entity.selectedTab = selectedTab;
  entity.loading = loading;
  entity.editable = true;

  useEffect(() => {
    setEntity(fetchedEntity);
  }, [fetchedEntity, setEntity, loading]);

  return (
      <EntityContext.Provider value={{entity, setEntity}}>
        {children}
      </EntityContext.Provider>
  );
};

const useEntity = () => {
  return useContext(EntityContext);
};

export { EntityProvider, useEntity };