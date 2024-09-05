import React from 'react';
import { Link } from 'react-router-dom';
import './circle.css';
import { ReactComponent as EditIcon } from './edit.svg';

const EditButton = () => {
    return (
        <div className="hoverresize">
            <div>
                <Link to={'edit'} rel="noopener noreferrer">
                    <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg">
                        <g className="rotating-circle">
                            <circle className="animated-circle" cx="25" cy="25" r="20"></circle>
                        </g>
                        <path transform="translate(13, 13)" stroke="#00F8F8" fill="#00B8B8"
                              d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34a.9959.9959 0 0 0-1.41 0L15.13 4.96l3.75 3.75 1.83-1.83z"/>
                    </svg>
                </Link>
            </div>
            <div style={{position: 'relative', top: 0, left: 0}}>
                <EditIcon/>
            </div>
        </div>
    );
};


export default EditButton;