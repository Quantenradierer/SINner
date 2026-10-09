import React, {useEffect, useState} from "react";
import styled, {keyframes} from "styled-components";

const COLORS = {
    stepInactive: "#2f3242",
    stepActive: "#05fdeb",
};

const SKEW_DEG = -20;

const sweep = keyframes`
  0% { background-position: -100% 0; }
  100% { background-position: 200% 0; }
`;

const Wrapper = styled.div`
  width: 100%;
`;

const BarWrapper = styled.div`
  display: flex;
  gap: 3px;
  width: 100%;
  padding: 0.5rem 0;
  box-sizing: border-box;
  transform: skewX(${SKEW_DEG}deg);
`;

const Step = styled.div`
  flex: 1;
  height: 22px;
  background: ${({highlight}) => highlight ? COLORS.stepActive : COLORS.stepInactive};
  box-shadow: ${({highlight}) => highlight ? `0 0 6px ${COLORS.stepActive}66` : "none"};
  transition: background 0.18s, box-shadow 0.18s;
`;

const Overrun = styled.div`
  height: 3px;
  margin-top: 4px;
  background: linear-gradient(90deg, transparent, ${COLORS.stepActive}, transparent) 0 0 / 50% 100% no-repeat;
  animation: ${sweep} 1.6s linear infinite;
`;

const Caption = styled.div`
  display: flex;
  justify-content: space-between;
  margin-top: 4px;
  color: ${COLORS.stepActive};
  font-size: 0.9em;
`;

export default function LoadingBar({estimated_time = 10000, steps = 60, title = ""}) {
    const [elapsed, setElapsed] = useState(0);

    useEffect(() => {
        const start = Date.now();
        setElapsed(0);
        const id = setInterval(() => setElapsed(Date.now() - start), 200);
        return () => clearInterval(id);
    }, [estimated_time]);

    // Fill linearly up to the estimate, then keep creeping towards (but never reaching) the end,
    // so a generation that takes longer than estimated doesn't look frozen.
    const ratio = elapsed <= estimated_time
        ? elapsed / estimated_time * 0.85
        : 0.85 + 0.14 * (1 - Math.exp(-(elapsed - estimated_time) / (estimated_time * 2)));
    const activeSteps = Math.floor(ratio * steps);
    const overrun = elapsed > estimated_time

    return (
        <Wrapper>
            <BarWrapper>
                {[...Array(steps)].map((_, i) => (
                    <Step key={i} highlight={i < activeSteps}/>
                ))}
            </BarWrapper>
            {overrun && <Overrun/>}
            <Caption>
                <span>{title}</span>
                <span>{Math.floor(elapsed / 1000)}s</span>
            </Caption>
        </Wrapper>
    );
}
