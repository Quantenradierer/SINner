import React, {useState} from "react";
import Warning from "../warning";
import i18next from "../../i18n";
import active_image from "../../active_image";
import {Helmet} from "react-helmet";
import image_path from "../../image_path";
import ImageGallery from "../image_gallery";
import {useLoaderData} from "react-router";
import useRefreshEntityCard from "../use_refresh_entity_card";
import {useLocation, useParams, Link} from "react-router-dom";
import Tabs from "../cyberpunk/tabs";
import LocationCard from "./location_card";
import CommentCard from "./comment_card";
import useEntitySchema from "../../loader/useEntitySchema";


function LocationTabsHeader(props) {
    const { id } = useParams();
    const entityType = 'locations';
    const { entity, loading, error } = useEntitySchema(entityType, id, props.selectedTab);

    const tabs = {
        'default': {
            url: `/locations/${id}`,
            element: <LocationCard entity={entity}/>,
            estimatedTime: 1000
        },
        'reviews': {
            url: `/locations/${id}/reviews`,
            element: <CommentCard entity={entity}/>,
            estimatedTime: 5000
        },
        'gallery': {
            url: `/locations/${id}/gallery`,
            element: <ImageGallery entity={entity} entityType={'locations'} factor={{'x': 5, 'y': 4}}
                                   attribute={'appearance'}/>,
            estimatedTime: 1000
        }
    };

    let activeImage = active_image(entity.image_objects) || {}
    return (
        <div style={{display: 'flex', flexDirection: 'column', maxWidth: '1250', width: '100%'}}>
            <Helmet>
                <title>Schattenakte - {entity.values['name']}</title>
                <meta name="description" content={entity.values['type']}/>
                <meta property="og:title" content="Schattenakte - {entity.values['name']}"/>
                <meta property="og:description" content={entity.values['type']}/>
                <meta property="og:image" content={image_path('locations', activeImage.name, true)}/>
            </Helmet>

            <Tabs tabs={tabs} loading={loading} entityType={entityType} selectedTab={props.selectedTab || 'default'}/>
        </div>
    )
}


export default LocationTabsHeader;