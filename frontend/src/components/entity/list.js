import React, {useState} from "react";
import {
    Button,
    FrameCorners,
    FrameLines,
    LoadingBars,
    Table,
    Text
} from "@arwes/core";
import {Animator} from "@arwes/animation";
import {useNavigate, useNavigation} from "react-router-dom";


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



class ListWrapped extends React.Component {
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
                    {this.props.children}
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


const List = props => {
  const navigate = useNavigate()
  const { state } = useNavigation()

  if (state === 'loading') {
      return <LoadingBars></LoadingBars>
  } else {
      return <ListWrapped navigate={navigate} entities={props.entities} {...props} />
  }
}

export default List;
