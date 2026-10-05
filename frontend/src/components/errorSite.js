import React from "react";
import i18next from "../i18n";
import {Button, FrameLines, FramePentagon, Text} from "@arwes/core";


const ErrorPage = props => {
    return (
        <FramePentagon style={{maxWidth: 800, width: '100%', margin: 10}}>
            <Text>
                <p>
                    <b>{i18next.t("error_title")}</b><br/>
                    <br/>
                    {i18next.t("error_greeting")}<br/>
                    <br/>
                    {i18next.t("error_body")}
                </p>
            </Text>
        </FramePentagon>
    )
}

export default ErrorPage;
