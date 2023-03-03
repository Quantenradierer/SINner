import NPCCard from "../components/npc_card";


class Npc {
    constructor(id, name, image_url, image_generator_description, attributes) {
        this.id = id
        this.name = name
        this.image_url = image_url
        this.image_generator_description = image_generator_description
        this.attributes = attributes
    }
}

export default Npc;
