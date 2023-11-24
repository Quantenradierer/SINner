import image_path from "../../image_path";
import {Blockquote, FramePentagon} from "@arwes/core";
import Comment from "./comment";
import React from "react";

const CommentCard = props => {
    if (props.comments.length == 0) {
        return <div/>
    }

    const comment_data = props.comments || []
    let comments_components = []

    for (let nr = 0; nr < comment_data.length; nr++) {
        comments_components.push(<Blockquote key={nr}><Comment rating={comment_data[nr]['rating']} comment={comment_data[nr]['comment']} name={comment_data[nr]['name']}/></Blockquote>)
    }

    return <div key={'commentcard' + comments_components.length}>
        <FramePentagon style={{width: 950, margin: 15}}>
            {comments_components}
        </FramePentagon>
    </div>
}



export default CommentCard;