import React from "react";
import {FramePentagon} from "@arwes/core";

import {useLoaderData} from "react-router";
import image_path from "../../image_path";
import List from "../entity/list";
import CustomCard from "./card";





const CustomList = props => {
    const entities = useLoaderData()

    const items = [];
    for (const entity of entities.results) {
        items.push(<CustomCard entity={entity} key={entity.id}/>)
    }

    return <List entities={entities} {...props}>{items}</List>
}

export default CustomList;
