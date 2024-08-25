import React, {useEffect, useState} from "react";

import {FramePentagon, LoadingBars, Text} from "@arwes/core";
import {useLoaderData} from "react-router";
import useRefreshEntityCard from "../use_refresh_entity_card";
import {useLocation, useParams, Link, useNavigation} from "react-router-dom";
import i18n from "../../i18n";
import EncryptedText from "./encryptedText";
import {useEntity} from "../entityProvider";
import {CustomFrame} from "./CustomFrame";
import {Animator} from "@arwes/animation";

function LoadingTab(props) {
      const [progress, setProgress] = React.useState(0);

      React.useEffect(() => {
        const timeout = setTimeout(() => {
          if (progress < 100) {
            setProgress(progress + 1);
          }
        }, props.estimatedTime / 100);
        return () => clearTimeout(timeout);
      }, [progress]);

    return (
        <FramePentagon style={{width: '100%', height: '100%'}}>
            <div style={{display: "flex", flexDirection: 'column'}}>
                <LoadingBars determinate progress={progress} length={20}/>
                <Text style={{textAlign: 'center'}}>{i18n.t('tab_loading_text')}</Text>
            </div>
        </FramePentagon>
    )

}

function Tabs(props) {
    const {entity, _} = useEntity();

    var tabs = Object.keys(props.tabs).map((key) => {
        return <Link key={'Tab' + key} to={props.tabs[key].url}>
            <CustomFrame squareSize={20} hideShapes={entity.selectedTab != key} style={{margin: '0px 0px 0px 0px'}}>
                <div>{i18n.t(`tab_header_${entity.entityType}_${key}`)}</div>
            </CustomFrame>
        </Link>
    })
    const element = props.tabs[entity.selectedTab].element
    const estimatedTime = props.tabs[entity.selectedTab].estimatedTime
    return (

        <div style={{display: 'flex', flexDirection: 'column'}}>
            <div style={{margin: 0, display: 'flex', justifyContent: 'left', alignItems: 'flex-end'}}>
                {tabs}
            </div>
            <div>
                <Animator  key={entity.selectedTab}>

                <FramePentagon key={entity.selectedTab} className='surrounding-frame' style={{padding: 0, margin: 0}} squareSize={35}>
                    {!entity.loading && element}
                    {entity.loading && <LoadingTab estimatedTime={estimatedTime}/>}
                </FramePentagon>
                </Animator>
            </div>
        </div>
    )
}


export default Tabs;