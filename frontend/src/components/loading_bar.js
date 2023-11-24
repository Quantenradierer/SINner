import React from "react";
import {Button, FrameCorners, FrameLines, FramePentagon, List, LoadingBars, Text} from "@arwes/core";
import {Animator} from "@arwes/animation";
import api from "../axios";
import i18next from "../i18n";
import {useLoaderData} from "react-router";
import {useNavigate, useNavigation} from "react-router-dom";
import LocationCard from "./location/location_card";
import CommentCard from "./location/comment_card";
import Comment from "./location/comment";


class LoadingBar extends React.Component {
    render() {
        return <FrameLines style={{width: '100%'}}>
                    <Animator animator={{
                        activate: true,
                        manager: 'stagger',
                        duration: {stagger: 300}
                    }}>
                        <Text>Bitte warten...</Text><br/>
                        <Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text>
                        <Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text><Text>.</Text>
                    </Animator>
                </FrameLines>


    }
}


export default LoadingBar;
