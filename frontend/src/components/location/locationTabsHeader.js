import React, {useState} from "react";
import Warning from "../warning";
import i18next from "../../i18n";
import active_image from "../../active_image";
import {Helmet} from "react-helmet";
import image_path from "../../image_path";
import ImageGallery from "../imageGallery";
import {useLoaderData} from "react-router";
import useRefreshEntityCard from "../use_refresh_entity_card";
import {useLocation, useParams, Link} from "react-router-dom";
import Tabs from "../entity/tabs";
import TabDefault from "./tabDefault";
import TabReviews from "./tabReviews";
import useEntitySchema from "../../loader/useEntitySchema";
import {useEntity} from "../entityProvider";
import OverlayButtons from "../../overlayButtons";
import SaveButton from "../../icons/saveButton";
import is_logged_in from "../../is_loggin_in";
import FavoriteButton from "../../icons/favoriteButton";


function LocationTabsHeader({selectedTab}) {
    const { id } = useParams();
    const {entity, _} = useEntity();

    const tabs = {
        'default': {
            url: `/locations/${id}`,
            name: i18next.t('tab_header_locations_default'),
            element: <TabDefault/>,
            estimatedTime: 1000
        },
        'gallery': {
            url: `/locations/${id}/gallery`,
            name: i18next.t('tab_header_locations_gallery'),
            element: <ImageGallery factor={{'x': 5, 'y': 4}}
                                   attribute={'appearance'}/>,
            estimatedTime: 1000
        }
    };

    const warning = <Warning text={i18next.t("location_entity_is_not_published")}/>;
    let activeImage = active_image(entity.image_objects) || {}
    return (
        <div key={selectedTab + entity.state}
             style={{display: 'flex', flexDirection: 'column', maxWidth: '1270px', width: '100%', margin: 5}}>
            <Helmet>
                <title>Schattenakte - {entity.values['name']}</title>
                <meta name="description" content={entity.values['type']}/>
                <meta property="og:title" content="Schattenakte - {entity.values['name']}"/>
                <meta property="og:description" content={entity.values['type']}/>
                <meta property="og:image" content={image_path('locations', activeImage.name, true)}/>
            </Helmet>

            {entity.state === 'Unpublished' && warning}
            <Tabs tabs={tabs}/>
            <OverlayButtons>
                <SaveButton/>
                {is_logged_in() && <FavoriteButton/>}
            </OverlayButtons>
        </div>
    )
}


export default LocationTabsHeader;