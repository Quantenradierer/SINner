import React from "react";
import {Blockquote, Button, Card, FramePentagon, List, LoadingBars, Table, Text} from "@arwes/core";
import {NPC_IMAGE_PATH} from "../config";
import api from "../axios";
import image_path from "../image_path";
import {useLoaderData} from "react-router";
import {useNavigate, useNavigation} from "react-router-dom";



class ImageGalleryWrapped extends React.Component {
    constructor(props) {
        super(props);

        this.state = {npc: this.props.npc}

        this.handleRecreateImages = this.handleRecreateImages.bind(this);
        this.setImageDefault = this.setImageDefault.bind(this);
    }

    async handleRecreateImages() {
        await api.post('api/npc_creator/npcs/' + this.state.npc.id + '/recreate_images/', {
                refresh_token: localStorage.getItem('refresh_token')
            }, {headers: {'Content-Type': 'application/json'}},
            {withCredentials: true})
        window.location.reload()
    }

    async setImageDefault(event, image_number) {
        event.preventDefault();

        let response = await api.post('api/npc_creator/npcs/' + this.state.npc.id + '/set_default_image/', {
                image_number: image_number,
                refresh_token: localStorage.getItem('refresh_token')
            }, {headers: {'Content-Type': 'application/json'}},
            {withCredentials: true})

        this.setState({npc: response.data.npc})
    }

    render() {
        const items = [];
        if (this.state.npc === undefined) {
            return (<div/>)
        }

        for (let i = 0; i < this.state.npc.max_image_number; i++) {
            let glowEffect = ''
            let addSize = 0
            if (i == this.state.npc.default_image_number) {
                glowEffect = '0px 0px 5px 5px #0ff'
                addSize = 15
            }

            items.push(
                <a href="" key={i} onClick={(event) => this.setImageDefault(event, i)}>
                    <img style={{margin: 15 - addSize, width: 92 * 2 + addSize * 2, minHeight: 120 * 2 + addSize * 2, boxShadow: glowEffect}}
                         src={image_path(this.state.npc.image_url, this.state.npc.id, i)}/>
                </a>)
        }

        return (

            <FramePentagon>
                <Text style={{margin: '10px 0px 20px 0px'}}>
                    <b>Detailliertes Aussehen:</b> {this.state.npc.attributes['Detailliertes Aussehen']}
                </Text>

                <div style={{flexWrap: 'wrap', display: 'flex'}}>
                    {items}
                </div>
                <Button onClick={this.handleRecreateImages}>Neue Bilder</Button>
            </FramePentagon>

        )
    }
}


const ImageGallery = props => {
  const npc = useLoaderData()
  const navigate = useNavigate()
  const { state } = useNavigation()

  if (state === 'loading') {
      return <LoadingBars></LoadingBars>
  } else {
      return <ImageGalleryWrapped navigate={navigate} npc={npc} {...props} />
  }
}



export default ImageGallery;
