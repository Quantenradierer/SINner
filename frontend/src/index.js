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
import {createBrowserRouter, Navigate, Outlet, redirect, RouterProvider, useNavigate} from "react-router-dom";
import npcLoader from "./loader/npc_loader";
import {npcListLoader} from "./loader/npc_list_loader";
import Impressum from "./components/impressum";
import Header from "./components/header";
import ErrorBoundary from "./components/error_site";
import ErrorPage from "./components/error_site";
import Login from "./components/login";
import Logout from "./components/logout";
import ImageGallery from "./components/image_gallery";
import npcDefinitionLoader from "./loader/npc_definition_loader";
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
                    <RouterProvider router={router}/>
                </AnimatorGeneralProvider>
            </ArwesThemeProvider>
        )
    }
}

const Redirector = props => {
    window.location.href = "npcs/"
    return <LoadingBars></LoadingBars>
}

const Root = props => {
    return (<div id="detail">
        <div style={{justifyContent: 'center', display: 'flex', margin: 15}}>
            <div style={{justifyContent: 'center', display: 'flex', width: 950}}>
                <Header/>
            </div>
        </div>
        <div style={{justifyContent: 'center', display: 'flex', margin: 15}}>
            <div style={{justifyContent: 'center', display: 'flex', width: 950}}>
                 {props.outlet ? props.outlet : <Outlet />}
            </div>
        </div>
        <div style={{justifyContent: 'center', display: 'flex', margin: 15}}>
            <div style={{justifyContent: 'center', display: 'flex', width: 950}}>
                <Footer/>
            </div>
        </div>
    </div>)
}



const router = createBrowserRouter([
    {
        path: "/",
        element: <Root/>,
        errorElement: <Root outlet={<ErrorPage />}/>,
        children: [
            {
                path: "",
                element: <NPCList/>,
                loader: npcListLoader,
            },
            {
                path: "impressum",
                element: <Impressum/>
            },
            {
                path: "npcs/:id",
                element: <NPCComplete/>,
                loader: npcLoader,
            },
            {
                path: "npcs/:id/gallery",
                element: <ImageGallery/>,
                loader: npcLoader,
            },
            {
                path: "npcs/",
                element: <NPCList/>,
                loader: npcListLoader,
            },
            {
                path: "prompt/",
                element: <Prompt/>,
                loader: npcDefinitionLoader,
            },
            {
                path: "login/",
                element: <Login/>
            },
            {
                path: "logout/",
                element: <Logout/>
            }
        ]
    }
]);

ReactDOM.render(
  <React.StrictMode>
      <Theme/>
  </React.StrictMode>,
    document.querySelector('#root')
);