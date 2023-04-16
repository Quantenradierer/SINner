import React from "react";
import {Button, FrameBox, FrameLines, Text} from "@arwes/core";
import Impressum from "./impressum";
import {useLoaderData} from "react-router";
import {Link, useNavigate, useNavigation} from "react-router-dom";


function redirectToImpressum() {
    window.location.href = '/impressum'
}

const Footer = props => {
    return (
            <Button FrameComponent={FrameLines}
                         style={{textAlign: 'center'}}
                         onClick={redirectToImpressum}>
                    Impressum / Disclaimer / Datenschutz / Nutzungsbedingungen
        </Button>
    )
}

export default Footer;
