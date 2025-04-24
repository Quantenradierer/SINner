import React, { useEffect, useState } from "react";
import styled, { css } from "styled-components";

const COLORS = {
  background: "#191c22",
  stepInactive: "#2f3242",
  stepActive: "#05fdeb",
};


const SKEW_DEG = -20;

const BarWrapper = styled.div`
  display: flex;
  gap: 1px;
  padding: 0.5rem 0.5rem;
  transform: skewX(${SKEW_DEG}deg);
`;

const Step = styled.div`
  width: 6px;
  height: 24px;
  background: ${({highlight}) => highlight ? COLORS.stepActive : COLORS.stepInactive};
  border-radius: 0;
  transition: background 0.18s;
`;

export default function LoadingBar({ estimated_time= 10000, steps = 60, title=""}) {
  const [activeSteps, setActiveSteps] = useState(0);

  useEffect(() => {
    setActiveSteps(0);
    let current = 0;
    const interval = estimated_time / steps;
    const id = setInterval(() => {
      current++;
      setActiveSteps(current);
      if (current >= steps) clearInterval(id);
    }, interval);

    return () => clearInterval(id);
  }, [estimated_time]);

  return (
      <div>
        <BarWrapper>
          {[...Array(steps)].map((_, i) => (
              <Step key={i} highlight={i < activeSteps}/>
          ))}
        </BarWrapper>
        {title && (
            <div style={{marginLeft: "10px", color: COLORS.stepActive}}>
              {title}
            </div>
        )}

      </div>
  );
}