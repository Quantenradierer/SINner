import React from "react";
import {Blockquote, Button, Card, FramePentagon, List, LoadingBars, Table, Text} from "@arwes/core";
import {NPC_IMAGE_PATH} from "../config";
import api from "../axios";
import {useLoaderData} from "react-router";
import {useNavigate, useNavigation} from "react-router-dom";
import is_logged_in from "../is_loggin_in";
import image_path from "../image_path";
import active_image from "../active_image";



class ImageGalleryWrapped extends React.Component {
    constructor(props) {
        super(props);

        this.state = {npc: this.props.npc}

        this.handleRecreateImages = this.handleRecreateImages.bind(this);
    }

    async handleRecreateImages() {
        await api.post('/api/npc_creator/npcs/' + this.state.npc.id + '/recreate_images/', {
                refresh_token: localStorage.getItem('refresh_token')
            }, {headers: {'Content-Type': 'application/json'}},
            {withCredentials: true})
        window.location.reload()
    }

    async upvote(event, image_number) {
        event.preventDefault();
        await api.post('/api/npc_creator/images/' + image_number + '/upvote/', {
                refresh_token: localStorage.getItem('refresh_token')
            }, {headers: {'Content-Type': 'application/json'}},
            {withCredentials: true})
    }

    async downvote(event, image_number) {
        event.preventDefault();
        await api.post('/api/npc_creator/images/' + image_number + '/downvote/', {
                refresh_token: localStorage.getItem('refresh_token')
            }, {headers: {'Content-Type': 'application/json'}},
            {withCredentials: true})
    }

    render() {
        const items = [];
        if (this.state.npc === undefined) {
            return (<div/>)
        }

        let activeImage = active_image(this.state.npc.image_objects)
        for (let image of this.state.npc.image_objects) {
            let glowEffect = ''
            let addSize = 0
            if (image.id == activeImage.id) {
                glowEffect = '0px 0px 5px 5px #0ff'
                addSize = 15
            }

            let buttons = ''
            if (is_logged_in()) {
                buttons = <div key='scoring'>
                    <div key='upvote' className='votes' style={{position: 'absolute', marginLeft: 92 * 2 - 25, marginTop: 120 * 2 - 70}}><a href="" style={{fontSize: '32px'}} onClick={(event) => this.upvote(event, image.id)}>👍</a></div>
                    <div key='downvote' className='votes' style={{position: 'absolute', marginLeft: 92 * 2 - 25, marginTop: 120 * 2 - 30}}><a href="" style={{fontSize: '32px'}} onClick={(event) => this.downvote(event, image.id)}>👎</a></div>
                </div>
            }

            items.push(
                <div style={{display: 'flex'}}>
                    {buttons}
                    <img style={{margin: 15 - addSize, width: 92 * 2 + addSize * 2, minHeight: 120 * 2 + addSize * 2, boxShadow: glowEffect}}
                         src={image_path(image.name)}/>
                </div>)
        }

        return (

            <FramePentagon>
                <Text style={{margin: '10px 0px 20px 0px'}}>
                    <b>Detailliertes Aussehen:</b> {this.state.npc.primary_values['Detailliertes Aussehen']}
                </Text>

                <div style={{flexWrap: 'wrap', display: 'flex'}}>
                    {items}
                </div>
                <div className={is_logged_in()? '': 'hidden'}>
                    <Button onClick={this.handleRecreateImages}>Neue Bilder</Button>
                </div>
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
