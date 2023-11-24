import React from "react";
import {useLoaderData} from "react-router";
import i18next from "../../i18n";
import AlternativeDialog from "../alternative_dialog";
import Warning from "../warning";
import LocationCard from "./location_card";
import CommentCard from "./comment_card";



class LocationCompleteWrapped extends React.Component {

    constructor(props) {
        super(props);

        this.state = {attributeAlternative: null}
        this.interval = null;

        this.setAlternatives = this.setAlternatives.bind(this);
    }

    setAlternatives(attribute) {
        this.setState({attributeAlternative: attribute})
    }

    render() {
        let warning = ''
        if (this.props.entity.image_objects.length == 0) {
            warning = <Warning text={i18next.t('image_generation_in_progress')}/>
        }

        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>
                {warning}

                {this.state.attributeAlternative && <AlternativeDialog entity={this.props.entity} attributeAlternative={this.state.attributeAlternative} setAlternatives={this.setAlternatives}/>}
                <LocationCard entity={this.props.entity} setAlternatives={this.setAlternatives}/>
                <CommentCard comments={this.props.entity.values['Bewertungen']}/>
            </div>
        )

    }
}


const LocationComplete = props => {
  const entity = useLoaderData()

  return <LocationCompleteWrapped entity={entity} {...props} />
}

export default LocationComplete;
