import React, {useState} from "react";
import {FramePentagon} from "@arwes/core";

import {useLoaderData} from "react-router";
import CustomCard from "./card";
import EntityList from "../entity/list";
import EntityLoader from "../../loader/entity_loader";
import {Animator} from "@arwes/animation";





const CustomList = props => {
    const loader = new EntityLoader('customs')

    const createItem = (entity) => {
        return <CustomCard key={'NPCListItem' + entity.id} entity={entity}/>
    }

    return <EntityList createItem={createItem} loader={loader} {...props}></EntityList>
}

export default CustomList;
