import React from "react";
import {FramePentagon, List} from "@arwes/core";
import {Helmet} from "react-helmet";
import i18n from "../i18n";

const ImpressumDe = props => {
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
                            <b>Gibt es das auch auf Englisch?</b><br/>
                            Die Oberfläche gibt es auf Deutsch und Englisch (Sprache oben rechts umschalten). NPCs und
                            Orte werden derzeit auf Deutsch erzeugt, Grundrisse in deiner Sprache.
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

// English courtesy translation; the German text above is the legally binding one.
const ImpressumEn = props => {
    return (
        <div key={'impressum'}>
            <Helmet>
                <title>{i18n.t(`page_impressum_title`)}</title>
            </Helmet>

            <FramePentagon style={{maxWidth: 1000}}>
                <div>
                    <h1>Imprint:</h1>
                    <p>
                        Bernd Schmidt<br/>
                        Grömitzer Weg 34A<br/>
                        22147 Hamburg, Germany<br/>

                        Email: <a
                        href='mailto:schmidt@schattenakte.de?subject=Feedback&body=Message'>schmidt@schattenakte.de</a><br/>
                        Phone: +49 160 40 88 626 (the imprint requirement unfortunately demands it)<br/>
                        <br/>

                        I am just a private person. I don't want to infringe any rights or make any money here,<br/>
                        I only want to offer a little help for other game masters 🙂.<br/>
                    </p>
                    <h1>Disclaimer:</h1>
                    <p>
                        This service creates non-player characters (NPCs) for the Shadowrun tabletop role-playing
                        game. NPCs are an essential element in making role-playing games lively and interesting. The
                        game master not only portrays the game world but also embodies the NPCs for the players.

                        In a dystopian future like Shadowrun's, where ubiquitous technology, corruption and capitalism
                        are viewed critically, you need characters who represent these aspects.

                        The generated texts and images are in no way meant to glorify violence, drugs or other negative
                        aspects. The goal is to enable a realistic and multi-layered role-playing experience without
                        promoting inappropriate or morally questionable content.

                        Please note that the texts and images in this service are for entertainment and role-playing
                        and should not be understood as support or endorsement of illegal or harmful activities.

                        I am committed to a responsible handling of the generated content and ask users to do the same.
                        If you come across inappropriate or questionable content, please don't hesitate to contact me
                        so that I can review it and remove it if necessary.
                    </p>

                    <p>
                        Shadowrun logo and content by kind permission of Pegasus Spiele under license from
                        Catalyst Game Labs and Topps Company, Inc. © 2020 Topps Company, Inc. All rights reserved.
                        Shadowrun is a registered trademark of Topps Company, Inc.
                    </p>
                    <h1>Privacy:</h1>
                    <p>
                        All data shown is fictional and was generated by AI technologies. (GPT, Midjourney, Stable Diffusion, Flux) <br/>
                    </p>
                    <br/>
                    Access to this website is logged by the web server in log files.<br/>
                    <List>
                        <li><b>Which data:</b> IP address, time of access and URL</li>
                        <li><b>Purpose:</b> This data is only used for troubleshooting</li>
                        <li><b>Deletion:</b> It is deleted regularly</li>
                        <li><b>Disclosure:</b> It is not passed on</li>
                    </List>
                    When an NPC is created, the input is stored - and is publicly accessible afterwards.<br/>
                    <List>
                        <li><b>Which data:</b> All input made when creating an NPC</li>
                        <li><b>Purpose:</b> Only to provide the functionality (see disclosures)</li>
                        <li><b>Deletion:</b> Deletion on request at <a
                            href='mailto:schmidt@schattenakte.de?subject=Feedback&body=Message'>schmidt@schattenakte.de</a><br/>
                            <br/>
                        </li>
                        <li><b>Disclosure:</b> Data is only passed on to the following services to ensure the
                            functionality
                        </li>
                        <li>Passed on to <a href='https://openai.com/'>OpenAI</a> to generate the texts</li>
                        <li>Passed on to <a href='https://midjourney.com/'>Midjourney</a> to generate the images;
                            the appearance descriptions are publicly accessible at Midjourney
                        </li>
                        <li>Passed on to <a href='https://discord.com'>Discord</a> as the transmission channel to
                            Midjourney
                        </li>
                    </List>
                    Cookies: No third-party cookies are set. When you log in, data is stored in your browser to recognise you.<br/>
                    <List>
                        <li><b>Which data:</b> A string that uniquely identifies the logged-in user.</li>
                        <li><b>Purpose:</b> Only to ensure the functionality: so that you stay logged in and can use
                            certain features.
                        </li>
                        <li><b>Deletion:</b> The data is deleted when you log out.</li>
                        <li><b>Disclosure:</b> It is not passed on.</li>
                    </List>

                    <h1>Terms of use:</h1>

                    <p>Please also pay some attention to what you enter: if the services consider the input
                        inappropriate, this service will be blocked.
                        I will also delete or change inappropriate NPCs manually.
                    </p><br/>

                    <List>
                        <li>Please do not enter private or personal data</li>
                        <li>Please refrain from extreme depictions of violence, racism or sexuality</li>
                        <li>Please do not create copyrighted people or characters</li>
                    </List>

                    Please observe the terms of use and guidelines of the services used:
                    <List>
                        <li><a href='https://docs.midjourney.com/docs/community-guidelines'>Midjourney
                            guidelines</a>
                        </li>
                        <li><a href='https://openai.com/policies/terms-of-use'>GPT guidelines</a></li>
                    </List>

                    <br/>
                    <h1>FAQ:</h1>
                    <p>
                        <b>Is this available in English?</b><br/>
                        The interface is available in German and English (switch the language at the top right). NPCs and
                        locations are currently generated in German; floorplans follow your language.
                    </p>
                    <p>
                        <b>Why isn't the image generated?</b><br/>
                        Different reasons. Usually Midjourney doesn't consider the motif acceptable
                        (e.g. blood on doctors or scars).
                    </p>
                    <p>
                        <b>Why do some images or descriptions not fit?</b><br/>
                        The generators are only as good as the data they were trained on.<br/>
                        The image generator also learns some aspects that are not helpful here.

                        It has learned that women are beautiful, with smooth skin and aesthetically pleasing. Images
                        of female trolls then contain these aspects - even though they should actually have wrinkled
                        skin and be less aesthetically pleasing.

                        So please be a little patient. The technology is still young.
                    </p>
                    <p>
                        <b>Does it cost anything?</b><br/>
                        No. The service is free for you and will stay that way.
                        There is no advertising, no payment options and no tracking tools.
                        There never will be.

                        I bear all the costs, which amount to a few euros a month.
                    </p>
                    <p>
                        <b>Where can I suggest changes - or report bugs?</b><br/>
                        Either write to <a
                        href='mailto:schmidt@schattenakte.de?subject=Feedback&body=Message'>schmidt@schattenakte.de</a> or
                        open an issue here:
                        <a href='https://github.com/Quantenradierer/SINner/issues/new'>https://github.com/Quantenradierer/SINner/issues/new</a>
                    </p>
                </div>

            </FramePentagon>
        </div>
    )
}

const Impressum = props => (i18n.language === "en" ? <ImpressumEn {...props}/> : <ImpressumDe {...props}/>);

export default Impressum;
