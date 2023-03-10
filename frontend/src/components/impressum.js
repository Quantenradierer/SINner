import React from "react";
import {Blockquote, Button, Card, FramePentagon, Table, Text} from "@arwes/core";
import {List} from '@arwes/core';

class Impressum extends React.Component {

    render() {
        return (
            <FramePentagon style={{width: 950, margin: 15}}>
                <h1>Impressum:</h1>
                <p>
                    Bernd Schmidt<br/>
                    Grömitzer Weg 34A<br/>
                    22147 Hamburg<br/>

                    E-Mails: schmidt.bernd.1989@gmail.com<br/>
                    <br/>
                    Ich bin nur eine Privatperson und möchte mit diesen Dienst keine Rechte verletzten, <br/>sondern nur eine Hilfe für andere Spielleiter anbieten 🙂.<br/>
                    Bitte schreibt mir falls die erstellten Inhalte eure Rechte verletzten.
                </p>
                <h1>Datenschutz:</h1>
                <p>
                    Sämtliche angezeigten Daten sind fiktiv, die von Openai/GPT anhand einer Eingabe generiert wurden.<br/>
                </p>
                <b>Bitte gebt keine privaten oder personenbezogene Daten ein!</b><br/>
                <br/>
                Der Zugriff auf diese Webseite wird vom Webserver in Log-Dateien protokolliert.<br/>
                <List>
                    <li><b>Welche Daten:</b> IP-Adresse, Zugriffszeit und URL</li>
                    <li><b>Verwendung:</b> Diese Daten dienen lediglich der Fehlersuche</li>
                    <li><b>Löschung:</b> Sie werden regelmäßig gelöscht</li>
                    <li><b>Weitergabe:</b> Es erfolgt keine Weitergabe</li>
                </List>
                Alle eingegebenen Daten werden dauerhaft gespeichert und sind öffentlich zugänglich.<br/>
                <List>
                    <li><b>Welche Daten:</b> Alle Eingaben in Textfeldern</li>
                    <li><b>Verwendung:</b> Lediglich um die Funktionalität bereit zu stellen (siehe Weitergaben) und zur Fehlersuche</li>
                    <li><b>Löschung:</b> Löschung nur auf Anfrage bei der Impressums-E-Mail, falls ihr Private oder Personenbezogene Angaben</li>
                    <li><b>Weitergabe:</b> Die Weitergabe erfolgt nur zur Sicherstellung der Funktionalität an die folgenden Dienste</li>
                    <li>Weitergabe an <a href='https://openai.com/'>OpenAI</a> um die Texte zu generieren</li>
                    <li>Weitergabe an <a href='https://midjourney.com/'>Midjourney</a> um die Bilder zu generieren, die Äusserlichen Beschreibungen bei Midjourney sind öffentlich zugänglich</li>
                    <li>Weitergabe an <a href='https://discord.com'>Discord</a> als Übertragungsweg an Midjourney</li>
                </List>
                Cookies werden nur beim Login gesetzt. Es werden keine Cookies von Drittanbietern gesetzt.<br/>
                <List>
                    <li><b>Welche Daten:</b> Einen Code um euch auf dem Server wiederzuerkennen </li>
                    <li><b>Verwendung:</b> Nur zur Sicherstellung der Funktionalität: Damit ihr eingeloggt bleibt und ihr bestimmte Rechte nutzen könnt </li>
                    <li><b>Löschung:</b> Beim Ausloggen wird der Cookie gelöscht</li>
                    <li><b>Weitergabe:</b> Es erfolgt keine Weitergabe</li>
                </List>

                <h1>Nutzungsbedingungen:</h1>
                <p>Dieser Dienst dient zur Erstellung von NPCs (non-player character) für Shadowrun. </p>

                <p>Wenn GPT oder Midjourney der Meinung ist, das die Inhalte unpassend sind, dann wird dieser Dienst ausgesperrt.
                Unpassende NPCs werden auch manuell gelöscht oder verändert.
                </p><br/>

                <p>Bei GPT ist es klar, das es sich lediglich um die Erstellung von Rollenspiel-NPCs handelt.
                    Bei Midjourney ist dies anhand der Äußerlichen Beschreibung nicht ersichtlich, weshalb ein Wortfilter implementiert wurde.</p>
                <List>
                    <li>Bitte gebt keine privaten oder personenbezogenen Daten an </li>
                    <li>Bitte unterlasst extreme Darstellung von Gewalt, Rassismus oder Sexualität</li>
                    <li>Bitte erstellt keine Urheberrechtlich geschützten Personen oder Figuren</li>
                </List>

                Bitte beachtet die Nutzungsbedingungen und Richtlinien von den verwendeten Diensten:
                <List>
                    <li><a href='https://docs.midjourney.com/docs/community-guidelines'>Midjourney Richtlinien</a></li>
                    <li><a href='https://openai.com/policies/terms-of-use'>GPT Richtlinien</a></li>
                </List>

                Shadowrun ist eine eingetragene Handelsmarke von Topps Company, Inc.

            </FramePentagon>
        )
    }
}

export default Impressum;
