import React from "react";
import {Blockquote, Button, Card, FrameLines, List, Table, Text} from "@arwes/core";

class ReloadButton extends React.Component {

    reloadWebsite() {
        window.location.replace('random');
    }

    render() {
        return (
            <Button FrameComponent={FrameLines} onClick={this.reloadWebsite}>
                <Text>Lade einen anderen zufälligen NPC</Text>
            </Button>
        )
    }
}

export default ReloadButton;
