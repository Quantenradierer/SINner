import active_image from "../../active_image";
import {Link} from "react-router-dom";
import Card from "../cyberpunk/card";
import image_path from "../../image_path";
import Blockquote from "../cyberpunk/blockquote";
import {List, Text} from "@arwes/core";
import React, {useState} from "react";
import {Animator} from "@arwes/animation";

function cutStreetname(name) {
    const match = name.match(/['"](.*?)['"]/);
    return match ? match[1] : name;
}

function NPCListItem(props) {
    let activeImage = active_image(props.entity.image_objects) || {}
    const cardStyle = {
        height: 500,
        imageHeight: 300,
    };

    return (<div style={{minWidth: 250, maxWidth: 310, width: '100%', margin: '15px 7.5px 0px 7.5px'}}>
            <Link to={'/npcs/' + props.entity.id}>

                <Card
                    image={{
                        src: image_path('npcs', activeImage.name, true),
                        alt: props.entity.image_generator_description
                    }}
                    title={cutStreetname(props.entity.values["name"])}
                    landscape
                    hover
                    style={cardStyle}
                    {...cardStyle}
                >
                    <Blockquote style={{height: '52px'}}>
                        <Text>
                            <div className="clampText">
                                {props.entity.values['catchphrase']}
                            </div>
                        </Text>
                    </Blockquote>
                    <div style={{height: '10px'}}></div>
                    <List>
                        <li><Text><b>Metatyp:</b> {props.entity.values['metatype']}</Text></li>
                        <li><Text><b>Beruf:</b> {props.entity.values['profession']}</Text></li>
                    </List>
                </Card>
            </Link>
        </div>
    )
}

export default NPCListItem;