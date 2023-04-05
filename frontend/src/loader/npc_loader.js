import api from "../axios";


export async function npcLoader({ params, request }) {
    let url = new URL(request.url);
    try {
        const response = await api.get('/api/npc_creator/npcs/' + params.id + '/' + url.search)
        return response.data
    } catch (error) {
        return {id: params.id, image_url: 'npc_load_error.png', attributes: {'Name': 'ERROR'}}
    }
}

export default npcLoader;
