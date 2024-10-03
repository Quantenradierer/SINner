import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import './circle.css';
import {useEntity} from "../components/entityProvider";
import api from "../axios";
import is_logged_in from "../is_loggin_in";
import i18n from "../i18n";

const toggleFavorite = (event, entity, reload) => {
  event.preventDefault()

  if (entity.collections.length > 0) {
    entity.collections.pop()
    api.patch('/api/npc_creator/entities/' + entity.id + '/favorite/', {'favorite': false})
  } else {
    entity.collections[0] = {'name': 'favorite'}
    api.patch('/api/npc_creator/entities/' + entity.id + '/favorite/', {'favorite': true})
  }

  reload();
}



const FavoriteButton = () => {
  const entity = useEntity().entity
  const [reload, setReload] = useState(0)

  if (!is_logged_in()) {
    return <></>
  }

  return (
    <div title={i18n.t("entity_favorite")} className="hoverresize" key={reload}>
      <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg">
        <Link onClick={(event) => {toggleFavorite(event, entity, () => { setReload(reload + 1)})}} rel="noopener noreferrer">
          <g className="rotating-circle">
            <circle className="animated-circle" cx="25" cy="25" r="20"></circle>
            <path transform="scale(1.3) translate(7.5, 7.5)"
                d="M12 17.27L18.18 21L16.54 13.97L22 9.24L14.81 8.62L12 2L9.19 8.62L2 9.24L7.46 13.97L5.82 21L12 17.27Z"
                 stroke="#00F8F8"  strokeWidth="1"  fill={entity.collections?.length > 0 ? "#00F8F8" : "none"}/>
          </g>
        </Link>
      </svg>
    </div>
  );
};


export default FavoriteButton;