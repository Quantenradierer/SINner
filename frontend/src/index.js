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
import LocationTabsHeader from "./components/location/locationTabsHeader";
import CharDefault from "./components/npc/charDefault";
import CharArcSR6 from "./components/npc/charArcSR6";
import {createTheme, createThemePaletteBasic, createThemePaletteElevation} from "@arwes/design";
import {ThemeProvider} from "@emotion/react";
const ROOT_FONT_FAMILY = '"Titillium Web", sans-serif';

const generalAnimator = {duration: {enter: 300, exit: 300}};

const themeSettings = {
    palette: {
        transparent: {
            main: '#fff',
        },
    },
};

class Theme extends React.Component {
    render() {
        return (
            <ArwesThemeProvider themeSettings={themeSettings}>
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
            },
            {
                path: "impressum",
                element: <Impressum/>
            },
            {
                path: "npcs/:id",
                element:<NpcTabsHeader selectedTab='default' loader={npcLoader}/>,
            },
            {
                path: "npcs/:id/gallery",
                element: <NpcTabsHeader selectedTab='gallery' loader={npcLoader}/>,
            },
            {
                path: "npcs/:id/sr6",
                element: <NpcTabsHeader selectedTab='sr6' loader={npcLoader}/>,
            },
            {
                path: "npcs/",
                element: <NPCList/>,
            },
            {
                path: "npcs/create",
                element: <Prompt/>,
            },
            {
                path: "locations/:id",
                element: <LocationTabsHeader selectedTab={'default'}/>,
            },
            {
                path: "locations/:id/gallery",
                element: <LocationTabsHeader selectedTab={'gallery'}/>,
            },
            {
                path: "locations/:id/reviews",
                element: <LocationTabsHeader selectedTab={'reviews'}/>,
            },
            {
                path: "locations/",
                element: <LocationList/>,
            },
            {
                path: "locations/create",
                element: <PromptLocation/>,
            },
            {
                path: "customs/:id",
                element: <CustomComplete/>,
            },
            {
                path: "customs/:id/gallery",
                element: <ImageGallery factor={{'x': 5, 'y': 5}} attribute={'Aussehen'} entity_type={'customs'}/>,
            },
            {
                path: "customs/",
                element: <CustomList/>,
            },
            {
                path: "customs/create",
                element: <CustomPrompt/>,
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