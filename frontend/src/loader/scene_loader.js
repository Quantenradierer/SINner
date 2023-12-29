import api from "../axios";


export default class SceneLoader {
    constructor() {
        this.list = this.list.bind(this);
    }


    list = async () => {
        try {
            const response = await api.get(`/api/npc_creator/scenes/`)
            if (response.status == 200) {
                return response.data
            }
        } catch (error) {
            console.log(error)
            return null
        }
    }
}