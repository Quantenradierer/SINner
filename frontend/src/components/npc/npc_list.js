import React from "react";
import {Blockquote, Card, List, Text} from "@arwes/core";
import {useLoaderData} from "react-router";
import image_path from "../../image_path";
import active_image from "../../active_image";
import EntityList from "../entity/list";
import { Link } from "react-router-dom";

function NPCListItem(props) {
    let activeImage = active_image(props.entity.image_objects) || {}

    return (<div style={{margin: 15}}>

            <Link to={'/npcs/' + props.entity.id}>
                <Card
                    image={{
                        src: image_path('npcs', activeImage.name, true),
                        alt: props.entity.image_generator_description
                    }}
                    title={props.entity.primary_values['Name']}
                    landscape
                    hover
                    style={{}}
                >
                    <Blockquote>
                        <Text>
                            {props.entity.primary_values['Catchphrase']}
                        </Text>
                    </Blockquote>

                    <List>
                        <li><Text><b>Metatyp:</b> {props.entity.primary_values['Metatyp']}</Text></li>
                        <li><Text><b>Beruf:</b> {props.entity.primary_values['Beruf']}</Text></li>
                        <li><Text><b>Eigenarten:</b> {props.entity.primary_values['Eigenarten']}</Text></li>
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
