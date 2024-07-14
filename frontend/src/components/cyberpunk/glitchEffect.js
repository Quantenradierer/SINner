import {useEffect, useState} from "react";
import './GlitchEffect.css';

const generateRandomPercentage = () => {
    const min = 0;
    const max = 100;
    const randomPercentage = Math.random() * (max - min) + min;
    return  Math.round(randomPercentage);
}


const generateRandomTransformation = () => {
    if (Math.random() > 0.5) {
        return `3px`
    }
    return `-3px`
}

const GlitchEffect = ({ children }) => {
    const [key, setKey] = useState(0); // Zustand hinzufügen
    const [randomPercentage, setRandomPercentage] = useState(generateRandomPercentage());

    useEffect(() => {
        const timer = setInterval(() => {
            setKey(prevKey => prevKey + 1);
            setRandomPercentage(generateRandomPercentage());
        },  5000);

        return () => clearInterval(timer);
    }, []);

const style = { '--min-value': `${randomPercentage}%`, '--max-value': `${randomPercentage + 7}%`, '--transform': `${generateRandomTransformation()}`};
    return (
        <div className="glitch-container">
            <div className="glitch-item unglitch-effect" style={style}>{children}</div>
            <div className="glitch-item glitch-effect" style={style}>{children}</div>
        </div>
    );
};

export default GlitchEffect;

