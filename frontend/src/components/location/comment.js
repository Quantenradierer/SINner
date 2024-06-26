import {Text} from "@arwes/core";
import {Component} from "react";


class Comment extends Component {
    render() {
        const stars = '⭐'.repeat(parseInt(this.props.rating));

        return (<div key={'whole_comment'}>
            <div key={'starsnames'}><Text>{stars} <strong>{this.props.name}</strong></Text></div>
            <div key={'comment'}><Text>
                <div className="clampText4Liner">{this.props.comment}</div>
            </Text></div>
        </div>)
    }
}

export default Comment;