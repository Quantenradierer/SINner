import { useState } from 'react';
import SceneLoader from "../../loader/scene_loader";


export const AddToListMenu = props => {
    const [menu, setMenu] = useState(false);

    function addToFavorite(event) {
        new SceneLoader().push('📌', props.entity_id)
    }

    return <div>
        {false && <div><a onClick={addToFavorite}>📌</a></div>}
    </div>
}
