import React, {useState} from "react";
import {
    Blockquote,
    Button,
    Card,
    FrameCorners,
    FrameLines,
    FramePentagon,
    LoadingBars,
    Table,
    Text
} from "@arwes/core";
import {useLoaderData} from "react-router";
import image_path from "../../image_path";
import active_image from "../../active_image";
import Comment from "./comment";
import List from "../entity/list";


class LocationListItem extends React.Component {

    render() {
        let activeImage = active_image(this.props.entity.image_objects) || {}

        let comments = this.props.entity.values['Bewertungen']
        let comment = undefined

        if (comments !== undefined) {
            let random_nr = Math.floor(Math.random() * comments.length);
            comment = comments[random_nr]
        }

        return (<div style={{margin: 15}}>

                <a href={'/locations/' + this.props.entity.id}>
                    <Card
                        image={{
                            src: image_path('locations', activeImage.name),
                            alt: this.props.entity.image_generator_description
                        }}
                        title={this.props.entity.primary_values['Name']}
                        hover
                        style={{}}
                    >
                        <div style={{margin: '0px 0px 10px 0px'}}>
                            <Text>{this.props.entity.primary_values['Typ']}</Text>
                        </div>
                        <Blockquote>
                            <Comment name={comment?.name} rating={comment?.rating} comment={comment?.comment}/>
                        </Blockquote>

                    </Card>
                </a>
            </div>
        )
    }
}


const LocationList = props => {
    const entities = useLoaderData()

    const items = [];
    for (const entity of entities.results) {
        items.push(<LocationListItem entity={entity} key={entity.id}/>)
    }

    return <List entities={entities} {...props}>{items}</List>
}

export default LocationList;
