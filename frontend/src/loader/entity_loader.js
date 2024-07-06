import api from "../axios";

export default class EntityLoader {
    constructor(kind) {
        this.kind = kind

        this.definition = this.definition.bind(this);
        this.entity = this.entity.bind(this);
        this.list = this.list.bind(this);
    }

     definition = async ({params, request})=> {
        try {
            const response = await api.get(`/api/npc_creator/${this.kind}/default/`)
            return response.data.entity
        } catch (error) {
            console.log(error)
            return null
        }
    }

    entity = async ({params, request}) => {
        try {
            const response = await api.get(`/api/npc_creator/${this.kind}/${params.id}/`)
            if (response.status == 200) {
                return response.data
            }
        } catch (error) {
            console.log(error)
            return {}
        }
    }

    list = async ({params, request}) => {
        const search = params.search || ''
        const page = params.page || 1

        let url = new URL(request.url);
        try {
            const response = await api.get(`/api/npc_creator/${this.kind}/?search=${search}&page=${page}`)
            if (response.status == 200) {
                return response.data
            }
        } catch (error) {
            console.log(error)
            return null
        }
    }
}