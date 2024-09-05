import { useState, useEffect } from 'react';
import axios from 'axios';
import api from "../axios";

const useEntitySchema = (kind, id, name) => {
  const [entity, setEntity] = useState({ values: { name: '' }, image_objects: [] });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [polling, setPolling] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      console.log('Fetching data with polling:', polling);
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
  }, [kind, id, name, polling]);

  useEffect(() => {
    console.log('Polling updated:', polling);
  }, [polling]);

  const refetch = () => {
    console.log('Refetching', kind, id, name, polling);
    setPolling(prevPolling => prevPolling + 1);
  };

  return { entity, loading, error, refetch };
};

export default useEntitySchema;