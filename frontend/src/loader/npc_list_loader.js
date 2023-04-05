import api from "../axios";


export async function npcListLoader({ request }) {
    let url = new URL(request.url);
    try {
        const response = await api.get('/api/npc_creator/npcs/' + url.search)
        return response.data
    } catch (error) {
        return null
    }

}

export default npcListLoader;
