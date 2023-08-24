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
import api from "../axios";
import {NPC_IMAGE_PATH} from "../config";
import {Animator} from "@arwes/animation";
import {useNavigate, useNavigation} from "react-router-dom";
import {useLoaderData} from "react-router";
import image_path from "../image_path";


class NPCListItem extends React.Component {

    render() {
        return (<div style={{margin: 15}}>

                <a href={'/npcs/' + this.props.npc.id}>
                    <Card
                        image={{
                            src: image_path(this.props.npc.image_url, this.props.npc.id, this.props.npc.default_image_number),
                            alt: this.props.npc.image_generator_description
                        }}
                        title={this.props.npc.attributes['Name']}
                        landscape
                        hover
                        style={{}}
                    >
                    <Blockquote>
                        <Text>
                            {this.props.npc.attributes['Catchphrase']}
                        </Text>
                    </Blockquote>

                        <List>
                            <li><Text><b>Metatyp:</b> {this.props.npc.attributes['Metatyp']}</Text></li>
                            <li><Text><b>Beruf:</b> {this.props.npc.attributes['Beruf']}</Text></li>
                            <li><Text><b>Eigenarten:</b> {this.props.npc.attributes['Eigenarten']}</Text></li>
                        </List>
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
                    <input placeholder="Freitextsuche" type="text" name="search" id="search" value={this.state.search}
                           onChange={this.handleSearchChange} style={{width: 480, margin: '0px 15px 0px 0px'}} />
                    <Button FrameComponent={FrameCorners}>
                        <Text>Suchen</Text>
                    </Button>
                </form>
            </div>
        </FrameLines>)
    }
}



class NPCListWrapped extends React.Component {
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
        url.searchParams.set('page', this.props.npcs.previous)
        this.props.navigate(url.search)
    }

    handleNext() {
        let url = new URL(window.location.href)
        url.searchParams.set('page', this.props.npcs.next)
        this.props.navigate(url.search)
    }

    render() {
        const items = [];
        for (const npc of this.props.npcs.results) {
            items.push(<NPCListItem npc={npc} key={npc.id}/>)
        }

        const pageSize = 20
        const pageMax = Math.ceil(this.props.npcs.count / pageSize)
        const hasPrev = this.props.npcs.previous !== null
        const hasNext = this.props.npcs.next !== null

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
                            <Text> {this.props.npcs.number - 1} / {pageMax} </Text>
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


const NPCList = props => {
  const npcs = useLoaderData()
  const navigate = useNavigate()
  const { state } = useNavigation()

  if (state === 'loading') {
      return <LoadingBars></LoadingBars>
  } else {
      return <NPCListWrapped navigate={navigate} npcs={npcs} {...props} />
  }
}

export default NPCList;
