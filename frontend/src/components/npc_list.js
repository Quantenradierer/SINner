import React, {useState} from "react";
import {Blockquote, Button, Card, FrameCorners, FrameLines, List, LoadingBars, Table, Text} from "@arwes/core";
import api from "../axios";
import {NPC_IMAGE_PATH} from "../config";
import {Animator} from "@arwes/animation";
import {useNavigate, useNavigation} from "react-router-dom";
import {useLoaderData} from "react-router";


class NPCListItem extends React.Component {

    render() {
        return (<div style={{margin: 15}}>

                <a href={this.props.npc.id}>
                    <Card
                        image={{
                            src: NPC_IMAGE_PATH + this.props.npc.image_url,
                            alt: this.props.npc.image_generator_description
                        }}
                        title={this.props.npc.attributes['Name']}
                        landscape
                        hover
                        style={{maxWidth: 800}}
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

        this.state = {search: params.get('search') || '', moderated: params.get('moderated') || ''};

        this.handleSearchChange = this.handleSearchChange.bind(this);
        this.handleModeratedChange = this.handleModeratedChange.bind(this);
    }

    handleSearchChange(event) {
        this.setState({search: event.target.value});
    }

    handleModeratedChange(event) {
        this.setState({moderated: event.target.checked});
    }

    render() {
        return (<FrameLines style={{justifyContent: 'center', display: 'flex'}}>
            <div>
                <form style={{display: 'flex'}}>
                    <input placeholder="Freitextsuche" type="text" name="search" id="search" value={this.state.search}
                           onChange={this.handleSearchChange} style={{width: 480}} />
                    <input type="checkbox" name="moderated" id="moderated" checked={this.state.moderated}
                           onChange={this.handleModeratedChange} style={{margin: 6, width: 20}}/>
                    <label htmlFor="moderated" style={{display: 'flex', alignItems: 'center', width: 150}}><Text>Nur
                        Auserlesene</Text></label>
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

        const pageSize = 10
        const pageMax = Math.ceil(this.props.npcs.count / pageSize)
        const hasPrev = this.props.npcs.previous !== null
        const hasNext = this.props.npcs.next !== null

        return (
            <div>
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
                        <FrameLines style={{margin: 0}}>
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
