import {useEffect, useState} from 'react';
import api from '../axios';

const FIRST_DELAY = 800;
const MAX_DELAY = 8000;
const BACKOFF = 1.5;
const MAX_CONSECUTIVE_ERRORS = 5;

const isRunning = (status) => status && (status.state === 'queued' || status.state === 'rendering');

const getFloorplan = async (id) => (await api.get(`/api/npc_creator/floorplans/${id}/`)).data;

/**
 * Loads a floorplan (nothing for an empty id) and, while it renders, polls its status with a growing delay.
 * Stops on done/failed (then loads the finished floorplan) and after repeated network
 * errors. Returns {floorplan, status, building, error}; `status.state` is
 * queued | rendering | done | failed.
 */
export default function useFloorplan(id) {
    const [floorplan, setFloorplan] = useState(null);
    const [status, setStatus] = useState(null);
    const [building, setBuilding] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        let cancelled = false;
        let timer = null;

        const load = async () => {
            const loaded = await getFloorplan(id);
            if (cancelled) return;
            setFloorplan(loaded);
            setStatus(loaded.status);
            if (loaded.status.state === 'done' && loaded.building_url) {
                const response = await api.get(loaded.building_url);
                if (!cancelled) setBuilding(response.data);
            }
        };

        const poll = async (delay, errors) => {
            if (cancelled) return;
            try {
                const response = await api.get(`/api/npc_creator/floorplans/${id}/status/`);
                if (cancelled) return;
                setStatus(response.data);
                if (isRunning(response.data)) {
                    timer = setTimeout(() => poll(Math.min(delay * BACKOFF, MAX_DELAY), 0), delay);
                } else {
                    await load();
                }
            } catch (e) {
                if (cancelled) return;
                if (errors + 1 >= MAX_CONSECUTIVE_ERRORS) {
                    setError(e);
                    return;
                }
                timer = setTimeout(() => poll(Math.min(delay * BACKOFF, MAX_DELAY), errors + 1), delay);
            }
        };

        setFloorplan(null);
        setStatus(null);
        setBuilding(null);
        setError(null);
        if (!id) return undefined;
        load().then(() => {
            if (!cancelled) timer = setTimeout(() => poll(FIRST_DELAY, 0), 0);
        }).catch((e) => !cancelled && setError(e));

        return () => {
            cancelled = true;
            clearTimeout(timer);
        };
    }, [id]);

    return {floorplan, status, building, error};
}
