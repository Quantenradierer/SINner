import React from "react";
import {Blockquote, Button, Card, FrameLines, List, Table, Text} from "@arwes/core";

class ReloadButton extends React.Component {
    constructor(props) {
        super(props);
        this.loadRandom = this.loadRandom.bind(this)
    }

    loadRandom() {
        this.props.loadNpc(0)
    }

    render() {
        return (
            <Button FrameComponent={FrameLines} onClick={this.loadRandom}>
                <Text>Lade einen anderen zufälligen NPC</Text>
            </Button>
        )
    }
}

export default ReloadButton;
