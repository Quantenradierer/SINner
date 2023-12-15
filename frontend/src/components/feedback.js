import React, {useState} from "react";
import {Button, FramePentagon, Text} from "@arwes/core";
import api from "../axios";
import i18next from "../i18n";
import {random} from "animejs";

function Feedback() {
    const [email, setEMail] = useState('');
    const [comment, setComment] = useState('');
    const [wasSent, setSent] = useState('init')

    function sendComment(event) {
        event.preventDefault()
        if (comment.length == 0) {
            return 0
        }

        api.post(`/api/npc_creator/feedback/`, {email: email, comment: comment})
            .then(function (response) {
                setSent('sent')
            })
            .catch(function (error) {
                setSent('error')
            })
    }

    return (
        <FramePentagon key={'feedback' + wasSent} style={{width: 950}}>
            {wasSent === 'sent' && <div key={'sent'}><Text>Danke für das Feedback!</Text></div>}
            {wasSent === 'error' &&
                <div key={'error'}><Text>Selbst das senden von Feedback funktioniert gerade nicht. Bitte sende dein
                    Feedback per E-Mail an: <a href="mailto:schmidt@schattenakte.de">schmidt@schattenakte.de</a> </Text></div>}

            {wasSent === 'init' &&
                <div key={'init'} style={{width: 880}}>
                    <form onSubmit={sendComment}>
                        <input style={{margin: 15}} type="text" id="email" placeholder="E-Mail (optional)"
                               onChange={e => setEMail(e.target.value)} value={email}/>
                        <textarea style={{margin: 15}} type="text" id="comment" rows={5}
                                  placeholder="Gibt es einen Bug? Verbesserungsvorschläge? Möchtest du dein Lieblingsrezept für Kekse teilen?"
                                  onChange={e => setComment(e.target.value)} value={comment}/>
                        <div style={{display: 'flex', justifyContent: 'right'}}>
                            <Button disabled={comment.length == 0} FrameComponent={FramePentagon}>Absenden</Button>
                        </div>
                    </form>
                </div>
            }
        </FramePentagon>
    )
}

export default Feedback;
