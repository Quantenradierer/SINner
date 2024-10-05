import api from "../axios";

function getFilterKeys(filter) {
  return Object.entries(filter)
    .filter(([key, value]) => value === true)
    .map(([key, value]) => key);
}

export default class EntityLoader {
    constructor() {
        this.list = this.list.bind(this);
    }

    list = async ({params, request}) => {
        const search = params.search || '';
        const page = params.page || 1;
        const filtered = params.filter || [];
        const favorites = params.favorites || null;
        const own = params.own || null;

        let url = new URL(request.url);
        try {
            const response = await api.get(`/api/npc_creator/entities/`, {params: {kind: filtered, search: search, page: page, favorites: favorites, own: own}})
            if (response.status == 200) {
                return response.data
            }
        } catch (error) {
            console.log(error)
            return null
        }
    }
}