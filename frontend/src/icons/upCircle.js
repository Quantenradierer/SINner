import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './circle.css';

const upCircle = () => {
  const [isVisible, setIsVisible] = useState(false);

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    });
  };

  const handleScroll = () => {
    const currentScrollPos = window.pageYOffset;
    if (currentScrollPos > 1000) {
      setIsVisible(true);
    } else {
      setIsVisible(false);
    }
  };

  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <>
      {isVisible && (
        <div onClick={scrollToTop} style={{ cursor: 'pointer', position: 'fixed'}}>
          <svg className='hoverresize' width="50" height="50" xmlns="http://www.w3.org/2000/svg">
            <g className="rotating-circle">
              <circle className="animated-circle" cx="25" cy="25" r="20"></circle>
            </g>
            <line x1="25" y1="30" x2="25" y2="18" stroke="#00F8F8" strokeWidth="2" strokeLinecap="round" />
            <line x1="25" y1="18" x2="21" y2="23" stroke="#00F8F8" strokeWidth="2" strokeLinecap="round" />
            <line x1="25" y1="18" x2="29" y2="23" stroke="#00F8F8" strokeWidth="2" strokeLinecap="round" />
          </svg>
        </div>
      )}
    </>
  );
};

export default upCircle;