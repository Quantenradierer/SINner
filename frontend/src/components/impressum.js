import React from "react";
import {FramePentagon, List} from "@arwes/core";
import {Helmet} from "react-helmet";
import i18n from "../i18n";

const Impressum  = props => {
        return (
            <div key={'impressum'}>
                <Helmet>
                    <title>{i18n.t(`page_impressum_title`)}</title>
                </Helmet>

                <FramePentagon style={{maxWidth: 1000}}>
                    <div>
                        <h1>Impressum:</h1>
                        <p>
                            Bernd Schmidt<br/>
                            Grömitzer Weg 34A<br/>
                            22147 Hamburg<br/>

                            E-Mails: <a
                            href='mailto:schmidt@schattenakte.de?subject=Feedback&body=Message'>schmidt@schattenakte.de</a><br/>
                            Telefonnummer: +49 160 40 88 626 (Impressumspflicht verlangt das leider)<br/>
                            <br/>

                            Ich bin nur eine Privatperson und möchte hier keine Rechte verletzen und auch kein Geld
                            verdienen, <br/>
                            sondern nur eine Hilfe für andere Spielleiter anbieten 🙂.<br/>
                        </p>
                        <h1>Disclaimer:</h1>
                        <p>
                            Dieser Dienst dient zur Erstellung von Nichtspielercharakteren (NPCs) für das Shadowrun
                            Pen&Paper-Rollenspiel. NPCs sind ein wesentliches Element, um Rollenspiele lebendig und
                            interessant zu gestalten. Der Spielleiter stellt dabei nicht nur die Spielwelt dar, sondern
                            verkörpert auch die NPCs für die Spieler.

                            In einer dystopischen Zukunft wie der von Shadowrun, in der allgegenwärtige Technologie,
                            Korruption und Kapitalismus kritisch hinterfragt werden, benötigt man Figuren, welche diese
                            Aspekte darstellen.

                            Die erzeugten Texte und Bilder sollen keinesfalls Gewalt, Drogen oder andere
                            negative Aspekte verherrlichen. Das Ziel ist es, ein realistisches und vielschichtiges
                            Rollenspielerlebnis zu ermöglichen, ohne dabei unangemessene oder moralisch bedenkliche
                            Inhalte zu fördern.

                            Bitte beachten Sie, dass die Texte und Bilder in diesem Dienst der Unterhaltung und dem
                            Rollenspiel dienen und nicht als Unterstützung oder Befürwortung von illegalen oder
                            schädlichen Aktivitäten verstanden werden sollten.

                            Ich setze mich für verantwortungsbewussten Umgang mit den generierten Inhalten ein und bitte
                            die Nutzer, das Gleiche zu tun. Sollten Sie auf unangemessene oder bedenkliche Inhalte stoßen,
                            zögern Sie bitte nicht, mich zu kontaktieren, damit ich die betreffenden Inhalte prüfen und
                            gegebenenfalls entfernen kann.
                        </p>

                        <p>
                            Shadowrun-Logo und Inhalte mit freundlicher Genehmigung von Pegasus Spiele unter Lizenz von
                            Catalyst Game Labs und Topps Company, Inc. © 2020 Topps Company, Inc. Alle Rechte
                            vorbehalten.
                            Shadowrun ist eine eingetragene Handelsmarke von Topps Company, Inc.
                        </p>
                        <h1>Datenschutz:</h1>
                        <p>
                            Sämtliche angezeigten Daten sind fiktiv, die von AI Technologien generiert wurden. (GPT, Midjourney, Stable Diffusion, Flux) <br/>
                        </p>
                        <br/>
                        Der Zugriff auf diese Webseite wird vom Webserver in Log-Dateien protokolliert.<br/>
                        <List>
                            <li><b>Welche Daten:</b> IP-Adresse, Zugriffszeit und URL</li>
                            <li><b>Verwendung:</b> Diese Daten dienen lediglich der Fehlersuche</li>
                            <li><b>Löschung:</b> Sie werden regelmäßig gelöscht</li>
                            <li><b>Weitergabe:</b> Es erfolgt keine Weitergabe</li>
                        </List>
                        Bei der Erstellung eines NPCs werden die Eingaben gespeichert - und sind danach öffentlich
                        zugänglich.<br/>
                        <List>
                            <li><b>Welche Daten:</b>Alle Eingaben bei der Erstellung eines NPCs</li>
                            <li><b>Verwendung:</b>Lediglich um die Funktionalität bereit zu stellen (siehe Weitergaben)
                            </li>
                            <li><b>Löschung:</b> Löschung auf Anfrage bei der <a
                                href='mailto:schmidt@schattenakte.de@gmail.com?subject=Feedback&body=Message'>schmidt@schattenakte.de</a><br/>
                                <br/>
                            </li>
                            <li><b>Weitergabe:</b> Die Weitergabe erfolgt nur zur Sicherstellung der Funktionalität an
                                die
                                folgenden Dienste
                            </li>
                            <li>Weitergabe an <a href='https://openai.com/'>OpenAI</a> um die Texte zu generieren</li>
                            <li>Weitergabe an <a href='https://midjourney.com/'>Midjourney</a> um die Bilder zu
                                generieren,
                                die
                                Äusserlichen Beschreibungen bei Midjourney sind öffentlich zugänglich
                            </li>
                            <li>Weitergabe an <a href='https://discord.com'>Discord</a> als Übertragungsweg an
                                Midjourney
                            </li>
                        </List>
                        Cookies: Es werden keine Cookies von Drittanbietern gesetzt. Beim Login werden in eurem Browser Daten gesetzt um wiederzuerkennen.<br/>
                        <List>
                            <li><b>Welche Daten:</b> Eine Zeichenfolge die den eingeloggten Nutzer eindeutig
                                identifiziert.
                            </li>
                            <li><b>Verwendung:</b> Nur zur Sicherstellung der Funktionalität: Damit ihr eingeloggt
                                bleibt und bestimmte Funktionen nutzen könnt.
                            </li>
                            <li><b>Löschung:</b> Beim Ausloggen werden die Daten gelöscht.</li>
                            <li><b>Weitergabe:</b> Es erfolgt keine Weitergabe.</li>
                        </List>

                        <h1>Nutzungsbedingungen:</h1>

                        <p>Bitte achtet auch ein wenig darauf was ihr eingebt: Wenn die Dienste der Meinung sind, das
                            die
                            Eingaben unpassend sind, dann wird dieser Dienst ausgesperrt.
                            Ich werde unpassende NPCs auch manuell löschen oder abändern.
                        </p><br/>

                        <List>
                            <li>Bitte gebt keine privaten oder personenbezogenen Daten an</li>
                            <li>Bitte unterlasst extreme Darstellung von Gewalt, Rassismus oder Sexualität</li>
                            <li>Bitte erstellt keine Urheberrechtlich geschützten Personen oder Figuren</li>
                        </List>

                        Bitte beachtet die Nutzungsbedingungen und Richtlinien von den verwendeten Diensten:
                        <List>
                            <li><a href='https://docs.midjourney.com/docs/community-guidelines'>Midjourney
                                Richtlinien</a>
                            </li>
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
                            Unterschiedliche Gründe. In der Regel findet Midjourney das Motiv nicht in
                            Ordnung. (z.B. Blut bei Ärzten oder Narben)
                        </p>
                        <p>
                            <b>Warum passen manche Bilder oder Beschreibungen nicht?</b><br/>
                            Die Generatoren sind nur so gut wie die Daten, mit denen sie trainiert wurden.<br/>
                            Der Bildgenerator lernt auch manche Aspekte, die nicht zur Erstellung förderlich sind.

                            Der Bildgenerator hat gelernt das Frauen schön sind, mit glatter Haut und ästhetisch
                            ansprechend. Die Bilder von weiblichen Trollen enthalten dann diese Aspekte - auch wenn sie
                            eigentlich schrumpelige Haut und ästhetisch weniger ansprechend sein sollten.

                            Daher: Bitte habt etwas Nachsicht. Die Technik ist noch jung.
                        </p>
                        <p>
                            <b>Kostet das was?</b><br/>
                            Nein. Der Dienst ist für euch kostenlos und wird es auch bleiben.
                            Es gibt keine Werbung, keine Bezahlmöglichkeiten und keine Tracking-Tools.
                            Diese wird es auch nie geben.

                            Ich trage sämtliche Kosten, welche sich auf ein paar Euro im Monat
                            belaufen.
                        </p>
                        <p>
                            <b>Wo kann ich Vorschläge für Änderungen einbringen - oder Fehler melden?</b><br/>
                            Entweder du schreibst an <a
                            href='mailto:schmidt@schattenakte.de?subject=Feedback&body=Message'>schmidt@schattenakte.de</a> oder
                            du trägst hier ein Issue ein:
                            <a href='https://github.com/Quantenradierer/SINner/issues/new'>https://github.com/Quantenradierer/SINner/issues/new</a>
                        </p>
                    </div>

                </FramePentagon>
            </div>

        )
}

export default Impressum;
