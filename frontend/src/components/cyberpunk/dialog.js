import React, {useState, useEffect} from "react";
import {FrameLines, FramePentagon, Text} from "@arwes/core";
import image_path from "../../image_path";
import {Animator} from "@arwes/animation";

const Dialog = ({children, title, dialogState, setDialogState}) => {
  useEffect(() => {
    function handleKeyDown(event) {
      if (event.key === 'Escape' && dialogState) {
        setDialogState(false);
      }
    }

    if (dialogState) {
      window.addEventListener('keydown', handleKeyDown);
    }
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [dialogState]);

  return (
      <>
        {dialogState && (
            <div
                onClick={() => setDialogState(false)}
                style={{
                  position: "fixed",
                  top: 0,
                  left: 0,
                  right: 0,
                  bottom: 0,
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  backgroundColor: "rgba(0, 0, 0, 0.5)",
                  zIndex: 1000,
                }}
            >
              <Animator>
                <div
                    className="cut-corner"
                    onClick={(e) => e.stopPropagation()}
                    style={{display: "inline-block"}}
                >
                  <FramePentagon
                        squareSize={35}
                      style={{
                        display: "inline-block",
                        padding: "0px",
                        backgroundColor: "#1a1a1a",
                        width: "auto",
                        height: "auto",
                        textAlign: "center",
                      }}
                  >
                    <FrameLines style={{
                      width: '100%', padding: 5,
                    }}>
                      <div style={{
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center'
                      }}>
                        <div style={{flex: 1, textAlign: 'center'}}><Text>{title}</Text></div>
                        <div style={{marginLeft: 'auto', cursor: 'pointer'}} onClick={() => setDialogState(false)}>X</div>
                      </div>
                    </FrameLines>
                    <div style={{padding: '20px'}}>
                      {children}
                    </div>
                  </FramePentagon>
                </div>
              </Animator>
            </div>
        )}
      </>
  );
};


export default Dialog;