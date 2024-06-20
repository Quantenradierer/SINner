import React, {useState} from "react";
import {useLoaderData} from "react-router";
import i18next from "../../i18n";
import AlternativeDialog from "../alternative_dialog";
import Warning from "../warning";
import LocationCard from "./location_card";
import CommentCard from "./comment_card";
import useRefreshEntityCard from "../use_refresh_entity_card";
import {Helmet} from "react-helmet";
import image_path from "../../image_path";
import active_image from "../../active_image";



class LocationCompleteWrapped extends React.Component {

    constructor(props) {
        super(props);

        this.interval = null;
    }

    render() {
        let warning = ''
        if (this.props.entity.image_objects.length == 0) {
            warning = <Warning text={i18next.t('image_generation_in_progress')}/>
        }
        let activeImage = active_image(this.props.entity.image_objects) || {}

        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>
                 <Helmet>
                  <title>Schattenakte - {this.props.entity.values['Name']}</title>
                  <meta name="description" content={this.props.entity.values['Typ']} />
                  <meta property="og:title" content="Schattenakte - {this.props.entity.values['Name']}" />
                  <meta property="og:description" content={this.props.entity.values['Typ']} />
                  <meta property="og:image" content={image_path('locations', activeImage.name, true)} />
                </Helmet>


                {warning}
                <LocationCard entity={this.props.entity}/>
                <CommentCard entity={this.props.entity}/>
            </div>
        )

    }
}


const LocationComplete = props => {
  const loaded_entity = useLoaderData()
  const [entity, setEntity] = useState(loaded_entity);
  useRefreshEntityCard('locations', entity, setEntity)
  return <LocationCompleteWrapped entity={entity} {...props} />
}

export default LocationComplete;
