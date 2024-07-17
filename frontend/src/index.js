import React from 'react';
import ReactDOM from 'react-dom';
import {AnimatorGeneralProvider} from '@arwes/animation';
import {ArwesThemeProvider, LoadingBars, StylesBaseline} from '@arwes/core';
import './index.css';
import Prompt from "./components/npc/prompt";
import NPCList from "./components/npc/npc_list";
import {createBrowserRouter, Navigate, Outlet, redirect, RouterProvider, useNavigate} from "react-router-dom";
import Impressum from "./components/impressum";
import Header from "./components/header";
import ErrorPage from "./components/error_site";
import Login from "./components/account/login";
import Logout from "./components/account/logout";
import ImageGallery from "./components/image_gallery";
import PromptLocation from "./components/location/prompt_location";
import LocationComplete from "./components/location/location_complete";
import EntityLoader from "./loader/entity_loader";
import LocationList from "./components/location/list";
import CustomList from "./components/custom/list";
import CustomPrompt from "./components/custom/prompt";
import CustomComplete from "./components/custom/complete";
import Feedback from "./components/feedback";
import Register from "./components/account/register";
import UserProvider from './userProvider';
import Navigation from "./navigation";
import NpcTabsHeader from "./components/npc/npcTabsHeader";
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
        <Header key={'header'}/>
        <div key='content' style={{justifyContent: 'center', display: 'flex', width: '100%'}}>
                {props.outlet ? props.outlet : <Outlet/>}
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
        errorElement: <Root outlet={<ErrorPage/>}/>,
        children: [
            {
                path: "navi",
                element: <Navigation/>,
            },
            {
                path: "",
                element: <NPCList/>,
                loader: npcLoader.list,
            },
            {
                path: "create",
                element: <Prompt/>,
                loader: npcLoader.definition,
            },
            {
                path: "impressum",
                element: <Impressum/>
            },
            {
                path: "npcs/:id",
                element: <NpcTabsHeader/>,
                loader: npcLoader.entity,
            },
            {
                path: "npcs/:id/sr6",
                element: <NpcTabsHeader selectedTab='sr6'/>,
                loader: npcLoader.entity,
            },
            {
                path: "npcs/:id/gallery",
                element: <NpcTabsHeader selectedTab={'gallery'}/>,
                loader: npcLoader.entity,
            },
            {
                path: "npcs/",
                element: <NPCList/>,
            },
            {
                path: "npcs/create",
                element: <Prompt/>,
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
            },
            {
                path: "locations/create",
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
            },
            {
                path: "customs/create",
                element: <CustomPrompt/>,
                loader: customLoader.definition,
            },
            {
                path: "feedback/",
                element: <Feedback/>
            },
            {
                path: "register/",
                element: <Register/>
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
    <UserProvider>
      <Theme/>
    </UserProvider>
  </React.StrictMode>,
    document.querySelector('#root')
);