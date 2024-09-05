import React, {useState} from "react";
import {FramePentagon} from "@arwes/core";
import image_path from "../../image_path";
import {Animator} from "@arwes/animation";

const Dialog = ({clickableElement, content}) => {
  const [isOpen, setIsOpen] = useState(false);

  function openDialog() {
    setIsOpen(true);
  }

  function closeDialog() {
    setIsOpen(false);
  }

  return (
      <div>
        <a onClick={openDialog} target="_blank">
          {clickableElement}
        </a>
        <div style={{position: 'absolute'}}>
          <div style={{position: 'absolute', left: 0, top: 0}}>
            {isOpen && (
                <div
                    onClick={closeDialog}
                    style={{
                      position: 'fixed',
                      top: 0,
                      left: 0,
                      right: 0,
                      bottom: 0,
                      display: 'flex',
                      justifyContent: 'center',
                      alignItems: 'center',
                      backgroundColor: 'rgba(0, 0, 0, 0.5)',
                      zIndex: 1000,

                    }}
                >

                  <Animator><FramePentagon>
                    {content}
                  </FramePentagon></Animator>
                </div>
            )}
          </div>
        </div>
      </div>
  );
}


export default Dialog;