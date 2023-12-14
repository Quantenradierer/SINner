import React from "react";
import {FramePentagon} from "@arwes/core";

import {useLoaderData} from "react-router";
import CustomCard from "./card";
import EntityList from "../entity/list";





const CustomList = props => {
    const entities = useLoaderData()

    const items = [];
    for (const entity of entities.results) {
        items.push(<CustomCard entity={entity} key={entity.id}/>)
    }

    return <EntityList entities={entities} {...props}>{items}</EntityList>
}

export default CustomList;
