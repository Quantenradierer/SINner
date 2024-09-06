import React from 'react';
import ReactDOM from 'react-dom';
import {AnimatorGeneralProvider} from '@arwes/animation';
import {ArwesThemeProvider, LoadingBars, StylesBaseline} from '@arwes/core';
import './index.css';
import Prompt from "./components/npc/prompt";
import NPCList from "./components/npc/list";
import {createBrowserRouter, Navigate, Outlet, redirect, RouterProvider, useNavigate} from "react-router-dom";
import Impressum from "./components/impressum";
import Header from "./components/header";
import ErrorPage from "./components/errorSite";
import Login from "./components/account/login";
import Logout from "./components/account/logout";
import ImageGallery from "./components/imageGallery";
import PromptLocation from "./components/location/prompt";
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
import {EntityProvider} from "./components/entityProvider";
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
                element:<EntityProvider entityType='npcs' selectedTab='default'><NpcTabsHeader/></EntityProvider>,
            },
            {
                path: "npcs/:id/gallery",
                element: <EntityProvider entityType='npcs' selectedTab='gallery'><NpcTabsHeader/></EntityProvider>,
            },
            {
                path: "npcs/:id/sr6",
                element: <EntityProvider entityType='npcs' selectedTab='sr6'><NpcTabsHeader/></EntityProvider>,
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
                element: <EntityProvider entityType='locations' selectedTab='default'><LocationTabsHeader/></EntityProvider>,
            },
            {
                path: "locations/:id/gallery",
                element: <EntityProvider entityType='locations' selectedTab='gallery'><LocationTabsHeader/></EntityProvider>,
            },
            {
                path: "locations/:id/reviews",
                element: <EntityProvider entityType='locations' selectedTab='reviews'><LocationTabsHeader/></EntityProvider>,
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