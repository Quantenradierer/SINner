import React from "react";
import {List, Text} from "@arwes/core";
import {useLoaderData} from "react-router";
import image_path from "../../image_path";
import active_image from "../../active_image";
import EntityList from "../entity/list";
import { Link } from "react-router-dom";
import Card from "../cyberpunk/card";
import Blockquote from "../cyberpunk/blockquote";

function cutStreetname(name) {
    const match = name.match(/['"](.*?)['"]/);
    return match ? match[1] : name;
}

function NPCListItem(props) {
    let activeImage = active_image(props.entity.image_objects) || {}
    const cardStyle = {
        minWidth: 270,
        maxWidth: 300,
        height: 500
    };

    return (<div style={{margin: '15px 7.5px 0px 7.5px'}}>

            <Link to={'/npcs/' + props.entity.id}>
                <Card
                    image={{
                        src: image_path('npcs', activeImage.name, true),
                        alt: props.entity.image_generator_description
                    }}
                    title={cutStreetname(props.entity.primary_values['Name'])}
                    landscape
                    hover
                    style={cardStyle}
                >
                    <Blockquote style={{height: '52px'}}>
                        <Text>
                            <div className="clampText">
                                {props.entity.primary_values['Catchphrase']}
                            </div>
                        </Text>
                    </Blockquote>
                    <div style={{height: '10px'}}></div>
                    <List>
                        <li><Text><b>Metatyp:</b> {props.entity.primary_values['Metatyp']}</Text></li>
                        <li><Text><b>Beruf:</b> {props.entity.primary_values['Beruf']}</Text></li>
                    </List>
                </Card>
            </Link>
        </div>
    )
}



const NPCList = props => {
    const entities = useLoaderData()

    const items = [];
    for (const entity of entities.results) {
        items.push(<NPCListItem entity={entity} key={entity.id}/>)
    }
    return <EntityList entities={entities} {...props}>{items}</EntityList>
}

export default NPCList;
