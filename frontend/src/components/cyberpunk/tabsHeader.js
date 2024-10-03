import {Link, useLocation} from "react-router-dom";
import i18next from "i18next";
import {CustomFrame} from "./CustomFrame";
import React from "react";
import EntityList from "../entity/list";


export const TabsHeader = ({tabs}) => {
    const location = useLocation();


    var tabsElements = Object.keys(tabs).map((key) => {
        const isActiveTab = location.pathname === tabs[key].url;
        return <Link key={'Tab' + key} to={tabs[key].url}>
            <CustomFrame squareSize={20} hideShapes={!isActiveTab} style={{margin: '0'}}>
                <div>{tabs[key].name}</div>
            </CustomFrame>
        </Link>
    })

    return <div style={{width: '100%', display: 'flex', justifyContent: 'center'}}>
        {tabsElements}
    </div>
}