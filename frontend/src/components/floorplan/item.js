import React from "react";
import {Link} from "react-router-dom";
import {Text} from "@arwes/core";
import active_image from "../../active_image";
import image_path from "../../image_path";
import Card from "../cyberpunk/card";
import i18next from "../../i18n";
import {pretty} from "./overlay";

const FloorplanListItem = ({entity}) => {
    const image = active_image(entity.image_objects) || {};
    const params = entity.values.params || {};
    const floors = (params.floors_above || 1) + (params.floors_below || 0);

    return (
        <div style={{minWidth: 250, maxWidth: 310, width: '100%', margin: '15px 7.5px 0px 7.5px'}}>
            <Link to={'/floorplans/' + entity.id}>
                <Card
                    image={{src: image_path('floorplans', image, true), alt: entity.values.name}}
                    title={pretty(entity.values.name || '')}
                    hover
                    style={{width: 310, height: 420}}
                >
                    <Text>
                        <div className="clampText">
                            {pretty(params.building_type || '')} · {params.wealth && pretty(params.wealth)}
                        </div>
                        <div>{i18next.t('floorplan_floors', {count: floors})}</div>
                    </Text>
                </Card>
            </Link>
        </div>
    );
};

export default FloorplanListItem;
