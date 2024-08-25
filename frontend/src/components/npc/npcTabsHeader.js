import React, {createContext, useEffect, useState} from "react";
import {useLocation, useParams, Link, useNavigation} from "react-router-dom";
import Tabs from "../cyberpunk/tabs";
import CharDefault from "./tabDefault";
import CharArcSR6 from "./charArcSR6";
import Warning from "../warning";
import active_image from "../../active_image";
import ImageGallery from "../image_gallery";
import {Helmet} from "react-helmet";
import image_path from "../../image_path";
import i18next from "i18next";
import OverlayButtons from "../../overlayButtons";
import EditButton from "../../icons/editButton";
import SaveButton from "../../icons/saveButton";
import {useEntity} from "../entityProvider";
import {CustomFrame} from "../cyberpunk/CustomFrame";




function NpcTabsHeader({selectedTab}) {
  const {id} = useParams();
  const {entity, _} = useEntity();

    const tabs = {
        'default': {
            url: `/npcs/${id}`,
            element: <CharDefault/>,
            estimatedTime: 1000,
        },
        'sr6': {
            url: `/npcs/${id}/sr6`,
            element: <CharArcSR6/>,
            estimatedTime: 3500,
        },
        'gallery': {
            url: `/npcs/${id}/gallery`,
            element: <ImageGallery entityType={entity.entityType} factor={{'x': 4, 'y': 5}}
                                   attribute={'appearance'}/>,
            estimatedTime: 1000,
        }
    };

    const warning = <Warning text={i18next.t("npc_entity_is_not_published")}/>;
    let activeImage = active_image(entity.image_objects) || {}
    return (
        <div key={selectedTab} style={{display: 'flex', flexDirection: 'column', maxWidth: '1270px', width: '100%', margin: 5, paddingBottom: 15}}>

            <Helmet>
                <title>Schattenakte - {entity.values['name']}</title>
                <meta name="description" content={entity.values['catchphrase']}/>
                <meta property="og:title" content={`Schattenakte - {entity.values['name']}`}/>
                <meta property="og:description" content={entity.values['catchphrase']}/>
                <meta property="og:image" content={image_path('npcs', activeImage.name, true)}/>
            </Helmet>

            {entity.state === 'Unpublished' && warning}
            <Tabs tabs={tabs}/>
            <OverlayButtons>
                <SaveButton/>
            </OverlayButtons>
        </div>
    )
}
//                <EditButton/>
export default NpcTabsHeader;