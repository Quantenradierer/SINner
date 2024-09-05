import {Text} from "@arwes/core";
import React, {useState} from "react";
import {Animator} from "@arwes/animation";

const Divider = ({ title }) => {
    const [triggerAnimation, setTriggerAnimation] = useState(false);

    return (
        <Animator animator={{onAnimateEntering: () => {
                setTriggerAnimation(true)
            }}
        }>
            <div className="divider-container">
                <div className={`divider-line ${triggerAnimation ? "animated" : ""}`}></div>
                {title && <span className="divider-title"><b><Text>{title}</Text></b></span>}
                <div className={`divider-line ${triggerAnimation ? "animated" : ""}`}></div>
            </div>
        </Animator>
    );
};

export default Divider;