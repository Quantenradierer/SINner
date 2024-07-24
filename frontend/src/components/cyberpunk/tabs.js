import React, {useEffect, useState} from "react";

import {FramePentagon, LoadingBars, Text} from "@arwes/core";
import {useLoaderData} from "react-router";
import useRefreshEntityCard from "../use_refresh_entity_card";
import {useLocation, useParams, Link, useNavigation} from "react-router-dom";
import i18n from "../../i18n";
import EncryptedText from "./encryptedText";

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
    var tabs = Object.keys(props.tabs).map((key) => {
        return <Link key={'Tab' + key} to={props.tabs[key].url}>
            <FramePentagon squareSize={20} hideShapes={props.selectedTab != key} className='rotated' style={{margin: 0}}>
                <div className='rotated'>{i18n.t(`tab_header_${props.entityType}_${key}`)}</div>
            </FramePentagon>
        </Link>
    })
    const element = props.tabs[props.selectedTab].element
    const estimatedTime = props.tabs[props.selectedTab].estimatedTime
    return (
        <div style={{display: 'flex', flexDirection: 'column', width: 1250}}>
            <div style={{margin: 0, display: 'flex', justifyContent: 'left', alignItems: 'flex-end'}}>
                {tabs}
            </div>
            <div>
                {!props.loading && element}
                {props.loading && <LoadingTab estimatedTime={estimatedTime}/>}
            </div>
        </div>
    )
}


export default Tabs;