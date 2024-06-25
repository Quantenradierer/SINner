import styled, {keyframes} from "styled-components";


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

const Blockquote = styled.div`
  position: relative;
  overflow: hidden;
  background-color: #08292B;
  padding-left: 15px;
  padding-right: 5px;
  padding-top: 5px;
  padding-bottom: 5px;
    
  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 3px;
    height: 0;
    background-color: #00f8f8;
    transform-origin: left center;
    animation: ${growLine} 0.8s linear forwards;
  }
`;

export default Blockquote;