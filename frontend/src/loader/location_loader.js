import api from "../axios";


export async function locationLoader({ params, request }) {
    let url = new URL(request.url);
    try {
        const response = await api.get('/api/npc_creator/locations/' + params.id + '/' + url.search)
        return response.data
    } catch (error) {
        return {}
    }
}

export default locationLoader;
