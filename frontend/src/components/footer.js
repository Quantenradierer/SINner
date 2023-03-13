import React from "react";
import {Button, FrameLines} from "@arwes/core";
import Impressum from "./impressum";

class Footer extends React.Component {
    constructor(props) {
        super(props);

        this.state = {showImpressum: false};

        this.showImpressum = this.showImpressum.bind(this)
    }

    showImpressum() {
        this.setState({showImpressum: true})
    }


    render() {

        if (this.state.showImpressum) {
            return (
                <Impressum/>
            )
        } else {
            return (
                <Button FrameComponent={FrameLines}
                        style={{textAlign: 'center'}}
                        onClick={this.showImpressum}>
                    Impressum / Datenschutz / Nutzungsbedingungen
                </Button>
            )
        }
    }
}

export default Footer;
