import React from 'react';
import {useLoaderData} from "react-router";
import {FrameLines, FramePentagon, Text} from "@arwes/core";


const EntityItem = props => {
    return <Text>{props.entity}</Text>
}

const SceneListItem = props => {
    const items = []
    for (const entity of props.scene.entities) {
        items.push(<EntityItem entity={entity}/>)
    }
    return <FrameLines>
        <b>{scene.title}</b>
        {items}
    </FrameLines>
}

const SceneList = props => {
    const scenes = useLoaderData()

    const items = []
    for (const scene of scenes.results) {
        items.push(<SceneListItem scene={scene} key={scene.id}/>)
    }

    return <FramePentagon>
        <div>
            {items}
        </div>
    </FramePentagon>
}

export default SceneList;
