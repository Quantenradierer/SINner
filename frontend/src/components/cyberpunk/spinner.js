import "./spinner.css";
import React from "react";

export const Spinner = ({}) => {
    return (
        <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%'}}>
            <div className="cyberpunk-spinner">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    )
}