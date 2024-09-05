import { Link } from 'react-router-dom';
import './circle.css';
import { ReactComponent as EditIcon } from './edit.svg';
import {useEntity} from "../components/entityProvider";
import EntityLoader from "../loader/entity_loader";
import api from "../axios";
import React, { useState } from 'react';
import Modal from 'react-modal';
import {FramePentagon} from "@arwes/core";





const SaveButton = () => {
    const {entity, setEntity} = useEntity()

    const saveEntity = async (event) => {
        event.preventDefault();
        var response = await api.put('/api/npc_creator/' + entity.entityType + '/' + entity.id + '/', entity)
        if (response.status === 200) {
            var fetchedEntity = response.data
            fetchedEntity.entityType = entity.entityType;
            fetchedEntity.editable = fetchedEntity.state === 'Unpublished';
            setEntity(fetchedEntity);
        } else {

        }
    };
    if (!entity.editable) {
        return <></>
    }

    return (
        <a href="#" onClick={saveEntity}  target="_blank">
            <div className="hoverresize">
                <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50">
                    <g className="rotating-circle">
                        <circle className="animated-circle" cx="25" cy="25" r="20"></circle>
                    </g>
                    <path d="M15 25l7 7l13-13" stroke="#00B8B8" strokeWidth="3" fill="none"
                          strokeLinecap="round"/>
                </svg>
            </div>
        </a>
    );
};


export default SaveButton;