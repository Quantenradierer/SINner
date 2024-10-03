import React, {useEffect, useState} from "react";

import {FramePentagon, LoadingBars, Text} from "@arwes/core";
import {useLoaderData} from "react-router";
import useRefreshEntityCard from "../use_refresh_entity_card";
import {useLocation, useParams, Link, useNavigation} from "react-router-dom";
import i18n from "../../i18n";
import EncryptedText from "../cyberpunk/encryptedText";
import {useEntity} from "../entityProvider";
import {CustomFrame} from "../cyberpunk/CustomFrame";
import {Animator} from "@arwes/animation";
import "../../index.css";

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
            <div style={{display: "flex", flexDirection: 'column', padding: 10}}>
                <LoadingBars determinate progress={progress} length={20}/>
                <Text style={{textAlign: 'center'}}>{i18n.t('tab_loading_text')}</Text>
            </div>
    )

}

function Tabs(props) {
    const {entity, _} = useEntity();

    var tabs = Object.keys(props.tabs).map((key) => {
        return <Link key={'Tab' + key} to={props.tabs[key].url}>
            <CustomFrame squareSize={20} hideShapes={entity.selectedTab != key} style={{margin: '0'}}>
                <div>{props.tabs[key].name}</div>
            </CustomFrame>
        </Link>
    })
    const element = props.tabs[entity.selectedTab].element
    const estimatedTime = props.tabs[entity.selectedTab].estimatedTime
    return (

        <div style={{display: 'flex', flexDirection: 'column'}}>
            <div className="no-print" style={{margin: 0, display: 'flex', justifyContent: 'left', alignItems: 'flex-end'}}>
                {tabs}
            </div>
            <div>
                <Animator key={entity.selectedTab + '_' + entity.loading}>
                    <FramePentagon className="no-print-arwes-frame surrounding-frame" key={entity.selectedTab + '_' + entity.loading} style={{padding: 0, margin: 0}} squareSize={35}>
                        {!entity.loading && element}
                        {entity.loading && <LoadingTab key='loading-tab' estimatedTime={estimatedTime}/>}
                    </FramePentagon>
                </Animator>
            </div>
        </div>
    )
}


export default Tabs;