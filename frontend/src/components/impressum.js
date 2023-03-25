import React from "react";
import {FramePentagon, List} from "@arwes/core";

class Impressum extends React.Component {

    render() {
        return (
            <FramePentagon style={{width: 950, margin: 15}}>
                <h1>Impressum:</h1>
                <p>
                    Bernd Schmidt<br/>
                    Grömitzer Weg 34A<br/>
                    22147 Hamburg<br/>

                    E-Mails: <a href='mailto:schmidt.bernd.1989@gmail.com?subject=Feedback&body=Message'>schmidt.bernd.1989@gmail.com</a><br/>
                    <br/>
                    Ich bin nur eine Privatperson und möchte mit diesen Dienst keine Rechte verletzen, <br/>
                    sondern nur eine Hilfe für andere Spielleiter anbieten 🙂.<br/>
                </p>
                <h1>Disclaimer:</h1>
                <p>
                    Shadowrun-Logo und Inhalte mit freundlicher Genehmigung von Pegasus Spiele unter Lizenz von Catalyst Game Labs und Topps Company, Inc. © 2020 Topps Company, Inc. Alle Rechte vorbehalten. Shadowrun ist eine eingetragene Handelsmarke von Topps Company, Inc.
                </p>

                <h1>Datenschutz:</h1>
                <p>
                    Sämtliche angezeigten Daten sind fiktiv, die von Openai/GPT sowie Midjourney generiert wurden.<br/>
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
                    <li><b>Welche Daten:</b>Alle Eingaben in Textfeldern</li>
                    <li><b>Verwendung:</b>Lediglich um die Funktionalität bereit zu stellen (siehe Weitergaben) und zur
                        Fehlersuche
                    </li>
                    <li><b>Löschung:</b> Löschung nur auf Anfrage bei der Impressums-E-Mail, falls ihr Private oder
                        Personenbezogene Angaben
                    </li>
                    <li><b>Weitergabe:</b> Die Weitergabe erfolgt nur zur Sicherstellung der Funktionalität an die
                        folgenden Dienste
                    </li>
                    <li>Weitergabe an <a href='https://openai.com/'>OpenAI</a> um die Texte zu generieren</li>
                    <li>Weitergabe an <a href='https://midjourney.com/'>Midjourney</a> um die Bilder zu generieren, die
                        Äusserlichen Beschreibungen bei Midjourney sind öffentlich zugänglich
                    </li>
                    <li>Weitergabe an <a href='https://discord.com'>Discord</a> als Übertragungsweg an Midjourney</li>
                </List>
                Cookies werden nur beim Login gesetzt. Es werden keine Cookies von Drittanbietern gesetzt.<br/>
                <List>
                    <li><b>Welche Daten:</b> Einen Code um euch auf dem Server wiederzuerkennen</li>
                    <li><b>Verwendung:</b> Nur zur Sicherstellung der Funktionalität: Damit ihr eingeloggt bleibt und
                        ihr bestimmte Rechte nutzen könnt
                    </li>
                    <li><b>Löschung:</b> Beim Ausloggen wird der Cookie gelöscht</li>
                    <li><b>Weitergabe:</b> Es erfolgt keine Weitergabe</li>
                </List>

                <h1>Nutzungsbedingungen:</h1>
                <p>Dieser Dienst dient zur Erstellung von NPCs (non-player character) für Shadowrun. </p>

                <p>Bitte achtet auch ein wenig darauf was ihr eingebt: Wenn GPT oder Midjourney der Meinung ist, das die
                    Eingaben unpassend sind, dann wird dieser Dienst ausgesperrt.
                    Ich werde unpassende NPCs auch manuell löschen oder abändern.
                </p><br/>

                <p>Bei GPT ist es klar, das es sich lediglich um die Erstellung von Rollenspiel-NPCs handelt.
                    Bei Midjourney ist dies anhand der Äußerlichen Beschreibung nicht ersichtlich, weshalb ein
                    Wortfilter implementiert wurde.</p>
                <List>
                    <li>Bitte gebt keine privaten oder personenbezogenen Daten an</li>
                    <li>Bitte unterlasst extreme Darstellung von Gewalt, Rassismus oder Sexualität</li>
                    <li>Bitte erstellt keine Urheberrechtlich geschützten Personen oder Figuren</li>
                </List>

                Bitte beachtet die Nutzungsbedingungen und Richtlinien von den verwendeten Diensten:
                <List>
                    <li><a href='https://docs.midjourney.com/docs/community-guidelines'>Midjourney Richtlinien</a></li>
                    <li><a href='https://openai.com/policies/terms-of-use'>GPT Richtlinien</a></li>
                </List>

                <br/>
                <h1>FAQ:</h1>
                <p>
                    <b>Will this be available in english?</b><br/>
                    I am working on it, but it isn't my main priority right now.
                </p>
                <p>
                    <b>Warum wird das Bild nicht erzeugt?</b><br/>
                    Manche Beschreibungen enthalten verbotene Wörter. Diese werden dann nicht erstellt.
                </p>
                <p>
                    <b>Warum ist Resonanz, Magie oder die Fertigkeiten nicht detailliert aufgeführt?</b><br/>
                    GPT ist ungenau. Es erzeugt manchmal Werte wenn sie nicht vorhanden sein sollten.
                    Deshalb werden diese erstmal nicht angezeigt, bis ich ein Muster entdeckt habe, was ich manuell
                    korrigieren kann.
                </p>
                <p>
                    <b>Warum passen manche Bilder nicht?</b><br/>
                    Die Generatoren sind nur so gut wie die Daten, mit denen sie trainiert wurden.<br/>
                    <br/>
                    Menschen können daher gut dargestellt werden. Zwerge aus diversen Gründen auch. Es werden nur manchmal Details ignoriert.<br/>
                    Elfen werden des öfteren in Fantasywerken verwendet, weshalb die Bilder und Ausrüstung oft dementsprechend aussieht.<br/>
                    Die Bilder von Orks und Trolle stammen vermutlich von Computerspielen, weshalb das Aussehen von dort kommt.<br/>
                </p>
                <p>
                    <b>Wo kann ich Vorschläge für Änderungen einbringen - oder Fehler melden?</b><br/>
                    Entweder du schreibst an <a
                    href='mailto:schmidt.bernd.1989@gmail.com?subject=Feedback&body=Message'>schmidt.bernd.1989@gmail.com</a> oder
                    du trägst hier ein Issue ein:
                    <a href='https://github.com/Quantenradierer/SINner/issues/new'>https://github.com/Quantenradierer/SINner/issues/new</a>
                </p>
            </FramePentagon>
        )
    }
}

export default Impressum;
