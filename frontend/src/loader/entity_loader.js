import api from "../axios";

export default class EntityLoader {
    constructor(kind) {
        this.kind = kind

        this.definition = this.definition.bind(this);
        this.entity = this.entity.bind(this);
        this.list = this.list.bind(this);
    }

     definition = async ({params, request})=> {
        let url = new URL(request.url);
        try {
            const response = await api.get(`/api/npc_creator/${this.kind}/default/`)
            return response.data.entity
        } catch (error) {
            return null
        }
    }

    entity = async ({params, request}) => {
        let url = new URL(request.url);
        try {
            const response = await api.get(`/api/npc_creator/${this.kind}/${params.id}/`)
            if (response.status == 200) {
                return response.data
            }
        } catch (error) {
            return {}
        }
    }

    list = async ({params, request}) => {
        let url = new URL(request.url);
        try {
            const response = await api.get(`/api/npc_creator/${this.kind}/${url.search}`)
            if (response.status == 200) {
                return response.data
            }
        } catch (error) {
            return null
        }
    }
}