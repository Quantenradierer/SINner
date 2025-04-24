import React, {useEffect, useRef, useState} from "react";
import {random} from "animejs";

function randomChar() {
    const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz';
    return chars[Math.floor(Math.random() * chars.length)];
}

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}


export const EncryptedTextState = Object.freeze({
  STATIC: "static",
  RUNNING: "running",
  ENCRYPTING: "encrypting"
});

const EncryptedText = ({children, state}) => {
    let decodingMessage = children.join('').split('');
    let decryptedLength = decodingMessage.length;

    const [content, setContent] = useState('')
    const contentRef = useRef(content);

    useEffect(() => {
        contentRef.current = content;
    }, [content]);

    useEffect(() => {
        const timer = setInterval(() => {
            if (state == EncryptedTextState.STATIC && contentRef.current !== '') {
                return;
            }
            const encryptedMapping = new Array(decodingMessage.length).fill(0).fill(1, 0, decryptedLength);

            const encryptedMessage = shuffleArray(encryptedMapping).map((value, index) => {
                if (value === 1) {
                    return randomChar();
                } else {
                    return decodingMessage[index];
                }
            });
            setContent(prevText => encryptedMessage.join(''));
            if (state == EncryptedTextState.RUNNING) {
                return;
            }

            if (decryptedLength === 0) {
                clearInterval(timer);
                return;
            }
            decryptedLength -= 1;

        }, 25);

        return () => clearInterval(timer);
    }, [state]);

    return <span style={{
        fontFamily: "monospace",
}}>{content}</span>;
}

export default EncryptedText;