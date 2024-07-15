import React from 'react';
import { Link } from 'react-router-dom';
import './circle.css';


const AddCircle = () => {
  return (
    <div className="hoverresize">
      <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg">
        <Link to={'create'} rel="noopener noreferrer">
          <g className="rotating-circle">
            <circle className="animated-circle" cx="25" cy="25" r="20"></circle>
            <line x1="18" y1="25" x2="32" y2="25" stroke="#00F8F8" strokeWidth="3" strokeLinecap="round"/>
            <line x1="25" y1="18" x2="25" y2="32" stroke="#00F8F8" strokeWidth="3" strokeLinecap="round"/>
          </g>
        </Link>
      </svg>
    </div>
  );
};



export default AddCircle;