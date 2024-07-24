import React, {useState} from "react";
import {
    Text
} from "@arwes/core";
import {useLoaderData} from "react-router";
import image_path from "../../image_path";
import active_image from "../../active_image";
import Comment from "./comment";
import EntityList from "../entity/list";
import { Link } from "react-router-dom";
import Card from "../cyberpunk/card";
import Blockquote from "../cyberpunk/blockquote";
import EntityLoader from "../../loader/entity_loader";
import {Animator} from "@arwes/animation";

class LocationListItem extends React.Component {

    render() {
        let activeImage = active_image(this.props.entity.image_objects) || {}

        let comments = this.props.entity.values['reviews']
        let comment = undefined

        const cardStyle = {
        width: 310,
        height: 450
        };


        if (comments !== undefined) {
            let random_nr = Math.floor(Math.random() * comments.length);
            comment = comments[random_nr]
        }

        return (<div style={{margin: '15px 7.5px 0px 7.5px'}}>
                <Link to={'/locations/' + this.props.entity.id}>
                    <Card
                        image={{
                            src: image_path('locations', activeImage.name, true),
                            alt: this.props.entity.image_generator_description
                        }}
                        title={this.props.entity.values['name']}
                        hover
                        style={cardStyle}
                    >
                        <div>
                            <Text>
                                <div className="clampText">
                                    {this.props.entity.values['type']}
                                </div>
                            </Text>
                        </div>
                        <Blockquote style={{height: '114px'}}>
                            <Comment name={comment?.name} rating={comment?.rating} comment={comment?.comment}/>
                        </Blockquote>

                    </Card>
                </Link>
            </div>
        )
    }
}


const LocationList = props => {
    const loader = new EntityLoader('locations')

    const createItem = (entity) => {
        return <LocationListItem key={'LocationListItem' + entity.id} entity={entity}/>
    }

    return <EntityList createItem={createItem} loader={loader} {...props}></EntityList>
}

export default LocationList;
