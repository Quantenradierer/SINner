import { useState, useEffect } from 'react';
import axios from 'axios';
import api from "../axios";

const useEntitySchema = (kind, id, name) => {
  const [entity, setEntity] = useState({values: {name: ''}, image_objects: []});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await api.get(`/api/npc_creator/${kind}/${id}/?schema=${name}`);
        if (response.status === 200) {
          setEntity(response.data);
        } else {
          console.error('Error: Non-200 response status', response);
          setError(new Error('Failed to fetch data'));
        }
      } catch (err) {
        console.error('Error fetching data', err);
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [kind, id, name]);

  return { entity, loading, error };
};

export default useEntitySchema;