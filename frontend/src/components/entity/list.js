import React, {useEffect, useState} from "react";
import {
    Button, FrameBox,
    FrameCorners, FrameHexagon,
    FrameLines, FramePentagon,
    LoadingBars,
    Table,
    Text
} from "@arwes/core";
import {Animator} from "@arwes/animation";
import {Link, useLocation, useNavigate, useNavigation} from "react-router-dom";
import AddCircle from "../../icons/addCircle";
import GlitchEffect from "../cyberpunk/glitchEffect";
import UpCircle from "../../icons/upCircle";
import { ReactComponent as SearchIcon } from '../../icons/search.svg';

import { ReactComponent as XIcon } from '../../icons/x.svg';
import {Helmet} from "react-helmet";
import image_path from "../../image_path";
import i18n from "../../i18n";
import OverlayButtons from "../../overlayButtons";
import {useAtom} from "jotai";
import {filterAtom} from "../../atom";
import NPCListItem from "../npc/item";
import LocationListItem from "../location/item";
import EntityLoader from "../../loader/entity_loader";
import i18next from "i18next";
import {CustomFrame} from "../cyberpunk/CustomFrame";
import {TabsHeader} from "../cyberpunk/tabsHeader";
import is_loggin_in from "../../is_loggin_in";
import Dialog from "../cyberpunk/dialog";

const CARDS = {
    npc: NPCListItem,
    location: LocationListItem
}



class SearchPrompt extends React.Component {
    constructor(props) {
        super(props);
        this.state = {search: ''};
        this.searchTimeout = null;
        this.handleSearchChange = this.handleSearchChange.bind(this);
    }

    handleSearchChange(event) {
        const newSearchValue = event.target.value;
        this.setState({search: newSearchValue});

        if (this.searchTimeout) {
            clearTimeout(this.searchTimeout);
        }

        this.searchTimeout = setTimeout(() => {
            this.props.searchCallback(newSearchValue);
        }, 150);
    }

    clearSearch = () => {
        this.setState({search: ""});
        this.props.searchCallback("");
    };

    render() {
        return (
            <div style={{}}>
                <Animator animator={{enter: 300, exit: 300}}>
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



const EntityList = ({ filter, favorites, own, emptyText }) => {
    const navigate = useNavigate();
    const {state} = useNavigation();

    const [search, setSearch] = useState('');
    const [page, setPage] = useState(null);
    const [mountedEntities, setMountedEntities] = useState([]);
    const [loading, setLoading] = useState(true);

    const loader = new EntityLoader();

    const [hasHandledNext, setHasHandledNext] = useState(false);

    const tabs = {
        'npcs': {
            url: `/npcs`,
            name: i18next.t('tab_header_npc_list'),

        },
        'locations': {
            url: `/locations`,
            name: i18next.t('tab_header_locations_list'),
        },

    };

    if (is_loggin_in()) {
        tabs['favorites'] = {
            url: `/collections`,
            name: i18next.t('tab_header_favorites_list'),
        }
        tabs['own'] = {
            url: `/own`,
            name: i18next.t('tab_header_own_list'),
        }
    }

    const handleScroll = () => {
        const withinThreshold = window.innerHeight + document.documentElement.scrollTop >= document.documentElement.offsetHeight - 300;
        if (withinThreshold && !hasHandledNext) {
            setPage(prevPage => prevPage + 1);
            setHasHandledNext(true);
        } else if (!withinThreshold) {
            setHasHandledNext(false);
        }
    };

    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, [hasHandledNext]);

    useEffect(() => {
        setMountedEntities([]);
        setPage(null);
    }, [filter, search]);

    useEffect(async () => {
        const load = async () => {
            setLoading(true);
            const response = await loader.list({
                params: {search, filter, page, favorites, own},
                request: {url: location}
            });
            if (response == null) {
                return;
            }
            createItems(response.results);
        };

        if (page === null) {
            setPage(1);
        } else {
            load();
        }
    }, [page]);

    const createItems = (entities) => {
        let items = [];
        for (const entity of entities) {
            items.push(createItem(entity));
        }
        if (items.length > 0) {
            setMountedEntities(prevEntities => [
                ...prevEntities,
                <Animator
                    key={'Animator' + page}
                    animator={{
                        activate: true,
                        manager: 'stagger',
                        duration: {stagger: 200},
                    }}>
                    {items}
                </Animator>,
            ]);
        }

        setLoading(false);
    };

    const createItem = (entity) => {
        const EntityComponent = CARDS[entity.kind.toLowerCase()];
        if (EntityComponent) {
            return <EntityComponent key={`${entity.kind}-${entity.id}`} entity={entity}/>;
        }
    };



    return (
        <div style={{width: '100%', position: 'relative'}}>
            <TabsHeader tabs={tabs}/>
            <Helmet>
                <title>{i18n.t(`page_list_title`)}</title>
            </Helmet>

            <OverlayButtons>
                <AddCircle/>
                <UpCircle/>
            </OverlayButtons>
            <div style={{zIndex: 0, position: 'relative', pointerEvents: 'all'}}>
                <div style={{width: '100%', pointerEvents: 'all'}}>
                    <SearchPrompt searchCallback={(value) => setSearch(value)}/>
                </div>
                {!loading && mountedEntities.length == 0 && <div style={{paddingTop: 15, paddingBottom: 15}}>
                    <FrameBox palette='secondary' style={{width: '100%', pointerEvents: 'all'}}><Text>{search? i18next.t('search_list_empty_text') : emptyText}</Text></FrameBox>
                </div>}
                <div style={{display: 'flex', justifyContent: 'center', flexWrap: 'wrap', pointerEvents: 'all'}}>
                    {mountedEntities}
                </div>
            </div>
        </div>
    );
};




export default EntityList;
