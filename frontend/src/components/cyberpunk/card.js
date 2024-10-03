import {FrameBox, FrameCorners} from "@arwes/core";
import {FRAME_POLYLINE, FRAME_POLYLINE_GENERIC} from "@arwes/core/lib/utils/Frame/Frame.component";
import styled, { keyframes } from 'styled-components';
import React, {useState} from "react";
import {Animator} from "@arwes/animation";

const growLine = keyframes`
  0% {
    height: 0;
    transform: translateX(0);
  }
  100% {
    height: 100%;
    transform: translateX(0);
  }
`;

const AnimatedLine = styled.div`
  position: relative;
  overflow: hidden;

  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 0;
    width: 1px;
    background-color: #00f8f8;
    transform-origin: left center;
    animation: ${growLine} 1s linear forwards;
  }
`;

const Card = props => {
    const [isHovered, setIsHovered] = React.useState(false);
    const [triggerAnimation, setTriggerAnimation] = useState(false);


    const textStyle = {
        overflow: 'hidden',
        textOverflow: 'ellipsis',
        whiteSpace: 'nowrap',
        paddingBottom: 10,
        margin: 0
    };

    const cardStyle = {
        transform: isHovered ? 'scale(1.05)' : 'scale(1)',
        transition: 'transform 0.2s ease-in-out',
        ...props.style || {},
    }

    return (
        <Animator animator={{
            onAnimateEntering: () => {
                setTriggerAnimation(true)
            }
        }}>

            <div className="card" style={cardStyle}
                 onMouseEnter={() => setIsHovered(true)}
                 onMouseLeave={() => setIsHovered(false)}>
                {triggerAnimation && <AnimatedLine style={{height: '100%', width: '100%'}}>
                    <FrameBox hover linesWidths={[0, 0, 0, 0]} style={{
                        padding: '0px 0px 0px 1px',
                        margin: 0,
                        height: '100%',
                        width: '100%',
                        overflow: 'hidden'
                    }}>
                        <div className="card-image" style={{height: 300, overflow: 'hidden'}}>
                            <img className='appearing-image' src={props.image.src} alt={props.image.alt}
                                 style={{objectFit: 'cover', objectPosition: 'top', width: '100%', height: '100%'}}/>
                        </div>
                        <div className="card-content" style={{padding: 10}}>
                            <div>
                                <h6 className='clampText'
                                    style={{marginBottom: 10, WebkitLineClamp: 1}}>{props.title}</h6>
                            </div>
                            <div>
                                {props.children}
                            </div>
                        </div>
                    </FrameBox>
                </AnimatedLine>}
            </div>
        </Animator>
    );
};

export default Card;