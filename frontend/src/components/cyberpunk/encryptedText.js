import React, {useEffect, useRef, useState} from "react";

function randomChar() {
    const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    return chars[Math.floor(Math.random() * chars.length)];
}

const EncryptedText = props => {
    let decodingMessage = props.children
    let messageArray = decodingMessage.split('');
    for (let i = 0; i < messageArray.length; i++) {
        messageArray[i] = randomChar()
    }
    const [content, setContent] = useState(messageArray.join(''))
    const contentRef = useRef(content);

    useEffect(() => {
        contentRef.current = content;
    }, [content]);

    useEffect(() => {
        const timer = setInterval(() => {
            if (contentRef.current === decodingMessage) {
                clearInterval(timer)
            }

            let nameArray = contentRef.current.split('');

            for (let i = 0; i < nameArray.length; i++) {
                const randChar = randomChar();
                if (nameArray[i] != decodingMessage[i]) {
                    nameArray[i] = randChar
                }

            }
            setContent(prevText => nameArray.join(''));


        }, 50);

        return () => clearInterval(timer);
    }, []);

    return <span style={{fontFamily: "monospace"}}>{content}</span>;
}

export default EncryptedText;