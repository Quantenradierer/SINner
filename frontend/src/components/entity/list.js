import React, {useEffect, useState} from "react";
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
import AddCircle from "../../icons/addCircle";
import GlitchEffect from "../cyberpunk/glitchEffect";
import UpCircle from "../../icons/upCircle";
import { ReactComponent as SearchIcon } from '../../icons/search.svg';

import { ReactComponent as XIcon } from '../../icons/x.svg';
import {Helmet} from "react-helmet";
import image_path from "../../image_path";
import i18n from "../../i18n";


class SearchPrompt extends React.Component {
    constructor(props) {
        super(props);
        this.state = {search: ''};

        this.handleSearchChange = this.handleSearchChange.bind(this);
    }

    handleSearchChange(event) {
        this.setState({search: event.target.value});
        this.props.searchCallback(event.target.value);
    }

    clearSearch = () => {
        this.setState({search: ""});
        this.props.searchCallback(event.target.value);
    };


    render() {
        return (
            <div style={{flexGrow: 1, margin: "0px 15px 0px 15px"}}>
                <Animator animator={{enter: 500, exit: 500}}>
                    <FrameLines style={{display: "flex", flexDirection: "column"}}>
                        <div style={{position: "relative", width: "100%"}}>
              <span style={{
                  position: "absolute",
                  top: "50%",
                  left: "0px",
                  transform: "translateY(-50%)",
                  opacity: 0.5,
              }}>
                <SearchIcon/>
              </span>
                            <input
                                placeholder="Wortsuche / RegEx"
                                type="text"
                                name="search"
                                id="search"
                                value={this.state.search}
                                onChange={this.handleSearchChange}
                                style={{
                                    width: "100%",
                                    paddingLeft: "30px",
                                    paddingRight: "30px",
                                }}
                            />
                            <span
                                onClick={this.clearSearch}
                                style={{
                                    position: "absolute",
                                    top: "50%",
                                    right: "0px",
                                    transform: "translateY(-50%)",
                                    cursor: "pointer",
                                    opacity: 0.5,
                                }}>
                               <XIcon/>
                            </span>
                        </div>
                    </FrameLines>
                </Animator>
            </div>
        );
    }
}


class ListWrapped extends React.Component {
    constructor(props) {
        super(props);

        this.hasHandledNext = false;

        this.handleScroll = this.handleScroll.bind(this);
    }

    componentDidMount() {
        window.addEventListener('scroll', this.handleScroll);
    }

    componentWillUnmount() {
        window.removeEventListener('scroll', this.handleScroll);
    }

    handleScroll() {
        const withinThreshold = window.innerHeight + document.documentElement.scrollTop >= document.documentElement.offsetHeight - 300;
        if (withinThreshold && !this.hasHandledNext) {
            this.props.handleNext();
            this.hasHandledNext = true;
        } else if (!withinThreshold) {
            this.hasHandledNext = false;
        }
    }

    render() {
        return (
            <div style={{maxWidth: 1315, width: '100%', position: 'relative'}}>
                <Helmet>
                    <title>{i18n.t(`page_list_title_${this.props.loader.kind}`)}</title>
                    <meta name="description" content={i18n.t(`page_list_description_${this.props.loader.kind}`)}/>
                    <meta property="og:title" content={i18n.t(`page_list_title_${this.props.loader.kind}`)}/>
                    <meta property="og:description" content={i18n.t(`page_list_description_${this.props.loader.kind}`)}/>
                    <meta property="og:image" content=""/>
                </Helmet>

                <div style={{
                    zIndex: 1,
                    position: 'fixed',
                    top: 0,
                    left: 0,
                    width: '100%',
                    height: '90%',
                    pointerEvents: 'none'
                }}>
                    <div style={{display: 'flex', justifyContent: 'center', height: '100%', pointerEvents: 'none'}}>
                        <div style={{
                            display: 'flex',
                            maxWidth: 1370 + 24,
                            width: '100%',
                            flexDirection: 'row-reverse',
                            justifyContent: 'flex-start',
                            alignItems: 'flex-end',
                            height: '100%',
                            pointerEvents: 'none'
                        }}>
                            <div style={{position: 'relative', pointerEvents: 'all'}}>
                                <AddCircle/>
                                <UpCircle/>
                            </div>
                        </div>
                    </div>
                </div>

                <div style={{zIndex: 0, position: 'relative', pointerEvents: 'none'}}>
                    <div style={{pointerEvents: 'all'}}>
                        <SearchPrompt searchCallback={this.props.searchCallback}/>
                    </div>
                    <div style={{display: 'flex', justifyContent: 'center', flexWrap: 'wrap', pointerEvents: 'all'}}>
                        {this.props.children}
                    </div>
                </div>

            </div>
        );
    }
}

const EntityList = props => {
    const navigate = useNavigate()
    const {state} = useNavigation()

    const [search, setSearch] = useState('');
    const [page, setPage] = useState(1);
    const [mountedEntities, setMountedEntities] = useState([]);

    const load = async (page, search, reset = false) => {
        if (page == null) {
            return
        }
        const response = await props.loader.list({params: {search: search, page: page}, request: {url: location}})

        if (reset === true) {
            setMountedEntities([])
        }
        if (response == null) {
            return
        }
        createItems(response.results)
        setPage(response.next)
    }

    const searchCallback = async (value) => {
        setSearch(value)
        await load(1, value, true)
    }

    const handleNext = async () => {
        await load(page, search)
    }

    const createItems = (entities) => {
        let items = []
        for (const entity of entities) {
            items.push(props.createItem(entity))
        }
        if (items.length > 0) {
            setMountedEntities(prevEntities => [...prevEntities,
                <Animator key={'Animator' + page} animator={{
                    activate: true,
                    manager: 'stagger',
                    duration: {stagger: 200},
                }}>{items}</Animator>]);
        }
    }

    useEffect(() => {
        load(1, search, true)
    }, [])

    if (state === 'loading') {
        return <LoadingBars></LoadingBars>
    } else {
        return <ListWrapped navigate={navigate} handleNext={handleNext} searchCallback={searchCallback} {...props}>{mountedEntities}</ListWrapped>
    }
}

export default EntityList;
