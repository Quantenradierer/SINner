import React from 'react';
import ReactDOM from 'react-dom';
import {AnimatorGeneralProvider} from '@arwes/animation';
import {ArwesThemeProvider, LoadingBars, StylesBaseline} from '@arwes/core';
import './index.css';
import Prompt_npc from "./components/prompt_npc";
import NPCComplete from "./components/npc/npc_complete";
import Footer from "./components/footer";
import api from "./axios";
import NPCList from "./components/npc/npc_list";
import {createBrowserRouter, Navigate, Outlet, redirect, RouterProvider, useNavigate} from "react-router-dom";
import Impressum from "./components/impressum";
import Header from "./components/header";
import ErrorPage from "./components/error_site";
import Login from "./components/login";
import Logout from "./components/logout";
import ImageGallery from "./components/image_gallery";
import PromptLocation from "./components/location/prompt_location";
import LocationComplete from "./components/location/location_complete";
import EntityLoader from "./loader/entity_loader";
import LocationList from "./components/location/location_list";
import CustomList from "./components/custom/list";
import CustomPrompt from "./components/custom/prompt";
import CustomComplete from "./components/custom/complete";
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

const npcLoader = new EntityLoader('npcs')
const locationLoader = new EntityLoader('locations')
const critterLoader = new EntityLoader('critters')
const customLoader = new EntityLoader('customs')

const router = createBrowserRouter([
    {
        path: "/",
        element: <Root/>,
        errorElement: <Root outlet={<ErrorPage />}/>,
        children: [
            {
                path: "",
                element: <NPCList/>,
                loader: npcLoader.list,
            },
            {
                path: "impressum",
                element: <Impressum/>
            },
            {
                path: "npcs/:id",
                element: <NPCComplete/>,
                loader: npcLoader.entity,
            },
            {
                path: "npcs/:id/gallery",
                element: <ImageGallery factor={{'x': 4, 'y': 5}}  attribute={'Detailliertes Aussehen'} entity_type={'npcs'}/>,
                loader: npcLoader.entity,
            },
            {
                path: "npcs/",
                element: <NPCList/>,
                loader: npcLoader.list,
            },
            {
                path: "npcs_prompt/",
                element: <Prompt_npc/>,
                loader: npcLoader.definition,
            },
            {
                path: "locations/:id",
                element: <LocationComplete/>,
                loader: locationLoader.entity,
            },
            {
                path: "locations/:id/gallery",
                element: <ImageGallery factor={{'x': 7, 'y': 4}} attribute={'Aussehen'} entity_type={'locations'}/>,
                loader: locationLoader.entity,
            },
            {
                path: "locations/",
                element: <LocationList/>,
                loader: locationLoader.list,
            },
            {
                path: "locations_prompt/",
                element: <PromptLocation/>,
                loader: locationLoader.definition,
            },
            {
                path: "customs/:id",
                element: <CustomComplete/>,
                loader: customLoader.entity,
            },
            {
                path: "customs/:id/gallery",
                element: <ImageGallery factor={{'x': 5, 'y': 5}} attribute={'Aussehen'} entity_type={'customs'}/>,
                loader: customLoader.entity,
            },
            {
                path: "customs/",
                element: <CustomList/>,
                loader: customLoader.list,
            },
            {
                path: "customs_prompt/",
                element: <CustomPrompt/>,
                loader: customLoader.definition,
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