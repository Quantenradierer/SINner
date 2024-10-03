import React from 'react';
import ReactDOM from 'react-dom';
import {AnimatorGeneralProvider} from '@arwes/animation';
import {ArwesThemeProvider, LoadingBars, StylesBaseline} from '@arwes/core';
import './index.css';
import NPCPrompt from "./components/npc/npcPrompt";
import {createBrowserRouter, Navigate, Outlet, redirect, RouterProvider, useNavigate} from "react-router-dom";
import Impressum from "./components/impressum";
import Header from "./components/header";
import ErrorPage from "./components/errorSite";
import Login from "./components/account/login";
import Logout from "./components/account/logout";
import ImageGallery from "./components/imageGallery";
import LocationPrompt from "./components/location/locationPrompt";
import EntityLoader from "./loader/entity_loader";
import CustomPrompt from "./components/custom/prompt";
import CustomComplete from "./components/custom/complete";
import Feedback from "./components/feedback";
import Register from "./components/account/register";
import UserProvider from './userProvider';
import Navigation from "./navigation";
import NpcTabsHeader from "./components/npc/npcTabsHeader";
import LocationTabsHeader from "./components/location/locationTabsHeader";
import {EntityProvider} from "./components/entityProvider";
import EntityList from "./components/entity/list";
import i18n from "./i18n";
import {Profile} from "./components/profile";
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
            <div style={{maxWidth: '1350px', width: '100%', padding: 10, display: 'flex', justifyContent: 'center'}}>
                {props.outlet ? props.outlet : <Outlet/>}
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
        errorElement: <Root outlet={<ErrorPage/>}/>,
        children: [
            {
                path: "navi",
                element: <Navigation/>,
            },
            {
                path: "",
                element: <Navigate to="/npcs" replace />,
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
                element: <EntityList filter={['Npc']} emptyText={i18n.t('npc_list_empty_text')}/>,
            },
            {
                path: "npcs/create",
                element: <NPCPrompt/>,
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
                element: <EntityList filter={['Location']} emptyText={i18n.t('location_list_empty_text')}/>,
            },
            {
                path: "locations/create",
                element: <LocationPrompt/>,
            },
            {
                path: "collections/create",
                element: <NPCPrompt/>,
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
                element: <EntityList filter={['Custom']}/>,
            },
            {
                path: "customs/create",
                element: <Navigate to="/npcs/create" replace />,
            },
            {
                path: "collections/",
                element: <EntityList filter={['Npc', 'Location', 'Custom']} favorites={true} emptyText={i18n.t('favorite_list_empty_text')}/>,
            },
            {
                path: "profile/",
                element: <Profile/>,
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