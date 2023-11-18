import api from "../axios";


export async function locationDefinitionLoader({ params, request }) {
    let url = new URL(request.url);
    try {
        const response = await api.get('/api/npc_creator/locations/default/')
        if (response.status == 200) {
            return response.data.entity
        }
    } catch (error) {
    }
    return {id: params.id, image_url: 'npc_load_error.png', attributes: {'Name': {'value': 'ERROR'}}}
}

export default locationDefinitionLoader;
