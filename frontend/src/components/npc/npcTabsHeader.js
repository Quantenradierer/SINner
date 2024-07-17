import React, {useState} from "react";
import Warning from "../warning";
import i18next from "../../i18n";
import active_image from "../../active_image";
import {Helmet} from "react-helmet";
import image_path from "../../image_path";
import {FramePentagon} from "@arwes/core";
import CharArcSR6 from "./charArcSR6";
import NPCCard from "./npc_card";
import ImageGallery from "../image_gallery";
import {useLoaderData} from "react-router";
import useRefreshEntityCard from "../use_refresh_entity_card";
import {useLocation, useParams, Link} from "react-router-dom";


function NpcTabsHeader(props) {
    const loaded_entity = useLoaderData()
    const [entity, setEntity] = useState(loaded_entity);
    useRefreshEntityCard('npcs', entity, setEntity)
    const tab = props.selectedTab || 'story'
    //const [tab, setTab] = useState(props.selectedTab || 'story')
    const { id } = useParams();

    let warning = ''
    if (entity.image_objects.length == 0) {
        warning = <Warning text={i18next.t('image_generation_in_progress')}/>
    }
    let activeImage = active_image(entity.image_objects) || {}

    return (
        <div style={{display: 'flex', flexDirection: 'column'}}>
            <Helmet>
                <title>Schattenakte - {entity.values['Name']}</title>
                <meta name="description" content={entity.values['Catchphrase']}/>
                <meta property="og:title" content={`Schattenakte - {entity.values['Name']}`}/>
                <meta property="og:description" content={entity.values['Catchphrase']}/>
                <meta property="og:image" content={image_path('npcs', activeImage.name, true)}/>
            </Helmet>

            {warning}

            <div style={{margin: 0, display: 'flex', justifyContent: 'left', alignItems: 'flex-end'}}>
                <Link to={`/npcs/${id}`}><FramePentagon squareSize={20} hideShapes={tab != 'story'} className='rotated' style={{margin: 0}}>
                    <div className='rotated'>Story</div>
                </FramePentagon></Link>
                <Link to={`/npcs/${id}/sr6`}><FramePentagon squareSize={20} hideShapes={tab != 'sr6'} className='rotated' style={{margin: 0}}>
                    <div className='rotated'>SR6</div>
                </FramePentagon></Link>
                 <Link to={`/npcs/${id}/gallery`}><FramePentagon inversed squareSize={20} hideShapes={tab != 'gallery'} className='rotated' style={{margin: 0}}>
                   <div className='rotated'>Galerie</div>
                </FramePentagon></Link>
            </div>

            <div style={{width: 1050}}>
                {tab == 'story' && <NPCCard entity={entity}/>}
                {tab == 'sr6' && <CharArcSR6 entity={entity} entitytype={'npcs'}/>}
                {tab == 'gallery' && <ImageGallery entity={entity} entity_type={'npcs'} factor={{'x': 4, 'y': 5}} attribute={'Detailliertes Aussehen'}/>}
            </div>
        </div>
    )

}


export default NpcTabsHeader;