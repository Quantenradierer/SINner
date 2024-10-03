import React, {useState} from "react";
import {Button, FramePentagon, Text} from "@arwes/core";
import {Link} from "react-router-dom";
import {Helmet} from "react-helmet";
import i18n from "../i18n";

export const Profile = () => {
    return (
        <FramePentagon style={{flex: 1, maxWidth: 300, width: '100%'}}>
            <Helmet>
                <title>{i18n.t(`page_profile_title`)}</title>
            </Helmet>

            <h1>Account</h1>
            <Text>An dieser Seite wird dran noch gearbeitet.</Text>
            <br/>
            <br/>
            <br/>
            <Link to={'/logout'}>
                <FramePentagon>
                    <Text>Logout</Text>
                </FramePentagon>
            </Link>

        </FramePentagon>
    )
}
