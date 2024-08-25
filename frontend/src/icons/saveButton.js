import React from 'react';
import { Link } from 'react-router-dom';
import './circle.css';
import { ReactComponent as EditIcon } from './edit.svg';
import {useEntity} from "../components/entityProvider";
import EntityLoader from "../loader/entity_loader";
import api from "../axios";

const SaveButton = () => {
    const {entity, _} = useEntity()

    const saveEntity = () => {
        api.put('/api/' + entity.entityType + '/' + entity.id + '/save', entity)
    };

    return (
        <div className="hoverresize" style={{position: 'relative', top: 0, left: 0}}>
            <div>
                <a onClick={saveEntity}>
                    <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50">
                        <g className="rotating-circle">
                            <circle className="animated-circle" cx="25" cy="25" r="20"></circle>
                        </g>
                        <path d="M15 25l7 7l13-13" stroke="#00B8B8" stroke-width="3" fill="none" stroke-linecap="round"/>
                    </svg>
                </a>
            </div>
            <div style={{position: 'relative', top: 0, left: 0}}>
                <EditIcon/>
            </div>

        </div>
    );
};


export default SaveButton;