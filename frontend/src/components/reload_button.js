import React from "react";
import {Blockquote, Button, Card, FrameLines, FramePentagon, List, Table, Text} from "@arwes/core";
import api from "../axios";

class ReloadButton extends React.Component {
    constructor(props) {
        super(props);
        this.loadRandom = this.loadRandom.bind(this)
        this.loadNext = this.loadNext.bind(this)
        this.loadPrev = this.loadPrev.bind(this)
    }

    loadRandom() {
        let self = this;
        let npc;

        api.get('/api/npc_creator/npc/random?')
            .then(function (response) {
                npc = response.data
            })
            .catch(function (error) {
                npc = {id: 'ERROR', image_url: 'npc_load_error.png', attributes: {'Name': 'ERROR'}}
            })
            .finally(function () {
                    self.props.changeNpc(npc)
                }
            );
    }

    loadPrev() {
        let self = this;
        let npc;

        api.get('/api/npc_creator/npc/prev?', { params: { id: this.props.npc.id } })
            .then(function (response) {
                npc = response.data
            })
            .catch(function (error) {
                npc = {id: 'ERROR', image_url: 'npc_load_error.png', attributes: {'Name': 'ERROR'}}
            })
            .finally(function () {
                    self.props.changeNpc(npc)
                }
            );
    }

    loadNext() {
        let self = this;
        let npc;

        api.get('/api/npc_creator/npc/next?', { params: { id: this.props.npc.id } })
            .then(function (response) {
                npc = response.data
            })
            .catch(function (error) {
                npc = {id: 'ERROR', image_url: 'npc_load_error.png', attributes: {'Name': 'ERROR'}}
            })
            .finally(function () {
                    self.props.changeNpc(npc)
                }
            );
    }

    render() {
        return (
            <div style={{justifyContent: 'center', display: 'flex'}}>
                <Button FrameComponent={FrameLines} onClick={this.loadPrev} style={{margin: 3}}>
                    <Text>&lt;&lt;&lt;</Text>
                </Button>
                <Button FrameComponent={FrameLines} onClick={this.loadRandom}>
                    <Text>Lade zufälligen NPC</Text>
                </Button>
                <Button FrameComponent={FrameLines} onClick={this.loadNext} style={{margin: 3}}>
                    <Text>&gt;&gt;&gt;</Text>
                </Button>
            </div>
        )
    }
}

export default ReloadButton;
