import {Text} from "@arwes/core";
import {Component} from "react";


class Comment extends Component {
    render() {
        const stars = '⭐'.repeat(parseInt(this.props.rating));

        return (<div key={'whole_comment'}>
            <div key={'starsnames'}><Text>{stars} <strong>{this.props.name}</strong></Text></div>
            <div key={'comment'}><Text>{this.props.comment}</Text></div>
        </div>)
    }
}

export default Comment;