import React, {useEffect, useState} from "react";
import {useLocation, useParams, Link, useNavigation} from "react-router-dom";
import Tabs from "../cyberpunk/tabs";
import CharDefault from "./charDefault";
import CharArcSR6 from "./charArcSR6";
import Warning from "../warning";
import active_image from "../../active_image";
import ImageGallery from "../image_gallery";
import {Helmet} from "react-helmet";
import image_path from "../../image_path";
import i18next from "i18next";
import useEntitySchema from "../../loader/useEntitySchema";




function NpcTabsHeader(props) {
    const {id} = useParams();
    const entityType = 'npcs';
    const {entity, loading, error} = useEntitySchema(entityType, id, props.selectedTab);

    const tabs = {
        'default': {
            url: `/npcs/${id}`,
            element: <CharDefault entity={entity}/>,
            estimatedTime: 1000,
        },
        'sr6': {
            url: `/npcs/${id}/sr6`,
            element: <CharArcSR6 entity={entity}/>,
            estimatedTime: 3500,
        },
        'gallery': {
            url: `/npcs/${id}/gallery`,
            element: <ImageGallery entity={entity} entityType={entityType} factor={{'x': 4, 'y': 5}}
                                   attribute={'appearance'}/>,
            estimatedTime: 1000,
        }
    };

    let activeImage = active_image(entity.image_objects) || {}
    return (
        <div key={props.selectedTab} style={{display: 'flex', flexDirection: 'column', maxWidth: '1250px', width: '100%'}}>
            <Helmet>
                <title>Schattenakte - {entity.values['name']}</title>
                <meta name="description" content={entity.values['catchphrase']}/>
                <meta property="og:title" content={`Schattenakte - {entity.values['name']}`}/>
                <meta property="og:description" content={entity.values['catchphrase']}/>
                <meta property="og:image" content={image_path('npcs', activeImage.name, true)}/>
            </Helmet>

            <Tabs tabs={tabs} loading={loading} entityType={entityType} selectedTab={props.selectedTab || 'default'}/>
        </div>
    )
}

export default NpcTabsHeader;