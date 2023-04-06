import React from 'react';
import ReactDOM from 'react-dom';
import {AnimatorGeneralProvider} from '@arwes/animation';
import {ArwesThemeProvider, LoadingBars, StylesBaseline} from '@arwes/core';
import './index.css';
import Prompt from "./components/prompt";
import NPCComplete from "./components/npc_complete";
import Footer from "./components/footer";
import api from "./axios";
import ReloadButton from "./components/reload_button";
import NPCList from "./components/npc_list";
import {createBrowserRouter, Navigate, redirect, RouterProvider, useNavigate} from "react-router-dom";
import npcLoader from "./loader/npc_loader";
import {npcListLoader} from "./loader/npc_list_loader";
import Impressum from "./components/impressum";
import Header from "./components/header";

// For the font-family to work, you would have to setup the Google Fonts link:
// <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300;400;600&display=swap" />
const ROOT_FONT_FAMILY = '"Titillium Web", sans-serif';

const generalAnimator = {duration: {enter: 300, exit: 300}};


class Theme extends React.Component {
    render() {
        return (
            <ArwesThemeProvider>
                <StylesBaseline styles={{
                    body: {fontFamily: ROOT_FONT_FAMILY},
                    'ul li::marker': {
                        content: '""'
                    }
                }}/>
                <AnimatorGeneralProvider animator={generalAnimator}>
                    <div style={{justifyContent: 'center', display: 'flex', margin: 15}}>
                        <div style={{width: 800}}>
                            <div style={{justifyContent: 'center', display: 'flex', margin: 15}}>
                                <Header/>
                            </div>
                            <div style={{justifyContent: 'center', display: 'flex', margin: 15}}>
                                <RouterProvider router={router}/>
                            </div>
                            <div style={{justifyContent: 'center', display: 'flex', margin: 15}}>
                                <Footer/>
                            </div>
                        </div>
                    </div>
                </AnimatorGeneralProvider>
            </ArwesThemeProvider>
        )
    }
}

const Redirector = props => {
    window.location.href = "npcs/"
    return <LoadingBars></LoadingBars>
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <Redirector/>
  },
  {
    path: "/impressum",
    element: <Impressum/>
  },
  {
    path: "/npcs/:id",
    element: <NPCComplete/>,
      loader: npcLoader,
  },
  {
    path: "/npcs/",
    element: <NPCList/>,
    loader: npcListLoader,
  },
  {
    path: "/prompt/",
    element: <Prompt/>
  }
]);


ReactDOM.render(
  <React.StrictMode>
      <Theme/>
  </React.StrictMode>,
    document.querySelector('#root')
);