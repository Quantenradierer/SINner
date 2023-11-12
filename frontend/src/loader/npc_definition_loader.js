import api from "../axios";


export async function npcDefinitionLoader({ params, request }) {
    let url = new URL(request.url);
    try {
        const response = await api.get('/api/npc_creator/npcs/default/')
        return response.data.entity
    } catch (error) {
        return {id: params.id, image_url: 'npc_load_error.png', attributes: {'Name': {'value': 'ERROR'}}}
    }
}

export default npcDefinitionLoader;
