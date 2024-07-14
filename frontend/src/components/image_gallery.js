import React from "react";
import {Blockquote, Button, Card, FramePentagon, List, LoadingBars, Table, Text} from "@arwes/core";
import {NPC_IMAGE_PATH} from "../config";
import api from "../axios";
import {useLoaderData} from "react-router";
import {useNavigate, useNavigation} from "react-router-dom";
import is_logged_in from "../is_loggin_in";
import image_path from "../image_path";
import active_image from "../active_image";
import EntityLoader from "../loader/entity_loader";



class ImageGalleryWrapped extends React.Component {
    constructor(props) {
        super(props);

        this.state = {entity: this.props.entity,
                      votes: {}}

        this.handleRecreateImages = this.handleRecreateImages.bind(this);
    }

    async handleRecreateImages() {
        await api.post('/api/npc_creator/' + this.props.entity_type + '/' + this.state.entity.id + '/recreate_images/', {
                refresh_token: localStorage.getItem('refresh_token')
            }, {headers: {'Content-Type': 'application/json'}},
            {withCredentials: true})
        window.location.reload()
    }

    async upvote(event, image_number) {
        event.preventDefault()
        var votes = this.state.votes
        votes[image_number] = true
        this.setState({votes: votes})

        await api.post('/api/npc_creator/images/' + image_number + '/upvote/', {headers: {'Content-Type': 'application/json'}})
        let entity = await new EntityLoader(this.props.entity_type).entity({'params': {'id': this.state.entity.id}, undefined})

        this.setState({entity: entity});
    }

    async downvote(event, image_number) {
        event.preventDefault()
        var votes = this.state.votes
        votes[image_number] = false
        this.setState({votes: votes})

        await api.post('/api/npc_creator/images/' + image_number + '/downvote/', {headers: {'Content-Type': 'application/json'}})
        let entity = await new EntityLoader(this.props.entity_type).entity({'params': {'id': this.state.entity.id}, undefined})

        this.setState({entity: entity});
    }

    render() {
        let sizeX = 48 * this.props.factor.x;
        let sizeY = 48 * this.props.factor.y

        const items = [];
        if (this.state.entity === undefined) {
            return (<div/>)
        }


        let activeImage = active_image(this.state.entity.image_objects)
        for (let image of this.state.entity.image_objects) {
            let glowEffect = ''
            let addSize = 0
            if (image.id == activeImage.id) {
                glowEffect = '0px 0px 5px 5px #0ff'
                addSize = 15
            }

            items.push(
                <div key={items.id} style={{display: 'flex'}}>
                    <div key='scoring'>
                        <div key='upvote' className={this.state.votes[image.id] === true? 'votes-clicked':'votes'}
                             style={{position: 'absolute', marginLeft: sizeX - 25, marginTop: sizeY - 70}}><a href=""
                                                                                                              style={{fontSize: '32px'}}
                                                                                                              onClick={(event) => this.upvote(event, image.id)}>👍</a>
                        </div>
                        <div key='downvote' className={this.state.votes[image.id] === false? 'votes-clicked':'votes'}
                             style={{position: 'absolute', marginLeft: sizeX - 25, marginTop: sizeY - 30}}><a href=""
                                                                                                              style={{fontSize: '32px'}}
                                                                                                              onClick={(event) => this.downvote(event, image.id)}>👎</a>
                        </div>
                    </div>
                    <img style={{
                        margin: 15 - addSize,
                        width: sizeX + addSize * 2,
                        minHeight: sizeY + addSize * 2,
                        boxShadow: glowEffect
                    }}
                         src={image_path(this.props.entity_type, image.name)}/>
                </div>)
        }

        return (
            <FramePentagon>
                <Text style={{margin: '10px 0px 20px 0px'}}>
                    <b>Aussehen:</b> {this.state.entity.primary_values[this.props.attribute]}
                </Text>

                <div style={{flexWrap: 'wrap', display: 'flex', justifyContent: 'space-evenly'}}>
                    {items}
                </div>
                <div className={is_logged_in() ? '' : 'hidden'}>
                    <Button onClick={this.handleRecreateImages}>Neue Bilder</Button>
                </div>
            </FramePentagon>

        )
    }
}


const ImageGallery = props => {
  const entity = useLoaderData()
  const navigate = useNavigate()
  const { state } = useNavigation()

  if (state === 'loading') {
      return <LoadingBars></LoadingBars>
  } else {
      return <div style={{maxWidth: 980, width: '100%', position: 'relative'}}>
          <ImageGalleryWrapped navigate={navigate} entity={entity} {...props} />
      </div>
  }
}


export default ImageGallery;
