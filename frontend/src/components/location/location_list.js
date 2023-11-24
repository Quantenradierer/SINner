import React, {useState} from "react";
import {
    Blockquote,
    Button,
    Card,
    FrameCorners,
    FrameLines,
    FramePentagon,
    List,
    LoadingBars,
    Table,
    Text
} from "@arwes/core";
import api from "../../axios";
import {NPC_IMAGE_PATH} from "../../config";
import {Animator} from "@arwes/animation";
import {useNavigate, useNavigation} from "react-router-dom";
import {useLoaderData} from "react-router";
import image_path from "../../image_path";
import active_image from "../../active_image";
import Comment from "./comment";


class LocationListItem extends React.Component {

    render() {
        let activeImage = active_image(this.props.entity.image_objects) || {}

        let comments = this.props.entity.values['Bewertungen']
        let comment = undefined

        if (comments !== undefined) {
            let random_nr = Math.floor(Math.random() * comments.length);
            comment = comments[random_nr]
        }

        return (<div style={{margin: 15}}>

                <a href={'/locations/' + this.props.entity.id}>
                    <Card
                        image={{
                            src: image_path('locations', activeImage.name),
                            alt: this.props.entity.image_generator_description
                        }}
                        title={this.props.entity.primary_values['Name']}
                        hover
                        style={{}}
                    >
                        <div style={{margin: '0px 0px 10px 0px'}}>
                            <Text>{this.props.entity.primary_values['Typ']}</Text>
                            {}
                        </div>
                        <Blockquote>
                            <Comment name={comment?.name} rating={comment?.rating} comment={comment?.comment}/>
                        </Blockquote>

                    </Card>
                </a>
            </div>
        )
    }
}


class SearchPrompt extends React.Component {
    constructor(props) {
        super(props);
        const params = new URLSearchParams(window.location.search)

        this.state = {search: params.get('search') || ''};

        this.handleSearchChange = this.handleSearchChange.bind(this);
    }

    handleSearchChange(event) {
        this.setState({search: event.target.value});
    }

    render() {
        return (<FrameLines style={{justifyContent: 'center', display: 'flex'}}>
            <div>
                <form style={{display: 'flex'}}>
                    <input placeholder="Wortsuche / RegEx" type="text" name="search" id="search" value={this.state.search}
                           onChange={this.handleSearchChange} style={{width: 480, margin: '0px 15px 0px 0px'}} />
                    <Button FrameComponent={FrameCorners}>
                        <Text>Suchen</Text>
                    </Button>
                </form>
            </div>
        </FrameLines>)
    }
}



class LocationListWrapped extends React.Component {
    constructor(props) {
        super(props);

        this.handlePrev = this.handlePrev.bind(this);
        this.handleNext = this.handleNext.bind(this);
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        window.scrollTo(0, 0)
    }

    handlePrev() {
        let url = new URL(window.location.href)
        url.searchParams.set('page', this.props.entities.previous)
        this.props.navigate(url.search)
    }

    handleNext() {
        let url = new URL(window.location.href)
        url.searchParams.set('page', this.props.entities.next)
        this.props.navigate(url.search)
    }

    render() {
        const items = [];
        for (const entity of this.props.entities.results) {
            items.push(<LocationListItem entity={entity} key={entity.id}/>)
        }

        const pageSize = 20
        const pageMax = Math.ceil(this.props.entities.count / pageSize)
        const hasPrev = this.props.entities.previous !== null
        const hasNext = this.props.entities.next !== null

        return (
            <div style={{width: '100%'}}>
                <SearchPrompt/>

                <Animator animator={{
                    manager: 'stagger',
                    duration: {stagger: 200}
                }}>
                    {items}
                </Animator>

                <div style={{justifyContent: 'center', display: 'flex'}}>
                    <Button FrameComponent={FrameLines} disabled={!hasPrev} onClick={this.handlePrev}>
                        <Text> &lt; </Text>
                    </Button>
                    <div>
                        <FrameLines>
                            <Text> {this.props.entities.number - 1} / {pageMax} </Text>
                        </FrameLines>
                    </div>
                    <Button FrameComponent={FrameLines} disabled={!hasNext} onClick={this.handleNext}>
                        <Text> &gt; </Text>
                    </Button>
                </div>
            </div>

        )
    }
}


const LocationList = props => {
  const entities = useLoaderData()
  const navigate = useNavigate()
  const { state } = useNavigation()

  if (state === 'loading') {
      return <LoadingBars></LoadingBars>
  } else {
      return <LocationListWrapped navigate={navigate} entities={entities} {...props} />
  }
}

export default LocationList;
