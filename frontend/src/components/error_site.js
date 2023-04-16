import React from "react";
import {Button, FrameLines, FramePentagon, Text} from "@arwes/core";


const ErrorPage = props => {
    return (
        <FramePentagon>
            <Text>
                <p>
                    <b>Ups! Falsche Abbiegung in der Matrix genommen...</b><br/>
                    <br/>
                    Hey Chummer,<br/>
                    <br/>
                    es sieht so aus, als hätten wir eine unerwartete Störung in der Matrix. Vielleicht wurde die
                    gesuchte Verbindung von einem feindlichen Megakonzern gelöscht oder ein
                    rachsüchtiger Sprite hat sie in den digitalen Abgrund gezogen.
                </p>
            </Text>
        </FramePentagon>
    )
}

export default ErrorPage;
