# Shadowrun 6 – Regeln mit Berechnungen (Grundregelwerk, vollständig)

Konsolidierte Fassung aller Berechnungen, Formeln, Schwellenwerte und Kostentabellen aus dem
deutschen **Shadowrun 6 – Grundregelwerk** (352 Buchseiten), zusammengeführt aus den zuvor
getrennten Chunk-Dateien. Ziel: eine einzige Referenz für die regelkonforme NPC-Generierung.

## Stand / Errata

Gegengeprüft (Stand 2026-08) gegen **`Shadowrun_6_Downloadversion_2024.pdf`** (354 PDF-Seiten)
und die [**Errata zum Grundregelwerk, 3. Auflage**](https://shadowrun6.de/downloads/errata/errata_sr6_grundregelwerk_aufl3.pdf).
Die Downloadversion 2024 ist bereits die **3. Auflage** — die regelrelevanten Errata (2. → 3. Auflage)
sind darin überwiegend eingearbeitet. Korrigierte bzw. ergänzte Stellen sind mit *„3. Auflage/Errata"*
markiert; die wichtigsten:

- **Kampf:** Vollautomatik-Modus (Flächenangriff Radius 1 m, −6 AW, 10 Schuss), Mehrfachangriffe nur noch
  gegen mehrere Ziele (keine Angriffs-Obergrenze), *Sich losreißen* als Vergleichende Probe, Edge-Handlung
  *Vorausschau* (Würfelpool verdoppeln + aufteilen), Nahkampfwaffen addieren Stärke zum Angriffswert
  (Peitschen: Reaktion).
- **Charaktererschaffung:** keine „alchemistischen Zauber" als eigene Kategorie mehr, Verfügbarkeits-Cap 7,
  bis zu 5 Karma dürfen ins Spiel, Magie/Resonanz-Cap 6.
- **Magie:** max. Anpassungen = max(Magie, Hexerei), Fahrzeugpanzerung → *Verstärkter Panzer*,
  Geister-Schwächen ergänzt, Fokus-Einzel-KS ≤ Magie, Adeptenkraft *Kampfsinn* wirkt auf Überraschungsproben.
- **Matrix:** Datenbombe `Stufe × 2`, *Volle Matrixabwehr* (Firewall bis Rundenende, Jederzeit),
  Cyberbuchsen-Spalte „Matrixinitiative-Bonuswürfel (VR)", Programm laden/entfernen = Nebenhandlung.
- **Riggen:** Rigger-/Drohnentabellen (S. 200/201) korrigiert & um *Heimlichkeit*/*Wahrnehmung* erweitert;
  Riggerkontrolle senkt Schwellenwert aller Proben zum *Betrieb des Fahrzeugs*.
- **Critter/Bioware:** *Regeneration*-Ausnahmen, Critterkraft *Bewegung* (→ Humpelnd), Adrenalinpumpe
  (halbe Rundenzahl Schaden), Ares Dragon Rumpf 22, mehrere mächtige Critter „2 Haupt"-Handlungen.
- **Bekannter Buchfehler:** Der Tabellen-Anhang **S. 330** zeigt die astrale Initiative weiterhin als
  `+ 2W6`; korrekt ist laut Errata (S. 163) `+ 3W6`.

## Hinweise zur Nutzung

- Buchseiten-Nummerierung folgt den gedruckten Fußzeilen im PDF, **nicht** dem internen PDF-Seitenindex.
- Item-Kataloge (einzelne Waffen-/Rüstungs-/Cyberware-Statblöcke ohne verallgemeinerbare Formel) sind
  bewusst **nicht** vollständig transkribiert; jeder Teil listet am Ende unter „Nicht erfasst", was fehlt.
- Einige Tabellen erscheinen doppelt (Fließtext + Tabellen-Anhang, Teil 9). Im Zweifel gilt die
  frühere/detailliertere Fassung; der Anhang verweist per Kommentar darauf.
- Bei verbleibenden Unstimmigkeiten mit dem PDF hat das Originalbuch Vorrang.

## Inhalt

1. [Grundlagen (Buchseiten 1–100)](#teil-1-grundlagen-buchseiten-1-100)
2. [Kampf (Buchseiten 100–129)](#teil-2-kampf-buchseiten-100-129)
3. [Magie (Buchseiten 130–159)](#teil-3-magie-buchseiten-130-159)
4. [Astralebene, Initiation & Matrix-Grundlagen (Buchseiten 160–189)](#teil-4-astralebene-initiation-matrix-grundlagen-buchseiten-160-189)
5. [Komplexe Formen, Sprites, Riggen & Schergen (Buchseiten 190–219)](#teil-5-komplexe-formen-sprites-riggen-schergen-buchseiten-190-219)
6. [Critter, Spielleiterhinweise & Ausrüstung I (Buchseiten 220–249)](#teil-6-critter-spielleiterhinweise-ausrüstung-i-buchseiten-220-249)
7. [Ausrüstung II: Waffen, Elektronik, Sensoren (Buchseiten 250–279)](#teil-7-ausrüstung-ii-waffen-elektronik-sensoren-buchseiten-250-279)
8. [Ausrüstung III: Bodytech, Magische Ausrüstung, Fahrzeuge (Buchseiten 280–305)](#teil-8-ausrüstung-iii-bodytech-magische-ausrüstung-fahrzeuge-buchseiten-280-305)
9. [Tabellen-Anhang (Buchseiten 310–339)](#teil-9-tabellen-anhang-buchseiten-310-339)
10. [Buchende: Index & Charakterbogen (Buchseiten 340–352)](#teil-10-buchende-index-charakterbogen-buchseiten-340-352)

---

## Teil 1: Grundlagen (Buchseiten 1–100)

<sub>Quelle-Chunk: `docs/sr6_rules_calculations.md` — Originaltitel: Shadowrun 6 – Regeln mit Berechnungen (Grundregelwerk, Seiten 1–100)</sub>

Quelle: `Shadowrun_6_Grundregelwerk.pdf` (deutsche Ausgabe, Pegasus Spiele), physische PDF-Seiten 1–100.

**Stand:** 2026-08 gegen `Shadowrun_6_Downloadversion_2024.pdf` (= 3. Auflage) und die [Errata zum Grundregelwerk, 3. Auflage](https://shadowrun6.de/downloads/errata/errata_sr6_grundregelwerk_aufl3.pdf) gegengeprüft. Von der Errata betroffene Stellen sind mit *„3. Auflage/Errata"* markiert. Die Gesamtübersicht der Errata-Änderungen steht im Abschnitt *Stand / Errata* am Anfang dieses Dokuments.

**Hinweis:** Physische PDF-Seiten 1–34 enthalten ausschließlich Titelei, Inhaltsverzeichnis, Einleitung, Shadowtalk-Glossar, die Kurzgeschichte "Vier ist eine runde Zahl" sowie das Fluff-Kapitel "Das Leben in der Sechsten Welt" (Metaplot/Weltbeschreibung). Dort finden sich **keine** Regeln oder Berechnungen. Alle unten aufgeführten Regeln stammen aus dem Kapitel **SPIELKONZEPTE**, das auf Buchseite 35 (≈ PDF-Seite 40) beginnt.

Buchseitenzahlen sind in Klammern angegeben, z. B. (S. 41).

---

### 1. Würfelpool & Proben (S. 36–39)

- **Würfelpool bilden**: `Fertigkeit + verknüpftes Attribut` = Anzahl der zu würfelnden W6 (sechsseitige Würfel). Bei manchen Proben werden stattdessen zwei Attribute addiert, oder dasselbe Attribut wird doppelt genommen.
- **Erfolg**: Ein Würfel zählt als Erfolg, wenn er eine 5 oder 6 zeigt.
- **Patzer**: Zeigen mehr als die Hälfte der Würfel eine 1, ist die Probe ein Patzer.
- **Kritischer Patzer**: Patzer **und** zusätzlich null erzielte Erfolge.
- **Einfache Probe**: `Erfolge ≥ Schwellenwert` → Erfolg. `Nettoerfolge = Erfolge − Schwellenwert`.
- **Vergleichende Probe**: Beide Seiten würfeln ihren Pool. `Nettoerfolge = höhere Erfolgszahl − niedrigere Erfolgszahl`. Bei Gleichstand gewinnt meist der Aggressor.
- **Ausgedehnte Probe**: Pool wird bei jedem Wurf um 1 Würfel kleiner; Erfolge aus allen Würfen werden aufsummiert, bis der Schwellenwert erreicht/überschritten ist oder keine Würfel mehr übrig sind. Jeder Wurf verbraucht ein Zeit-**Intervall** (siehe Tabelle).
- **Erfolge kaufen**: `Erfolge = Würfelpool ÷ 4, abgerundet`. Kein Edge-Einsatz möglich; nicht erlaubt, wenn ein Patzer/Kritischer Patzer das Ergebnis entscheidend beeinflussen könnte.
- **Neuer Versuch**: Jede Wiederholung derselben Probe bringt einen kumulativen `Würfelpoolmalus von −2` (−2, dann −4, dann −6, …), sofern sich die äußeren Umstände nicht geändert haben.
- **Teamworkprobe**: Helfer würfeln ihren eigenen Pool (Fertigkeit + Attribut); ihre Erfolge werden dem Anführer als Zusatzwürfel zum Pool addiert. Obergrenze: `Gesamtzahl der Zusatzwürfel ≤ Fertigkeitswert des Anführers` (bzw. der höhere der beiden Attributswerte, falls die Probe zwei Attribute verwendet).

#### Intervalle für Ausgedehnte Proben (S. 37)

| Zeitrahmen | Intervall |
|---|---|
| Extrem kurz | 1 Kampfrunde |
| Sehr kurz | 1 Minute |
| Kurz | 10 Minuten |
| Durchschnittlich | 30 Minuten |
| Lang | 1 Stunde |
| Sehr lang | 1 Tag |
| Extrem lang | 1 Woche |
| Mammutprojekt | 1 Monat |

#### Richtlinien für Schwellenwerte (S. 37)

Schwellenwerte 1–7, aufsteigend von "Einfache Aufgabe" (1) bis "Herausragend aus den Besten" (7).

#### Fixe Attribut-Proben (S. 37) – keine Fertigkeit, nur Attribute

- **Erinnerungsvermögen**: `Logik + Intuition`
- **Heben/Tragen**: `Konstitution + Willenskraft`
- **Menschenkenntnis**: `Willenskraft + Intuition`
- **Selbstbeherrschung**: `Willenskraft + Charisma`

---

### 2. Attribute (S. 39–40)

- **Modifikations-Cap**: Ein modifiziertes Attribut kann nie höher sein als `unmodifiziertes Attribut + 4`.
- **Magieattribut (max.)**: `6 + Initiatengrad`
- **Resonanzattribut (max.)**: `6 + Wandlungsgrad`
- **Essenz**: Startwert 6; sinkt durch Cyberware/Bioware. Bei jedem Unterschreiten einer ganzen Zahl verliert der Charakter 1 Punkt Magie bzw. Resonanz. Bei Essenz 0 stirbt der Charakter.

#### Zustandsmonitore (S. 40)

- **Körperlicher Zustandsmonitor**: `(Konstitution ÷ 2, aufgerundet) + 8` Kästchen
- **Betäubungs-Zustandsmonitor**: `(Willenskraft ÷ 2, aufgerundet) + 8` Kästchen
- Kästchen sind in Dreierreihen organisiert. Jede vollständig ausgefüllte Reihe erhöht den Würfelpoolmalus (auf alle Proben außer Schadenswiderstandsproben) um einen weiteren Punkt: **−1 / −2 / −3 / −4**.
- Ist der letzte Wert (−4-Reihe) komplett voll, wird der Charakter bewusstlos.
- **Überzähliger Schaden**: Schaden, der über den Körperlichen Zustandsmonitor hinausgeht, wird 1:1 auf den Betäubungs-Zustandsmonitor übertragen (s. S. 124). Erreicht der Überzählige Schaden `Konstitution × 2` Kästchen, ist der Charakter endgültig tot.

---

### 3. Initiative (S. 40–41)

- **Initiativewert**: `Reaktion + Intuition` (kann durch Bodytech/Effekte weiter erhöht werden)
- **Initiativewürfel**: Basis = 1 W6, erhöhbar durch Modifikatoren/Zauber/Effekte. Maximum: **5 W6**.
- **Initiativeergebnis**: `Initiativewert + Summe der Augenzahlen aller Initiativewürfel` (hier zählen die tatsächlichen Augenzahlen, **nicht** die Erfolge).
- **Zusätzliche Nebenhandlung**: Pro Initiativewürfel, den der Charakter besitzt, erhält er **1 zusätzliche Nebenhandlung**.
- Jeder Charakter erhält pro Kampfrunde standardmäßig **1 Nebenhandlung + 1 Haupthandlung**.
- **Handlungstausch**: 1 Haupthandlung = 4 Nebenhandlungen (und umgekehrt tauschbar).

---

### 4. Angriffs- & Verteidigungswert (S. 41)

- **Angriffswert im waffenlosen Kampf**: `Reaktion + Stärke`
- **Verteidigungswert**: Kombination aus Konstitution, Schutzkleidung/Panzerung und anderen Effekten (z. B. Bodytech, Magie).

#### Bewegung (S. 43–45)

- **Bewegen** (Nebenhandlung): bis zu **10 Meter**, nur einmal pro Kampfrunde.
- **Sprinten** (Haupthandlung): Mindeststrecke **15 Meter**, `+1 Meter pro Erfolg` einer Probe auf `Athletik + Geschicklichkeit`.

#### Zielen (S. 44)

- **Zielen**-Handlung: `+1 Würfelpoolbonus` pro Ausführung; Bonus kann über mehrere Kampfrunden akkumuliert werden. **Cap**: maximaler zusätzlicher Würfelpool durch Zielen = `Willenskraft des Charakters`.

#### Ziel ansagen (S. 44)

- `+2 Schaden`, aber `−4 Würfelpoolmalus` auf die Angriffsprobe.

#### Zu Fall bringen (S. 44)

- `−2` auf den Angriffswürfelpool; bei Erfolg Probe auf `Athletik + Geschicklichkeit` mit Schwellenwert = modifizierter Schaden des Angriffs.

#### Weghechten / Ausweichenmalus (S. 44)

| Entfernung zum Detonationspunkt (DP) | Würfelpoolmalus |
|---|---|
| Detonationspunkt | −6 |
| Sehr nah | −4 |
| Nah | −2 |

#### Volle Deckung (S. 44)

- `+2 Würfelpoolbonus` auf die Verteidigungsprobe gegen den betreffenden Angriff.
- Bis Handlung *Aufstehen*: `−2 Würfelpoolmalus` auf alle Proben mit Aktionsfertigkeiten.

---

### 5. Edge (S. 46–51)

- **Start jeder Spielsitzung**: Edge-Punkte in Höhe des Edge-Attributs.
- **Maximum während einer Sitzung**: `7`, inklusive verheiztem Edge (nicht dem Grundattributswert).
- **Edge-Erhalt durch Angriffs-/Verteidigungswert-Vergleich**: Ist der Angriffswert des Angreifers um `≥4` höher als der Verteidigungswert des Ziels (bzw. umgekehrt), erhält die überlegene Seite **1 Edge**. Bei Flächenwirkung wird der höchste Verteidigungswert der betroffenen Ziele verglichen.
- **Cap**: Maximal `2 Bonuspunkte Edge` pro Kampfrunde und Charakter.

#### Edge-Boosts (Kosten in Edge, S. 47–48)

| Kosten | Beispiel-Effekt |
|---|---|
| 1 Edge | Einen Würfel neu werfen; `+3` auf das Initiativeergebnis; heile 1 Kästchen Betäubungsschaden |
| 2 Edge | Verbündetem 1 Edge geben; Gegner 1 Edge negieren |
| 3 Edge | Automatischen Erfolg kaufen (addiert zu den erwürfelten Erfolgen) |
| 4 Edge | Edge-Attribut zum Würfelpool addieren, 6en "explodieren" (6 zählt als Erfolg und wird erneut gewürfelt) |
| 5 Edge | Beim gegnerischen Wurf zählen 2en zusätzlich als Patzer-Ergebnis |

#### Edge-Handlungen (Kosten in Edge, S. 48–49)

| Handlung | Kosten | Effekt (Kurzform) |
|---|---|---|
| Abstechen | 1 | Würfelpoolmalus von *Ziel ansagen* sinkt von −4 auf −2 |
| Plötzliche Erkenntnis | 1 | Fertigkeit ohne Ausbildung/Fertigkeitswert einsetzbar |
| Taktische Rolle | 1 | Nahkampfangriff ohne die üblichen Mali der Handlung *Volle Deckung* |
| Umwerfen | 1 | Ziel bei Erfolg zusätzlich zu Fall bringen |
| Aus der Deckung feuern | 2 | Keine Nebenhandlung nötig, Deckung bleibt erhalten |
| Dramaqueen | 2 | Geforderten Preis bei Überreden um bis zu 20 % erhöhen |
| Entwinden | 2 | Probe `Nahkampf + Geschicklichkeit` vs. Stärke des Gegners, um ihm die Waffe zu entwinden |
| K.-o.-Schlag | 2 | Betäubungs-Zustandsmonitor sofort voll befüllt, wenn Schaden > Willenskraft des Ziels |
| Große Rede | 4 | Zwei Proben auf `Einfluss + Charisma`, erste als Teamwork-Bonus zur zweiten |
| Vorausschau | 4 | Bei einem Mehrfachangriff: Würfelpool **verdoppeln** und dann möglichst gleichmäßig auf alle Ziele aufteilen (Korrektur 3. Auflage/Errata; früher „voller Pool gegen jedes Ziel") |
| Angesagtes Ziel – Entwaffnen | 5 | Erfolgreicher Treffer entwaffnet statt Schaden zu verursachen |
| Angesagtes Ziel – Lebenswichtige Organe | 5 | `+3 zusätzlicher Schaden` bei Erfolg |

#### Edge verheizen (S. 50)

- Permanenter Verlust von **1 Punkt** des Edge-Attributs (kann bis 0 sinken).
- **Durchbruch**: Nächste Probe gelingt automatisch mit **4 Nettoerfolgen**.

#### Schicksalswürfel (S. 51)

- 1 zusätzlicher, optisch unterscheidbarer W6 wird zum Würfelpool hinzugefügt.
- Erfolg auf dem Schicksalswürfel (5 oder 6) zählt als **3 Erfolge statt 1**.
- Zeigt der Schicksalswürfel eine 1, werden **alle anderen gewürfelten 5en unbrauchbar** (2, 3, 4 auf dem Schicksalswürfel haben keine besondere Bedeutung).
- Bei Edge-Einsatz mit explodierenden 6en: Eine 6 auf dem Schicksalswürfel zählt als 3 Erfolge und wird neu gewürfelt; weitere Erfolge/1en aus der Wiederholung zählen als normale Würfelergebnisse.

---

### 6. Heben & Tragen (S. 37)

- **Basis-Traglast**: `Stärke × 10 kg` (Tragen), bzw. `Stärke × 5 kg` (Heben über den Kopf).
- Bei einer Probe auf `Konstitution + Willenskraft` erhöht sich der Multiplikator um **1 pro Erfolg**.
- Die Probe selbst verursacht **1 Kästchen Betäubungsschaden**, mit Konstitution widerstanden.
- Der Schaden steigt um **1 pro weiterer Kampfrunde**, in der das Gewicht gehalten/getragen wird.

---

### 7. Connections & Beinarbeit (S. 52–53)

- **Beinarbeit-Probe**: `Einflussstufe + Charisma`. Anzahl der Erfolge bestimmt über die Tabelle *Beinarbeit*, welches Informationslevel die Connection kostenlos mitteilt.
- **Loyalitätsprobe**: `Loyalitätsstufe + Charisma` als Würfelpoolbonus, um zu ermitteln, wie viel die Connection bereit ist mitzuteilen.
- Wissen oberhalb der kostenlosen Stufe kostet **100 Nuyen pro (weiterem) Level**.
- Einfluss- und Loyalitätsstufe reichen jeweils von **1 bis 12**.

#### Beinarbeit-Tabelle (S. 53)

| Erfolge | Informationsstufe |
|---|---|
| 0 | Keine brauchbaren Informationen |
| 1 | Grundlegende, allgemein verfügbare Hintergrundinformationen |
| 2 | Ein paar Informationsbröckchen durch flüchtige Beschäftigung mit der Materie |
| 3 | Informationen durch frühere Kurse/Seminare oder einfaches professionelles Wissen |
| 4 | Schon tiefschürfenderes Wissen, ein bisschen Klatsch |
| 5 | Tiefgehendes akademisches Wissen, fundierte Vertrautheit, gute Kenntnisse |
| 6 | Wissen über Geheimnisse und verborgene Informationen |
| 7 | Hochkarätiges Wissen, fundiertes Verständnis der historischen Hintergründe |
| 8 | Fast schon enzyklopädisches Wissen, darunter tief verborgene Geheimnisse |
| 9 | Rares Wissen, das nur wenigen Eingeweihten bekannt ist |
| 10 | Tief verborgene Geheimnisse, die andere aktiv zu verbergen versuchen |

(Jede Stufe schließt das Wissen aller darunterliegenden Stufen ein.)

---

### 8. Lebensstil-Kosten (S. 59)

Monatliche Kosten pro Lebensstil:

| Lebensstil | Kosten/Monat |
|---|---|
| Auf der Straße | 0 Nuyen |
| Squatter | 500 Nuyen |
| Unterschicht | 2.000 Nuyen |
| Mittelschicht | 5.000 Nuyen |
| Oberschicht | 10.000 Nuyen |
| Luxus | 100.000 Nuyen |

---

### 9. Status-Effekte mit Berechnungen (S. 53–55)

Auszug der Status mit konkreten Zahlenwerten (viele weitere Status auf S. 55 f. sind noch nicht erfasst, da sie außerhalb des Seitenbereichs 1–60 liegen):

- **Benommen**: `−4` auf das Initiativeergebnis; kein Edge-Erhalt/-Einsatz möglich (Verheizen weiterhin möglich).
- **Bewegungsunfähig**: Angriffswert `−3`; Würfelpoolmalus `−3` auf alle Angriffe; keine Reaktion bei Verteidigungsproben.
- **Deckung I–IV**: pro Stufe `+1 Verteidigungswert` **und** `+1 Würfelpoolbonus` auf Verteidigungsproben; aus der Deckung angreifen kostet zusätzlich eine Nebenhandlung und `−2 Würfelpoolmalus` (in Deckung IV kein Edge-Erhalt beim Angreifen möglich).
- **Erschöpft I–III**: pro Stufe `−2 Würfelpoolmalus` auf alle Proben außer Schadenswiderstandsproben; Bewegung 5 m statt 10 m Gehen, 10 m statt Sprinten.
- **Erstarrt**: `−10` auf den Verteidigungswert gegen Angriffe (Minimum 0); keine Handlungen außer Wahrnehmung/geistiger Kommunikation; keine Schadenswiderstandsproben.
- **Ertaubt I–III**: Stufen 1–2: `−3 Würfelpoolmalus` auf hörbezogene Proben; Stufe 3: automatisches Scheitern hörbezogener Proben.
- **Geblendet I–III**: analog zu Ertaubt, aber für Sehen (`−3` auf Stufen 1–2, automatisches Scheitern auf Stufe 3).
- **Gebrutzelt**: `−2` auf Initiativeergebnis; `−1 Würfelpoolmalus` auf alle Handlungen.
- **Geräuschlos #**: Zahl = Schwellenwert für Wahrnehmungsprobe, um den Charakter zu hören.
- **Humpelnd**: Bewegungsrate (zu Fuß) wird halbiert (aufgerundet).
- **Liegend**: Bewegungsrate 2 m, kein Sprinten; `+2 Würfelpoolbonus` gegen Fernkampf aus mittlerer/größerer Entfernung, `−2` gegen Angriffe aus naher/sehr naher Entfernung; `−4` gegen Nahkampf-/Bogenangriffe; Angriffswert von Feuer-/Projektilwaffen (außer Bögen) `+2`.
- **Nass**: `−6 Würfelpoolmalus` auf Schadenswiderstandsproben gegen Kälte-/Elektrizitätsschaden.
- **Panisch**: Keine Handlungen außer Flucht vor der auslösenden Ursache.
- **Unsichtbar # / Unsichtbar (verbessert) #**: Zahl = Schwellenwert für Wahrnehmungsprobe, um den Charakter zu sehen.
- **Unterkühlt**: `−4` auf Initiativeergebnis; `−1 Würfelpoolmalus` auf alle Proben außer Schadenswiderstandsproben.
- **Verängstigt**: `−4 Würfelpoolmalus` auf alle Proben gegen die Quelle des Effekts.
- **Verätzt #**: Schaden entsprechend der angegebenen Zahl pro Kampfrunde; verringert sich um **1 pro Kampfrunde**.
- **Vergiftet #**: Schaden gemäß angegebenem Wert; am Ende jeder Kampfrunde Probe auf Konstitution, bei Erfolg Schaden `−1`.
- **Versteinert**: Verteidigungswert `+10`; keine Handlungen möglich.
- **Verwirrt #**: Zahl = Würfelpoolmalus für alle Handlungen.
- **Übelkeit**: Probe auf `Konstitution + Willenskraft` (Schwellenwert 2) zu Beginn jeder Kampfrunde; bei Misslingen keine Handlung, bei Gelingen Verlust der Nebenhandlung.

---

---

### 10. Charaktererschaffung: Prioritätensystem (S. 64–66)

Fünf Kategorien (Metatyp/Anpassungspunkte, Attribute, Fertigkeiten, Magie oder Resonanz, Ressourcen) erhalten je eine Priorität A–E (jede Priorität nur einmal vergeben).

#### Prioritätentabelle (S. 65)

| Priorität | Metatyp (Anpassungspunkte) | Attribute | Fertigkeiten | Magie oder Resonanz | Ressourcen |
|---|---|---|---|---|---|
| A | Ork, Troll, Zwerg (13) | 24 | 32 | Aspektzauberer: Magie 5; Vollzauberer/Magieadept/Adept: Magie 4; Technomancer: Resonanz 4 | 450.000 ¥ |
| B | Elf, Ork, Troll, Zwerg (11) | 16 | 24 | Aspektzauberer: Magie 4; Vollzauberer/Magieadept/Adept: Magie 3; Technomancer: Resonanz 3 | 275.000 ¥ |
| C | Elf, Mensch, Ork, Troll, Zwerg (9) | 12 | 20 | Aspektzauberer: Magie 3; Vollzauberer/Magieadept/Adept: Magie 2; Technomancer: Resonanz 2 | 150.000 ¥ |
| D | Elf, Mensch, Ork, Troll, Zwerg (4) | 8 | 16 | Aspektzauberer: Magie 2; Vollzauberer/Magieadept/Adept: Magie 1; Technomancer: Resonanz 1 | 50.000 ¥ |
| E | Elf, Mensch, Ork, Troll, Zwerg (1) | 2 | 10 | Mundan | 8.000 ¥ |

- Attributspunkte werden **1:1** ausgegeben: jeder Punkt erhöht das gewählte Körperliche oder Geistige Attribut um 1. **Edge kann nur mit Anpassungspunkten erhöht werden**, nicht mit normalen Attributspunkten.
- **Fortgeschrittenes Spielniveau** (optional, S. 65): Individualisierungskarma wird verdoppelt (50 → 100).

#### Attribute nach Metatyp (S. 66) – gültige Bandbreiten

| Metatyp | KON | GES | REA | STA | WIL | LOG | INT | CHA | EDG |
|---|---|---|---|---|---|---|---|---|---|
| Mensch | 1–6 | 1–6 | 1–6 | 1–6 | 1–6 | 1–6 | 1–6 | 1–6 | 1–7 |
| Elf | 1–6 | 1–7 | 1–6 | 1–6 | 1–6 | 1–6 | 1–8 | 1–6 | 1–6 |
| Ork | 1–8 | 1–6 | 1–6 | 1–8 | 1–6 | 1–6 | 1–5 | 1–6 | 1–6 |
| Troll | 1–9 | 1–5 | 1–6 | 1–9 | 1–6 | 1–6 | 1–5 | 1–6 | 1–6 |
| Zwerg | 1–7 | 1–6 | 1–5 | 1–8 | 1–6 | 1–6 | 1–6 | 1–6 | 1–6 |

#### Magie/Resonanz – kostenlose Zauber, Kraftpunkte, Komplexe Formen (S. 67)

- **Vollzauberer**: kostenlose Zauber und/oder Rituale (zusammen) = `Magie × 2` (unmodifizierter Magiewert laut Prioritätentabelle, vor Anpassungspunkten/Karma). *(3. Auflage/Errata: alchemistische Zauber sind keine eigene Kategorie mehr — Alchemie nutzt die normalen bekannten Zauber.)*
- **Aspektzauberer – Hexer**: kostenlose Zauber/Rituale = `Magie × 2`.
- **Aspektzauberer – Verzauberer**: kostenlose alchemistische Zauber = `Magie × 2`.
- **Adepten**: Kraftpunkte für Adeptenkräfte = `Magieattribut` (1:1, direkt gleich dem Attributswert).
- **Technomancer**: Anzahl Komplexer Formen = `Resonanz × 2` (unmodifizierter Wert laut Prioritätentabelle).

---

### 11. Vor-/Nachteile, Individualisierungskarma & letzte Berechnungen (S. 68–70)

- **Vor- und Nachteile-Limit**: max. **6** Vor- und Nachteile insgesamt bei der Charaktererschaffung; Netto-Karmabonus (Nachteile − Vorteile) darf **20 Karma nicht überschreiten**. Vor-/Nachteile durch den Metatyp zählen nicht gegen dieses Limit.
- **Individualisierungskarma**: **50 Karma** (100 im "fortgeschrittenen Spielniveau") zur freien Verbesserung von Fertigkeiten/Attributen (reguläre Entwicklungskosten gelten, s. Abschnitt 12) oder zum Umwandeln in Geld.
- **Karma-zu-Geld-Umtausch**: `1 Karma = 2.000 Nuyen` (bzw. `5.000 Nuyen` mit dem Nachteil *Verschuldet*, s. S. 81).
- **Übrig gebliebenes Karma** (S. 69, 3. Auflage/Errata): Bis zu **5 Karma** aus der Charaktererschaffung dürfen ins Spiel mitgenommen werden (früher: verfällt vollständig).
- **Verfügbarkeits-Cap bei der Erschaffung** (S. 69, 3. Auflage/Errata): Es darf nur Ausrüstung mit **Verfügbarkeit ≤ 7** gekauft werden (früher: legale Ausrüstung unbegrenzt, illegale max. 6).
- **Magie/Resonanz-Cap bei der Erschaffung** (S. 67, 3. Auflage/Errata): Mit Anpassungspunkten aus der Spalte *Metatyp* oder mit Individualisierungskarma darf Magie/Resonanz **bis maximal 6** erhöht werden.
- **Connections**: Bei der Charaktererschaffung stehen `Charisma × 6` Punkte zur Verfügung, die frei auf Einfluss- und Loyalitätsstufen der Connections verteilt werden. Keine Einzelstufe darf zu diesem Zeitpunkt höher sein als das Charisma des Charakters.
- **Wissens- und Sprachfertigkeiten**: Anzahl der Wissensfertigkeiten bei Erschaffung = `Logik-Wert`, zusätzlich 1 Muttersprache kostenlos.
- **Angriffswert (waffenlos)**: `Reaktion + Stärke` (Wiederholung der Regel aus S. 41/69).
- **Verteidigungswert**: `Konstitution + Verteidigungswertbonus durch Panzerung` (+ ggf. Bodytech/Magie-Boni).
- **Initiative**: `Reaktion + Intuition` als Initiativewert, plus Initiativewürfel (Basis 1W6, erhöhbar, max. 5W6). Beispielschreibweise: `9 + 1W6` für Reaktion 4 + Intuition 5.
- **Startkapital**: übriges Geld nach dem Ausrüstungskauf. Bei mehr als 5.000 Nuyen Restbetrag muss weiter eingekauft werden (z. B. ein Lebensstil), da man nicht mehr als 5.000 Nuyen Bargeld mit ins Spiel nehmen darf.

---

### 12. Charakterentwicklung – Karma-Kosten für Verbesserungen (S. 71–72)

Charaktere verbessern Fertigkeiten/Attribute im Spielverlauf mit verdientem Karma nach folgenden Kosten:

#### Entwicklungskosten-Tabelle (S. 72)

| Art | Karmakosten | Trainingszeit |
|---|---|---|
| Aktionsfertigkeiten | `neue Stufe × 5` | `[neue Stufe]` Monate |
| Spezialisierungen | 5 | 1 Monat |
| Expertise | 5 | 2 Monate |
| Attribute | `neue Stufe × 5` | `[neue Stufe × 2]` Monate |
| Wissensfertigkeiten | 3 | 1 Monat |
| Sprachfertigkeiten | 3 pro Stufe | 1 Monat pro Stufe |
| Neuer Vorteil | Karmakosten bei Erschaffung × 2 | 1 Woche |
| Nachteil entfernen | Karmabonus bei Erschaffung × 2 | 1 Woche |
| Neuer Zauber * | 5 pro Zauber | siehe S. 132 |
| Neues Ritual * | 5 pro Ritual | siehe S. 132 |
| Neue Komplexe Form * | 5 pro Form | 1 Woche |
| Initiation | `10 + neuer Initiatengrad` | `[neuer Initiatengrad + 1]` Monat(e) |
| Wandlung | `10 + neuer Wandlungsgrad` | `[neuer Wandlungsgrad + 1]` Wochen |

- `*` **3. Auflage/Errata**: Zeile *Neuer alchemistischer Zauber* entfernt; neue Zauber, Rituale und Komplexe Formen können **nicht während der Charaktererschaffung** erworben werden (nur im Spiel mit Karma).
- Jede Attribut-/Fertigkeitssteigerung wird **einzeln pro Stufe** bezahlt und aufsummiert, z. B. Attribut von 4 auf 6: `Stufe 5 (5×5=25) + Stufe 6 (6×5=30) = 55 Karma`.
- Trainingsvoraussetzung: mindestens **4 Stunden Training pro Tag**; mehrere Fertigkeiten können parallel trainiert werden (mehrere 4-Stunden-Blöcke pro Tag).
- Vorteil kaufen (nach Erschaffung): **doppelter** ursprünglicher Karmapreis. Neue Nachteile können nach der Erschaffung *nicht* "gekauft" werden. Bestehende Nachteile lassen sich entfernen für das **Doppelte** des ursprünglichen Karmabonus.

#### Kumulative Kosten – Entwicklung von Attributen und Fertigkeiten (S. 72)

Kumulierte Karmakosten, um von der Ausgangsstufe (Zeile) auf die gewünschte Stufe (Spalte) zu kommen:

| Ausgangsstufe → | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 5 | 15 | 30 | 50 | 75 | 105 | 140 | 180 | 225 | 275 |
| **1** | — | 10 | 25 | 45 | 70 | 100 | 135 | 175 | 220 | 270 |
| **2** | — | — | 15 | 35 | 60 | 90 | 125 | 165 | 210 | 260 |
| **3** | — | — | — | 20 | 45 | 75 | 110 | 150 | 195 | 245 |
| **4** | — | — | — | — | 25 | 55 | 90 | 130 | 175 | 225 |
| **5** | — | — | — | — | — | 30 | 65 | 105 | 150 | 200 |
| **6** | — | — | — | — | — | — | 35 | 75 | 120 | 170 |
| **7** | — | — | — | — | — | — | — | 40 | 85 | 135 |
| **8** | — | — | — | — | — | — | — | — | 45 | 95 |
| **9** | — | — | — | — | — | — | — | — | — | 50 |

(Entspricht der Summenformel `Σ(Stufe × 5)` über alle Zwischenstufen.)

---

### 13. Fertigkeiten – Formeln und Schwellenwerte (S. 94–99)

- **Fertigkeitswerte**: 1–9 (10 mit dem Vorteil *Talentiert*).
- **Spezialisierung**: `+2 Würfelpoolbonus` auf das entsprechende Teilgebiet. **Expertise** (erfordert vorher erworbene Spezialisierung + Fertigkeitswert ≥5): Bonus steigt auf `+3`; erlaubt zusätzlich eine zweite Spezialisierung in derselben Fertigkeit (max. 1 Expertise + 1 Spezialisierung pro Fertigkeit).
- **Ungeübter Einsatz** (nur Fertigkeiten mit "Ungeübt: Ja"): Würfelpool = `verknüpftes Attribut − 1`.

#### Athletik (S. 95)

- **Springen** (`Athletik + Geschicklichkeit`): Weitsprung `1 Meter` (aus dem Stand) bzw. `2 Meter` (mit Anlauf) **pro Erfolg**, maximal `Geschicklichkeit × 1,5` Meter. Hochsprung: `0,5 Meter pro Erfolg`, maximal `Körpergröße × 1,5` Meter.
- **Klettern** (`Athletik + Stärke`): pro Nettoerfolg **1 Meter** in beliebige Richtung (hoch/runter/seitwärts). Kletterausrüstung gewährt zu Beginn 1 Edge-Punkt für diese Kletterpartie.
  - **Schwellenwerte Klettern** (S. 95): Basis 3; `+1` glatte Oberfläche; `+1` nasse/rutschige Oberfläche; `+1` eingefettete Oberfläche; `−1` Oberfläche mit ausgeprägten Hand-/Fußgriffen.
- **Schwimmen** (`Athletik + Geschicklichkeit(2)`, Nebenhandlung): Grundgeschwindigkeit `3 Meter/Kampfrunde`; zusätzliche Strecke = `[Nettoerfolge ÷ 2, abgerundet]` Meter. Schwellenwert erhöht sich alle 15 Minuten um 1.
- **Entfesseln** (`Heimlichkeit + Geschicklichkeit`) – **Schwellenwerte**: Seil/Plastikhandschellen 2, Metallhandschellen 3, Zwangsjacke 4, Cyberwareblocker 5 (`+1` bei verstärktem Material). Situationsmodifikator: Charakter wird beobachtet `+1`.

#### Mechanik – Bauen/Reparieren (S. 97–98)

- Probe: `Mechanik + Logik`, Ausgedehnte Probe.
- **Schwellenwerte** (Basis 3, kumulative Modifikatoren): Normales Fahrzeug `+4`, Industriefahrzeug `+6`, Militärfahrzeug `+8`, Cyberdeck (siehe *Reparieren von Matrixschaden*, S. 175), Lizenzpflichtige Elektronik `+1`, Illegale Elektronik `+2`, Nur für spezielle Einsatzzwecke `+1`.
- **Intervalle** (Basis 1 Stunde, Multiplikatoren): Einfach `×1`, Komplex `×2`, Weitreichend `×4`, Totalschaden `×10`.
- **Cyberware-Einbau**: Schwellenwert = `Stufe × 3` (ohne Stufen: wie Stufe 2 behandeln), Intervall 1 Stunde.
- **Improvisieren** (Mechanik + Intuition, Einfache Probe, *nicht* nach den obigen Schwellenwerten): Gegenstand funktioniert `[Nettoerfolge]` Minuten; danach neue Probe mit um mind. 1 höherem Schwellenwert möglich.

#### Heimlichkeit – Gruppentarnung (S. 97)

- Bei sehr großen Gruppen kann die Spielleitung einen Würfelpoolmalus von bis zu `[Konstitution ÷ 2, aufgerundet]` des jeweiligen Charakters auf die Schleichenprobe verhängen.

#### Wahrnehmung – Schwellenwerte (S. 99)

| Ziel | Schwellenwert | Beispiele |
|---|---|---|
| Offensichtlich/Groß/Laut | 1 | Neonschild, Menschenmasse, Geschrei, Schüsse |
| Normal | 2 | Verkehrszeichen, Fußgänger, gedämpfte Schüsse |
| Verborgen/Klein/Gedämpft | 3 | Gegenstand unter dem Tisch, Kontaktlinse, Flüstern |
| Versteckt/Winzig/Leise | 4 | Geheimtür, Nadel im Heuhaufen, subvokale Kommunikation |

---

### Nicht erfasst / außerhalb des Bereichs

Der Bereich PDF-Seiten 1–100 endet in der Fertigkeitenliste kurz vor *Wissensfertigkeiten*/*Sprachfertigkeiten* (S. 100). Kampf-, Magie-, Matrix- und Ausrüstungsformeln (Schadenswert, Panzerung, Zauberkraft, Matrixattribute, Verfügbarkeit/Preis-Berechnungen, Initiative-Varianten für Astral/Matrix/Rigging usw.) liegen jenseits von Seite 100 und sind hier nicht enthalten.

---

## Teil 2: Kampf (Buchseiten 100–129)

<sub>Quelle-Chunk: `docs/sr6/sr6_calc_p101-130.md` — Originaltitel: SR6 Regeln mit Berechnungen — Buchseiten 100–129</sub>

Quelle: `sr6_p101-130.pdf` (physische PDF-Seiten 101–130 des deutschen Grundregelwerks). Die gedruckten Buchseiten in diesem Auszug reichen von S. 100 bis S. 129.

**Hinweis:** Die Buchseiten 102–106 enthalten ausschließlich die Kurzgeschichte "Der Weg nach oben" (reiner Fluff, keine Regeln). Buchseite 129 ist lediglich die Kapitelauftaktseite von MAGIE (Fluff-Text, keine Zahlen). Beide Bereiche sind unten nicht vertreten.

---

### 1. Fertigkeiten – Skala und Sprachstufen (S. 100–101)

- **Fertigkeitswerte-Tabelle** (S. 101): Werte 0–12+ entsprechen `Fertigkeitswert + Spezialisierungs-/Expertise-Bonus` (Summe). 0 = Ungeübt, 12+ = "Bester der Besten".
- **Sprachfertigkeiten** (S. 100), vier Stufen pro Sprache:
  - Stufe 1 (Sprachfertigkeit selbst): Verstehen einzelner Wortfetzen nur via Wahrnehmungsprobe (Schwellenwert nach *Richtlinien für Schwellenwerte*, S. 37).
  - Stufe 2 (Spezialist): `+2 Würfelpoolbonus` auf alle Proben, die mit dem Verstehen der Sprache zusammenhängen.
  - Stufe 3 (Experte): Bonus steigt auf `+3`.
  - Stufe 4 (Muttersprachler): keine Probe nötig.

---

### 2. Kampfablauf – Schritt für Schritt (S. 107–109)

#### Schritt 1: Würfelpools bilden

- **Angriffswürfelpool**: `[passende Waffenfertigkeit] + Geschicklichkeit` (bei Fahrzeugwaffen: `Mechanik + Logik` statt Geschicklichkeit).
- **Verteidigungswürfelpool**: `Reaktion + Intuition`.

#### Schritt 2: Edge verteilen

- **Angriffswert vs. Verteidigungswert**: Ist einer der Werte um `≥4` höher, erhält die überlegene Seite `1 Edge`. (Waffenloser Angriffswert = `Reaktion + Stärke`.)
- **Umgebung/Sichtverhältnisse**: Kompensiert nur eine Seite eine schlechte Sicht-/Lichtsituation (z. B. Dunkelsicht), erhält sie `1 Edge`. Kompensieren beide oder keine, erhält niemand Edge.
- **Cap**: maximal `2 Bonus-Edge` pro Charakter und Kampfrunde (Session-Maximum weiterhin 7, s. Abschnitt Edge im ersten Regelteil).

#### Schritt 3: Würfeln und Edge ausgeben

- Erfolg = 5 oder 6. Patzer-Bestimmung wie gehabt (mehr als die Hälfte der Würfel zeigt 1).
- Vergleich der Erfolge Angreifer vs. Verteidiger: `Nettoerfolge = höhere Erfolgszahl − niedrigere Erfolgszahl`, addiert zum `Schadenswert` der Waffe.
- Bei **Gleichstand der Erfolge** ist der Angriff automatisch erfolgreich, aber nur mit dem unmodifizierten (normalen) Schadenswert der Waffe (Nettoerfolge = 0).

#### Schritt 4: Schaden widerstehen

- **Konstitutionsprobe**: Würfelpool = Konstitution. Jede 5/6 absorbiert `1 Punkt` des modifizierten Schadens.

#### Schritt 5: Schmerz spüren

- Restschaden wird auf den passenden Zustandsmonitor eingetragen. Zusatzeffekte (elementare Schadensarten) greifen nur, wenn der Angriff `≥1 Kästchen` Schaden verursacht hat.

#### Edge-Boosts im Kampf (S. 109) – Timing: *vor* Wurf / *nach* Wurf / *immer*

| Kosten | Effekt (Timing) |
|---|---|
| 1 Edge | 1 Würfel neu würfeln (nach) · +3 auf Initiativeergebnis (immer) · Edge-Handlung ausführen (vor) |
| 2 Edge | +1 zu einem einzelnen Würfelwurf (nach) · Verbündetem 1 Edge geben (immer) · 1 Edge eines Gegners negieren (vor) · Edge-Handlung ausführen (vor) |
| 3 Edge | Automatischen Erfolg kaufen (immer) · 1 Kästchen Betäubungsschaden heilen (immer) |
| 4 Edge | Edge-Attribut zum Würfelpool addieren + Sechsen explodieren (vor) · 1 Kästchen Körperlichen Schaden heilen (immer) · alle erfolglosen Würfel neu würfeln (nach) · Edge-Handlung ausführen (vor) |
| 5 Edge | 2en zählen beim Gegner zusätzlich als Patzer (vor) · speziellen Effekt hervorrufen (immer) · Edge-Handlung ausführen (vor) |

---

### 3. Initiative und Handlungen (S. 110)

- **Kampfrunde** ≈ 3 Sekunden Spielwelt-Zeit.
- Jeder Charakter: `1 Nebenhandlung + 1 Haupthandlung` als Grundausstattung, `+1 Nebenhandlung pro Initiativewürfel`.
- **Handlungstausch**: `1 Haupthandlung = 4 Nebenhandlungen` (in beide Richtungen tauschbar).
- **Cap**: Ein Charakter kann seinen Zug in einer Runde nie mit mehr als `5 Nebenhandlungen` beginnen; ein höherer Wert wird auf 5 gekappt.
- **Gleichstand der Initiativeergebnisse**: Auflösung in der Reihenfolge ERIM (Edge, Reaktion, Intuition, Münzwurf); der Münzwurf löst jeden verbleibenden Gleichstand endgültig auf.
- Zwischen Kampfrunden wird nicht neu gewürfelt; die Reihenfolge bleibt bestehen, bis Verletzungen/Effekte sie ändern.

### 4. Überraschung (S. 110–111)

- **Überraschungsprobe**: `Reaktion + Intuition`, Schwellenwert 3 (vom Spielleiter je nach Informationsgrad/Vorbereitung modifizierbar).
- Wer die Probe nicht schafft: würfelt zwar Initiative, kann aber in der ersten Kampfrunde keine Handlungen durchführen (Verteidigung/Schadenswiderstand weiterhin möglich).

---

### 5. Reichweitenkategorien (S. 111–112)

| Kategorie | Entfernung |
|---|---|
| Sehr nah | 0–3 Meter |
| Nah | 4–50 Meter |
| Mittel | 51–250 Meter |
| Weit | 251–500 Meter |
| Sehr weit | 501+ Meter |

Besitzt eine Waffe in einer Reichweitenkategorie keinen Angriffswert, ist sie dort nicht einsetzbar.

### 6. Waffen-/Panzerungswerte, Feuermodi (S. 112)

- **Waffenloser Nahkampf-Schadenswert**: `2B` (Basis).
- **Feuermodi** (3. Auflage/Errata): **Jede** Fernkampfwaffe kann im **EM** feuern, auch wenn nicht ausdrücklich aufgeführt. HM/SM/AM sind zusätzliche taktische Optionen auf Kosten der Genauigkeit und **erfordern keine Nebenhandlung *Mehrfachangriffe***.
  - **EM** (Einzelschuss, eine Kugel): keine Modifikation.
  - **HM** (Halbautomatisch, zwei Kugeln): `Angriffswert −2`, `Schadenswert +1`.
  - **SM – Enge Salve** (4 Kugeln, ein Ziel): `Angriffswert −4`, `Schadenswert +2`.
  - **SM – Breite Salve** (4 Kugeln): Würfelpool auf zwei Ziele aufgeteilt, jedes Ziel wird effektiv im HM-Modus behandelt (`Angriffswert −2`, `Schadenswert +1` je Ziel), keine Nebenhandlung *Mehrfachangriffe* nötig. *Vorausschau* (S. 49) darf mit einer Breiten Salve kombiniert werden, ebenfalls ohne Nebenhandlung *Mehrfachangriffe*.
  - **Nicht genug Munition** für volle Salve (4 Kugeln): `Angriffswert −1` pro fehlender Kugel; `Schadenswert +1` (statt +2) nur, wenn mindestens 2 Kugeln abgefeuert wurden.
  - **AM** (Vollautomatisch) — *neu 3. Auflage/Errata*: **Ein** Angriff gegen **jedes gültige Ziel in einem Bereich mit Radius 1 Meter**. Es wird nur **eine Angriffsprobe** abgelegt, aber **jeder Verteidiger** legt seine eigene Verteidigungsprobe ab. `Angriffswert −6`, verbraucht **10 Schuss**. Der Zielbereichs-Radius kann mehrfach um je 1 Meter vergrößert werden, indem pro Meter zusätzlich `−2` vom Angriffswert abgezogen wird — aber nur, solange der Angriffswert dabei mindestens 1 bleibt.

### 7. Elementare Schadensarten (S. 112–113)

- **Chemisch** (Säuren/Basen): Schaden über mehrere Kampfrunden hinweg; Status *Verätzt*. Übersteigt der modifizierte Schadenswert eines chemischen Angriffs den Verteidigungswert der getroffenen Panzerung, sinkt deren Verteidigungswert permanent um `1`.
- **Elektrizität**: Erleidet der Charakter mindestens `1 Kästchen` Schaden (trotz Widerstand), erhält er für `2 Kampfrunden` den Status *Gebrutzelt*.
- **Feuer**: Bei Feuerschaden erhält das Ziel den Status *Brennend*; brennbare Objekte fangen Feuer und brennen mehrere Runden weiter.
- **Kälte**: Bei Kälteschaden Status *Unterkühlt* für `3 Kampfrunden`. Übersteigt der modifizierte Schadenswert eines Kälteangriffs den Verteidigungswert der getroffenen Panzerung, sinkt deren Verteidigungswert permanent um `1`.

---

### 8. Nahkampfoptionen (S. 113–114)

- **Angriffe mit der Nebenhand**: kein Edge-Erhalt und keine Edge-Ausgabe möglich (außer mit dem Vorteil *Beidhändigkeit*).
- **Niederschlag**: Ist der nach der Widerstandsprobe erlittene Schaden höher als die Konstitution des Ziels, erhält es den Status *Liegend* (Aufhebung nur über die Nebenhandlung *Aufstehen*).
- **Ringen** (Einleitung): Angriff wie gewohnt mit `Nahkampf + Geschicklichkeit`. Bei Erfolg: Vergleichende Probe `Stärke + Nettoerfolge` (Angreifer) gegen `Stärke` (Verteidiger). Gewinnt der Angreifer, ist der Verteidiger im Griff: Verteidiger erhält `−4 Würfelpoolmalus` auf Verteidigungsproben; Angreifer erhält automatisch `1 Edge`.

#### Handlungen im Griff (S. 113–114)

- **Festhalten** (Angreifer): Vergleichende Probe `Nahkampf + Stärke` vs. `Nahkampf + Stärke`, Verteidiger weiterhin mit `−4`.
- **Schaden zufügen** (Angreifer): Vergleichende Probe `Nahkampf + Stärke` vs. `Reaktion + Stärke` (Verteidiger mit `−4`). Erfolg: Schaden = `2B + Nettoerfolge`.
- **Gegner zu Boden werfen** (Angreifer): Vergleichende Probe `Nahkampf + Stärke` vs. `Konstitution + Stärke` (Verteidiger **ohne** `−4`, da nicht mehr festgehalten). Erfolg: Status *Liegend* + Schaden `(Konstitution des Angreifers + Nettoerfolge)B`, widerstanden mit Konstitution.
- **Sich losreißen** (Verteidiger, 3. Auflage/Errata): **Vergleichende Probe** `Nahkampf + Stärke` gegen `Nahkampf + Stärke` des Angreifers, **ohne** den `−4`-Malus (für die Edge-Verteilung zählen die waffenlosen Angriffswerte). Gelingt die Probe, verursacht der Verteidiger keinen Schaden, befreit sich aber aus dem Griff. *(Früher als Schwellenwert-Probe gegen die Nettoerfolge der Ringen-Probe formuliert.)*

### 9. Mehrfachangriffe (S. 114, Fassung 3. Auflage/Errata)

- Mehrfachangriffe richten sich gegen **mehr als einen Gegner** (das mehrfache Angreifen desselben Ziels sowie eine Obergrenze für die Angriffszahl sind in der 3. Auflage **entfallen**).
- Würfelpool wird durch die **Anzahl der Angriffe** geteilt (Würfel so gleichmäßig wie möglich verteilen).
- Zwei unterschiedliche Angriffsarten (z. B. Pistole + Messer): beide normalerweise verwendeten Würfelpools **zuerst je durch 2 teilen und abrunden**, dann jeweils noch durch die Anzahl der mit diesem Angriffstyp angegriffenen Ziele teilen.
- Die Verteidiger legen wie gewohnt je eine eigene Verteidigungsprobe ab.

---

### 10. Barrieren – Durchbrechen (S. 115–117)

- **Deckung durch Barriere**: `(Strukturstufe der Barriere ÷ 2, aufgerundet)` wird vom unmodifizierten Schaden eines Angriffs auf die dahinter befindliche Person abgezogen.

#### Mit normalen Feuerwaffen (S. 115)

| Bedingung (unmodifizierter Schadenswert SW vs. Strukturstufe ST) | Ergebnis |
|---|---|
| `SW < ST/2` | kein Loch |
| `ST/2 ≤ SW < ST` | Loch ⌀ 1 cm |
| `SW = ST` | Loch ⌀ 2 cm |
| `SW > ST` | Loch ⌀ `2 cm + 1 cm pro Punkt über ST` |

- Einzelschuss-Modus: 1 Loch pro Angriff. Halbautomatischer Modus: 2 Löcher pro Angriffshandlung. Salvenmodus: 1 Loch pro Angriff, aber der Schadenswert wird vorher gemäß Feuermodi erhöht (Enge Salve: `+2`).

#### Mit Vollautomatischem Modus (S. 115)

| Bedingung | Ergebnis |
|---|---|
| `SW < ST/2` | nur Querschläger, kein Loch |
| `ST/2 ≤ SW < ST` | Loch ⌀ 5 cm |
| `SW = ST` | Loch ⌀ 10 cm |
| `SW > ST` | `+1 cm Durchmesser pro Punkt über ST` |

#### Mit geeigneten Nahkampfwaffen (Äxte, Pickel, Hämmer) (S. 115)

- Vorab eine Stärkeprobe ablegen; Erfolge erhöhen den Schadenswert der Waffe (`modifizierter SW = SW + Erfolge`).
- Gleiche Schwellen wie beim Vollautomatischen Modus (`ST/2` → 5 cm, `ST` → 10 cm, `+1 cm` pro Punkt darüber); unter `ST/2` kann die Waffe die Barriere nicht durchdringen.

#### Mit Sprengstoffen (S. 115)

- Vergleich nutzt den `Schadenswert in der Reichweite Sehr nah`.

| Bedingung | Ergebnis |
|---|---|
| `SW < ST/2` | Explosion durchschlägt nicht |
| `ST/2 ≤ SW < ST` | Loch ⌀ ≈ 0,5 m |
| `SW = ST` | Loch ⌀ 1 m, `+0,5 m pro Punkt über ST` |

- **Schrapnellwolke bei zerstörter Barriere**: `Schadenswert = Schadenswert des Sprengstoffs − Strukturstufe der Barriere`; `Explosionsradius = (modifizierter Schadenswert ÷ 2) Meter`.

### 11. Strukturstufen-Tabelle (S. 117)

| Stufe | Material |
|---|---|
| 1 | Papier (dünn) |
| 2 | Glas (dünn) |
| 3 | Papierstapel (1 cm) |
| 4 | Glas (1 cm) |
| 5 | Mörtel, hohle Holztür, Leichtbaumöbel |
| 6 | Gipskarton |
| 7 | Massive Holztür, Massivholzmöbel |
| 8 | Elektronische Ausrüstung, Absperrkette |
| 9 | Sicherheitsglas, Blech |
| 10 | Densiplast, dünner Baum |
| 11 | Holztür mit Metallkern/-verkleidung, Panzerglas |
| 12 | Ziegel, dicker Baum |
| 13 | Kevlar-Wandplatte |
| 14 | Plasbeton |
| 15 | Beton |
| 16 | Sicherheitstür |
| 17 | Metallträger, dicke Metallplatte |
| 18 | Verkleidung aus abgereichertem Uran |
| 19 | Stahlbeton |
| 20 | Bunker |

### 12. Fallschaden (S. 117)

- Fall aus mehr als `3 Metern`: Schadenswert = `(gefallene Meter ÷ 2, aufgerundet? – Buch: Hälfte der Meter)`, widerstanden mit Konstitution. Spielleiter passt den Wert je nach Untergrund an.

### 13. Schergen-Gruppen (S. 117)

- **Grundwerte der Gruppe**: höchster Angriffswert + höchster Würfelpool unter den Mitgliedern.
- `Angriffswert_Gruppe = höchster Angriffswert + (Anzahl Mitglieder − 1)` (jedes zusätzliche Mitglied ab dem zweiten `+1`).
- `Würfelpool_Gruppe = höchster Würfelpool + 1` für jedes **ungerade** Mitglied ab dem dritten (3., 5., 7. Mitglied usw.).
- Empfehlung: Gruppengröße max. `5 Mitglieder`.
- Die Gruppe legt **eine** Angriffsprobe ab und verursacht auch nur **einmal** Schaden.

---

### 14. Sprengangriffe und Abweichung (S. 118–119)

- Reichweitenkategorien für Explosionswirkung: **Detonationspunkt** (DP, innerhalb 1 m), **Sehr nah** (1–3 m), **Nah** (4–50 m), darüber hinaus Mittel/Weit/Sehr weit je nach Sprengwaffe (Standard-Maximalradius ohne Angabe: 50 m).
- **Angriffsprobe**: `Waffenfertigkeit + Geschicklichkeit`. Zusätzliche Erfolge verringern die Abweichungsdistanz.
- Abweichungsrichtung: Spielleiter würfelt `2W6` gegen das Abweichungsdiagramm (Ergebnisse 2 und 12 = Abweichung Richtung Angreifer).
- **Volle Deckung** (Handlung) senkt den Schadenswert eines Sprengangriffs auf einen selbst um `2`.
- **Airburst-Verbindung**: verdoppelt die Erfolge, die zur Senkung der Abweichung verwendet werden.

#### Tabelle Abweichung (S. 118)

| Reichweite | Abweichung geworfen (m) | Abweichung abgefeuert (m) |
|---|---|---|
| Sehr nah | `2W6 − 4 − Erfolge` | `2W6 + 2 − Erfolge` |
| Nah | `2W6 − 2 − Erfolge` | `2W6 − Erfolge` |
| Mittel | `2W6 − Erfolge` | `2W6 + 2 − Erfolge` |
| Weit | `2W6 + 2 − Erfolge` | `2W6 + 4 − Erfolge` |
| Sehr weit | `2W6 + 4 − Erfolge` | `2W6 + 6 − Erfolge` |

(Geworfene Granaten haben je nach Reichweitenkategorie die Angriffswerte Waffenlos / Waffenlos−1 / Waffenlos−6 / – / –; sinkt der Angriffswert auf 0, kann so weit nicht geworfen werden.)

### 15. Gasangriffe (S. 120)

- Kenngrößen: **Radius**, **Konzentration**, **Schadenswert**.
- Effektivität nimmt mit der Entfernung vom Freisetzungspunkt ab: über den Radius hinaus sinkt die Wirkung auf die Hälfte, ein Viertel oder null (immer abgerundet).
- Barriere im Wirkungsbereich: Konzentration baut sich über die ersten `5 Runden` auf volle Wirkung auf, sinkt ab Runde `9` und `10`. In einem versiegelten Raum baut sie sich bis Runde `5` auf und sinkt erst ab Runde `11`.

#### Tabelle Radius, Wirkung und Dauer von Gasangriffen (S. 120; Werte = Kampfrunden nach Einschlag)

| Radius | Volle Wirkung | Halbe Wirkung | Viertel Wirkung | Keine Wirkung |
|---|---|---|---|---|
| Radius | 1–5 | 6–8 | 9–10 | 11+ |
| Radius × 2 | – | 1–5 | 6–8 | 9+ |
| Radius × 3 | – | – | 1–4 | 5–6 |
| Radius × 4 | – | – | – | 6+ |

### 16. Sprühangriffe (S. 121)

- Drei Stile: **gerade** (normale Regeln, kein Angriffs-/Schadenswertmodifikator), **schwankend**, **streichend**.
- **Schwankend**: bedeckt ≈ 3 m Breite; `Angriffswert +2`, `Schadenswert −1`.
- **Streichend**: bedeckt ≈ 10 m Breite; `Angriffswert +4`, `Schadenswert −3`.
- Bei schwankenden/streichenden Angriffen kann zusätzlich ein Würfel des Würfelpools durch den Schicksalswürfel ersetzt werden, um die Waffe schneller zu bewegen.
- Personen im Weg des Sprühstrahls zum Ziel hin werden ebenfalls getroffen.

### 17. Sprengstoffe gezielt einsetzen – "Mehr Bums" (S. 121–122)

- **Schadenswirkung gegen Personen erhöhen**: Probe `Mechanik + Logik (Schwellenwert 2)`. Jeder Nettoerfolg erhöht den Schadenswert der Sprengwaffe in einer Reichweitenkategorie um `1` (mehrere Nettoerfolge können auf mehrere Kategorien verteilt werden, aber die Waffe muss an einem bestimmten Punkt platziert werden).
- **Konventionelle Sprengstoffe gegen Strukturen platzieren**: Probe `Mechanik + Logik`, **kein Schwellenwert**. Jeder Erfolg erhöht die effektive Stufe (= Schadenswert) des Sprengstoffs für den Einsatz gegen die Strukturstufe um `1`.
- **Konventionelle Sprengstoffe gegen Personen**: gleiche Probe mit Schwellenwert `2`.
- **Schadenswert von Sprengladungen gegen Personen** (abhängig von Sprengstoff-Stufe): Detonationspunkt = `Stufe`, Sehr nah = `Stufe + 2`, Nah = `Stufe + 4`. Explosionsradius = `Stufe` in Metern.

---

### 18. Erste Hilfe und Medkit (S. 122)

#### Erste Hilfe – `Biotech + Logik (5 − Essenz)`

- Zeitfenster: `1 Minute (20 Kampfrunden)` nach Ende der Kampfbegegnung, in der ein Charakter verletzt wurde.
- Ohne Erste-Hilfe-Set: `−2 Würfelpoolmalus`, kein Edge-Einsatz möglich.
- Schwellenwert: `5 − [Essenz des Ziels, abgerundet]` (bei Essenz 6 automatischer Erfolg).
- Heilung: pro Nettoerfolg `1 Kästchen Betäubungsschaden`; pro **2** Nettoerfolge `1 Kästchen Körperlichen oder Überzähligen Schaden`.
- Nur **einmal** pro Verletzungssatz anwendbar.

#### Medkit – `Biotech + Logik` oder `Medkit-Stufe + Logik (5 − Essenz)`

- Verbindungsaufbau/Diagnose: 1 Minute; danach Heilprozess `1 Minute pro Kästchen` (bei Unterbrechung von vorn beginnen).
- Jede Anwendung verbraucht einen Satz Vorräte.
- Heilung: pro Nettoerfolg `1 Kästchen Betäubungsschaden` **oder** `1 Kästchen Körperlichen/Überzähligen Schaden` (hier 1:1, nicht 2:1 wie bei Erster Hilfe).
- Nur **einmal** pro Verletzungssatz und Medkit anwendbar.

### 19. Magische Heilung und natürliche Genesung (S. 123)

- **Magische Heilung** (`Hexerei + Magie`, Schwellenwert wie oben `5 − Essenz`): pro Nettoerfolg `1 Kästchen` Betäubungs-, Körperlichen oder Überzähligen Schaden. Nur einmal pro Verletzungssatz.
- **Natürliche Genesung – Betäubungsschaden**: Einfache Probe `Konstitution + Willenskraft` pro Stunde Ruhe; pro Erfolg `1 Kästchen` geheilt.
- **Natürliche Genesung – Körperlicher Schaden**: Einfache Probe `Konstitution + Konstitution` pro Tag Ruhe; pro Erfolg `1 Kästchen` geheilt.
- **Medizinische Hilfe** (Biotech-ausgebildete Pflegeperson mind. die Hälfte der Ruheperiode anwesend): `+2 Würfelpoolbonus` auf die Genesungsprobe.
- Genesungsproben werden **ohne** Verletzungsmodifikatoren abgelegt; beide Schadensarten können parallel geheilt werden.

### 20. Überzähliger Schaden (S. 124)

- Heilprobe: `Konstitution + Konstitution` (wie Körperlicher Schaden).
- (Zur Erinnerung, s. S. 40: bei `Konstitution × 2` Kästchen Überzähligem Schaden ist der Charakter endgültig tot.)

---

### 21. Toxine und Drogen – Grundregeln (S. 124–125)

- **Kraft** dient als Schadenswert (falls das Toxin Schaden verursacht).
- **Toxinwiderstandsprobe**: `Konstitution + Willenskraft + Stufe schützender Ausrüstung/Systeme`. Jeder Erfolg senkt die Kraft um `1`. Sinkt die Kraft auf `≤0`, entsteht kein Schaden und keine Wirkung (sofern nicht anders angegeben).
- **Konzentration bei Mehrfachdosis**: `+1 Kraft pro zusätzlicher Dosis` innerhalb des Wirkungszeitraums.
- **Anhaltende Exposition**: Nach `10 Kampfrunden` fortgesetzter Exposition erneute Widerstandsprobe (danach alle weiteren 10 Runden). Ab der zweiten Widerstandsprobe steigt die Kraft kumulativ um `+1` je Probe.
- **Gegenmittel**: wirkt nur, wenn es **vor** Wirkungseintritt verabreicht wird (verhindert die Wirkung vollständig); danach verabreicht, stoppt es nur weitere/andauernde Effekte, heilt aber keinen bereits verursachten Schaden. Gegen manche Neurotoxine existiert kein Gegenmittel.
- **Dauer-Formel** (substanzabhängig, allgemeines Muster): `[Basiswert − Konstitution] × Zeiteinheit`, mindestens ein angegebener Minimalwert (siehe Tabellen unten).

### 22. Toxine – Werte-Tabelle (S. 125–128)

| Toxin | Vektor | Geschwindigkeit | Dauer | Kraft | Verfügbarkeit | Preis/Dosis |
|---|---|---|---|---|---|---|
| Brechreiz-Gas | Inhalation | 3 Kampfrunden | `[6−KON]` Min., min. 1 | 9 | 3L | 25 ¥ |
| CS-/Tränengas | Kontakt, Inhalation | 1 Kampfrunde | `[6−KON] × 5` Min., min. 5 | 8 | 2L | 20 ¥ |
| Gamma-Skopolamin | Injektion | Sofort | `[6−KON] × 30` Min., min. 30 | 12 | 7I | 200 ¥ |
| Narcoject | Injektion | Sofort | `[6−KON]` Std., min. 1 | 15 | 4L | 50 ¥ |
| Neuro-Stun VIII | Kontakt, Inhalation | 1 Kampfrunde | `[6−KON] × 10` Min., min. 10 | 9 | 5L | 60 ¥ |
| Neuro-Stun IX | Kontakt, Inhalation | 1 Kampfrunde | `[6−KON] × 10` Min., min. 10 | 12 | 6L | 60 ¥ |
| Neuro-Stun X | Kontakt, Inhalation | 1 Kampfrunde | `[6−KON] × 10` Min., min. 10 | 15 | 7L | 100 ¥ |
| Pepper Punch | Kontakt, Inhalation | 1 Kampfrunde | `[8−KON] × 20` Min., min. 20 | 11 | – | 5 ¥ |
| Seven-7 | Kontakt, Inhalation | 1 Kampfrunde | `[6−KON] × 10` Min., min. 10 | 12 | 10I | 1.000 ¥ |

- Gamma-Skopolamin: nach Ablauf der Primärwirkung (≈1 Stunde) wirkt der Rest im Blutkreislauf eine weitere Stunde als "Wahrheitsserum": `Willenskraft des Ziels −3` (Minimum 1).

### 23. Drogen – Werte-Tabelle (S. 126–128)

| Droge | Vektor | Geschwindigkeit | Dauer | Kraft | Verfügbarkeit | Preis/Dosis |
|---|---|---|---|---|---|---|
| Alkohol | Einnahme | 1 Minute | `[8−KON]` Std., min. 1 | 6 | – | 5–500 ¥ |
| Bliss | Inhalation, Injektion | 1 Kampfrunde | `[6−KON]` Std., min. 1 | 8 | 2I | 15 ¥ |
| Cram | Einnahme, Inhalation | 10 Minuten | `[12−KON]` Std., min. 1 | 8 | 2L | 10 ¥ |
| Deepweed | Einnahme, Inhalation | Sofort | `[6−KON]` Std., min. 1 | 7 | 4I | 400 ¥ |
| Jazz | Inhalation | Sofort | `10 × 1W6` Min. | 9 | 2L | 75 ¥ |
| Kamikaze | Inhalation | Sofort | `10 × 1W6` Min. | 10 | 3L | 100 ¥ |
| Long Haul | Injektion | 10 Minuten | 4 Tage | 11 | – | 50 ¥ |
| Nitro | Inhalation | 1 Kampfrunde | `10 × 1W6` Min. | 12 | 2L | 50 ¥ |
| Novacoke | Inhalation, Injektion | 1 Kampfrunde | `[10−KON]` Std., min. 1 | 12 | 2L | 10 ¥ |
| Psyche | Einnahme | 10 Minuten | `[12−KON]` Std., min. 1 | 8 | – | 200 ¥ |
| Zen | Inhalation | 5 Minuten | `10 × 1W6` Min. | 7 | 3L | 5 ¥ |

Nach-Wirkungs-Effekte mit eigenen Zahlenwerten:

- **Cram**: nach Wirkungsende `6B Schaden` (ohne Widerstandsprobe).
- **Jazz**: nach Wirkungsende Status *Benommen* für die gleiche Dauer, die die Droge gewirkt hat.
- **Kamikaze**: nach der **doppelten** Wirkungsdauer `6B Schaden` (ohne Widerstandsprobe) + `Reaktion −1` + Status *Erschöpft II*.
- **Long Haul**: nach Wirkungsende `8W6 Stunden` Schlaf; vorzeitiges Wecken erzeugt/erhöht Status *Erschöpft* (I → II → III je nach Dosis); 4. Dosis: `12B Schaden` (ohne Widerstandsprobe) + Bewusstlosigkeit bis die `8W6 Stunden` nachgeholt wurden.
- **Nitro**: nach Wirkungsende `9B Schaden` (ohne Widerstandsprobe) + `−2 Würfelpoolmalus` auf alle Proben für die gleiche Dauer, die die Droge gewirkt hat.
- **Novacoke**: nach Wirkungsende `Charisma` und `Willenskraft` auf `0` für eine der ursprünglichen Wirkungsdauer entsprechende Zeit.
- **Psyche**: senkt bei Erwachten/Digitalen den Würfelpoolmalus für das Aufrechterhalten von Zaubern/Komplexen Formen auf `−1` (statt der üblichen `−2`).

---

### Nicht erfasst

- Buchseiten 102–106 (Kurzgeschichte "Der Weg nach oben") und die Kapitelauftaktseite MAGIE (S. 129) enthalten keine Regeln/Zahlen.
- Zauberformeln, Zauberkraft, Drain-Berechnungen und weitere Magie-Mechaniken beginnen erst **nach** S. 129 (Kapitel MAGIE) und sind hier nicht enthalten.

---

## Teil 3: Magie (Buchseiten 130–159)

<sub>Quelle-Chunk: `docs/sr6/sr6_calc_p131-160.md` — Originaltitel: SR6 Regeln mit Berechnungen — Buchseiten 130–159</sub>

Quelle: `sr6_p131-160.pdf` (physische PDF-Seiten 131–160 des deutschen Grundregelwerks), entspricht den gedruckten Buchseiten **130–159** (Kapitel **MAGIE**, Abschnitte *Grundlagen der Magie*, *Zauber*, *Antimagie*, *Ritualzauberei*, *Beschwören*, *Verzaubern*, *Foki*, *Adepten*). Buchseitenzahlen stehen in Klammern, z. B. (S. 134).

---

### 1. Entzug (Drain) – Grundmechanik (S. 130, 133–134)

- **Entzugswiderstand**: Probe `Traditionsattribut + Willenskraft` (Traditionsattribut: Logik für Hermetiker, Charisma für Schamanen).
- **Schadensreduktion**: Der Schaden durch Entzug wird **pro Erfolg** der Entzugswiderstandsprobe um **1** reduziert, Minimum 0.
- **Schadenstyp**: Ist der (nach Widerstand verbleibende) Schaden durch Entzug **maximal so hoch wie das Magieattribut** des Charakters → **Betäubungsschaden**. Ist er **höher als das Magieattribut** → **Körperlicher Schaden**.
- Schaden durch Entzug kann nicht durch Magie, Erste Hilfe oder Medkits geheilt werden – nur durch natürliche Genesung (S. 123). Edge kann für die Heilung von Entzugsschaden eingesetzt werden.

---

### 2. Objektwiderstand (S. 131)

Maß dafür, wie schwer ein unbelebtes Objekt magisch zu beeinflussen ist (Alchemie, Manipulationszauber, Fokusherstellung, Trennen u. a.):

| Art des Objekts | Stufe |
|---|---|
| Natürliche Objekte (Bäume, Steine, Erde, Holz, unbehandeltes Wasser, von Hand kaltverformtes Metall) | 3 |
| Hergestellte einfache Objekte und Materialien (Ziegel, Glas, Leder, Papier, einfache Kunststoffe) | 6 |
| Hightech-Objekte und -Materialien (fortschrittliche Kunststoffe, Legierungen, Beton, elektronische Ausrüstung, Feuerwaffen, Sensoren) | 9 |
| Hochgradig verarbeitete Objekte (Kommlinks, Cyberdecks, Drohnen, Fahrzeuge, komplexer Giftmüll, Cheez-Bitz) | 15+ |

---

### 3. Magisches Refugium & Magie lernen (S. 131–132)

- **Permanentes Magisches Refugium einrichten**: Materialkosten = `500 Nuyen × Kraftstufe`. Errichtungszeit = `Kraftstufe` Tage.
- **Refugium verbessern**: Materialkosten für die Differenz zur neuen Kraftstufe, Zeit = Anzahl Tage gleich der **neuen** Kraftstufe (nicht der Differenz).
- **Temporäres Magisches Refugium** (mit Reagenzien, s. Abschnitt 18): `1 Dram Reagenzien pro gewünschter Kraftstufe`. Errichtungsdauer = `1 Stunde pro Punkt Kraftstufe`. Hält bis zum nächsten Sonnenauf-/-untergang.
- **Formel/Zauber kaufen**: Preis siehe Tabelle *Magische Ausrüstung* (S. 170).
- **Lehrer-Gebühr**: ungefähr `[Einfluss-Fertigkeit des Lehrers] × [Kosten der Formel]` Nuyen.
- **Lernzeit**: `12 Tage ÷ Erfolge` der Probe `Hexerei + Intuition`. *(3. Auflage/Errata: nur bei Aspektzauberern, die ausschließlich* Verzaubern *beherrschen, stattdessen `Verzaubern + Intuition`. Alchemistische Zauber sind keine eigene Lernkategorie mehr — Alchemie nutzt die normalen, bekannten Zauber; ein gelernter Zauber steht danach sowohl für Spruchzauberei als auch fürs Verzaubern zur Verfügung.)*
- **Lernprobe-Modifikator**: Formel oder Lehrer aus fremder Tradition → `−4 Würfelpoolmalus`.
- **Lernaufwand**: 8 Stunden Studium/Tag; am Ende der Lernzeit **5 Karma** zum endgültigen Lernen des Zaubers **oder** Rituals (deckt sich mit der Entwicklungskosten-Tabelle in Teil 1, Abschnitt 12; S. 132 dort referenziert).
- Bricht die Probe ohne jeden Erfolg ab, scheitert der Lernversuch; kein Karma verloren, aber ggf. gezahltes Geld für Unterricht ist verloren.

---

### 4. Zauber wirken: Merkmale, Anpassung, Probe, Entzugswiderstand (S. 133–134)

**Grundschritte**: (1) Zauber anpassen, (2) Zauberprobe `Hexerei + Magie` ablegen, (3) Entzug widerstehen (Kampfzauber haben davor noch einen vierten Schritt: Ziel wählen).

#### Zauber-Merkmale (Terminologie)
- **Reichweite**: Berührung (B) · Blickfeld (BF) · Blickfeld mit Flächenwirkung (BF (F), ohne Anpassung 2 m Radius) · Speziell.
- **Dauer**: Sofort (S) · Aufrechterhalten (A) · Zeitlich Begrenzt (ZB) · Permanent (P).
- **Art**: Manazauber (M) vs. Physischer Zauber (P).

#### Anpassungen
- **Hochdrehen** (nur Kampfzauber): pro zusätzlichem Punkt Grundschaden steigt der Entzug des Zaubers um **2**.
- **Fläche Vergrößern**: Standard-Flächenwirkung ist eine Kugel mit **2 Meter Radius**. Pro Vergrößerung des Radius um **2 Meter** steigt der Entzug um **1**.
- **Fläche Verschieben** (nur bei manchen Flächenzaubern möglich): keine Entzugsänderung, Nebenhandlung.
- **Maximale Anzahl an Anpassungen** (S. 133, 3. Auflage/Errata): gleich dem **höheren** der beiden Werte des Charakters in **Magie oder Hexerei**.

#### Entzugswiderstand
Probe `Willenskraft + Traditionsattribut` gegen den Entzugswert des Zaubers (inkl. Anpassungen). `Erfolge ≥ Entzugswert` → kein Schaden. `Erfolge < Entzugswert` → Schaden = Differenz (Typ siehe Abschnitt 1).

---

### 5. Laufende Kosten aufrechterhaltener Zauber (S. 134)

- Für jeden gleichzeitig aufrechterhaltenen Zauber: `−2 Würfelpoolmalus` auf **alle** Handlungsproben (ausgenommen Schadens-, Entzugs- oder sonstige Widerstandsproben). Mali mehrerer aufrechterhaltener Zauber sind kumulativ.

---

### 6. Heil- und Steigerungszauber (S. 134–135)

Gemeinsame Würfelpool-Formel vieler Heil-/Steigerungszauber (Heilen, Kühlendes/Neutralisierendes/Wärmendes Heilen, Attribut steigern, Reflexe steigern, Schmerzresistenz):

`Hexerei + Magie (5 – [Essenz des Ziels, abgerundet])`

- **Attribut senken**: Vergleichende Probe `Hexerei + Magie` gegen `Willenskraft + betroffenes Attribut` des Ziels. Pro genutztem Nettoerfolg sinkt das Attribut um 1 (min. 1). Ab dem 2. genutzten Nettoerfolg steigt der Entzug kumulativ um 1.
- **Attribut steigern**: Probe wie oben. Pro genutztem Nettoerfolg steigt das Attribut um 1 (Cap: `unmodifiziert + 4`, allgemeine Attribut-Regel). Ab dem 2. genutzten Nettoerfolg steigt der Entzug kumulativ um 1.
- **Heilen / Kühlendes Heilen / Neutralisierendes Heilen / Wärmendes Heilen**: Pro Nettoerfolg wird **1 Kästchen** Überzähliger, Körperlicher oder Betäubungsschaden geheilt. Ein Satz Verletzungen kann nur **einmal** mit einem Heilzauber behandelt werden.
- **Gegenmittel** (S. 135): Probe `Hexerei + Magie`; jeder Erfolg senkt die Kraft eines Toxins im Ziel um 1. *(3. Auflage/Errata: Man darf mehrere aufeinanderfolgende Haupthandlungen aufwenden, um die Probe zu wiederholen, ohne den Zauber neu zu wirken.)* Fällt die Kraft auf **0**, werden alle noch aktiven Wirkungen des Toxins beseitigt.
- **Reflexe steigern**: Pro genutztem Nettoerfolg: `+1 Initiativewert` **und** `+1 Initiativewürfel`. Ab dem 2. genutzten Nettoerfolg steigt der Entzug kumulativ um 1. Cap: nie mehr als **5W6** Initiativewürfel insgesamt.
- **Schmerzresistenz**: Pro Nettoerfolg kann das Ziel seinen Verletzungsmodifikator um 1 senken.
- **Stabilisieren**: Probe `Hexerei + Magie` mit Schwellenwert = Anzahl der Kästchen Überzähligen Schadens des Ziels; bei Erfolg werden alle diese Kästchen entfernt.

---

### 7. Illusionszauber (S. 136–137)

Meist Vergleichende Probe `Hexerei + Magie` gegen ein Attributspaar des Ziels; die **Anzahl der Erfolge bzw. Nettoerfolge** bei der Hexereiprobe wird zur **Stufe des erzeugten Status** bzw. zum **Schwellenwert**, mit dem die Illusion durchschaut werden kann:

- **Maske / Physische Maske**: Anzahl der Erfolge = Schwellenwert für die Probe `Willenskraft + Intuition`, um die Illusion zu durchschauen.
- **Schmerz**: Vergleichende Probe `Hexerei + Magie` gegen `Willenskraft + Logik`. Jeder Nettoerfolg erzeugt 1 zusätzliches illusorisches Kästchen Schaden (wirkt auf beide Zustandsmonitore, nur für Verletzungsmodifikatoren).
- **Schweigen / Stille**: Ziel erhält Status *Geräuschlos* mit Stufe = Anzahl Erfolge der Hexereiprobe (= Schwellenwert, um es zu hören).
- **Sensortäuschung / Trugbild / Trideo-Trugbild / Unsichtbarkeit / Verbesserte Unsichtbarkeit**: analog — Stufe des jeweiligen Status = Anzahl Erfolge der Hexereiprobe = Schwellenwert für Wahrnehmung.
- **Verwirrung / Chaos**: Vergleichende Probe `Hexerei + Magie` gegen `Willenskraft + Logik`. Ziel erhält Status *Verwirrt* mit Stufe = Nettoerfolge (= Würfelpoolmalus auf alle Proben außer Schadenswiderstand).
- Bei allen einfachen (nicht flächenwirkenden) Illusionszaubern kann per *Fläche Vergrößern* (ab 2 m Radius, +1 Entzug) Flächenwirkung erzeugt werden; ist die Flächenwirkung vorhanden, kann zusätzlich *Fläche Verschieben* genutzt werden.

---

### 8. Kampfzauber (S. 137–138)

- **Angriffswert des Zauberers**: `Magie + Traditionsattribut`.
- **Verteidigungswert des Ziels** (physische Ebene): `Intuition + natürliche Panzerung + Panzerungseffekte`. Auf der Astralebene gilt ein anderer Wert (S. 163). Bei mehreren Zielen (Flächenwirkung) zählt der **höchste** Verteidigungswert der Gruppe für den Edge-Vergleich; Differenz `≥ 4` → 1 Edge für die überlegene Seite (Standardregel aus Abschnitt Edge).

#### Direkte Kampfzauber
Vergleichende Probe `Hexerei + Magie` gegen `Willenskraft + Intuition` des Ziels (bzw. Pilot bei Drohnen).
- Ziel hat mehr Erfolge → Zauber wirkungslos (Entzug muss der Zauberer trotzdem widerstehen).
- Zauberer erfolgreich mit Nettoerfolgen → `Schaden = Nettoerfolge + Schaden durch Hochdrehen`.
- Zauberer erfolgreich ohne Nettoerfolge → `Schaden = Schaden durch Hochdrehen` (falls gewählt), sonst kein Schaden.
- Dem Schaden durch direkte Kampfzauber kann nicht widerstanden werden.

#### Indirekte Kampfzauber
Vergleichende Probe `Hexerei + Magie` gegen `Reaktion + Willenskraft` des Ziels (bzw. Pilot bei Drohnen).
- Ziel hat mehr Erfolge → Zauber verfehlt (Entzug weiterhin zu widerstehen).
- Zauberer erfolgreich → `Schaden = [Magie ÷ 2, aufgerundet] + Nettoerfolge + Schaden durch Hochdrehen`.
- Ziel widersteht dem Schaden wie im physischen Kampf mit Konstitution.
- Indirekte Kampfzauber verursachen oft elementaren Schaden (S. 112).

**Rechenbeispiel aus dem Buch** (S. 138, Feuerball): Zauberer mit Magie 6 → Grundschaden = `6 ÷ 2 = 3`. Bei 2 Nettoerfolgen: `Schaden = 3 + 2 = 5K`. Der zugehörige Status *Brennend* erhält eine Stufe gleich der Anzahl Nettoerfolge (hier `Brennend 2`).

---

### 9. Manipulationszauber (S. 139–143)

- **Widerstand**: gegen Lebewesen mit deren Attributen (siehe jeweilige Beschreibung), gegen unbelebte Ziele mit **Objektwiderstand** (Abschnitt 2).
- **Dauer ZB**: Standardmäßig maximal aufrechterhaltbar für `Anzahl Minuten = Nettoerfolge der Hexereiprobe`.
- **Standardmenge beeinflussbaren Materials**: `½ Kubikmeter pro Nettoerfolg` (Formen/Beleben-Zauber). Umrechnungstabelle:

| Nettoerfolge | Volumen | Beispiel |
|---|---|---|
| 1 | 0,5 m³ | Einfacher Kühlschrank |
| 2 | 1 m³ | Normalgroße Couch |
| 3 | 1,5 m³ | Motorrad |
| 4 | 2 m³ | Müllcontainer |
| 5 | 2,5 m³ | Esstisch mit acht Stühlen |
| 6 | 3 m³ | Michelangelos David |

#### Einzelformeln
- **Astralpanzerung / Elementarpanzerung / Panzerung**: Probe `Hexerei + Magie`; Erfolge werden zum Verteidigungswert des Ziels addiert (Astralpanzerung: nur gegen Mana-Kampfzauber im Astralkampf).
- **Fahrzeugpanzerung**: Vergleichende Probe `Hexerei + Magie` gegen den Objektwiderstand des Fahrzeugs; das Fahrzeug erhält **pro Nettoerfolg 1 Punkt *Verstärkter Panzer*** (S. 227). *(3. Auflage/Errata; früher: „Panzerungswert +1 pro Nettoerfolg".)*
- **Wand verstärken**: Vergleichende Probe `Hexerei + Magie` gegen Objektwiderstand; Strukturstufe steigt um `1 pro Nettoerfolg`. Grundversion: 4 m² Wandfläche; *Fläche Vergrößern* fügt `+4 m² pro Punkt höherem Entzug` hinzu.
- **Donnerknall / Dunkelheit / Licht**: Grundfläche Kugel 2 m Radius. Pro Erfolg: Lärm hält 1 Kampfrunde länger an (Donnerknall) bzw. Beleuchtung sinkt/steigt um eine Abstufung (Dunkelheit/Licht, Tabelle *Umgebung und Lichtverhältnisse*, S. 108).
- **Fokus-Boost**: Vergleichende Probe `Hexerei + Magie` gegen `Kraftstufe × 2` des Fokus. Nettoerfolg → Kraftstufe des Fokus steigt um 1 (temporär). Kritischer Patzer → Kraftstufe sinkt **permanent** um 2.
- **Gedanken beherrschen / Handlungen beherrschen**: Vergleichende Probe `Hexerei + Magie` gegen `Willenskraft + Logik` des Ziels.
- **Holz/Kunststoff/Metall/Stein Beleben**: Vergleichende Probe gegen Objektwiderstand; belebte Materialmenge nach der Volumina-Tabelle. Maximalgeschwindigkeit 5 m/Kampfrunde. Kollisionsschaden bei unachtsamem Ziel: Metall 4K, Stein 3K, Holz 2B, Kunststoff 1B. Widerstand gegen Kontrolle des Objekts: Vergleichende Probe `Nettoerfolge der Hexereiprobe + [4 Metall/3 Stein/2 Holz/1 Kunststoff]` gegen `Konstitution + Stärke` des Störenden.
- **Holz/Kunststoff/Metall/Stein Formen**: Probe gegen Objektwiderstand; `1 Kubikmeter Material pro Nettoerfolg` formbar (Tabelle Volumina).
- **Levitieren**: Probe `Hexerei + Magie`. Jeder Erfolg levitiert `50 kg` Material/Personen. Unwillige Person: Probe `Konstitution + Stärke`, jeder Erfolg senkt die Erfolge des Zauberers um 1. Bewegungsrate = `[Magie des Zauberers]` Meter/Runde (Nebenhandlung).
- **Manabarriere / Physische Barriere**: Probe `Hexerei + Magie`; Strukturstufe = `Magie + Erfolge`. Grundgröße 2×2 m; *Fläche Vergrößern* fügt jeweils `+2 m Breite und Höhe` hinzu (nicht Dicke).
- **Schleuder**: Probe `Hexerei + Magie` gegen Objektwiderstand; `0,5 kg Material pro Nettoerfolg` schleuderbar. Angriffswert nach Entfernung: Sehr nah `Magie`; Nah `Magie + 2`; Mittel `Magie + 1`; Weit `Magie − 2`; Sehr weit `—`. Betäubungsschaden = Gewicht in kg (aufgerundet).
- **Übertakten**: Vergleichende Probe gegen Objektwiderstand; jeder Nettoerfolg erhöht ein Geräteattribut (Gerätestufe, Angriff, Datenverarbeitung, Firewall, Schleicher) um 1. Nach Zauberende: Matrixschaden = Anzahl der genutzten Nettoerfolge, widerstanden mit Firewall.

---

### 10. Wahrnehmungszauber (S. 143–145)

- **Sinnesreichweite**: sofern nicht anders angegeben, Kugel-Radius `2 m`; bei Zaubern mit Beobachter-Verbindung: `[Magie des Zaubernden + Nettoerfolge der Hexereiprobe]` Meter.
- **Allgemeines Ergebnis-Schema** (z. B. Wahrnehmungszauber allgemein):

| Nettoerfolge | Ergebnis |
|---|---|
| 1 | Allgemeine Informationen ohne Details |
| 2 | Weitere Informationen über Form/Funktion ohne Details |
| 3 | Spezifische Details |
| 4+ | Entscheidende Details inkl. Emotionen/Funktionen |

- **Geistessonde**: Vergleichende Probe `Hexerei + Magie` gegen `Willenskraft + Logik`. Ergebnis nach Nettoerfolgen:

| Nettoerfolge | Ergebnis |
|---|---|
| 1–2 | Nur oberflächliche Gedanken |
| 3–4 | Alles bewusst Gewusste + Erinnerungen der letzten 72 Stunden |
| 5+ | Zugriff auch aufs Unterbewusstsein (verdrängte Ängste, verschüttete Erinnerungen) |

- **Gerät analysieren**: Erfolge gegen Objektwiderstand liefern Information. Bei Erstnutzung eines Geräts während aufrechterhaltenem Zauber: Edge in Höhe der Nettoerfolge (übliche Obergrenze 2 Edge/Kampfrunde).
- **Kampfsinn**: Erfolge der Hexereiprobe werden zum Verteidigungswert **und** zum Würfelpool für Überraschungsproben addiert, solange aufrechterhalten.
- **Magie analysieren**: Vergleichende Probe; Würfelpool der Gegenseite = `2 × Erfolge` (nicht Nettoerfolge) der ursprünglichen magischen Probe (Beschwören/Verzaubern/Hexerei), die den zu analysierenden Effekt erschaffen hat.
- **Magie entdecken**: Grundfläche Kugel 2 m Radius; pro `Dram Reagenzien` Radius `+1 m`. Erfolge aller sich verteidigenden Ziele werden zu deren Würfelpool addiert. Zauberabwehr hält `Magieattribut des Zaubernden` Kampfrunden an.

---

### 11. Antimagie: Zauberabwehr & Zauberbannung (S. 145)

- **Zauberabwehr**: Haupthandlung *Antimagie*, Probe `Hexerei + Magie` als Grundform der Verteidigung gegen eintreffende Zauber (Aufbau vorab).
- **Zauberbannung** (gegen aufrechterhaltene Zauber/Effekte): Haupthandlung *Antimagie*, Vergleichende Probe `Hexerei + Magie` gegen `Entzug des gegnerischen Zaubers × 2` (inkl. aller Entzugserhöhungen durch Anpassungen). Nettoerfolge negieren im Verhältnis **1:1** die Nettoerfolge der ursprünglichen gegnerischen Probe. Werden dessen Nettoerfolge auf 0 gesenkt, ist der Zauber gebannt. Der bannende Charakter muss danach in jedem Fall dem Entzug widerstehen, als hätte er den Zauber selbst gewirkt.

---

### 12. Ritualzauberei – Ablauf (S. 145–146)

Rituale werden wie Zauber gelernt und haben dieselben Karmakosten (5 Karma, Abschnitt 3).

- **Teilnehmer fremder Tradition**: `−2 Würfelpoolmalus` auf alle Handlungen während des Rituals.
- **Schritt 4 (Reagenzien ausgeben)**: Standardmenge = Schwellenwert des Rituals in Dram. Zusätzliche Reagenzien senken den Entzug beim Besiegeln: `1 Dram = −1 Entzug`, maximal `−2`.
- **Schritt 6 (Ritual besiegeln)**: Probe `Hexerei + Magie` des Ritualleiters (Teamworkprobe der übrigen Teilnehmer möglich) gegen den ritualspezifischen Schwellenwert.
  - **Entzugswiderstand für alle Teilnehmer** = Anzahl der **Erfolge** (nicht Nettoerfolge, Minimum 2) der **verteidigenden Seite** bei dieser letzten Probe. Nur zur Bestimmung dieses Entzugs wird eigens mit `Schwellenwert × 2` Würfeln gewürfelt.
- **Fehlschlag eines Rituals**: Alle Teilnehmer widerstehen sofort einem Entzug; Wurf mit `Schwellenwert` Würfeln, Entzug = `2 × Erfolge` dieses Wurfs. Bereits ausgegebene Reagenzien sind verloren.
- **Patzer bei Ritualen**: kann zu zusätzlichem Entzug (z. B. `+2`) oder erhöhtem Schwellenwert führen; Kritischer Patzer kann das Ritual völlig entgleisen lassen (SL-Ermessen).

---

### 13. Einzelne Rituale – Formeln (S. 147–148)

| Ritual | Schwellenwert | Vollendungsdauer | Numerischer Effekt |
|---|---|---|---|
| Fernwahrnehmung | 5 | 3 Stunden | Reichweite = `[Magie des Ritualleiters + Erfolge beim Besiegeln] × 100` Meter |
| Fernzauber | 6 | 4 Stunden | Kampfzauber auf Ziele außerhalb der Sichtlinie wirkbar |
| Fluch | 5 | (materielle Verbindung) | Zauber über Materielle Verbindung statt Späher wirken. *3. Auflage/Errata:* Der Zauber wird **normal gewirkt** (ggf. mit Teamwork), mit allen erforderlichen Proben und dem entsprechenden **Entzug** (früher: Nettoerfolge des Besiegelns = Nettoerfolge des Zaubers). Materielle Verbindung wird in Schritt 4 verbraucht. |
| Herrschaft | 6 | 4 Stunden | Wirkungsbereich: Kugel-Radius = `Magieattribut des Ritualleiters` Meter; Dauer 1 Std., **verdoppelt sich pro weiterem Nettoerfolg beim Besiegeln** (1, 2, 4, 8 … Std.) |
| Hüter | 6 | 4 Stunden | Manabarriere, Kraftstufe = `Magieattribut des Ritualleiters + Nettoerfolge beim Besiegeln`; Volumen bis `50 × Summe der Magieattribute aller Teilnehmer` m³; Bestand `Nettoerfolge` Wochen (permanent bei Einsatz von 6 Karma) |
| Kreis der Heilung | 7 | 5 Stunden | Radius = `Magieattribut des Ritualleiters` Meter; Nettoerfolge = Würfelpoolbonus für alle im Kreis durchgeführten Heilungs-/Genesungsproben; Bestand `Nettoerfolge` Tage |
| Schutzkreis | 6 | 4 Stunden | Radius = `Magieattribut des Ritualleiters` Meter; Strukturstufe (Physische Barriere + duale Manabarriere) = `Magieattribut des Ritualleiters + Nettoerfolge beim Besiegeln`; Bestand `Nettoerfolge` Stunden |
| Watcher (Diener) | 4 | 1 Stunde | Attribute/Fertigkeiten starten bei 2; Bestand `Nettoerfolge × 3` Stunden. Pro zusätzlicher Ritual-Stunde: Attribute/Fertigkeiten und Schwellenwert je `+1` |

---

### 14. Beschwören (S. 148–149)

- **Herbeirufen**: Vergleichende Probe `Beschwören + Magie` gegen `Kraftstufe des Geistes × 2`. Mindestens 1 Nettoerfolg nötig. Anzahl der geschuldeten **Dienste** = Anzahl der Nettoerfolge des Beschwörers. Entzugswiderstand des Beschwörers = Anzahl der **Erfolge** (nicht Nettoerfolge) des Geistes bei dieser Probe.
- **Maximal gebundene Geister**: Summe der Kraftstufen aller gleichzeitig in Diensten stehenden Geister ≤ `Magie × 3`.
- **Reagenzien beim Herbeirufen**: `Dram = Kraftstufe des herbeigerufenen Geistes`, um 1 Edge zu erhalten.
- **Verbannen**: Vergleichende Probe `Beschwören + Magie` gegen `Kraftstufe des Geistes × 2`. Jeder Nettoerfolg senkt die Anzahl offener Dienste um 1; bei 0 verschwindet der Geist. Entzugswiderstand des Verbannenden = `2 × Erfolge` (nicht Nettoerfolge) des Geistes bei dieser Probe. Reagenzien: `Dram = Kraftstufe des Geistes` für +1 Edge.
- **Geister und Edge**: Geister können kein eigenes Edge erhalten, außer der Beschwörer/Verbündete gibt für 2 Edge Ausgabe 1 Edge an den Geist weiter; Geist muss sich innerhalb `[Kraftstufe × 10]` Metern der gebenden Person befinden.
- **Geister und Entfernung**: Ist ein Geist weiter als `[Magie des Beschwörers × 100]` Meter entfernt, versucht er zurückzukehren (sofern nicht anders befohlen).
- **Zusatzkräfte von Geistern**: `1 Zusatzkraft pro volle 3 Kraftstufen` (keine bis Kraftstufe 2, eine bei 3–5, zwei bei 6–8 usw. → `⌊Kraftstufe ÷ 3⌋`).

---

### 15. Geister – Attribut-/Wert-Skalierung nach Kraftstufe (S. 150–151)

Alle Werte skalieren direkt mit der **Kraftstufe (KS)** des Geistes. Gemeinsame Regeln für alle Geistertypen:
- **Handlungen**: immer 1 Haupthandlung + 3 Nebenhandlungen pro Kampfrunde.
- **Zustandsmonitor**: `(KS ÷ 2, aufgerundet) + 8` Kästchen.
- **Essenz**: gleich der Kraftstufe.
- Attribute können nie niedriger als 1 sein, selbst wenn die Formel einen niedrigeren Wert ergäbe.

| Geistertyp | K | G | R | S | W | L | I | C |
|---|---|---|---|---|---|---|---|---|
| Erdgeister | KS+4 | KS−2 | KS−1 | KS+4 | KS | KS−1 | KS | KS |
| Luftgeister | KS−2 | KS+3 | KS+4 | KS−3 | KS | KS | KS | KS |
| Feuergeister | KS+1 | KS+2 | KS+3 | KS−2 | KS | KS | KS+1 | KS |
| Geister des Menschen | KS+1 | KS | KS+2 | KS−2 | KS | KS | KS+1 | KS |
| Geister des Tieres | KS+2 | KS+1 | KS | KS+2 | KS | KS | KS | KS |
| Wassergeister | KS | KS+1 | KS+2 | KS | KS | KS | KS | KS |

| Geistertyp | Initiative | Astrale Initiative | Bewegung |
|---|---|---|---|
| Erdgeister | (KS×2)−1+2W6 | (KS×2)−1+3W6 | 5/10/+1 |
| Luftgeister | (KS×2)+4+2W6 | (KS×2)+3W6 | 5/10/+1 |
| Feuergeister | (KS×2)+4+2W6 | (KS×2)+1+3W6 | 5/10/+5 |
| Geister des Menschen | (KS×2)+3+2W6 | (KS×2)+1+3W6 | 5/10/+1 |
| Geister des Tieres | (KS×2)+2W6 | (KS×2)+3W6 | 5/10/+3 |
| Wassergeister | (KS×2)+2+2W6 | (KS×2)+3W6 | 5/10/+2 |

Der **Verteidigungswert** jedes Geistes besteht aus drei Teilwerten (astral / physisch gegen magische Angriffe / physisch gegen normale Waffen); die genaue Formel je Geistertyp ist im Buch als Kleinstschrift-Tabelle angegeben und sollte für den NPC-Generator direkt am Original (S. 150 f.) verifiziert werden (siehe „Nicht erfasst“).

Angriffe (sofern vorhanden) skalieren ebenfalls mit KS, z. B. Geister des Menschen: `Fäuste [Schaden ([KS÷2]−1)B]`; Geister des Tieres: `Kralle/Biss [Schaden ([KS÷2]+1)K]`.

#### Schwächen der Geistertypen (S. 150–151, 3. Auflage/Errata — in der 2. Auflage fehlten diese Zeilen)

| Geistertyp | Schwäche |
|---|---|
| Erdgeister | Allergie (Elektrizität, Schwer) |
| Feuergeister | Allergie (Kälte, Schwer); Verwundbarkeit (Feuerlöscher) |
| Luftgeister | Allergie (Toxine mit Inhalationsvektor, Schwer) |
| Geister des Menschen | Allergie (Eisenmetalle, Schwer) |
| Geister des Tieres | Allergie (Silber, Schwer) |
| Wassergeister | Allergie (Feuer, Schwer) |

**Luftgeister – Zusätzliche Kräfte** (3. Auflage/Errata): *Elementarer Angriff (Elektrizität **oder** Kälte)*, *Energieaura (Elektrizität **oder** Kälte)*, Gifthauch, Grauen, Psychokinese, Schutz (früher als getrennte Elektrizitäts-/Kälte-Kräfte gelistet).

---

### 16. Verzaubern: Alchemistische Erzeugnisse (S. 152–153)

- **Zauber auswählen** (S. 152, 3. Auflage/Errata): Für das Erzeugnis kann nur **ein Zauber gewählt werden, den der Verzauberer kennt** (es gibt keine separaten „alchemistischen Zauber" mehr).
- **Auslöser-Entzugszuschlag**: Befehl `+2`, Kontakt `+1`, Zeitzünder `+2`.
- **Herstellungsdauer**: `Anzahl Stunden = Gesamtentzug` (Zauber inkl. Anpassungen + Auslöser, nach Reagenzienreduktion).
- **Reagenzien**: können den Entzug bei der Herstellung um bis zu `2` (1 Dram = −1 Entzug) senken; dies verkürzt nicht die Herstellungszeit.
- **Entzugswiderstand (Herstellung)**: Vergleichende Probe `Verzaubern + Magie` gegen den (ggf. gesenkten) Entzug; Widerstand mit `Traditionsattribut + Willenskraft`. Die Nettoerfolge werden zur **Wirksamkeit** des Erzeugnisses.
- **Zerfall des fertigen Erzeugnisses**: Volle Wirksamkeit hält `[Wirksamkeit × 2]` Stunden. Danach sinkt die Wirksamkeit alle weiteren `[gegenwärtige Wirksamkeit × 2]` Stunden um 1, bis 0 (Erzeugnis unbrauchbar).
- **Verwenden eines Erzeugnisses**: Probe `Wirksamkeit des Erzeugnisses + Magie des Verwenders` (ersetzt Hexerei+Magie); kein zusätzlicher Entzug beim Auslösen.

---

### 17. Fokusherstellung (S. 154–156)

- **Fokusformel**: Kraftstufe der Formel ≤ Magieattribut des Herstellers; Kraftstufe des fertigen Fokus (Schritt 5) ≤ Kraftstufe der Formel.
- **Reagenzien**: `Dram = Karmakosten für das spätere Binden`, mindestens `Kraftstufe` Dram.
- **Herstellungsdauer**: `Anzahl Tage = Kraftstufe der Fokusformel`.
- **Schritt 5 – Aktivieren**: Vergleichende Probe `Verzaubern + Magie` gegen `Kraftstufe der Fokusformel + Objektwiderstand des Telesmas`. Nettoerfolge = tatsächliche Kraftstufe des fertigen Fokus. Kein Edge-Einsatz erlaubt.
- **Schritt 6 – Entzugswiderstand**: `Entzugswert = Kraftstufe der Fokusformel + 2 × Erfolge der Gegenseite` (nicht Nettoerfolge) bei der Probe aus Schritt 5.
- **Fokusbindung**: dauert `Kraftstufe des Fokus` Stunden Kontemplation; kostet Karma nach Tabelle *Magische Ausrüstung* (S. 170).
- **Askennen von Foki**: Vergleichende Probe `Verzaubern + Magie` gegen `Kraftstufe des Fokus × 2`.
- **Entzaubern (Deaktivieren)**: Vergleichende Probe `Verzaubern + Magie` gegen `Kraftstufe des Fokus + Magie des Besitzers`.
- **Entzaubern (Zerstören/Reagenzien gewinnen)**: nach erfolgreicher Deaktivierung, Probe `Verzaubern + Magie`; jeder Erfolg erzeugt `1 Dram` Reagenzien bis maximal `⅓ der ursprünglich für die Herstellung verwendeten Reagenzien`; Dauer = `Kraftstufe des zerstörten Fokus` Stunden.
- **Trennen (alchemistische Erzeugnisse)**: Haupthandlung, Vergleichende Probe `Verzaubern + Magie` gegen `Kraftstufe des Erzeugnisses + Magie des Herstellers` (+ Metamagie-Fixierung-Karma falls zutreffend). Jeder Nettoerfolg senkt die Wirksamkeit um 1; bei 0 unbrauchbar.

---

### 18. Reagenzien (S. 155–156)

- **Standardmaß**: `1 Dram Orichalkum` = Standardmessgröße für die Macht von Reagenzien.
- **Fremde Tradition**: Reagenzien einer anderen Tradition wirken nur mit halber Macht → **doppelte Menge** nötig für denselben Effekt.
- Einsatzgebiete mit Zahlenwert: Alchemistische Erzeugnisse (Entzugsreduktion), Antimagie (Vergrößerung Zauberabwehr-Bereich), Fokusherstellung (Pflicht), Herbeirufen (+1 Edge pro Kraftstufe-Dram), Ritualzauberei (Pflicht + Entzugsreduktion), Temporäre Magische Refugien (1 Dram/Kraftstufe).

---

### 19. Foki – Bindung & Kategorien (S. 156–157)

- **Maximale Anzahl gebundener Foki** = Magieattribut (Stückzahl).
- **Kraftstufe eines einzelnen Fokus** ≤ Magieattribut (3. Auflage/Errata — diese Einzel-Obergrenze fehlte in der 2. Auflage).
- **Summe der Kraftstufen aller gebundenen Foki** ≤ `Magieattribut × 5`.
- Pro Probe kann nur **ein** gebundener Fokus seine Kraftstufe als Bonus beisteuern.
- **Qi-Foki** können nur von **Adepten und Magieradepten** verwendet werden (3. Auflage/Errata; früher nur Adepten).
- **Bindungsdauer**: `Kraftstufe des Fokus` Stunden Kontemplation; Karmakosten nach Tabelle *Magische Ausrüstung* (S. 170).
- **Qi-Fokus**: Kraftstufe = `4 × Kraftpunktkosten der gebannten Adeptenkraft` (z. B. Verbesserte Fertigkeit (Nahkampf) 1 kostet 1 KP/Stufe → Fokus KS 4; Todeskralle kostet 0,5 KP → Fokus KS 2).

#### Bonus-Wirkung nach Fokusart

| Fokusart | Bonus wirkt auf |
|---|---|
| Geisterfokus: Herbeirufungsfokus | `+KS` auf Herbeirufen-Proben der passenden Geisterart |
| Geisterfokus: Verbannungsfokus | `+KS` auf Verbannen-Proben der passenden Geisterart |
| Kraftfokus | `+KS` auf alle Proben, an denen das Magieattribut beteiligt ist |
| Metamagiefokus: Formungsfokus | `+KS` zum Magieattribut bei der Formung von Zaubern |
| Metamagiefokus: Maskierungsfokus | `+KS` Würfelpoolbonus gegen Askennen durch Maskierung |
| Waffenfokus | `+KS` auf Nahkampf-Angriffsproben (auch im Astralkampf) |
| Verzauberungsfoki: Alchemiefokus | `+KS` Würfelpoolbonus auf Verzaubern-Proben bei Herstellung alchemistischer Erzeugnisse |
| Verzauberungsfoki: Entzauberungsfokus | `+KS` Würfelpoolbonus auf die Entzauberungsprobe (bei Kontakt) |
| Zauberfoki: Antimagiefokus | `+KS` auf Zauberbannung passender Kategorie und auf Zauberabwehr |
| Zauberfoki: Ritualfokus | `+KS` Würfelpoolbonus auf Ritualzauberei-Proben |
| Zauberfoki: Zauberspeicher | erlaubt Aufrechterhalten ohne Würfelpoolmalus (Entzugswert des Zaubers ≤ Kraftstufe des Fokus, gleiche Kategorie) |
| Zauberfoki: Zauberspruchfokus | `+KS` Würfelpoolbonus auf Spruchzauberei-Proben passender Kategorie |
| Signaturschleier (Initiation) | `+KS` zum Initiatengrad beim Erhöhen des Askennen-Schwellenwerts durch Flexible Signatur |
| Zentrierungsfokus (Initiation) | `+KS` zum Initiatengrad beim Einsatz der Metamagie Zentrierung für Entzugswiderstandsproben |

---

### 20. Adepten – Kraftpunkte & Kräfte (S. 158–159)

- **Kraftpunkte**: 1 pro Punkt Magieattribut (auch bei Steigerung: jeder neue Magiepunkt bringt sofort 1 kostenlosen Kraftpunkt). Beim Verlust eines Magiepunkts geht auch 1 Kraftpunkt (und die zugehörige Kraftstufe) verloren.
- **Maximale Stufe einer Kraft** = Magieattribut des Adepten (sofern das Kraft-eigene Maximum nicht niedriger liegt). *(3. Auflage/Errata: Erhöhungen durch Qi-Foki zählen bei dieser Obergrenze mit.)*

| Kraft | Kosten (Kraftpunkte) | Aktivierung | Numerischer Effekt |
|---|---|---|---|
| Adrenalinschub | 0,25/Stufe | Nebenhandlung | Initiativeergebnis `+2/Stufe` für `[Magie]` Kampfrunden; danach Entzug = Stufe |
| Astrale Wahrnehmung | 1 (fix) | Nebenhandlung | ermöglicht astrale Wahrnehmung |
| Attributsschub (Attribut) | 0,25/Stufe (max. Stufe 6) | Haupthandlung | Probe `Stufe + Magie`; jeder Erfolg `+1` auf gewähltes Attribut (Cap `+4`), hält `[Erfolge]` Kampfrunden, danach Entzug = Stufe |
| Beschleunigte Heilung | 0,5/Stufe | passiv | `+1 Erfolg/Stufe` bei Heilungs-/Genesungsproben |
| Erhöhte Präzision | 0,5 | passiv | Angriffswert jeder benutzten Waffe `+2` |
| Gefahrensinn | 0,5 | passiv | 1 Edge für Überraschungsproben (verfällt ungenutzt) |
| Geschärfter Sinn | 0,25 | passiv | 1 Edge pro gewähltem Sinn pro Begegnung |
| Kampfsinn | 0,5/Stufe | passiv | `+1 Würfelpoolbonus/Stufe` auf alle Verteidigungsproben; dieser Bonus gilt **auch für alle Überraschungsproben** (S. 110). *(3. Auflage/Errata; früher: „Chance, Überraschung per Wahrnehmungsprobe zu vermeiden".)* |
| Körpersprache | 0,25 | passiv | 1 Edge/Begegnung bei sozialen Proben |
| Kritischer Schlag | 1/Stufe | passiv | Schadenswert von Nahkampfangriffen `+1/Stufe` |
| Magieresistenz | 0,5 | passiv | 1 Edge, wenn Ziel eines gegen ihn verteidigten Zaubers |
| Mystische Panzerung | 0,25/Stufe | passiv | Verteidigungswert `+1/Stufe`, kumulativ mit getragener Panzerung |
| Richtungssinn | 0,25 | passiv | 1 Edge für Natur-Probe mit Orientierung |
| Schmerzresistenz | 0,25/Stufe | passiv | Verletzungsmodifikatoren setzen 1 Kästchen später/Stufe ein |
| Spurloser Schritt | 0,5 | passiv | hinterlässt keine Spuren, löst keine bewegungsbasierten Fallen aus |
| Stimmkontrolle | 0,5 | passiv | 1 Edge/Begegnung bei Proben mit Stimmeinsatz (Überreden/Einfluss) |
| Todeskralle | 0,5 | Nebenhandlung | wählbar Körperlicher/Betäubungsschaden im waffenlosen Kampf; magisch (umgeht Immunität gg. Normale Waffen) |
| Verbesserte Fertigkeit (Fertigkeit) | Kampffertigkeiten 1/Stufe, sonst 0,5/Stufe | passiv | dauerhaft `+Stufe` auf gewählte Fertigkeit, Cap `1,5× aufgerundete aktuelle Stufe` oder `+4` (niedrigerer Wert entscheidet) |

---

### 21. Spell-Entzugswerte (Referenztabelle, S. 135–144)

Grundentzug der einzelnen Zauber (vor Anpassungen wie Hochdrehen/Fläche Vergrößern):

**Heilzauber**: Attribut senken 3 · Attribut steigern 3 · Gegenmittel 5 · Heilen 3 · Kühlendes Heilen 5 · Neutralisierendes Heilen 5 · Reflexe steigern 5 · Schmerzresistenz 3 · Stabilisieren 3 · Wärmendes Heilen 5

**Illusionszauber**: Chaos 4 · Maske 3 · Physische Maske 4 · Schmerz 3 · Schweigen 3 · Sensortäuschung 2 · Stille 4 · Trideo-Trugbild 4 · Trugbild 3 · Unsichtbarkeit 3 · Verbesserte Unsichtbarkeit 4 · Verwirrung 3

**Kampfzauber**: Betäubungsball 4 · Betäubungsblitz 3 · Blitzstrahl 5 · Druckwelle 4 · Eisspeer 5 · Eissturm 6 · Energieball 5 · Energieblitz 4 · Feuerball 6 · Flammenstoß 5 · Kugelblitz 6 · Manaball 5 · Manablitz 4 · Säurestrahl 5 · Säurewelle 6 · Stoß 3

**Manipulationszauber**: Astralpanzerung 3 · Donnerknall 3 · Dunkelheit 3 · Elementarpanzerung 5 · Fahrzeugpanzerung 6 · Fokus-Boost 7 · Gedanken beherrschen 4 · Handlungen beherrschen 4 · Holz beleben 4 · Holz formen 3 · Kunststoff beleben 3 · Kunststoff formen 2 · Levitieren 6 · Licht 3 · Manabarriere 5 · Metall beleben 6 · Metall formen 5 · Panzerung 4 · Physische Barriere 6 · Schleuder 5 · Stein beleben 5 · Stein formen 4 · Übertakten 4 · Wand verstärken 4

**Wahrnehmungszauber**: Feinde entdecken 3 · Geistessonde 5 · Gerät analysieren 2 · Hellhören 3 · Hellsicht 3 · Kampfsinn 3 · Leben entdecken 3 · Magie analysieren 3 · Magie entdecken 4 · Telepathie 3 · Wahrheit prüfen 3

---

### Nicht erfasst

- Die genaue, dreiteilige **Verteidigungswert-Formel** der Geister (astral / physisch gegen Magie / physisch gegen normale Waffen, S. 150 f.) stand in sehr kleiner Schrift und sollte für den NPC-Generator direkt am Originaltext verifiziert werden, bevor sie produktiv genutzt wird.
- Das Kapitel **Adepten** endet auf S. 159 mitten in der Kräfteliste (letzte erfasste Kraft: *Verbesserte Fertigkeit*); weitere Adeptenkräfte liegen vermutlich auf S. 160+ außerhalb dieses Seitenbereichs.
- Mehrfach referenzierte Themen wie **Askennen** (S. 161), **Astralkampf** (S. 162) und **Magische Refugien als Manabarriere** (S. 163) werden im vorliegenden Seitenbereich nur erwähnt, aber erst auf späteren Seiten mit eigenen Berechnungen behandelt.
- Die exakte Fortsetzung des Abschnitts **Zauberabwehr** (S. 145, unterer Rand) wurde durch den Seitenumbruch abgeschnitten; nur die Grundform (Haupthandlung Antimagie, Probe Hexerei+Magie) ist gesichert erfasst.

---

## Teil 4: Astralebene, Initiation & Matrix-Grundlagen (Buchseiten 160–189)

<sub>Quelle-Chunk: `docs/sr6/sr6_calc_p161-190.md` — Originaltitel: Shadowrun 6 – Regeln mit Berechnungen (Grundregelwerk, Buchseiten 160–189)</sub>

Quelle: Sub-PDF `sr6_p161-190.pdf` (physische PDF-Seiten 161–190 des deutschen Grundregelwerks). Die im PDF gedruckten Buchseiten-Fußzeilen reichen von **S. 160** bis **S. 189** (Offset PDF-Seite = Buchseite + 1). Der Bereich deckt das Ende des Kapitels **MAGIE** (Magieadepten, Astralebene, Schutzgeister, Initiation/Metamagie, magische Ausrüstung) sowie den Anfang des Kapitels **MATRIX** (Grundlagen, Matrixhandlungen, Hosts/IC, Technomancer) ab.

Buchseitenzahlen sind in Klammern angegeben, z. B. (S. 175).

---

### 1. Magieadepten – Kräfte mit Zahlenwerten (S. 160)

- **Verbesserte Reflexe**: `1 Kraftpunkt (KP) pro Stufe`. Pro Stufe: `+1 Initiativewürfel` und `+1 Reaktion`. Maximalstufe **4**; nicht mit anderen Initiative-/Reaktionssteigerungen kombinierbar.
- **Verbesserte Wahrnehmung**: `0,5 KP`. Gewährt 1 Edge bei der Handlung *Genau beobachten* oder bei einer Wahrnehmungsprobe zum Auffinden/Hören von Verstecktem. Der Punkt muss sofort für diese Probe ausgegeben werden, sonst verfällt er.
- **Verbessertes Körperliches Attribut**: `1 KP pro Stufe`. Permanente Steigerung eines Körperlichen Attributs (KON, GES, REA oder STA) um die Stufe der Kraft. **Cap**: `Attribut ≤ 1,5 × aktuelle Stufe (aufgerundet)` **oder** `+4`, je nachdem, welcher Wert niedriger ist.
- **Wandlaufen**: `0,5 KP`, Aktivierung Nebenhandlung. Nicht zweimal hintereinander einsetzbar; erfordert dazwischen mindestens eine horizontale Bewegung.

#### Kraftpunkte & Zauber bei Magieadepten (S. 160)

- Magieadepten teilen ihr Magieattribut bei der Charaktererschaffung zwischen Adepten- und Magierseite auf: `1 Kraftpunkt pro Punkt Magie` auf der Adeptenseite; Zauber auf der Magierseite werden wie bei Vollzauberern mit `Magie × 2` berechnet (s. Abschnitt "Magie/Resonanz" der Charaktererschaffung).
- Jede Steigerung des Magieattributs per Karma bringt automatisch **1 zusätzlichen kostenlosen Kraftpunkt**.
- Verliert ein Magieadept einen Punkt Magie, verliert er auch **1 Kraftpunkt** und die entsprechenden Adeptenkräfte.

---

### 2. Askennen (S. 161)

Vergleichende Probe Astral + Intuition. Anzahl der Erfolge bestimmt die erhaltene Informationsmenge:

| Erfolge | Informationen |
|---|---|
| 0 | Keine |
| 1 | Gesundheits-/Gefühlszustand, ob Erwacht oder mundan |
| 2 | Standard-Cyberware, aktive Magie (Feuergeist, Manipulationszauber, Kraftfokus etc.); bereits bekannte Aura wird mit Erinnerungsvermögen (S. 37) wiedererkannt |
| 3 | Alpha-Cyberware; Vergleich Essenz/Magie ≥/≤ des Wahrnehmenden; Vergleich Kraftstufe ≥/≤ Magie des Wahrnehmenden; allgemeine Diagnose von Krankheiten/Toxinen; astrale Signaturen am Ziel |
| 4 | Beta-Cyberware und Bioware; exakte Essenz/Magie/Kraftstufe; Ursache einer bestehenden astralen Signatur |
| 5+ | Delta-Cyberware, Gentech, Nanotech; genaue Diagnose von Krankheiten/Giften; ob Ziel Technomancer oder Monade ist |

Ohne die Fähigkeit Astral kann Askennen nur als ungeübte Fertigkeit (S. 95) versucht werden.

---

### 3. Astrale Signatur & Astrales Verblassen (S. 161–162)

- **Verblassen astraler Signaturen**: Das astrale Leuchten eines gewirkten Zaubers bleibt für `Magieattribut des Zauberers` Stunden bestehen. *Reinigen* (Hauptbehandlung) zählt jede Anwendung als 1 Stunde verstrichener Zeit; wiederholbar bis die Signatur vollständig entfernt ist.
- **Würfelpoolmalus beim astralen Betrachten der physischen Ebene**: `−2` auf alle Handlungen auf der physischen Ebene, während astral wahrgenommen wird.

---

### 4. Astrale Projektion (S. 162)

- **Maximale Projektionsdauer**: `Magie × 2` Stunden außerhalb des physischen Körpers.
- **Essenzverlust bei Überschreitung**: `−1 Essenzpunkt pro Stunde` über das Limit hinaus. Sinkt die Essenz auf 0, stirbt der Charakter.
- **Essenz-Regeneration nach Rückkehr**: `+1 Punkt pro Stunde`.
- **Astrale Bewegungsgeschwindigkeit**: `5 km/Kampfrunde` (astrales Rennen, dabei unscharf/blind für die Umgebung) oder `100 m/Kampfrunde` (langsamere Bewegung, Umgebung bleibt wahrnehmbar).

#### Astrale Heimkehr (S. 162, Kasten)

- Versuch, zum unbekannten Körper zurückzufinden: Probe auf Astral + Intuition; Schwellenwert vom Spielleiter nach Versteckqualität festgelegt.
- Erfolgreiche Probe: Körper wird **innerhalb einer Stunde** gefunden. `Pro Nettoerfolg über dem Schwellenwert halbiert sich die Suchzeit` (1 Nettoerfolg = 30 Min., 2 = 15 Min., 3 = 7,5 Min. usw.).

---

### 5. Astralkampf (S. 162–163)

#### Kampfwerte (Kasten *Astralkampf*, S. 163)

- **Angriffswert**: `Magie + Traditionsattribut`
- **Verteidigungswert**: `Intuition + natürliche Panzerung + Panzerungseffekte` (physische Panzerung/Konstitution zählen nicht; Metamenschen ohne natürliche Panzerung sind i. d. R. ungeschützt, da nur ihr astraler Körper geschützt wird)
- **Initiative**: `Logik + Intuition + 3W6` (Errata Grundregelwerk 3. Auflage: korrigiert von 2W6 auf 3W6, S. 163 — der Tabellen-Anhang S. 330 wurde bei der Errata-Korrektur offenbar übersehen und zeigt weiterhin die alte 2W6-Fassung)

| Würfelpool | Formel |
|---|---|
| Waffenloser Kampf | Astral + Willenskraft |
| Waffenfoki | Nahkampf + Willenskraft |
| Spruchzauberei | Hexerei + Magie |
| Verteidigung | Logik + Intuition |
| Schadenswiderstand | Willenskraft |

| Schadenswert | Formel |
|---|---|
| Waffenlos | `Traditionsattribut ÷ 2 (aufgerundet)`, `+1 pro Nettoerfolg` |
| Waffenfokus | Wert der physischen Waffe, `+1 pro Nettoerfolg` |

Der Angreifer wählt jeweils, ob Körperlicher oder Betäubungsschaden verursacht wird. Manabarrieren können nur Körperlichen Schaden im Astralkampf verursachen.

---

### 6. Astrales Spurenlesen (S. 163)

- Ausgedehnte Probe Astral + Intuition (Schwellenwert 5, Intervall 1 Stunde).
- Modifikatoren (Kasten *Astrales Spurenlesen*):

| Situation | Schwellenwert-Modifikator |
|---|---|
| Pro Stunde seit die astrale Verbindung aktiv war | `+1` |
| Ziel befindet sich hinter einer Manabarriere | `+ (Kraftstufe der Barriere)` |
| Auffinden des Beschwörers durch Geist | `+2` |

---

### 7. Manabarrieren (S. 163–164)

- **Struktur**: Manabarriere erhält bei Erschaffung eine Strukturstufe (meist abhängig von Erfolgen der Zauberprobe). Regeneriert am Ende der Kampfrunde auf volle Strukturstufe.
- **Zauber durch eine Barriere wirken**: `Kraftstufe der Barriere` als Würfelpoolmalus zur Verteidigungsprobe; bei Zaubern ohne Vergleichende Probe wird die Zauberprobe stattdessen gegen eine Vergleichende Probe mit `Kraftstufe der Barriere × 2` abgewickelt.
- **Barriere gewaltsam durchbrechen**: Vergleichende Probe `Charisma + Magie` gegen `Strukturstufe × 2` der Manabarriere. Bei Erfolg: Durchbruch; `pro Nettoerfolg über den ersten hinaus` kann 1 weiteres Wesen/Fokus/aufrechterhaltener Zauber/astrale Gestalt mitgenommen werden. Barriere muss mindestens gleich viele Erfolge erzielen, sonst scheitert der Versuch.
- **Verdrängungsproben bei blockierten Objekten** (Vergleichende Probe, jeweilige Seite):

| Objekt | Widerstandswert |
|---|---|
| Lebewesen | Charisma + Magie |
| Foki | Kraftstufe × 2 |
| Alchemistische Erzeugnisse | Wirksamkeit × 2 |
| Manabarrieren | Strukturstufe × 2 |
| Aufrechterhaltene Zauber | Magie des Zauberers × 2 |

#### Manabarrieren-Typen (S. 164)

| Manabarriere | Astral oder physisch | Seite |
|---|---|---|
| Hüter (Ritual) | Beide Ebenen | S. 147 |
| Magisches Refugium | Beide Ebenen | S. 132 |
| Manabarriere (Zauber) | Eine Ebene | S. 142 |
| Schutzkreis (Ritual) | Beide Ebenen | S. 147 |

---

### 8. Schutzgeister – allgemeine Vorteilsformel (S. 164–168)

Nicht als Statblock-Liste erfasst (Flavortext je Archetyp), aber die zugrunde liegende Mechanik ist einheitlich: Jeder Schutzgeist gewährt **3 Vorteile** (1 allgemeiner, 1 nur für Zauberer, 1 nur für Adepten) und **1 Nachteil**, permanent in Kraft ab Wahl des Schutzgeists.

- Häufigste Vorteilsform: **Edge-Boosts bei [Kategorie]-Proben kosten 1 Edge weniger als normal** (Minimum weiterhin 1 Edge).
- Adepten-Vorteile sind meist ein kostenloser Kraftpunkt in einer bestimmten Adeptenkraft/-stufe.
- Magieadepten müssen sich beim Wählen des Schutzgeists auf den Zauberer- oder Adeptenvorteil festlegen (nicht rückgängig machbar); Auswahl des Schutzgeists selbst kann nachträglich ebenfalls nicht geändert werden.

---

### 9. Initiation (S. 168)

- **Probe**: Ausgedehnte Probe auf `höchste magische Fertigkeit + Magie` (Schwellenwert = `neuer Initiatengrad`, Intervall 1 Monat). Adepten verwenden dafür die höchste Fertigkeit, die mit einer ihrer Adeptenkräfte verknüpft ist.
- **Karmakosten**: `10 + neuer Initiatengrad` (vgl. Entwicklungskosten-Tabelle in Teil 1, Abschnitt 12; S. 72).
- Mindestens **8 Stunden Training pro Tag** während der Initiation.
- **Magieattribut-Maximum**: `6 + Initiatengrad`. Die Erhöhung des tatsächlichen Magieattributs erfolgt nicht automatisch, sondern muss separat mit Karma bezahlt werden (normale Attributkosten).
- Ab Initiatengrad 1: Zugang zu den Metaebenen bei astraler Projektion.
- Bei jeder Initiation: Wahl **einer** Metamagie (sofern nicht anders angegeben).

---

### 10. Metamagie mit Berechnungen (S. 168, 170)

- **Abschirmung**: Beim Ansagen von *Zauberabwehr* (S. 145) zusätzliche Würfel bis zur Höhe des Initiatengrads einsetzbar (nur für Zauberabwehr, nicht für andere Antimagie-Handlungen).
- **Adeptenzentrierung** (nur Adepten): Zentrierungshandlung (Nebenhandlung) verhindert, dass schlechte Umgebungsbedingungen (Beleuchtung, Illusionen usw.) Nachteile verursachen bzw. dass Gegner dadurch Edge erhalten.
- **Fixierung**: Beim Herstellen eines alchemistischen Erzeugnisses `1 bis Wirksamkeit des Erzeugnisses` Karma einsetzbar. Wirksamkeit sinkt dann `1 Stufe pro Tag` statt `pro [aktuelle Wirksamkeit × 2] Stunden`. Erzeugnis erhält beim Widerstand gegen *Trennen* (S. 155) einen Würfelpoolbonus in Höhe des eingesetzten Karmas.
- **Flexible Signatur**: Verändern/Fälschen der astralen Signatur. Schwellenwert für Askennen-Erkennung der Fälschung = `Initiatengrad` des Fälschers; ab Erreichen dieses Schwellenwerts erkennt der Betrachter die Wahrheit dahinter (z. B. Initiat Grad 2 → Fälschung hält 3 Erfolgen stand, erst 5 Erfolge enttarnen sie). Haltbarkeit der eigenen Signatur kann um `Initiatengrad` Stunden reduziert werden.
- **Zauberformung**: `−1 Würfelpoolmalus pro Meter`, um den Radius eines Flächenzaubers zu vergrößern/verkleinern bzw. in eine Kugel von 1 m Radius umzuformen. **Cap**: maximaler Malus = `Magieattribut`.
- **Zentrierung** (allgemein, nicht Adepten-spezifisch): Würfelpoolbonus auf alle Entzugswiderstandsproben in Höhe von `Initiatengrad`.
- **Kraftpunkt** (nur Adepten): Statt einer Metamagie kann ein Adept bei jeder neuen Initiation 1 Kraftpunkt erhalten.
- **Maskierung**: Verändert die scheinbare Magiestufe der Aura um bis zu `Initiatengrad` nach oben oder unten (oder mundan). Bei Entdeckungsversuch: Vergleichende Probe `Magie + Initiatengrad` (Maskierer) gegen die Askennenprobe des Betrachters.

---

### 11. Magische Ausrüstung (S. 170)

#### Foki – Bindungskosten, Verfügbarkeit, Preis

| Fokus | Bindungskosten (Karma) | Verfügbarkeit | Preis |
|---|---|---|---|
| Geisterfokus | `Kraftstufe × 2` | `(Kraftstufe)L` | `Kraftstufe × 4.000 ¥` |
| Kraftfokus | `Kraftstufe × 6` | `(Kraftstufe + 3)L` | `Kraftstufe × 18.000 ¥` |
| Metamagiefokus | `Kraftstufe × 3` | `(Kraftstufe)L` | `Kraftstufe × 9.000 ¥` |
| Qi-Fokus | `Kraftstufe × 2` | `(Kraftstufe)L` | `Kraftstufe × 3.000 ¥` |
| Verzauberungsfokus | `Kraftstufe × 3` | `(Kraftstufe)L` | `Kraftstufe × 5.000 ¥` |
| Waffenfokus | `Kraftstufe × 3` | `(Kraftstufe + 3)L` | `Kraftstufe × 4.000 ¥` |
| Zauberfokus | `Kraftstufe × 2` | `(Kraftstufe)L` | `Kraftstufe × 3.000 ¥` |

#### Formeln (zum Herstellen der Foki/Zauber)

| Formel | Verfügbarkeit | Preis |
|---|---|---|
| Fokusformel | wie zugehöriger Fokus | `Fokuskosten × 0,25 ¥` |
| Ritualformel | 3L | 1.000 ¥ |
| Zauberformel – Heilung | 2L | 500 ¥ |
| Zauberformel – Illusion | 3L | 1.000 ¥ |
| Zauberformel – Kampf | 3L | 2.000 ¥ |
| Zauberformel – Manipulation | 3L | 1.500 ¥ |
| Zauberformel – Wahrnehmung | 2L | 500 ¥ |

*(3. Auflage/Errata: Zeile* Ritualformel *(3L / 1.000 ¥) ergänzt.)*

#### Magische Vorräte

| Vorrat | Verfügbarkeit | Preis |
|---|---|---|
| Materialien für Magische Refugien | `(Kraftstufe)L` | `Kraftstufe × 500 ¥` |
| Reagenzien, pro Dram | 2 | 50 ¥ |

---

### 12. Matrix-Zustandsmonitor & Reparatur (S. 175)

- **Matrix-Zustandsmonitor eines Geräts**: `[8 + (Gerätestufe ÷ 2, aufgerundet)]` Kästchen.
- Bei jedem beschädigten Gerät: `−1 Würfelpoolmalus pro Kästchen Matrixschaden` auf alle mit dem Gerät durchgeführten Proben. Voller Zustandsmonitor → Gerät ist **lahmgelegt**.
- **Reparatur**: Ausgedehnte Probe `Mechanik + Logik` (Schwellenwert = Anzahl der Schadenskästchen, Intervall 1 Stunde). Werkzeugkiste nötig; Gerät währenddessen nicht nutzbar. Kritischer Patzer → Gerät ist unreparierbar zerstört.

---

### 13. Matrixkampf & Edge in der Matrix (S. 176)

- **Angriffswert (Matrixkampf/Hacking)**: `Angriff + Schleicher` der Persona.
- **Verteidigungswert**: `Datenverarbeitung + Firewall` des Ziels.
- **Edge-Erhalt**: Übertrifft ein Wert den anderen um `≥4`, erhält die überlegene Seite 1 Edge (analog zur physischen Edge-Regel, S. 46).
- Edge über das Edge-Attribut hinaus, das in der VR erhalten wurde, verfällt am Ende der Konfrontation (Host verlassen, Gerät neu starten, Ausstöpseln, oder Erreichen der Fokussierung).
- **Volle Matrixabwehr** (S. 184, Matrix-Äquivalent zu *Volle Abwehr*, 3. Auflage/Errata): Addiere bis **zum Ende der Kampfrunde** die **Firewall** zu **allen** Verteidigungsproben in der Matrix. **Jederzeit-Handlung** — auch außerhalb des eigenen Zuges einsetzbar. *(Frühere Fassung: nur die nächste Verteidigungsprobe, und nur im eigenen Zug.)*

#### Matrix-Edge-Handlungen (Kasten, S. 176)

| Handlung | Kosten | Effekt |
|---|---|---|
| Notfall-Boost | 1 Edge | `+1` auf ein Matrixattribut, vorübergehend für eine Probe |
| Signalschrei | 2 Edge | Nächste Handlung ignoriert alle Rauschen-Modifikatoren |
| Technoplappern (nur Technomancer) | 2 Edge | Nächste Matrixhandlung verwendet Charisma statt Logik |
| Überfordern | 2 Edge | Ziel: `−2 Datenverarbeitung`, `−1 aktiver Programmslot` für `[Angriffswert des Angreifers]` Kampfrunden |
| Unterm Radar | 3 Edge | Nächste illegale Handlung in dieser Kampfrunde lässt den OW nicht steigen (macht sie aber nicht legal) |

---

### 14. Overwatch-Wert & Fokussierung (S. 177)

- **Fokussierung** tritt ein, sobald der Overwatch-Wert (OW) **40** erreicht.
- **OW-Anstieg durch Hacking-Programme**: `+1 pro Matrixhandlung`, die durch ein aktiv genutztes Hacking-Programm modifiziert wird (bloßes Laden zählt nicht).
- **OW-Anstieg durch Aufrechterhaltung illegalen Zugangs**: `+1 pro Runde` je Host/Gerät mit aufrechterhaltenem illegalem User-Zugang; `+3 pro Runde` je Host/Gerät mit illegalem Admin-Zugang.
- **OW-Anstieg durch illegale Handlungen**: `+1 pro erzieltem Erfolg der Gegenseite`, unabhängig vom Erfolg der eigenen Verteidigung.
- OW ist nicht zurücksetzbar, solange man in der Matrix bleibt.

---

### 15. Auswurfschock & Linksperre (S. 177)

- **Auswurfschock**-Schaden: `3 Kästchen Betäubungsschaden` bei kaltem Sim, `3 Kästchen Körperlicher Schaden` bei heißem Sim; Widerstand mit Willenskraft (Biofeedback-Schaden).
- **Zusätzlich** (auch bei vollständig widerstandenem Schaden): Status *Benommen* für `[10 − Willenskraft]` Minuten.

---

### 16. Rauschen (S. 177)

Pro Punkt Rauschen: `−1 Würfelpoolmalus` auf alle Matrixproben. Übersteigt der Rauschenwert die Gerätestufe (physische Entfernung) oder gilt eine Quelle mit dem höchsten Rauschenwert, ist kein Matrixzugriff möglich.

| Physische Entfernung/Hindernis | Rauschenwert |
|---|---|
| Direktverbindung (jede Entfernung) | 0 |
| Bis 100 m | 0 |
| 101–1.000 m | 1 |
| 1.001–10.000 m | 3 |
| 10.001 m – 100 km | 5 |
| Mehr als 100 km | 8 |
| Dichtes Laubwerk | 1 pro 5 m |
| Faradaykäfig | kein Signal, keine Handlung möglich |
| Süßwasser | 1 pro 10 cm |
| Störsender | 1 pro Erfolg bei der Handlung *Signal stören* |
| Metallüberzogene Erde/Mauer | 1 pro 0,5 m |
| Salzwasser | 1 pro cm |
| Spam-Zone oder Matrixloch | Stufe der Zone/des Lochs |
| WiFi-Abschirmung (Tapete/Farbe) | Stufe der Abschirmung |

Es gilt immer die Rauschen-Quelle mit dem höchsten Wert (nicht kumulativ über mehrere Quellen).

---

### 17. Matrix-Hardware (S. 178)

#### Cyberbuchsen

| Stufe | Attribute (D/F) | Matrixinitiative-Bonuswürfel (VR) | Verfügbarkeit | Essenz | Preis |
|---|---|---|---|---|---|
| 1 | 4/3 | +1 | 3L | 1 | 45.000 ¥ |
| 2 | 5/4 | +1 | 3L | 1,5 | 65.000 ¥ |
| 3 | 6/5 | +1 | 3L | 2 | 80.000 ¥ |
| 4 | 7/6 | +2 | 4L | 2,3 | 95.000 ¥ |
| 5 | 8/7 | +2 | 5L | 2,6 | 140.000 ¥ |
| 6 | 9/8 | +2 | 6L | 3 | 210.000 ¥ |

#### Kommlinks

| Kommlink | Gerätestufe | Attribute (D/F) | Aktive Programmslots | Verfügbarkeit | Preis |
|---|---|---|---|---|---|
| Meta Link | 1 | 1/0 | 0 | 2 | 100 ¥ |
| Sony Emperor | 2 | 1/1 | 1 | 2 | 700 ¥ |
| Renraku Sensei | 3 | 2/0 | 1 | 2 | 1.000 ¥ |
| Erika Elite | 4 | 2/1 | 2 | 2 | 2.500 ¥ |
| Hermes Ikon | 5 | 3/0 | 2 | 3 | 5.000 ¥ |
| Transys Avalon | 6 | 3/1 | 3 | 3 | 8.000 ¥ |

#### Cyberdecks

| Cyberdeck | Gerätestufe | Attribute (A/S) | Aktive Programmslots | Verfügbarkeit | Preis |
|---|---|---|---|---|---|
| Erika MCD-6 | 1 | 4/3 | 2 | 3l | 24.750 ¥ |
| Spinrad Falcon | 2 | 5/4 | 4 | 3l | 61.500 ¥ |
| MCT 360 | 3 | 6/5 | 6 | 3l | 95.000 ¥ |
| Renraku Kitsune | 4 | 7/6 | 8 | 4l | 107.000 ¥ |
| Shiawase Cyber-6 | 5 | 8/7 | 10 | 5l | 172.500 ¥ |
| Fairlight Excalibur | 6 | 9/8 | 12 | 6l | 410.600 ¥ |

*(3. Auflage/Errata: Der Spaltentitel wurde von „Matrixinitiative-Bonus" zu „Matrixinitiative-Bonuswürfel (VR)" korrigiert — der Wert sind zusätzliche Initiative­würfel in der VR, kein Zuschlag auf den Initiativewert. Die Werte selbst bleiben +1 (Stufe 1–3) bzw. +2 (Stufe 4–6); in der Cyberware-Tabelle S. 284 war für Stufe 5/6 zuvor fälschlich +3 angegeben.)*

Bei einem Decker werden die vier Matrixattribute (Angriff/Schleicher/Datenverarbeitung/Firewall) frei aus den Attributen der genutzten Geräte zusammengestellt (kein Attribut darf 0 sein); mit der Handlung *Matrixattribute austauschen* (Nebenhandlung) lassen sich die Werte danach beliebig zwischen den vier Attributen verschieben.

---

### 18. Matrixinitiative (S. 179)

| Modus | Formel |
|---|---|
| AR | `Reaktion + Intuition + 1W6` |
| VR (kaltes Sim) | `Intuition + Datenverarbeitung + 2W6` |
| VR (heißes Sim) | `Intuition + Datenverarbeitung + 3W6` |

---

### 19. Matrixhandlungen – Würfelpools & Formeln (S. 179–184)

Allgemeines Prinzip: Ist eine Handlung mit einem "niedrigeren" der beiden verbundenen Attribute (Angriff oder Schleicher) verknüpft als das andere (z. B. Brute Force nutzt Angriff, ist aber mit Schleicher verknüpft, falls Schleicher > Angriff), erhält die Handlung einen `Würfelpoolmalus = Differenz der beiden Attribute`.

Bei „Entweder/oder"-Würfelpools (z. B. *Intuition + Firewall oder Schleicher + Firewall*) nutzen Personas mit Geistigen Attributen den Pool, der ein Geistiges Attribut enthält; **Drohnen verwenden ihre Pilotstufe statt des Geistigen Attributs** (3. Auflage/Errata); eine Persona, die aktiv einen Host/ein Gerät verteidigt, darf auch den Pool mit den Geräte-/Hostattributen verwenden.

| Handlung | Zugangsstufe | Würfelpool (Angreifer) | Gegenprobe/Wert (Verteidiger) | Handlungsart |
|---|---|---|---|---|
| Ausstöpseln | Gast/User/Admin | Elektronik + Willenskraft | Charisma + Datenverarbeitung ODER Angriff + Datenverarbeitung | Haupt |
| Befehl vortäuschen | Gast/User/Admin | Cracken + Logik (illegal) | Datenverarbeitung + Firewall ODER Pilot + Firewall | Haupt |
| Brute Force | Gast/User/Admin | Cracken + Logik (illegal) | Willenskraft + Firewall ODER Firewall × 2 | Haupt |
| Datei cracken | User/Admin | Cracken + Logik (illegal) | Verschlüsselungsstufe × 2 | Haupt |
| Datei editieren | User/Admin | Elektronik + Logik | Intuition + Firewall ODER Schleicher + Firewall | Haupt |
| Datei verschlüsseln | User/Admin | Elektronik + Logik | – (Erfolge = neue Verschlüsselungsstufe) | Haupt |
| Datenbombe entschärfen | User/Admin | Elektronik + Logik | Stufe der Datenbombe × 2 | Haupt |
| Datenbombe legen | Admin | Cracken + Logik (illegal) | Gerätestufe × 2 | Haupt |
| Datenspike | Gast/User/Admin | Cracken + Logik (illegal) | Datenverarbeitung + Firewall ODER Logik + Firewall | Haupt |
| Gerät formatieren | Admin | Elektronik + Logik | Willenskraft + Firewall ODER Firewall × 2 | Haupt |
| Gerät neu starten | Admin | Elektronik + Logik | Willenskraft + Firewall ODER Firewall × 2 | Haupt |
| Gerät steuern | User/Admin | Elektronik + Logik | Willenskraft + Firewall ODER Firewall × 2 | Haupt |
| Hineinspringen | User/Admin | Elektronik + Logik | Willenskraft + Firewall ODER Firewall × 2 | Haupt |
| Hintertür benutzen | Gast | Cracken + Logik (illegal) | Willenskraft + Firewall ODER Firewall × 2 | Haupt |
| Icon aufspüren | Admin | Cracken + Intuition (illegal) | Willenskraft + Schleicher ODER Firewall + Schleicher | Haupt |
| Matrixsignatur löschen | User/Admin | Cracken + Logik (illegal) | Willenskraft + Firewall ODER Firewall × 2 | Haupt |
| Matrixwahrnehmung | Gast/User/Admin | Elektronik + Intuition | Willenskraft + Schleicher ODER Firewall + Schleicher | Haupt (Neben in VR) |
| Overwatch-Wert bestimmen | Admin | Cracken + Logik (illegal) | Schwellenwert 4 | Haupt |
| Programm abstürzen lassen | Admin | Cracken + Logik (illegal) | Datenverarbeitung + Gerätestufe | Haupt |
| Prüfsummensuche | User/Admin | Cracken + Logik (illegal) | Schwellenwert 1 (mit Prüfsumme) oder 4 (schätzen) | Haupt |
| Signal stören | Admin | Cracken + Logik (illegal) | – | Haupt |
| Sondieren | Gast/User/Admin | Cracken + Logik (illegal) | Willenskraft + Firewall ODER Firewall × 2 | Haupt (Intervall 1 Min.) |
| Teergrube | Gast/User/Admin | Cracken + Logik (illegal) | Datenverarbeitung + Firewall ODER Logik + Firewall | Haupt |
| Übertragung abfangen | Admin | Cracken + Logik (illegal) | Logik + Firewall ODER Datenverarbeitung + Firewall | Haupt |
| Verstecken | Gast/User/Admin | Cracken + Intuition (illegal) | Intuition + Datenverarbeitung ODER Schleicher + Datenverarbeitung | Haupt |
| Matrixsuche | Gast/User/Admin | Elektronik + Intuition | – (Ausgedehnt, 10 Min.) | Haupt |
| Host betreten/verlassen, Icon verändern, Interfacemodus wechseln, Matrixattribute austauschen, Nachricht übermitteln | – | keine Probe | – | Neben |

#### Regeländerungen 3. Auflage/Errata bei einzelnen Handlungen (Schwellenwerte unverändert)

- **Gerät neu starten** (S. 181): Zielgerät/-PAN/-persona geht offline und ist am Ende der **folgenden** Kampfrunde wieder online. Overwatch-Wert des Ziels und alle Zugriffe werden zurückgesetzt. Der Neustart verursacht **keinen Auswurfschock**. Nicht möglich, wenn man selbst Opfer einer **Linksperre** ist.
- **Hineinspringen** (S. 182): Solange man hineingesprungen bleibt, kann das Gerät **nicht Ziel von Matrixhandlungen** sein. In ein bereits von jemand anderem besetztes Gerät kann man **nicht** hineinspringen.
- **Datenbombe legen** (S. 181): Auslösungsschaden `Stufe × 2` (s. u.).

#### Zahlenformeln einzelner Handlungen

- **Datenspike-Schaden**: `Angriffsattribut ÷ 2 (aufgerundet)`, `+1 pro Nettoerfolg`.
- **Datenbombe – Stufe**: max. = `Anzahl der Nettoerfolge` beim Legen. **Schaden bei Auslösung**: `Stufe × 2` Kästchen Matrixschaden (widerstanden mit Firewall). *(3. Auflage/Errata; früher `Stufe × 4`.)*
- **Teergrube**: bei Erfolg `1 + Nettoerfolge` Kästchen Matrixschaden (mit Firewall widerstanden) und Absenkung der Datenverarbeitung des Ziels um denselben Wert; Regeneration `1 Punkt pro Kampfrunde` ab der Folgerunde des Angriffs. Bei Datenverarbeitung 0: keine Matrixhandlungen mehr möglich, bis wieder ≥1.
- **Hintertür-Haltbarkeit** (aus *Sondieren*): `[10 − Host-/Gerätestufe]` Stunden, oder bis Neustart des Geräts/Hosts.
- **Prüfsummensuche**: max. 32 potenzielle Treffer; `jeder Nettoerfolg halbiert die Trefferzahl` (16 bei 1 NE, 8 bei 2 NE usw.). Wiederholung mit `−2 Würfelpoolmalus` (Neuer Versuch, S. 38) möglich; jeder weitere Erfolg halbiert erneut.
- **Signal stören**: Erfolge werden zum Rauschenwert für Matrixhandlungen mit oder gegen Geräte im Umkreis von 100 m addiert.
- **Gerät steuern – Attributsubstitution je nach Modus**: Über AR mit Körperlichem Attribut → normales Attribut; über VR mit Körperlichem Attribut → entsprechendes Geistiges Attribut (`Konstitution=Willenskraft, Geschicklichkeit=Logik, Reaktion=Intuition, Stärke=Charisma`).

---

### 20. Hosts & IC (S. 185–187)

- **Hoststufe**: 1–12. **Attributreihe**: `Hoststufe, Hoststufe+1, Hoststufe+2, Hoststufe+3` (beliebig auf Angriff/Schleicher/Datenverarbeitung/Firewall verteilbar). Beispiel: Host Stufe 4 → z. B. Angriff 5, Schleicher 4, Datenverarbeitung 7, Firewall 6.
- Die Attribute eines Hosts gelten auch für dessen IC.
- **Verschachtelte Hoststruktur**: Der OW steigt für **alle** Hosts, zu denen gleichzeitig Zugang besteht – nicht nur für den, in dem gerade gearbeitet wird.
- **IC allgemein**: `Angriffswert = Hoststufe × 2`; derselbe Wert dient als Gerätestufe für den Matrix-Zustandsmonitor des IC und für die meisten Proben. **Initiative** = `Datenverarbeitung (Host) × 2 + 3W6`. Ein Host darf pro Kampfrunde 1 IC starten und Kopien gleich der Hoststufe gleichzeitig laufen lassen (max. 1 Kopie pro IC-Art aktiv).

#### IC-Typen mit Zahlenformeln

| IC | Verteidigung | Effekt bei Treffer |
|---|---|---|
| Absturz | Intuition + Firewall | Kein Matrixschaden; stattdessen stürzt ein zufälliges Programm des Ziels ab (Neustart nötig) |
| Aufspüren | Willenskraft + Schleicher | Kein Schaden; deckt physischen Aufenthaltsort des Ziels auf |
| Blaster | Logik + Firewall | `[Hoststufe + Nettoerfolge]` Kästchen Matrixschaden (Firewall-Widerstand) + Linksperre |
| Bremse | Willenskraft + Datenverarbeitung | Datenverarbeitung des Ziels `−1 pro Nettoerfolg` (min. 1 für Handlungsfähigkeit); Regeneration 1 Pkt./Min. nach Verlassen des Hosts |
| Killer | Intuition + Firewall | `[Hoststufe + Nettoerfolge]` Kästchen Matrixschaden (Firewall-Widerstand) |
| Leuchtspur | Willenskraft + Schleicher | Schleicher des Ziels `−1 pro Nettoerfolg` (min. 1); Regeneration 1 Pkt./Min. nach Verlassen |
| Patrouille | – (führt *Matrixwahrnehmung* als Nebenhandlung aus, 1×/Minute) | Erfolge gelten für jede Matrixwahrnehmung des IC bis zur nächsten Aktualisierung |
| Säure | Willenskraft + Firewall | Firewall des Ziels `−1 pro Nettoerfolg`; Regeneration 1 Pkt./Min. nach Verlassen |
| Schwarzes IC | Intuition + Firewall | `[Hoststufe + Nettoerfolge]` Kästchen **gleichzeitig** als Matrixschaden (Firewall) und Biofeedback-Schaden (Willenskraft) |
| Sparky | Intuition + Firewall | `[Hoststufe + Nettoerfolge]` Kästchen Biofeedback-Schaden (Willenskraft-Widerstand) |
| Störer | Willenskraft + Angriff | Angriff des Ziels `−1 pro Nettoerfolg` (min. 1); Regeneration 1 Pkt./Min. nach Verlassen |
| Teerbaby | Logik + Firewall | Belegt das Ziel mit einer Linksperre |
| Wirbel | Willenskraft + Firewall | Erzwingt Neustart des Ziels (verliert nächste Handlung, statt Linksperre) |

---

### 21. Programme (S. 184–185)

Zahlenrelevante Effekte (Auswahl, kein vollständiger Statblock):

- **Programm-Handling** (S. 184, 3. Auflage/Errata): Start/Beendigung eines Programms erfordert **keine** Handlung; das **Laden/Entfernen** eines Programms in einen/aus einem aktiven Programmslot erfordert eine **Nebenhandlung**.

- **Editieren / Schmöker / Aufspüren / Tarnkappe**: gewähren je 1 Edge bei Erfolg der zugehörigen Handlung; muss sofort für diese Handlung ausgegeben werden, sonst verfällt es.
- **Signalreiniger**: senkt den Rauschenwert um `2`.
- **Toolbox**: `+1` auf Datenverarbeitung.
- **Verschlüsselung**: `+2 Würfel` für die Handlung *Datei verschlüsseln*.
- **Virtuelle Maschine**: `2` zusätzliche Programmslots; bei Angriffen `+1` zusätzliches Kästchen Matrixschaden (ungewidmet).
- **Ausnutzen**: Verteidigungswert der Gegenseite bei Hacking-Versuchen `−2`.
- **Entschärfen / Entschlüsselung**: `+2 Würfel` für *Datenbombe entschärfen* bzw. *Datei cracken*.
- **Panzerung**: `+2` auf Verteidigungswert.
- **Übertakten**: `+2 Würfel` für eine Matrixhandlung; einer der Würfel muss der Schicksalswürfel sein. *(3. Auflage/Errata: Das Programm muss für **jede** Matrixhandlung separat gekauft werden.)*

---

### 22. Technomancer – Lebende Persona (S. 188–189)

- **Matrixattribute** entsprechen Geistigen Attributen: `Gerätestufe = Resonanz`, `Angriff = Charisma`, `Schleicher = Intuition`, `Datenverarbeitung = Logik`, `Firewall = Willenskraft`.
- **Zusatzpunkte** zur freien Verteilung auf die Matrixattribute = `Resonanz`. **Cap pro Attribut**: Erhöhung ≤ `aufgerundete Hälfte des Ausgangswerts` **und** ≤ `+4` (der niedrigere Wert gilt). Beispiel: Logik 5 → max. Erhöhung um `⌈5/2⌉ = 3`, also Datenverarbeitung 5 → 8.
- Zusatzpunkte können jederzeit mit der Handlung *Matrixattribute austauschen* neu verteilt werden.
- **Matrixinitiative**: Initiativewert = `Datenverarbeitung + Intuition` plus die üblichen Initiativewürfel je nach Interfacemodus (S. 179).
- **Schwund**: Widerstand mit `Willenskraft + Logik`. Übersteigt der (widerstandene) Schadenswert des Schwunds die Resonanz, ist der Schaden Körperlich, sonst Betäubung.
- **Matrixschaden der Lebenden Persona** (S. 189, 3. Auflage/Errata): Kein eigener Matrix-Zustandsmonitor — Matrixschaden (meist Betäubung) läuft auf die normalen Zustandsmonitore des Technomancers. Ist der **Betäubungs-Zustandsmonitor voll**, wird der Technomancer aus der Matrix ausgeworfen (sofern keine *Linksperre*, S. 177) und erleidet in der Regel **Auswurfschock**.
- **Als Technomancer erkennbar** (S. 188): In der Matrix sind mindestens **5 Nettoerfolge** bei einer Matrixwahrnehmungsprobe (S. 183) nötig, um eine Lebende Persona als Technomancer zu identifizieren.
- **Komplexe Formen** bei Erschaffung: `Resonanz (Prioritätentabelle) × 2`. Zusätzliche Komplexe Formen kosten `5 Karma` (S. 72). Angriffswert für Komplexe Formen: `Elektronik + Resonanz`.
- **Dauerarten**: Sofort (S), Aufrechterhalten (A, `−2 Würfelpoolmalus` pro gleichzeitig aufrechterhaltener Komplexer Form auf jede Handlung), Permanent (P).

#### Komplexe Formen mit Schwund/Dauer-Werten (S. 189)

| Komplexe Form | Schwund | Dauer | Effekt-Formel |
|---|---|---|---|
| Editor | 3 | P | Wie *Datei editieren*, ohne nötige Zugangsstufe (Datei muss entdeckt sein) |
| [Matrixattribut]-Senkung | 4 | A | Vergleichende Probe Elektronik+Resonanz vs. Willenskraft+Firewall; `−1 Attribut pro Nettoerfolg` (min. 1) |
| [Matrixattribut]-Steigerung | 4 | A | Probe Elektronik+Resonanz (Schwellenwert 4); `+1 Attribut pro Nettoerfolg`, max. `2 × Ausgangswert` (max. jedoch `+4`) |
| Petze | 3 | P | Probe Elektronik+Resonanz; `+1 OW des Ziels pro Erfolg` |
| [Programm] emulieren | 0 | A | Zählt als eigenes Programm; als Autosoft max. Stufe = aktuelle Datenverarbeitung (max. 6) |
| Puppenspieler | 5 | A | Wie *Gerät steuern*, ohne nötige Zugangsstufe (Gerät muss entdeckt sein) |
| Reiniger | 2 | P | Probe Elektronik+Resonanz; `−1 eigener OW pro Erfolg` |

---

### Nicht erfasst

- **Sprites** (S. 191) und weiterführende Technomancer-Regeln (Wandlung, Echos, S. 195) liegen jenseits von Buchseite 189 und wurden hier nicht erfasst.
- Vollständige Statblöcke der Schutzgeister-Archetypen (S. 165–168) und der Standard-/Hacking-Programme (S. 184–185) wurden nur in ihrer allgemeinen Formel-Logik erfasst, nicht als vollständige Liste jedes Einzeleintrags.
- Autosofts, Agenten und weiterführende Matrix-Ausrüstungstabellen (falls jenseits S. 189 fortgesetzt) sind nicht enthalten.

---

## Teil 5: Komplexe Formen, Sprites, Riggen & Schergen (Buchseiten 190–219)

<sub>Quelle-Chunk: `docs/sr6/sr6_calc_p191-220.md` — Originaltitel: Shadowrun 6 – Regeln mit Berechnungen (Grundregelwerk, Buchseiten 190–219)</sub>

Quelle: Sub-PDF `sr6_p191-220.pdf` (physische PDF-Seiten 191–220 der deutschen Ausgabe), entsprechend den im Fußtext gedruckten Buchseiten **190–219** (Buchseite = PDF-Seite − 1 in diesem Abschnitt). Der Bereich deckt das Ende des Kapitels **MATRIX / TECHNOMANCER** (Sprites, Wandlung, Echos), das komplette Kapitel **RIGGEN** sowie den Anfang des Kapitels **DAS WILDE LEBEN** (Schergen/Professionalitätsstufe, Top-Runner, Connections, Critter) ab.

Buchseitenzahlen sind in Klammern angegeben, z. B. (S. 196).

---

### 1. Komplexe Formen – Schwund/Dauer (S. 190–191)

Fortsetzung der Komplexe-Formen-Liste aus dem Technomancer-Kapitel. Schwund-Werte werden gegen die Probe der jeweiligen Komplexen Form widerstanden (Mechanik s. S. 189, hier nicht erneut ausgeführt).

| Komplexe Form | Schwund | Dauer |
|---|---|---|
| Resonanzillusion | 4 | A |
| Resonanzkanal | 2 | A |
| Resonanznebel | 6 | S |
| Resonanzspike | 4 | S |
| Signalschleier | 3 | A |
| Signalsturm | 3 | A |
| Spiegelpersona | 3 | A |
| Zusammenflicken | 4 | P |

- **Resonanzillusion**: Vergleichende Probe `Elektronik + Resonanz` gegen `Intuition + Datenverarbeitung` des Ziels. Um die Illusion trotz Verdachts zu durchschauen, ist eine Matrixwahrnehmungsprobe mit Schwellenwert = Anzahl der Nettoerfolge nötig.
- **Resonanzkanal**: Probe `Elektronik + Resonanz`; jeder Erfolg senkt den Rauschenwert um 1.
- **Resonanznebel**: Einzelne Vergleichende Probe `Elektronik + Resonanz` gegen `Intuition + Datenverarbeitung` gleichzeitig gegen alle erkennenden Ziele; ein Ziel mit Nettoerfolgen nimmt den Nutzer nicht mehr wahr und braucht eine neue Matrixwahrnehmungsprobe zur Relokalisierung.
- **Resonanzspike**: Probe `Cracken + Resonanz` gegen `Willenskraft + Firewall` des Ziels; jeder Nettoerfolg verursacht 1 Kästchen Matrixschaden ohne Widerstandsmöglichkeit.
- **Signalschleier**: Vergleichende Probe `Elektronik + Resonanz` gegen `Willenskraft + Firewall` oder `Firewall × 2` des Hosts; solange aufrechterhalten steigt der Overwatch-Wert nicht durch illegalen Host-Zugriff (wohl aber weiterhin durch illegale Handlungen).
- **Signalsturm**: Vergleichende Probe `Elektronik + Resonanz` gegen `Logik + Datenverarbeitung`; jeder Nettoerfolg erhöht den Rauschenwert des Ziels um 1.
- **Spiegelpersona**: Probe `Elektronik + Resonanz`; die Matrixattributwerte der erschaffenen Zusatzpersona entsprechen der Erfolgszahl dieser Probe; dieselbe Zahl dient als Schwellenwert für fremde Matrixwahrnehmungsproben, um die Spiegelpersona vom Original zu unterscheiden. *(3. Auflage/Errata: Misslingt einem Gegner die Unterscheidungsprobe und wählt er die Spiegelpersona als Ziel seiner Matrixhandlungen, **endet die Komplexe Form**.)*
- **Zusammenflicken**: Probe `Elektronik + Resonanz`; jeder Erfolg repariert 1 Kästchen Matrixschaden (nur an Matrixobjekten, nicht an Hardware).

---

### 2. Sprites – Kompilieren, Registrieren, Dekompilieren (S. 191–192)

- **Kompilieren**: Haupthandlung, Vergleichende Probe `Tasken + Resonanz` gegen `Spritestufe × 2`. Die **maximale Stufe** eines kompilierbaren Sprites = `Resonanz × 2` (3. Auflage/Errata). Alle Nettoerfolge werden zu Aufgaben des Sprites. Nach dem Kompilieren widersteht das Sprite Schwund (S. 189) in Höhe der **Erfolge (nicht Nettoerfolge)** dieser Probe.
- Ein Technomancer kann nur **1 unregistriertes Sprite** gleichzeitig haben.
- **Lebenszeit unregistrierter Sprites**: `[Spritestufe × 2]` Stunden.
- **Registrieren**: Dauert `Spritestufe` Stunden (weder Technomancer noch Sprite können währenddessen andere Handlungen ausführen; OW steigt in dieser Zeit nicht). Am Ende: Vergleichende Probe `Tasken + Resonanz` gegen `Spritestufe × 2`. Schwund = `Erfolge × 2` (nicht Nettoerfolge × 2), **mindestens aber 2**. Bei ≥1 Nettoerfolg ist das Sprite registriert; Nettoerfolge werden zusätzlich zu den Aufgaben des Sprites addiert, und seine Lebenszeit ist danach unbegrenzt.
- **Maximale Anzahl registrierter Sprites** = `Resonanz` des Technomancers; zusätzlich darf er weiterhin 1 unregistriertes Sprite haben.
- **Dekompilieren**: Haupthandlung, Vergleichende Probe `Tasken + Resonanz` gegen `Spritestufe (+ Resonanz des kompilierenden Technomancers, falls registriert)`. Jeder Nettoerfolg entfernt eine offene Aufgabe des Sprites; sinkt die Zahl offener Aufgaben auf 0, ist das Sprite dekompiliert. Schwund = `Erfolge × 2` (nicht Nettoerfolge × 2), **mindestens aber 2**.
- **Aufgabe für registriertes Sprite – Komplexe Form aufrechterhalten**: Sprite kann für bis zu `[Spritestufe]` Kampfrunden eine Komplexe Form (inkl. Würfelpoolmalus) für den Technomancer aufrechterhalten.

#### Werte von Sprites (S. 192)

- Gerätestufe, Resonanz, **Geistige Attribute** und Fertigkeitswerte = Spritestufe (3. Auflage/Errata: Geistige Attribute werden **nicht** mehr über die Tabelle *Matrixattribute und Geistige Attribute*, S. 189, hergeleitet, sondern sind direkt gleich der Spritestufe).
- **Matrix-Zustandsmonitor** = `[8 + (Spritestufe ÷ 2, aufgerundet)]` Kästchen.
- Matrixattribute, Initiative und Matrix-Zustandsmonitor hängen von Art und Stufe des Sprites ab (s. *Arten von Sprites*).

#### Arten von Sprites – Matrixattribute (S. 193)

`S` = Spritestufe.

| Sprite-Typ | Angriff | Schleicher | Datenverarbeitung | Firewall | Initiative | Resonanz |
|---|---|---|---|---|---|---|
| Daten-Sprite | S−1 | S | S+4 | S+1 | (S×2)+4+4W6 | S |
| Infiltrator-Sprite | S | S+3 | S+2 | S+1 | (S×2)+2+4W6 | S |
| Kurier-Sprite | S | S+3 | S+1 | S+2 | (S×2)+1+4W6 | S |
| Maschinen-Sprite | S+1 | S | S+3 | S+2 | (S×2)+3+4W6 | S |
| Stör-Sprite | S+3 | S | S+1 | S+2 | (S×2)+1+4W6 | S |

---

### 3. Spritekräfte mit Zahlenwerten (S. 193–194)

- Sprites erleiden **keine** Würfelpoolmodifikatoren für das Aufrechterhalten einer Kraft (3. Auflage/Errata).

- **Cookie**: Vergleichende Probe `Cracken + Resonanz` gegen `Intuition + Firewall` des Ziels; Nettoerfolge = Informationstiefe des Trackings (1 Nettoerfolg = grobe Umrisse, 4+ = detaillierter Bericht).
- **Diagnose**: Probe `Elektronik + Resonanz`; bei Erfolg **pro Erfolg** `+1` Würfelpoolbonus für den unterstützten Charakter bei Benutzung (nur Fertigkeiten Elektronik, Mechanik, Steuern) oder Reparatur des Geräts (3. Auflage/Errata; früher pauschal +1).
- **Elektronensturm**: Vergleichende Probe `Cracken + Resonanz` gegen `Intuition + Firewall`; verursacht `[Resonanz]` Kästchen Matrixschaden pro Handlung (normal widerstanden) und erhöht den Rauschenwert des Ziels um 2.
- **Falle**: Probe `Cracken + Resonanz` gegen `Willenskraft + Firewall`; bei Erfolg kann das Ziel keine Handlungen ausführen, solange die Kraft aufrechterhalten wird.
- **Hash**: Maximale Wirkzeit = `[Spritestufe × 10]` Kampfrunden.
- **Übernehmen**: Vergleichende Probe `Elektronik + Resonanz` gegen `Gerätestufe + Firewall` des Geräts; bei Erfolg volle Kontrolle, Sprite nutzt seine eigene Spritestufe statt der Pilotstufe.
- **Unterdrücken**: Verzögert den Start von Host-IC um `[Spritestufe + 2]` Kampfrunden; verzögertes IC kann in dieser Zeit nicht handeln/Ziel von Handlungen sein.

---

### 4. Wandlung – Resonanzmaximum & Echos (S. 195)

- **Wandlungsgrad-Kosten**: `[10 + neuer Wandlungsgrad]` Karma (analog zur Initiation, vgl. bereits dokumentierte Entwicklungskosten-Tabelle S. 71–72).
- **Natürliches Maximum der Resonanz**: `6 + Wandlungsgrad`, reduziert um `−1 pro angefangenem verlorenen Essenzpunkt`. Eine Erhöhung dieses Maximums erhöht das Attribut nicht automatisch – Steigerung muss weiterhin mit Karma bezahlt werden.
- **Echos mit Zahlenwerten**:
  - Maschinenbeherrschung: Vorteile einer Riggerkontrolle **Stufe 1** (nur einmal wählbar).
  - Matrixattribut-Upgrade: `+1` auf ein Matrixattribut der Lebenden Persona pro Wahl; jedes Attribut maximal **2×** steigerbar.
  - Neurofilter: `+1 Würfelpoolbonus` gegen Biofeedback-Schaden pro Wahl; maximal **2×** wählbar (max. +2).
  - Übertakten: `+1W6` auf Initiative und `+1` zusätzliche Nebenhandlung (nur bei VR mit heißem Sim).

---

### 5. Riggen – Grundlagen (S. 196–197)

- **Zustandsmonitor von Fahrzeugen/Drohnen**: `[Rumpf ÷ 2, aufgerundet] + 8` Kästchen. Für je **3 ausgefüllte Schadenskästchen** steigt das Handling (S. 198) um `+1` (verschlechtert sich). Bei voll ausgefülltem Zustandsmonitor versagt das Gerät seinen Dienst.
- **Riggerkontrolle** (3. Auflage/Errata): Beim Hineinspringen senkt sie den Schwellenwert **aller Proben zum Betrieb des Fahrzeugs** (z. B. Steuern-Proben, Proben zum Abfeuern von Fahrzeugwaffen) um ihre **Stufe**, gewährt einen Würfelpoolbonus in Höhe ihrer **Stufe** sowie **1 Edge je Probe**. *(Frühere Fassung: „alle Proben, bei denen Steuern Teil des Pools ist".)*
- **Attributsubstitution beim Hineinspringen in VR** (Tabelle *Riggerkontrolle*, S. 197):

| Normales Attribut | Ersetzt durch (hineingesprungen, VR) |
|---|---|
| Konstitution | Willenskraft |
| Geschicklichkeit | Logik |
| Reaktion | Intuition |
| Stärke | Charisma |

- **Riggerkonsole**: Kann gleichzeitig mit `[Gerätestufe × 3]` Slave-Drohnen/-Geräten verbunden werden. Initiative beim Fernsteuern in VR über Riggerkonsole: `Datenverarbeitung + Intuition + 2W6/3W6` (kaltes/heißes Sim). Anzahl gemeinsam nutzbarer Autosofts/Programme für alle Slaves = unmodifiziertes **Datenverarbeitungsattribut** der Konsole. Rauschenmodifikatoren aller Slaves werden auf die **Gerätestufe** der Konsole gesenkt (geteilte Rauschenunterdrückung).
- **Auswurfschock**: Biofeedbackschaden `3B` (kaltes Sim) oder `3K` (heißes Sim), widerstanden mit Willenskraft; bei Schaden Status *Benommen* für `[10 − Willenskraft]` Minuten.

#### Riggerprogramme (S. 197–198)

| Programm | Effekt |
|---|---|
| Brandmauer | `+1` auf Firewall |
| Panzerung | `+2` Verteidigungswert gg. Matrixangriffe; `+2` Würfelpoolbonus auf Schadenswiderstandsproben des Riggers in der Matrix (bei heißem Sim) |
| Signalreiniger | Senkt Rauschenwert um `2` |
| Tarnkappe | Bei *Verstecken*: `+1` Edge-Punkt, muss sofort für dieselbe Handlung ausgegeben werden, sonst verfällt er |
| Toolbox | `+1` auf Datenverarbeitung |
| Virtuelle Maschine | `2` zusätzliche Programmslots; bei Angriffen `+1` zusätzliches Kästchen Matrixschaden ohne Widerstandsmöglichkeit |

---

### 6. Fahrzeugbewegung (S. 198–199)

- **Handling**: Schwellenwert für Steuern-Proben (getrennter Wert für Straße/Gelände bei Bodenfahrzeugen).
- **Geschwindigkeitsintervall-Malus**: Bei jedem neu erreichten Geschwindigkeitsintervall steigt der kumulative Würfelpoolmalus auf alle Handlingsproben und aus dem Fahrzeug heraus durchgeführte Angriffsproben um `−1`. Formel: `Würfelpoolmalus = −⌊Geschwindigkeit ÷ Geschwindigkeitsintervall⌋`. Beispiel: Intervall 20 → Malus −1 ab Geschwindigkeit 20, −2 ab 40 usw.
- **Bewegungsformel**: `Distanz pro Kampfrunde = Geschwindigkeit zu Rundenbeginn ± (Beschleunigungsrate ÷ 2)` (sofern in dieser Runde beschleunigt oder gebremst wird; ohne Beschleunigen/Bremsen legt das Fahrzeug einfach die aktuelle Geschwindigkeit in Metern zurück).
- **Geschwindigkeitsumrechnung**: `km/h = (m/Kampfrunde) × 1,2`.
- **Fahren und Proben**: Handlingprobe = `Steuern + Reaktion` (AR/manuell) bzw. `Steuern + Intuition` (VR hineingesprungen) gegen Schwellenwert = Handlingwert. Wettrennen zwischen Fahrern: Vergleichende Probe `Steuern + Reaktion` gegen `Steuern + Reaktion`, jeweils mit dem eigenen Geschwindigkeitsintervall-Malus.

#### Riggerhandlungen (S. 199)

| Handlung | Handlungsart | Wofür |
|---|---|---|
| Angriff | Haupt (I) | Angriff mit Fahrzeug/Fahrzeugwaffe |
| Drohne befehligen | Neben (I) | Befehl an eine/mehrere Drohnen |
| Fertigkeit einsetzen | Haupt (I) | Handling-Proben u. Ä. |
| Gerät neu starten | Haupt (I) | Auswerfen eines Hackers |
| Hineinspringen | Haupt (II) | Wechsel in ein Fahrzeug/eine Drohne |
| Interfacemodus wechseln | Neben (I) | Wechsel zwischen AR und VR |
| Matrixattribute austauschen | Neben (J) | Datenverarbeitung/Firewall der Riggerkonsole tauschen |
| Verstecken | Haupt (JJ) | Persona von Fahrzeug/Drohne verstecken |
| Volle Matrixabwehr | Haupt (JJ) | Verteidigung gegen Hacker |

#### Würfelpools und Werte für Rigger und ihre Fahrzeuge (S. 200, Fassung 3. Auflage/Errata — korrigiert & um *Heimlichkeit*/*Wahrnehmung* erweitert)

| Würfelpool/Wert | Manuelle/AR-Steuerung | Hineingesprungen (VR) † |
|---|---|---|
| Initiative | Reaktion + Intuition + 1W6 * | Intuition + Intuition + 2W6/3W6 (kaltes/heißes Sim) †† |
| Angriffswert | Steuern + Sensor | Steuern + Sensor |
| Verteidigungswert | Steuern + Panzerung | Steuern + Panzerung |
| Handlingprobe | Steuern + Reaktion * | Steuern ** + Intuition |
| Angriffsprobe (Fahrzeug als Waffe) | Steuern + Reaktion * | Steuern ** + Intuition |
| Angriffsprobe (Fahrzeugwaffe) | Mechanik + Logik | Mechanik ** + Logik |
| Verteidigungsprobe | Steuern + Reaktion * | Steuern ** + Intuition |
| Heimlichkeit | Heimlichkeit + Geschicklichkeit | Heimlichkeit ** + Logik |
| Wahrnehmung | Wahrnehmung + Intuition | Wahrnehmung ** + Sensor |
| Schadenswiderstandsprobe | Rumpf | Rumpf |
| Zustandsmonitor | [Rumpf ÷ 2, aufgerundet] + 8 Kästchen | [Rumpf ÷ 2, aufgerundet] + 8 Kästchen |

\* Bei manueller Steuerung gelten eventuelle Boni auf Reaktion und Initiative durch Bodytech.
\*\* zzgl. Stufe der Riggerkontrolle (in der 3. Auflage nur noch in der VR-Spalte und nicht mehr bei Angriffs-/Verteidigungswert).
† *Steuern in VR ohne Riggerkontrolle* ist nicht separat aufgeführt: gleiche Würfelpools wie „Hineingesprungen (VR)", aber ohne die Riggerkontrolle-Boni.
†† Nimmt Kabelverbindung an. Per WiFi hineingesprungen: Initiative = `Datenverarbeitung + Intuition + 2W6/3W6`.

---

### 7. Crashs (S. 200)

- Bei misslungener Handlingprobe: sofortige Crashprobe (`Steuern`, Schwellenwert = Handling), ohne dass der Fahrer dafür eine Handlung aufwendet. Derselbe Geschwindigkeitsintervall-Malus gilt; die Spielleitung kann weitere situative Mali verhängen.
- Misslingt die Crashprobe, crasht das Fahrzeug: alle Insassen legen eine Schadenswiderstandsprobe gegen `(Geschwindigkeit in m/Kampfrunde ÷ 10, aufgerundet)K` Schaden ab. Sicherheitsfeatures (Airbags, Sicherheitsschaum, Gurte) senken diesen Schaden.

---

### 8. Fahrzeugmodifikationen – Waffenhalterungen (S. 200)

- **Anzahl Standard-Waffenhalterungen** = `unmodifiziertes Rumpfattribut + 3` (abgerundet).
- Standard-Waffenhalterung: Waffe bis Größe eines Sturmgewehrs + 250 Schuss Munition.
- Schwere Waffenhalterung zählt als **2** Standard-Waffenhalterungen: beliebig große Waffe + Gurt mit bis zu 500 Schuss oder bis zu `[Rumpf]` (Lenk-)Raketen.
- Alle Halterungen sind fernsteuerbar und bestreichen horizontal/vertikal einen Winkel von 90 Grad; manuelle Steuerung ist nur bei Fahrzeugen (nicht Drohnen) und gegen Zusatzkosten nachrüstbar.

---

### 9. Fahrzeugkampf (S. 200–201)

- **Waffeneinsatz aus dem Fahrzeug heraus**: Geschwindigkeitsintervall-Würfelpoolmalus (Abschnitt 6) gilt zusätzlich zu normalen Fernkampfregeln. Fahrzeugmontierte Waffen: Probe `Mechanik + Logik`.
- **Nahkampfschaden gegen Fahrzeuge**:
  - Gegen stationäres Ziel: Schadenswert `+ aktuelles Geschwindigkeitsintervall`.
  - Zwei Fahrzeuge bewegen sich in dieselbe Richtung: Schadenswert `+ Differenz der Geschwindigkeitsintervalle` beider Fahrzeuge.
  - Fahrzeuge bewegen sich aufeinander zu: Schadenswert `+ Summe der Geschwindigkeitsintervalle` beider Fahrzeuge.
- **Angriffswert eines Fahrzeugs** = `Steuern (Fahrer) + Sensor`. **Verteidigungswert** anderer Fahrzeuge = `Steuern (Fahrer) + Panzerung`; Personen nutzen ihren normalen Verteidigungswert.
- **Rammschaden** = `(Rumpf ÷ 2, aufgerundet) + 1 pro erreichtem Geschwindigkeitsintervall` als `K`-Schaden. Rammt ein Fahrzeug ein anderes, widersteht dieses mit seinem eigenen Rumpfattribut (Insassen widerstehen wie bei einem Crash, Abschnitt 7). Rammt ein Fahrzeug eine Person, widersteht diese mit Konstitution; die Fahrzeuge selbst widerstehen Rammschaden stets mit ihrem Rumpfattribut.

---

### 10. Riggen von Drohnen (S. 201)

- Gerätestufe einer nicht als Slave verbundenen Drohne = ihre **Sensorstufe**.
- Eine Drohne kann so viele Autosofts/Matrixprogramme gleichzeitig nutzen, wie `[Pilotstufe ÷ 2, aufgerundet]` entspricht. Fehlt ein benötigtes Autosoft, wird das entsprechende Attribut `−1` (ungeübter Einsatz, vgl. S. 95) verwendet.
- **Initiative unabhängig agierender Drohnen** = `Pilot × 2 + 3W6`. Hineingesprungene Rigger nutzen ihre eigene VR-Initiative.

#### Würfelpools von autonomen Drohnen (S. 201)

| Wert | Berechnung |
|---|---|
| Angriffswert | Montierte Waffe bzw. Manövrieren + Sensor |
| Verteidigungswert | Manövrieren + Panzerung |
| Rigger-Initiative | Datenverarbeitung + Intuition + 2W6/3W6* |
| Drohnen-Initiative | Pilot × 2 + 3W6 |
| Angriffs-Würfelpool | [Waffe] Zielerfassung + Sensor |
| Verteidigungs-Würfelpool | Ausweichen + Pilot |
| Heimlichkeit | Stealth + Pilot |
| Wahrnehmung | Clearsight + Sensor |

\* Für Befehlserteilung (kaltes/heißes Sim) bzw. für in Drohnen hineingesprungene Rigger.
*(3. Auflage/Errata: Angriffswert nutzt jetzt **+ Sensor** statt + Pilot; Zeilen* Heimlichkeit *und* Wahrnehmung *ergänzt.)*

Autosoft-Attributzuordnung: Ausweichen → Pilot; Clearsight → Sensor; Elektronische Kriegsführung → Sensor; Manövrieren → Pilot; Stealth → Pilot; [Waffe] Zielerfassung → Sensor.

---

### 11. Schergen – Zustandsmonitor & Professionalitätsstufe (S. 203–204)

- **Zustandsmonitor eines Schergen** = `8 + (aufgerundete Hälfte von max(Konstitution, Willenskraft))` Kästchen (ein einziger Monitor für Körperlichen und Betäubungsschaden gemeinsam). Ein Anführer addiert zusätzlich seine **Professionalitätsstufe**.
- **Verletzungsmodifikatoren**: bereits alle **2 ausgefüllten Kästchen** (statt 3 wie bei Spielercharakteren) erhöhen den kumulativen Malus.
- Wird der Monitor durch den letzten Treffer mit Körperlichem Schaden komplett gefüllt, stirbt der Scherge; füllt ihn Betäubungsschaden, ist er nur bewusstlos.
- **Fluchtprobe pro Scherge**: Sobald erlittene Schadenskästchen `> Professionalitätsstufe`, Selbstbeherrschungsprobe (`Willenskraft + Charisma`, S. 37), um Flucht zu bestimmen.
- **Edge-Pool der Schergengruppe** = Professionalitätsstufe (als Startwert), geteilt von allen Schergen der Gruppe; unabhängig von Unterteilung in Trupps kann **nur ein Trupp pro Kampfrunde** Edge aus diesem Pool einsetzen.

#### Professionalitätsstufe – Rückzugsschwellen (S. 203)

| Stufe | Bezeichnung | Rückzugsschwelle der Gruppe |
|---|---|---|
| 0 | ungeübt | Verliert die Gruppe 1 Mitglied, flieht der Rest |
| 1–4 | erfahren | > 25 % Verluste → Kampfabbruch/Rückzug |
| 5–7 | Veteranen | > 50 % Verluste → taktischer Rückzug (Rückzugsgefecht) |
| 8–10 | Elite | Kein automatischer Rückzug (Kampf bis zum letzten Mann oder Rückzugsbefehl) |

#### Optionale Regeln „Mäht sie nieder“ (S. 203, empfohlen für Professionalitätsstufe < 3)

- Schergen würfeln ihre Initiative nicht aus, sondern nutzen direkt ihren Initiativewert als Initiativeergebnis.
- Eine einzige Wunde schaltet einen Schergen sofort aus.
- Alle Proben gegen Schergen sind Einfache Proben (kein Widerstandswurf); Zauber wirken ungehindert; Schergen würfeln nicht, um Fernkampfangriffen auszuweichen.
- Erzielt ein Spielercharakter ≥1 Erfolg bei einer Heimlichkeitsprobe, bemerken Schergen ihn automatisch nicht.

---

### 12. Top-Runner – Erschaffung nach Kategorie (S. 211)

Erschaffung basiert auf der Prioritätentabelle (S. 65), modifiziert nach Kategorie:

| Kategorie | Modifikator bei Erschaffung |
|---|---|
| Unterlegen | Nutzt in jeder Spalte den **nächstniedrigeren** Prioritäts-Eintrag (A→B, B→C, …); Ausnahme Priorität E (bereits niedrigste): Top-Runner erhält die E-Einträge in **zwei** Spalten |
| Gleichwertig | Erschaffung identisch zu Spielercharakteren (inkl. Individualisierungskarma); zusätzliches Karma zur Anpassung an den Entwicklungsstand der SC |
| Überlegen | Keine Ausrüstungsbegrenzungen der Charaktererschaffung (S. 69) |
| Übermenschlich | Keine Ausrüstungsbegrenzungen; Karmasteigerung „sehr viel mehr“ als bei SC |

- Karmasteigerung bei Weiterentwicklung: Überlegene Top-Runner `+50–100 %` mehr Karma als Spielercharaktere; Übermenschliche Top-Runner deutlich mehr.
- Top-Runner erhalten ein eigenes, individuelles Edge-Attribut (unabhängig vom geteilten Edge-Pool der Schergen).

---

### 13. Attributsmodifikatoren nach Metatyp (S. 212)

(Referenz-Tabelle zur Umwandlung menschlicher Connection-/NSC-Werte in andere Metatypen.)

| Metatyp | Modifikatoren |
|---|---|
| Zwerg | +1 Konstitution oder Willenskraft, +1 Stärke |
| Elf | +1 Geschicklichkeit, +1 Charisma |
| Ork | +1 Konstitution, +1 Stärke |
| Troll | +2 Konstitution oder Stärke, +1 auf den jeweils anderen der beiden Werte |

---

### 14. Critter – Formeln mit Zahlenwerten (S. 218–219)

- **Handlungen mächtiger Critter/Drachen** (3. Auflage/Errata): Bei mehreren Critter-Wertetabellen wurde die Handlungszahl von *1 Haupt* auf *2 Haupt* korrigiert — u. a. Zerberus (S. 219) und Gefiederte Schlange (S. 220) je „2 Haupt, 3 Neben", Östlicher Drache (S. 221) „2 Haupt, 4 Neben", Westlicher Drache (S. 221) „2 Haupt, 3 Neben".
- **Pechratte – Unglücksbringer** (einzigartige Kraft, Haupthandlung, Reichweite BF (F), Art M): Vergleichende Probe `Reaktion + Magie` gegen `Edge` des Ziels; bei Nettoerfolgen erhält das Ziel für `[Nettoerfolge]` Minuten den Nachteil *Unglück*.
- **Vampir – Magieattribut**: Magie-Anfangswert = `min(6, Essenz)` (der niedrigere der beiden Werte).

---

### Nicht erfasst

- Die Beschreibung der **Dracoformen (Drachen)** beginnt auf S. 219, wird aber inhaltlich erst auf den Folgeseiten (S. 220+, außerhalb dieses Extraktionsbereichs) fortgeführt und enthält dort ggf. eigene Statblock-/Attributformeln.
- Ausführliche NSC- und Connection-Statblöcke (z. B. Humanis-Schlägertyp, Yakuza-Klingenmeister, Barkeeper, Mechaniker, Mr Johnson, Schieber, kompletter Critter-Katalog S. 216–219) wurden absichtlich **nicht** als Stat-Prosa transkribiert – nur generische Formeln/Schwellen wurden extrahiert (siehe Abschnitte 11 und 14). Waffenschaden-/Rüstungscodes einzelner NSC sind Ausrüstungswerte aus Kapitel *Ausrüstung* und hier nicht neu hergeleitet.

---

## Teil 6: Critter, Spielleiterhinweise & Ausrüstung I (Buchseiten 220–249)

<sub>Quelle-Chunk: `docs/sr6/sr6_calc_p221-250.md` — Originaltitel: Shadowrun 6 – Regeln mit Berechnungen (Grundregelwerk, Buchseiten 220–249)</sub>

Quelle: `Shadowrun_6_Grundregelwerk.pdf` (deutsche Ausgabe, Pegasus Spiele), Sub-PDF mit physischen PDF-Seiten 221–250, entsprechend den im Fuß der Seiten gedruckten Buchseiten **220–249**.

Abgedeckte Kapitel: Ende **Critterkräfte** und **Schwächen** (Kapitel *Das wilde Leben*), das komplette Kapitel **Spielleiterhinweise** bis einschließlich *Belohnungen für Runs*, und der Beginn des Kapitels **Ausrüstung** (Ausrüstungswerte, Verfügbarkeit, Kauf/Verkauf, Nahkampfwaffen).

Buchseitenzahlen sind in Klammern angegeben, z. B. (S. 222).

---

### 1. Critterkräfte – Rahmenkonzepte (S. 221)

- Jede Critterkraft wird durch vier Charakteristika beschrieben: **Art** (M = Manakraft, P = Physische Kraft), **Handlung** (H = Haupt-, N = Nebenhandlung, oder „Auto“ = passiv/immer aktiv), **Reichweite** (BF = Blickfeld, B = Berührung, Selbst) und **Dauer** (Sofort, Aufrechterhalten, Permanent, Immer, Speziell).
- **Manakräfte (M)** wirken nicht auf unbelebte Ziele; **Physische Kräfte (P)** wirken nicht im Astralraum bzw. gegen astrale Gestalten.
- **Aufrechterhalten-Limit**: Ein Critter kann gleichzeitig eine Anzahl Kräfte aufrechterhalten (auch dieselbe Kraft mehrfach), die `seinem Magieattribut entspricht`. Ausnahme: die Kraft *Natürlicher Zauberspruch* folgt den Hexereiregeln (S. 134) und erlaubt das gleichzeitige Aufrechterhalten mehrerer Zauber.
- Kräfte mit Dauer „Aufrechterhalten“ erleiden **keinen** Würfelpoolmalus fürs Aufrechterhalten (im Gegensatz zu Zauberern).

---

### 2. Critterkräfte – Formeln nach Kraft (S. 222–227)

Alle Werte skalieren mit dem **Magieattribut** des jeweiligen Critters (aus dem individuellen Statblock).

- **Ätzender Speichel** (S. 222): Fernkampfangriffsprobe `Geschicklichkeit + Magie`. Schaden `(Magie)K` (Chemisch). Angriffswerte für die 5 Reichweiten: `Magie×2 / (Magie×2)−2 / (Magie×2)−8 / (Magie×2)−10 / –`. Sinkt ein Angriffswert auf 0, erreicht die Kraft diese Reichweite nicht.
- **Bewegung** (S. 222, Fassung 3. Auflage/Errata): Der Critter kann die Bewegungsrate eines beweglichen Ziels (Fahrzeug, Charakter, Critter) mit einem Wert **bis zu seinem Magieattribut multiplizieren** (Division entfällt). Gegen Lebewesen, die nicht beeinflusst werden wollen: Vergleichende Probe `Willenskraft + Magie` gegen `Willenskraft + Logik`; gelingt sie, erhält das Ziel für `[Nettoerfolge des Critters]` Runden den Status **Humpelnd** (S. 54). Gegen Fahrzeuge: Probe `Willenskraft + Magie`, Schwellenwert = `Rumpf des Fahrzeugs ÷ 2, aufgerundet, mindestens 2`; Nettoerfolge × Beschleunigung werden der Fahrzeuggeschwindigkeit in der nächsten Kampfrunde zu-/abgerechnet. *(Frühere Fassung: freier Multiplikator/Divisor = Nettoerfolge bzw. Magie.)*
- **Bindung** (S. 222): Angriffsprobe `Geschicklichkeit + Magie` gegen `Athletik + Reaktion` (Reichweite BF) bzw. gegen `Nahkampf + Reaktion` (Reichweite Berührung) → Status *Bewegungsunfähig*. Befreiung: Probe `Konstitution + Stärke` gegen `Willenskraft + Magie` des Critters. Für Mitbewegen des Opfers benötigt der Critter mindestens `halbe Konstitution des Opfers` an Stärke.
- **Einfluss** (S. 223): Vergleichende Probe `Charisma + Magie` (Critter) gegen `Willenskraft + Logik` (Opfer). Überwinden der Suggestion: Probe `Willenskraft + Logik` gegen Magie des Critters; Nettoerfolge = Würfelpoolmalus auf die erzwungene Handlung. Ladehemmung durch Willenskraftprobe: `4 Edge` zum Abziehen vom Würfelpool, `5 Edge` um ein Ereignis herbeizuführen.
- **Elementarer Angriff** (S. 223): Fernkampfangriffsprobe `Geschicklichkeit + Magie`. Schaden `(Magie)K` (Elektrizität/Feuer/Chemie/Kälte). Angriffswerte für die 5 Reichweiten: `Magie×2 / (Magie×2)−2 / (Magie×2)−8 / 10 / –`.
- **Energieaura** (S. 223): erhöht Schaden jedes eigenen Nahkampfangriffs um `Magieattribut ÷ 2, aufgerundet`. Berührt ein Gegner den Critter waffenlos, erleidet er selbst Schaden: Schadenswiderstandsprobe gegen `(Magie des Critters)K`.
- **Essenzentzug** (S. 223): Ausgedehnte Probe `Charisma + Magie`, Schwellenwert `10 − Essenz des Opfers`, Intervall 1 Minute. Critter kann seine Essenz maximal auf `2× natürliches Maximum` steigern. Nebenhandlung: 1 entzogener Essenzpunkt kann `+1` in ein Körperliches/Geistiges Attribut oder die Magie gepumpt werden (max. `+4` pro Attribut), Effekt hält 12 Stunden.
- **Gift** (S. 224): Toxin – Vektor Injektion, Geschwindigkeit 1 Kampfrunde, Kraft `= Magie`, Wirkung Benommen + Vergiftet `(Magie)K`.
- **Gifthauch** (S. 224): Sprühangriffsprobe `Geschicklichkeit + Magie`, Angriffswerte `Magie×2 / Magie / – / – / –`. Giftangriff: Vektor Inhalation, Geschwindigkeit Sofort, Kraft `= Magie`, Wirkung Betäubungsschaden + Benommen + Übelkeit.
- **Grauen** (S. 224): Vergleichende Probe `Willenskraft + Magie` (Critter) gegen `Willenskraft + Logik` (Opfer). Status hält `1 Kampfrunde pro Nettoerfolg` des Critters, doppelt so lang wie der zugrundeliegende Status. Danach: Probe `Willenskraft + Logik`, Schwellenwert `= halbe Magie des Critters, aufgerundet`, sonst wirkt das Grauen erneut.
- **Lähmende Berührung** (S. 224): wie *Lähmendes Heulen*, aber per Berührung; automatisch erfolgreich bei überraschten/wehrlosen Opfern, sonst Vergleichende Probe `Geschicklichkeit + Magie` gegen `Reaktion + Willenskraft` des Opfers.
- **Lähmendes Heulen** (S. 225): Radius `Magie × 15` Meter. Vergleichende Probe `Charisma + Magie` gegen `Willenskraft + Intuition` des Opfers. Gewinnt der Critter mit `≥4 Nettoerfolgen` → Status *Erstarrt*, sonst bei jedem Gewinn → *Bewegungsunfähig*.
- **Materialisierung** (S. 225): Solange materialisiert, Immunität gegen Normale Waffen (wie S. 224 *Immunität*).
- **Natürliche Waffe** (S. 225): Schadenswert i. d. R. `Stärke + 2` (sofern nicht individuell anders angegeben).
- **Natürlicher Zauberspruch** (S. 225): normaler Entzug plus `Würfelpoolmalus −2`, wenn aufrechterhalten.
- **Nebelgestalt** (S. 225): Bewegungsrate `5 Meter pro Bewegungshandlung` (≈ `6 km/h`).
- **Psychokinese** (S. 226): Stärke/Geschicklichkeit der „Hand“ = Erfolge der Probe `Willenskraft + Magie`; Bewegungsrate bis `10 Meter/Kampfrunde`.
- **Regeneration** (S. 226): am Ende jeder Kampfrunde Probe `Konstitution + Magie`; heilt Kästchen = Erfolge (zuerst Überzähliger, dann Körperlicher, dann Betäubungsschaden). Übersteigt der Überzählige Schaden `Konstitution × 2`, ist der Critter endgültig tot. **Nicht** regenerierbar (3. Auflage/Errata): Gehirnschaden durch einen angesagten Kopfschuss (*Ziel ansagen*, S. 44, oder *Angesagtes Ziel – Lebenswichtige Organe*, S. 48), magischer Schaden durch Waffenfoki, Schaden durch eine *Verwundbarkeit* sowie Schaden durch Entzug. Bei Schaden durch ein Allergen darf die Regenerationsprobe erst abgelegt werden, wenn der Kontakt zum Allergen endet.
- **Suche** (S. 226): Ausgedehnte Probe `Intuition + Magie`, Basis-Schwellenwert 5, Intervall 10 Minuten, modifiziert nach Tabelle *Suchmodifikatoren* (s. u.).
- **Tierbeherrschung** (S. 226): Befehle bleiben gültig für `Charismaattribut` Minuten. Gleichzeitig beherrschbar: kleine Tiere bis `Charisma × 5`, größere Tiere bis `Charisma` (1:1), oder ein einzelnes paranormales Tier.
- **Unfall** (S. 227): Vergleichende Probe `Willenskraft + Magie` (Critter) gegen `Reaktion + Charisma` (Opfer). Gewinnt der Critter mit `≥4 Nettoerfolgen`, wird das Ereignis wie ein *Kritischer* Patzer des Opfers behandelt (statt normalem Patzer).
- **Verschleierung** (S. 227): Status *Unsichtbar (Verbessert)* in Höhe `Magieattribut`. Gleichzeitig verschleierbare Ziele: `Magieattribut` (Konstitution ≤5 zählt als 1 Ziel, >5 als 2 Ziele), oder sehr viel kleinere Objekte bis `Magieattribut × 5`.
- **Verschlingen** (S. 227): Nahkampfangriff, Schadenswert `(Magie)K`; Nettoerfolge erhöhen den Schaden wie üblich, Opfer wird zusätzlich *Bewegungsunfähig*. Befreiung: Vergleichende Probe `Athletik + Stärke` gegen `Konstitution + Magie` des Critters. Elementvarianten: Erde `(Magie+2)K` (+ Status *Erschöpft I*); Feuer `(Magie+2)K` (+ Status *Brennend*, 1 weitere Kampfrunde); Luft `(Magie+2)B` (+ *Erschöpft I*, Betäubung überfließt bei Bewusstlosigkeit in Körperlich); Wasser `(Magie+2)B` (+ *Nass* + *Erschöpft I*, gleiches Überfließen).
- **Versteinerung** (S. 228): Vergleichende Probe `Intuition + Magie` gegen `Reaktion + Willenskraft` des Opfers. Gewinnt der Critter → *Bewegungsunfähig*; bei `≥4 Nettoerfolgen` (auch kumuliert über mehrere Angriffe) → *Versteinert*.
- **Verwirrung** (S. 228): Vergleichende Probe `Willenskraft + Magie` gegen `Willenskraft + Logik`. Nettoerfolge des Critters = Stufe des Status *Verwirrt*, zusätzlich Status *Benommen*.
- **Wetterbeherrschung** (S. 228): Ausgedehnte Probe `Willenskraft + Magie`, Schwellenwert 10, Intervall 30 Minuten.
- **Zwang** (S. 228): Vergleichende Probe `Charisma + Magie` gegen `Willenskraft + Logik`.

#### Suchmodifikatoren (S. 226)

| Umstand | Schwellenwert-Modifikator |
|---|---|
| Entfernung | `+1 pro km` |
| Hinter einem Hüter | `+(Kraftstufe des Hüters × 5)` |
| Kraft Verschleierung aktiv | `+(Magie des Verschleiernden × 3)` |
| Unbelebter Gegenstand oder Ort | `+5` |

---

### 3. Schwächen (S. 228–229)

- **Allergie**: regeltechnisch identisch zum Nachteil *Allergie* (S. 78).
- **Essenzverlust**: `−1 Essenzpunkt pro Monat`, jeweils bei Neumond. Sinkt die Essenz auf 0, stirbt der Critter nach `(Konstitution + Willenskraft) Tagen` ohne Essenz-Auffrischung. Jede Anwendung einer nicht-automatischen Critterkraft (also einer, die eine Handlung erfordert) beschleunigt den Essenzverlust um `1 Woche`.
- **Nahrungsbedarf**: An jedem Tag ohne Deckung des Nahrungsbedarfs kumulativer `Würfelpoolmalus −2` auf alle Handlungen, und Konstitution sinkt um `1`. Fällt Konstitution auf 0, stirbt der Critter.
- **Ungebildet**: regeltechnisch identisch zum Nachteil *Ungebildet* (S. 81).
- **Verwundbarkeit**: Schadenswert von Angriffen mit der verwundbarkeitsauslösenden Substanz erhöht sich um `Magieattribut des Critters` oder `+3` (der höhere Wert). Bei der Widerstandsprobe gegen eine *Bedingung* (statt Substanz) als Verwundbarkeit: `Würfelpoolmalus −3` oder `−Magieattribut` (der höhere Wert).
- **Geschwächte Sinne**: betroffene Sinne funktionieren typischerweise nur noch mit `halber Reichweite/Effektivität`, in Einzelfällen weiter abgeschwächt bis zum Totalausfall.

---

### 4. Patzer und Kritische Patzer – numerische Eckwerte der Ideentabelle (S. 232–234)

Die *Ideen-für-Patzer*-Tabelle ist primär eine Inspirationsliste für die Spielleitung (kein systemisches Regelwerk), enthält aber einige feste Zahlenwerte, die als Richtwerte für Patzerfolgen dienen:

- **Nahkampf-Kritischer Patzer**: Waffe zerbricht → nur noch `halber Schadenswert, abgerundet`.
- **Fahr-Kritischer Patzer** (Reparatur nach gelungener Ausgedehnter Probe `Mechanik + Logik`, Schwellenwert 10, Intervall 1 Tag): Standardreparatur kostet `20 % des Fahrzeugpreises`; eine zerschmetterte Windschutzscheibe allein kostet `5 % des Fahrzeugpreises`.
- Schwere Fahrpatzer verweisen auf die *Crashprobe* (S. 200), deren Schwellenwert der aktuellen Fahrzeuggeschwindigkeit entspricht.

---

### 5. Reputation (S. 235)

- Reputation ist ein positiver oder negativer Zahlenwert, der unmittelbar nach relevanten Aktionen angepasst wird (Richtlinien in der Tabelle unten, mit Ermessensspielraum der Spielleitung).
- **Edge-Auswirkung**: Reputation `≥ +10` gewährt `1 Punkt zusätzliches Edge` zu Beginn sozialer Interaktionen mit abgebrühten Kriminellen (organisiert oder nicht); abgebrühte Kriminelle erhalten dabei ebenfalls `1 Edge`. Reputation `≤ −10` kehrt das um: Gesetzeshüter, brave Bürger und andere Runner erhalten `1 Edge` zu Beginn der Interaktion, während der Runner zusätzlich `1 Edge` erhält, wenn er es mit abgebrühten Kriminellen zu tun hat.

#### Änderungen der Reputation (S. 235)

| Aktion | Reputationsänderung |
|---|---|
| An gewaltsamer Auseinandersetzung in der Öffentlichkeit beteiligt, ein Unbeteiligter kommt zu Tode | −1 |
| An gewaltsamer Auseinandersetzung in der Öffentlichkeit beteiligt, mehrere Unbeteiligte kommen zu Tode | −3 |
| Tötet Polizisten und wird dabei gesehen | −2 |
| Hat Leuten in Not Schaden zugefügt | −1 |
| Hat eine unschuldige Person entführt oder gefoltert | −1 |
| Hat einen Deal mit Mr Johnson nicht eingehalten | −1 |
| Hat verletzten Passanten Erste Hilfe geleistet und wurde dabei gesehen | +1 |
| Hat einen Teil seines Geldes Unterprivilegierten überlassen | +1 |
| Hat bei der Arbeit für nicht reiche, aber mächtige Leute Preisnachlass gewährt | +1 |
| Hat ein altes Versprechen eingelöst, ohne Geld dafür zu nehmen | +1 |
| Hat eine potenziell gewalttätige Situation entschärft | +1 |
| Hat eine beliebte berühmte Person aus der Not gerettet | +2 |

---

### 6. Fahndungsstufe (S. 235–237)

- **Probe am Sitzungsende**: Die Spielleitung wirft `2W6`. Bei einem (modifizierten) Ergebnis von `9` oder mehr erhöht sich die Fahndungsstufe aller Runner um `1`; bei `15` oder mehr um `2`.
- **Gesamtmodifikator**: Summe der Modifikatoren aus der Tabelle unten wird zum Würfelergebnis addiert. Beträgt der Fahndungsstufen-Gesamtmodifikator `−4` oder niedriger, entfällt der Wurf (die Fahndungsstufe steigt nicht) und jeder Runner erhält stattdessen `+1 Reputation`.

#### Fahndungsstufen-Modifikatoren (S. 236)

| Steigernder Umstand | Modifikator |
|---|---|
| Exzessive Gewalt in der Spielsitzung | +1 |
| Mord in der Spielsitzung | +1 |
| Feindseliger Kontakt mit reichen/prominenten Individuen | +1 |
| Direkter Kontakt mit einem erwachsenen Drachen | +1 |
| Direkter Kontakt mit einem Großen Drachen | +2 |
| Medienberichte (inkl. Matrixstream) über Runneraktivitäten | +1 |
| Team hat Runner mit Reputation > +10 oder < −10 | +1 |

| Senkender Umstand | Modifikator |
|---|---|
| Illegale Aktivitäten ohne Aufmerksamkeit zu erregen | −1 |
| Mr Johnson vertuscht Aspekte des Runs | −1 |
| Ausreichend Bestechungsgelder gezahlt | −1 |
| Connection bei der Polizei gewonnen/genutzt, um Spuren zu verwischen | −1 |
| Genug Wohlwollen, um Beteiligung unwahrscheinlich erscheinen zu lassen | −1 |
| Team hat Runner mit Reputation > −5 und keinen mit Reputation > +5 | −1 |

#### Auswirkungen der Fahndungsstufe (S. 236)

| Fahndungsstufe | Auswirkung |
|---|---|
| 0–3 | Keine Auswirkungen |
| 4–6 | Reaktionszeiten der Polizei um `25 %` verringert |
| 7–9 | Reaktionszeiten der Polizei um `50 %` verringert |
| 10 | SIN mit der niedrigsten Stufe der Runner gilt als verbrannt; als kriminell im System erfasst, löst bei Nutzung Alarm aus |
| 11–13 | Zwei zusätzliche Gesetzeshüter pro Einsatz mit Runner-Bezug |
| 14–16 | Runner auf Meistgesuchten-Liste eines Polizeikonzerns/der Großen Zehn/einer einflussreichen Nation; Verfolgung ggf. über nationale/interkorporative Grenzen |
| 17+ | Fahndungsdruck wird an eine Eliteeinheit übertragen (z. B. Rote Samurai, Sioux Wildcats); Verfolgung über alle Grenzen hinweg |

#### Fahndungsstufe senken (S. 236–237)

- **Beziehungen spielen lassen**: benötigt Connection (Polizeiorganisation/Sicherheitskonzern) mit Einflussstufe `≥3`. Kostet die Loyalitätsstufe der Connection `−1` und senkt die Fahndungsstufe um `2`. Jeder Teamgefährte, der den Vorteil ebenfalls nutzen will, zahlt selbst `−1 Loyalitätsstufe` der Connection.
- **Schmiergeld zahlen**: `1.000 Nuyen` senken die Fahndungsstufe eines Runners um `1`; jeder weitere Runner oder jede weitere Senkung kostet erneut `1.000 Nuyen`.
- **Untertauchen**: pro Monat (im Shadowrun-Universum) ohne Schattenjobs sinkt die Fahndungsstufe um `1`. Maximale Senkung auf diesem Weg: `3` innerhalb eines Jahres.
- **Einen Sündenbock finden**: erfordert diverse Proben (Überreden u. a.) und mindestens `3 Monate` Zeit.
- Sinkt die Fahndungsstufe durch diese Maßnahmen exakt auf `10`, löst der zugehörige Effekt (verbrannte SIN) sich nicht erneut aus; erst ein erneuter Anstieg von `9` auf `10` löst ihn wieder aus.

#### Fahndungsstufe für Fortgeschrittene (S. 237)

- Optional: statt eines einzelnen Werts können mehrere Fahndungsstufen je Organisation/Kategorie (Polizeikonzern, Verbrechersyndikat, Konzern, Region, Nation) geführt werden.
- Bei mehrfachen Fahndungsstufen sollten die Stufen-Schwellen der Tabelle *Auswirkungen der Fahndungsstufe* verkleinert werden, z. B. `1–3/4–6/…` → `1–2/3–4/…` oder enger.

---

### 7. Sicherheitszonen und ihre Stufen (S. 238–240)

Sicherheitsstufen (Z bis AAA) geben grobe Richtwerte für Reaktionszeiten, magische/Matrix-Überwachung und typische Wachtrupps (mit **Professionalitätsstufe**) je Zone.

| Zone | Polizei-/Sicherheitsreaktion | Magie- & Matrixüberwachung | Typische Trupps (Professionalitätsstufe) |
|---|---|---|---|
| Z | Keine | Keine | Keine |
| E | Praktisch keine; reagiert nur auf Notrufe von Personen mit gültiger SIN | Keine | 2 Streifenpolizisten (Stufe 3) **oder** 5–6 Gangmitglieder (Stufe 1) + 1 Anführer |
| D | ~2 Streifen/Tag, oberflächlich; Reaktion binnen 20 Min. | Wenig bis keine | 2 Streifenpolizisten (Stufe 3) **oder** 4 Gangmitglieder (Stufe 1) + 1 Anführer |
| C | Reaktion binnen 15 Min. | Geister Kraftstufe 2–3 (bei gewalttätiger Magie); Spinnen Stufe 3 (Distanz-Hacking-Ermittlung) | 4 Streifenpolizisten + 1 Anführer (Stufe 3) **oder** 3 Mitglieder krimineller Organisation (Stufe 4) |
| B | Vor-Ort-Sicherheit 24/7; Verstärkung binnen 10 Min. | 2 Geister Kraftstufe 4; Spinnen Stufe 4 (regelmäßige Matrixkontrolle) | 4 Streifenpolizisten/Sicherheitsleute + 1 Anführer vor Ort (Stufe 3); 4 weitere Polizisten (Stufe 3) + 2 SWAT (Sonderteinsatz); 5 Mitglieder krimineller Organisation + 1 Anführer |
| A | Patrouillen alle 5 Min. | Geister Kraftstufe 4–5, Drohnen Gerätestufe 4–5 (gelegentlich) | 6 Streifenpolizisten/Sicherheitsleute + 2 Anführer (Stufe 3); 4 SWAT + 1 Anführer (Stufe 5), mehrere Teams; 6 Mitglieder krimineller Organisation + 2 Anführer (Stufe 4) |
| AA | Patrouillen alle 5 Min.; magische Barrieren | 2 Geister Kraftstufe 5–6, Drohnen Gerätestufe 5–6 | 4 Elite-Konzernsicherheitsleute + 1 Anführer (Stufe 7); 6 SWAT + 2 Anführer (Stufe 5), mehrere Teams; 8 Mitglieder krimineller Organisation + 4 Anführer (Stufe 4) |
| AAA | Ständige Überwachung; magische + physische Barrieren | Geister Kraftstufe 6+, Drohnen Gerätestufe 6+, beste Spinnen mit GOD verbunden | 8 Elite-Konzernsicherheitsleute + 2 Anführer (Stufe 9–10); 4 Mitglieder Spezialeinheiten + 2 Anführer (Stufe 9–10), mehrere Teams |

---

### 8. Verschlossene Türen und Mechanismen (S. 240–241)

- **Türen/Fenster – Strukturstufe**: Türen ab `5` (bessere Wohngegenden/Büros `7–9`); Glas ab `2` normal, `9–11` bei besonders schützenswertem Inhalt. Fenster ab Strukturstufe `4` haben reflektierende, zauberblockierende Beschichtung.
- **Standardschlösser**: Dietrich-Set + Probe `Mechanik + Geschicklichkeit`, Schwellenwert = Stufe des Schlosses. Automatischer Dietrich gibt `+1 Würfel`.
- **Transponderschlüssel**: Elektronik-Werkzeugkiste + Probe `Mechanik + Geschicklichkeit`, Schwellenwert = Schlossstufe.
- **Magschlösser**: Gehäuse aufbrechen = Ausgedehnte Probe `Mechanik + Geschicklichkeit`, Schwellenwert `Schlossstufe × 2`, Intervall 1 Kampfrunde. Alternativ: Struktur aufbrechen, Strukturstufe = `Schlossstufe × 2`.
- **Tastatur-Magschloss**: Ausgedehnte Probe `Mechanik + Geschicklichkeit`, Schwellenwert `Schlossstufe × 2`, Intervall 1 Kampfrunde — oder Sequencer: Vergleichende Probe Sequencer-Stufe gegen Schlossstufe.
- **Kartenleser-Magschloss**: wie Tastatur, alternativ Magschlossknacker (S. 279): Vergleichende Probe Magschlossknacker-Stufe gegen Schlossstufe.
- **Biometrische Scanner**: Fälschen erfordert passendes Kopie-Gadget (Abdruckhandschuh, Retinaduplikat, Stimmenmodulator o. ä.) plus Ausgedehnte Probe `Biotech + Logik`, Schwellenwert 5, Intervall 1 Stunde (chemisches Bad zur Konservierung nötig für Fingerabdrücke). Für Gesichtsscanner: Vergleichende Probe `Überreden + Charisma` gegen Gerätestufe des Scanners (mit Make-up/Verkleidungs-Set); bei magischer Verkleidung zählt Erfolg der Hexereiprobe als Schwellenwert mit Gerätestufe als Vergleichswert.

---

### 9. Sensoren und Scanner (S. 241–243)

- **Alarmanlagen umgehen**: Ausgedehnte Probe `Mechanik + Geschicklichkeit`, Schwellenwert 5, Intervall 1 Minute.
- **Stolperdraht**: Wahrnehmungsprobe (`Wahrnehmung + Intuition`) gegen Schwellenwert `1` (normaler Draht), `2` (elektrifiziert), `3` (Monodraht), um ihn zu bemerken. Schaden bei Berührung: Stacheldraht `2K`, elektrifizierter Draht `3B(e)`, Monodraht `4K`.
- **Lichtschranken**: Probe `Wahrnehmung + Intuition`, Schwellenwert `2` (sichtbares Licht) bzw. `3` (Infrarot); Rauch/Aerosolspray senkt den Schwellenwert auf `1`. Überwindung per Laseremitter: Probe `Athletik + Geschicklichkeit` gegen vom SL festgelegten Schwellenwert. Spiegelsystem-Muster finden: Probe `Mechanik + Logik`, Schwellenwert 3; danach pro Spiegel Probe `Athletik + Geschicklichkeit`, Schwellenwert 3.
- **Druckpolster/-geflecht**: Wahrnehmungsprobe Schwellenwert `3` (Polster) bzw. `4` (Geflecht); nach Betreten sinkt der Schwellenwert auf `2`. Gewicht zurücknehmen, bevor Auslöseschwelle überschritten wird: Probe `Reaktion + Intuition`, Schwellenwert 3, mit Konstitution des Charakters als Widerstand.
- **Bewegungsmelder**: Ultraschallfeld erkennt Bewegung bis `5 Meter` Entfernung. Überwinden: Probe `Heimlichkeit + Geschicklichkeit`, Schwellenwert 3 (mit halber Bewegungsrate); Schnelligkeitsmodifikatoren geben zusätzlich Würfelpoolmalus in Höhe der zusätzlichen Initiativewürfel.
- **Schall-/Vibrationsdetektoren**: Probe `Heimlichkeit + Geschicklichkeit`, Schwellenwert 3.
- **Überwachungskameras**: kleine/verborgene Mikrokameras entdecken via `Wahrnehmung + Intuition`, Schwellenwert 3 (höher, wenn gut versteckt).
- **Geruchsscanner/Chemsniffer**: Würfelpool = Stufe des Geräts, gegen Schwellenwert `2` (bzw. `3`, wenn Sprengstoff/Munition hermetisch versiegelt ist), modifiziert nach Tabelle unten.
- **Pheromonscanner**: Gerätestufe als Würfelpool gegen Schwellenwert `3` (`2` bei maßgeschneiderten Pheromonen).
- **MAD (Magnetanomaliedetektoren)**: Probe mit Gerätestufe als Würfelpool; `1 Erfolg` reicht zur Erkennung metallischer/eisenhaltiger Objekte.
- **Millimeterwellen-/Cyberwarescanner**: identifizieren durch dicke Kleidung bis `15 Meter` Entfernung. Würfelpool = Gerätestufe, verglichen mit Schwellenwerten aus der Tabelle *Cyberwarescanner* (unten), modifiziert nach Anzahl der Implantate/Gegenstände.
- **Induktionsmelder**: erkennen elektrische Ladung metamenschlicher/tierischer Körper innerhalb `2 Metern`.

#### Modifikatoren für Chemische Detektoren (S. 243)

| Situation | Würfelpool-Modifikator |
|---|---|
| Pro 10 Schuss Munition | +1 |
| Pro Granate | +1 |
| Pro 2 Stufen Standard-(Nichtplastik-)Sprengstoff | +1 |
| Pro 4 Stufen Plastiksprengstoff | +1 |
| Sprengstoff/Munition in geschlossenem Plastikbehälter | −1 |

#### Cyberwarescanner (S. 243)

| Gegenstand | Schwellenwert |
|---|---|
| Standard-Cyberware, Waffen | 1 |
| Alphaware, andere Gegenstände | 2 |
| Betaware | 3 |
| Deltaware | 5 |

| Situation | Schwellenwert-Modifikator |
|---|---|
| 1 oder 2 Implantate/Gegenstände | +3 |
| 3 oder 4 Implantate/Gegenstände | +2 |
| 5 oder 6 Implantate/Gegenstände | +1 |
| 7+ Implantate/Gegenstände | — |

---

### 10. Belohnungen für Runs (S. 243)

- **Karma**: Richtwert `5 Karma` — entspricht dem Multiplikator pro Stufe bei Verbesserungskosten (siehe Teil 1, Abschnitt 12). Als Sitzungsrichtlinie: `1–2 Karma` bei geringem Fortschritt, `3–4 Karma` bei wichtigen Schritten/guter Leistung, `5 Karma` bei gutem Job, bis `6 Karma` bei hervorragender Leistung.
- **Geld**: Richtwert für finanzielle Entschädigung pro Run `5.000 Nuyen` (entspricht dem Preis eines Monats Mittelschicht-Lebensstil, S. 59). Skaliert je nach Komplexität/Dauer/Risiko des Runs (einfacher kurzer Job am unteren Ende, mehrmonatiger gefährlicher Auftrag deutlich darüber).

---

### 11. Ausrüstungswerte – Begriffe mit Zahlenbezug (S. 244–246)

- **Verfügbarkeit**: liegt normalerweise zwischen `1` und `6`, kann in Ausnahmefällen (v. a. Alphaware/Betaware/Deltaware-Bodytech) auf `9` und mehr steigen. Dient als **Schwellenwert für Matrixsuche-Proben**, um einen Verkäufer/Besitzer des Gegenstands zu finden. Bei der **Charaktererschaffung** darf nur Ausrüstung mit Verfügbarkeit **≤ 7** gekauft werden (S. 69, 3. Auflage/Errata; früher: legale Ware unbegrenzt, illegale max. 6).
- **Aktive Programmslots**: Anzahl gleichzeitig laufender Programme auf einem elektronischen Gerät.
- **Angriffswerte**: 5 Zahlen für die Reichweiten Sehr nah/Nah/Mittel/Weit/Sehr weit einer Waffe. **Nahkampfwaffen addieren die Stärke des Charakters zu ihrem Angriffswert** (S. 245, 3. Auflage/Errata; Ausnahme *Peitschen*: sie addieren stattdessen die **Reaktion** — S. 250). Der waffenlose Angriffswert ist `Reaktion + Stärke`.
- **Essenzkosten**: Betrag, um den die Essenz eines Charakters bei Implantation von Cyberware/Bioware sinkt.
- **Gerätestufe**: Standardbereich `1–3` (Haushaltsgeräte bis Alphaware-Cyberware); Stufe `4+` = High-End/Militär/Spezialeinheiten.
- **Kapazität**: Stufe, die den verfügbaren Platz für Modifikationen/Erweiterungen angibt; wird durch eingebaute Komponenten (in eckigen Klammern `[]`) verbraucht.
- **Matrixattribute**: 4 Werte für Angriff (A), Schleicher (S), Datenverarbeitung (D), Firewall (F); bei gehackten Slave-Geräten entspricht die Gerätestufe dem Datenverarbeitungs-/Firewallattribut.
- **Munition**: Kapazitäts-/Formcode einer Waffe: `(k)` Klapplademechanismus, `(s)` Stangenmagazin, `(i)` internes Magazin, `(t)` Trommelmagazin, `(g)` Gurtmunition, `(tr)` aufklappbare Trommel, `(v)` Vorderlader.
- **Schadenswert**: Grundschaden bei Treffer, gefolgt von Schadensart-Buchstabe (K = Körperlich, B = Betäubung) und ggf. Zusatzbuchstabe für Spezialschaden (z. B. `(e)` Elektrizität).
- **Sprengwirkung**: Ausdehnung einer Explosion (Reichweiten Detonationspunkt/Sehr nah 1–3 m/Nah 4–50 m).
- **Verteidigungswert**: Betrag, um den ein Gegenstand den Verteidigungswert eines Charakters erhöht.
- **WiFi-Funktionalität**: Geräte ohne WiFi-Fähigkeit können nicht mit der Matrix verbunden werden und erhalten keinen WiFi-Vorteil-Bonus.

#### Verfügbarkeit – Stufen (S. 245)

| Stufe | Bedeutung (Kurzform) |
|---|---|
| 1 | Praktisch überall erhältlich |
| 2 | Etwas spezieller, in Spezialläden zu finden |
| 3 | Fachgeschäft nötig, im Sprawl aber auffindbar |
| 4 | Nur bei Spezialhändlern, begrenzte Vorräte |
| 5 | Nischenmarkt, aber auffindbar |
| 6 | Handgefertigt, kleine Werkstätten, muss gesucht werden |
| 7 | Nur auf Bestellung spezialgefertigt |
| 8 | Termin + Hintergrundüberprüfung nötig |
| 9+ | Exklusive Sammlerstücke; kennzeichnet Elite-Status, kostet zusätzliches Geld |

- **Legalität**: `I` = für Privatbesitzer illegal (nur Sicherheitsfirmen/Konzerne/Behörden dürfen es nutzen); `L` = Lizenzpflicht (an eine bestimmte SIN gebunden).

---

### 12. Ausrüstung kaufen, verkaufen, verbergen (S. 246)

- **Anfangsausrüstung**: wird aus dem Ressourcen-Budget der Charaktererschaffung finanziert (siehe Prioritätentabelle, vorheriges Dokument Abschnitt 10).
- **Gestohlene Ware verkaufen**: Erlös `= 10 % des Grundpreises`, `+1 Prozentpunkt pro Erfolg` bei einer Probe auf `Einfluss + Charisma` (erfordert passende Connection).
- **Ausrüstung verbergen**: aktive Probe `Wahrnehmung + Intuition` des Suchenden gegen den Tarnbarkeits-Schwellenwert des versteckten Gegenstands (Basiswert nach Größe/Form, siehe Tabelle).

#### Tarnbarkeit (S. 247)

| Größe | Schwellenwert | Beispiel |
|---|---|---|
| Echt groß | 0 | Sturmkanone |
| Unhandlich | 1 | Sturmgewehr |
| Verstaubar | 2 | Schwere Pistole, Maschinenpistole |
| Taschengroß | 3 | Automatikpistole, Leichte Pistole |
| Handflächengroß | 4 | Kartenspiel, Holdout-Pistole |
| Kleine Handfläche | 5 | Einzelne Karte |
| Mit der Hand umschließbar | 6 | Feuerzeug |
| Klein | 7 | Sechsseitiger Würfel |
| Mini | 8 | Spionage-RFID-Chip |
| Fein | 9 | Pulverspuren |
| Mikroskopisch | 10 | Ein Floh auf der Schulter |

---

### 13. Kostenanpassung für Größe & nicht angepasste Ausrüstung (S. 246–247)

- **Zwerge und Trolle**: zahlen `10 % Aufschlag` auf für sie passend angepasste Ausrüstung (Panzerung, Kleidung); gilt **nicht** für Waffen oder Kommlinks. Bei Trollen entscheidet die Spielleitung im Zweifelsfall über den Aufschlag.
- **Nicht angepasste Ausrüstung nutzen** (z. B. Zwerg/Troll benutzt menschengroße Ausrüstung): `Würfelpoolmalus −2` auf alle Handlungen mit diesem Gegenstand.

---

### 14. Nahkampfwaffen – Werte (S. 249)

**Wichtig (S. 245/250, 3. Auflage/Errata):** Die unten gelisteten Angriffswerte sind die reinen Waffenwerte. Im Spiel addiert der Charakter seine **Stärke** (bei Peitschen: **Reaktion**) hinzu, um den effektiven Angriffswert zu erhalten.

#### Klingenwaffen

| Waffe | Schaden | Angriffswerte | Verfügbarkeit | Preis |
|---|---|---|---|---|
| Kampfaxt | 5K | 9/–/–/–/– | 4 | 500 ¥ |
| Kampfmesser | 3K | 8/2*/–/–/– | 2 | 220 ¥ |
| Katana | 4K | 10/–/–/–/– | 3 | 350 ¥ |
| Messer | 2K | 6/1*/–/–/– | 1 | 20 ¥ |
| Schwert | 3K | 9/–/–/–/– | 3 | 320 ¥ |
| Stangenwaffe | 4K | 8/–/–/–/– | 3 | 210 ¥ |
| Überlebensmesser | 3K | 8/–/–/–/– | 2 | 220 ¥ |
| Unterarmschnappklingen | 3K | 6/2*/–/–/– | 3 | 185 ¥ |

`*` Maximale Wurf-Reichweite 20 m.

#### Knüppel

| Waffe | Schaden | Angriffswerte | Verfügbarkeit | Preis |
|---|---|---|---|---|
| Betäubungsschlagstock | 5B(e) | 6/–/–/–/– | 2 | 600 ¥ |
| Knüppel | 3B | 6/–/–/–/– | 1 | 65 ¥ |
| Stab | 4B | 8/–/–/–/– | 1 | 150 ¥ |
| Teleskopschlagstock | 2B | 5/–/–/–/– | 2 | 50 ¥ |
| Teleskopstab | 4B | 8/–/–/–/– | 2 | 250 ¥ |
| Totschläger | 2B | 6/–/–/–/– | 1 | 75 ¥ |

- **Betäubungsschlagstock**: 10 Ladungen, lädt sich am Stromnetz mit `1 Ladung pro 10 Sekunden` nach; per WiFi-Vorteil ohne Stromnetz mit `1 Ladung pro halbe Stunde`.

---

### Nicht erfasst

Der Bereich Buchseiten 220–249 endet mitten im Abschnitt *Nahkampfwaffen* des Ausrüstungskapitels. Die restlichen Nahkampfwaffentypen (weitere „Andere Nahkampfwaffen“ mit eigenen Werten), Wurfwaffen, das komplette Feuerwaffen-Kapitel (Schadenswerte, Reichweiten, Modus, Rückstoß-Formeln), Panzerung, Munitionsarten sowie die Verfügbarkeits-/Preistabellen für Cyberware, Bioware, Drohnen und Fahrzeuge liegen jenseits von Seite 249 und sind hier nicht enthalten.

---

## Teil 7: Ausrüstung II: Waffen, Elektronik, Sensoren (Buchseiten 250–279)

<sub>Quelle-Chunk: `docs/sr6/sr6_calc_p251-280.md` — Originaltitel: Shadowrun 6 – Regeln mit Berechnungen (Grundregelwerk, Buchseiten 250–279)</sub>

Quelle: `Shadowrun_6_Grundregelwerk.pdf` (deutsche Ausgabe, Pegasus Spiele), physische PDF-Seiten 251–280, entsprechend den gedruckten Buchseiten **250–279** (Kapitel AUSRÜSTUNG: Nahkampf-/Wurfwaffen, Feuerwaffen, Waffenzubehör, Munition, Sprengmittel, Kleidung & Panzerung, Elektronik, Software, ID/Credsticks, Werkzeuge, optische/Audio-Geräte, Sensoren, Sicherheitsgeräte).

Buchseitenzahlen sind in Klammern angegeben, z. B. (S. 260).

Dieses Kapitel ist größtenteils ein Warenkatalog. Einzelne Waffen-/Gerätestatzeilen wurden **nicht** transkribiert; erfasst sind nur generelle Regeln, Formeln und kurze strukturelle Referenztabellen.

---

### 1. Bögen & Wurfwaffen – stufenbasierte Skalierung (S. 250)

- **Bogen-Stufe**: Ein Bogen hat eine Stufe (1–14), die zugleich die **Mindeststärke** zur Bedienung angibt. Schaden und Angriffswerte skalieren mit der Stufe:
  - `Schaden = (Stufe ÷ 2)K`
  - `Verfügbarkeit = (Stufe ÷ 3)L`
  - `Preis = (Stufe × 10) + 100 ¥`
  - Die Angriffswerte über die Reichweiten skalieren ebenfalls mit der Stufe (abnehmend mit der Distanz; Details siehe Tabelle *Projektil- und Wurfwaffen*, S. 250).
- **Pfeile**: `Preis = Stufe × 2 ¥`. Ein Pfeil muss mindestens die Stufe des verwendeten Bogens haben.
- **Injektionspfeile/-bolzen**: `Verfügbarkeit = 4` (fix), `Preis = (Stufe × 20) ¥` zzgl. separat gekaufter Nutzlast (Medikament/Gift). Ein Treffer muss mindestens **1 Kästchen Schaden** (nach Schadenswiderstandsprobe) verursachen, damit die Injektion wirkt.
- **Waffe bereit machen** (Wurfwaffen, Haupthandlung): Es können gleichzeitig bis zu `[Geschicklichkeit ÷ 2, aufgerundet]` Wurfmesser/Shuriken bereitgemacht werden (S. 46/250, 3. Auflage/Errata; frühere Fassung: volles Geschicklichkeitsattribut).
- **Nahkampfwaffen-Angriffswert** (S. 245/250, 3. Auflage/Errata): Katalog-Angriffswerte sind reine Waffenwerte; der Charakter addiert im Spiel seine **Stärke**. **Peitschen** (Bullen-/Monofilamentpeitsche, S. 250) addieren stattdessen die **Reaktion**.

---

### 2. Feuerwaffen – allgemeine Regeln (S. 251)

- **WiFi-Fähigkeit**: Alle modernen Feuerwaffen sind WiFi-fähig, besitzen einen digitalen Munitionszähler und ein ARO, das die Art der geladenen Munition anzeigt. Bei DNI erhält der Schütze eine zusätzliche Nebenhandlung, sobald er ein Magazin auswirft oder (bei Mehrmodus-Waffen) den Feuermodus wechselt.
- **Zubehörbeschränkung**: Taser können nur mit aufmontiertem Zubehör versehen werden. Holdout-Pistolen können **gar nicht** mit Zubehör/Modifikationen versehen werden.

---

### 3. Waffenzubehör – Halterungen & Effekte (S. 259–261)

- **Halterungsprinzip**: Zubehör wird an einer von drei Halterungsarten angebracht – *auf dem Lauf*, *am Lauf* oder *unter dem Lauf*. Jede Halterung kann **nur ein** Zubehörteil gleichzeitig aufnehmen.
- **Anbringen/Entfernen**: In der Regel eine Nebenhandlung (Ein-/Ausklappen) oder Hauptmandlung (Befestigen/Lösen); WiFi-Vorteile verkürzen dies häufig auf eine Nebenhandlung.
- **Lasermarkierer**: `+1` auf die Angriffswerte für alle verfügbaren Reichweiten (nicht kumulativ mit Smartgun-Boni).
- **Smartgunsystem**: `+2` auf die Angriffswerte für alle verfügbaren Reichweiten. Internes System erhöht den Waffenpreis um `500 ¥`; externes System kann mit einer Ausgedehnten Probe `Mechanik + Logik (4, 1 Stunde)` an-/umgebaut werden. WiFi-Vorteil (Smartlink aktiv): zusätzlich `+1 Würfelpoolbonus` auf Angriffsproben sowie eine zusätzliche Nebenhandlung beim Nachladen/Moduswechsel; ermöglicht zudem Feuern aus voller Deckung ohne den sonst dafür fälligen Würfelpoolmalus.
- **Rückstoßkompensation** (Gasventilsystem, Gyrostabilisator, Dreibein, Schockpolster, Smart-Feuerplattform): Diese Zubehörteile heben den Angriffswertmalus für halbautomatisches und Salvenfeuer auf (bzw. senken ihn) und senken den Angriffswertmalus für vollautomatisches Feuer (Basis siehe S. 112) typischerweise auf `−2` bis `−3`, je nach Zubehör. Ein einmal eingebautes Gasventilsystem kann nicht mehr entfernt werden.
- **Periskop**: Senkt den Würfelpoolmalus des Status *Volle Deckung* (Angriffe) von der Deckung aus um `1` (mit WiFi-Vorteil um `2` insgesamt, effektiv auf `0`).
- **Zielfernrohr/Sichtgerät**: Kapazität `3` für Sichtverstärkungen (siehe Abschnitt 13).
- **Zweibein**: `+2` auf den Angriffswert, wenn vollständig ausgeklappt und der Schütze liegt/kniet.

#### Referenztabelle Waffenzubehör – Halterung, Verfügbarkeit, Preis (S. 261)

| Zubehör | Halterung | Verfügbarkeit | Preis |
|---|---|---|---|
| Airburst-Verbindung | – | 3 | 600 ¥ |
| Dreibein | Unter | 2 | 500 ¥ |
| Ersatzmagazin | – | 2 | 5 ¥ |
| Gasventilsystem | Lauf | 3 | 500 ¥ |
| Gyrostabilisator | Unter | 3 | 1.400 ¥ |
| Lasermarkierer | Auf oder Unter | 1 | 125 ¥ |
| Periskop | Auf | 2 | 70 ¥ |
| Schalldämpfer | Lauf | 4 | 500 ¥ |
| Schnelllader | – | 1 | 25 ¥ |
| Schnellziehholster | – | 2 | 175 ¥ |
| Schockpolster | – | 2 | 50 ¥ |
| Smart-Feuerplattform | Unter | 5 | 2.500 ¥ |
| Smartgunsystem, extern | Auf oder Unter | 2L | 200 ¥ |
| Smartgunsystem, intern | – | 1L | +500 ¥ |
| Springarm | – | 2 | 350 ¥ |
| Tarnholster | – | 1 | 150 ¥ |
| Zielfernrohr | Auf | 1 | 350 ¥ |
| Zweibein | Unter | 1 | 200 ¥ |

- **Airburst-Verbindung**: Beim Berechnen der Abweichung von Granaten/Raketen zählt jeder Erfolg **doppelt** (s. *Sprengangriffe und Abweichung*, S. 118), wenn der WiFi-Zünder verwendet wird. Funktioniert nur im eingeschalteten WiFi-Modus.

---

### 4. Munition – Kosten & Munitionsarten (S. 261–262)

- **Waffentausch von Munition**: Alle Waffen derselben Klasse können ihre Munition austauschen (z. B. alle schweren Pistolen untereinander).
- **Munitionsarten-Modifikator**: `Angriffswertmodifikator` und `Schadensmodifikator` der Munitionsart werden zu den Basiswerten der Waffe addiert; der `Preismultiplikator` gilt auf den Grundpreis der Munition.

#### Munitionsarten (S. 262)

| Art | Angriffswert | Schaden | Preismultiplikator |
|---|---|---|---|
| APDS | +2 | −1 | ×3 |
| Explosiv | – | +1 | ×2 |
| Flechette | +1 | −1 | ×1,5 |
| Gel | – | B (Betäubung) | ×1,5 |
| Schocker | +1 | −1B(e) | ×2 |
| Standard | – | – | ×1 |
| Hülsenlos | – | – | ×2 |

- **Explosivmunition**: Zündet bei einem Kritischen Patzer fehl – der Schütze muss dann gegen den normalen (unmodifizierten) Schadenswert der Waffe Widerstand leisten, der eigentliche Angriff verfehlt sein Ziel, und die Waffe wird zerstört.
- **APDS/Flechette**: werden praktisch nie hülsenlos hergestellt.

#### Munitionskosten nach Waffenart (S. 262, Preis pro 10 Schuss)

| Waffenklasse | Verfügbarkeit | Preis (pro 10 Schuss) |
|---|---|---|
| Taser | 1 | 10 ¥ |
| Holdout-/Leichte Pistole/Automatikpistole | 1 | 5 ¥ |
| Schwere Pistole/Maschinenpistole | 1 | 10 ¥ |
| Schrotflinte | 2L | 15 ¥ |
| Sonstiges Gewehr | 2L | 20 ¥ |
| Maschinengewehr | 2L | 15 ¥ |
| Sturmkanone | 4I | 50 ¥ |
| DMSO-Gelpack | – | 10 ¥ |
| Injektionspfeil | 2 | 5 ¥ + Toxin |

(Endpreis der Munition = Preis nach Waffenart-Tabelle × Preismultiplikator der Munitionsart.)

- **RFID in Munition**: In der Hälfte aller Fabrikpatronen sind Mikro-RFID-Chips eingebaut, die die Waffe/den Ort identifizieren und bei Abfeuern alarmieren. Löschen erfordert einen RFID-Löscher (S. 271) oder eine Ausgedehnte Probe `Elektronik + Logik (2, 1 Minute)` pro 10 Patronen.

---

### 5. Granaten, Raketen & Sprengstoffe (S. 262–264)

- **Wurf/Abschuss**: Granaten werden mit `Athletik + Geschicklichkeit` geworfen oder mit `Exotische Waffen (Werfer) + Geschicklichkeit` aus einem Granatwerfer abgefeuert. Es gelten die Regeln für Sprengangriffe (S. 118).
- **Angriffswerte geworfener Granaten**: `Waffenlos / Waffenlos − 1 / Waffenlos − 6 / Waffenlos` für die vier Reichweitenkategorien. Sinkt der Angriffswert auf `0`, kann die Granate auf diese Entfernung nicht mehr geworfen werden.
- **Schadensabnahme mit Distanz**: Granaten (und Raketen) haben drei Schadenswerte – am Detonationspunkt (DP), im Bereich „Sehr nah“ (1–3 m) und „Nah“ (4–50 m); Schaden sinkt mit zunehmender Entfernung vom Detonationspunkt.
- **Scharfmachung**: Minigranaten (Granatwerfer) schärfen sich nach 5 m Flugbahn, Raketen/Lenkraketen nach 10 m (sofern keine Airburst-Verbindung verwendet wird). Die Sicherheitsdistanz kann mit einer Ausgedehnten Probe `Mechanik + Logik (4, 5 Minuten)` deaktiviert werden.
- **WiFi-Zünder**: Erlaubt die Detonation einer Granate/Rakete per ARO/Kommlink über DNI, auch ohne direktes Neuralinterface (Voraussetzung: Granate/Rakete ist per WiFi mit dem PAN des Werfers verbunden).
- **Lenkraketen**: `Preis = Preis der (Dumb-)Rakete + (Sensorstufe × 500) ¥`; `Verfügbarkeit = Verfügbarkeit der Rakete + 1` (Stufe der Genauigkeit); Sensorstufe (1–6) wird zusätzlich als Würfelpoolbonus zur Angriffsprobe addiert.
- **Sprengstoff-Stufen** (Kommerzieller/Plastiksprengstoff): Stufe definiert Sprengkraft und Menge in einem Paket, ohne beide separat zu beziffern.

#### Sprengstoffpakete – Preisskalierung nach Stufe (S. 264)

| Stufe | Verfügbarkeit | Preis |
|---|---|---|
| 1–3 | 4I | Stufe × 10 ¥ |
| 4–6 | 4I | Stufe × 50 ¥ |
| 7–9 | 4I | Stufe × 100 ¥ |
| 10–12 | 4I | Stufe × 250 ¥ |
| 13–15 | 5I | Stufe × 500 ¥ |
| 16–18 | 5I | Stufe × 1.000 ¥ |
| 19–20 | 5I | Stufe × 5.000 ¥ |

- **Sprengkapsel**: Zünder für Sprengstoff, per Timer oder Funksignal ausgelöst; WiFi-Vorteil erlaubt Detonation per Nebenhandlung *Gerätemodus ändern*.

---

### 6. Kleidung & Panzerung (S. 265–267)

- **Stacking-Regel**: Panzerung erhöht den Verteidigungswert. **Zusätzliche Panzerteile wirken nicht kumulativ**, sofern nicht ausdrücklich anders angegeben (Ausnahmen: Helme und Schilde, siehe Abschnitt 7).
- **Elektrochrome Modifikation**: Farb-/Musterwechsel der Kleidung; Nebenhandlung zum Ändern der Einstellung, aber der eigentliche Farbwechsel ist erst nach **zwei Kampfrunden** abgeschlossen.
- **Chamäleonanzug (WiFi-Vorteil)**: Erhöht den Verteidigungswert des Trägers zusätzlich um `1` (aktiver Anzug), wenn dieser sich verstecken will.

#### Panzerungsmodifikationen – Kapazitätsmechanik (S. 266–267)

- Panzerungsteile besitzen eine **Kapazität** (siehe Tabelle *Panzerung*). Panzerungsmodifikationen benötigen jeweils Kapazität in Höhe ihrer Stufe.
- Modifikationen (Chemische/Elektrische Isolierung, Feuerresistenz, Kälteresistenz) **neutralisieren einen entsprechenden Status** (Verätzt, Gebrutzelt, Brennend, Unterkühlt) so oft, wie es ihrer Stufe entspricht; danach ist die Beschichtung „verbraucht“ und bietet keinen Schutz mehr.
- **Chemische Versiegelung** (nur für Ganzkörperpanzerungen): fixe Kapazität `6`, Preis `3.000 ¥`, neutralisiert jeden Kontakt-/Inhalationsvektor-Status insgesamt 6-mal; zusätzlich max. 1 Stunde Schutz vor Luftmangel-Situationen.

| Modifikation | Kapazität | Verfügbarkeit | Preis |
|---|---|---|---|
| Chemische Isolierung | [Stufe] | 3 | Stufe × 250 ¥ |
| Chemische Versiegelung | 6 | 5 | 3.000 ¥ |
| Elektrische Isolierung | [Stufe] | 3 | Stufe × 250 ¥ |
| Feuerresistenz | [Stufe] | 3 | Stufe × 250 ¥ |
| Kälteresistenz | [Stufe] | 3 | Stufe × 250 ¥ |

---

### 7. Helme & Schilde – additive Ausnahme zur Stacking-Regel (S. 267)

- **Helm**: Verteidigungswert wird **zum Verteidigungswert der getragenen Rüstung addiert** (Ausnahme von der Nicht-Stapel-Regel in Abschnitt 6). Helme haben eine **Kapazität** für Zubehör (Trodennetze, Sichtverstärkungen), deren Höhe der Tabelle *Helme und Schilde* zu entnehmen ist (Standard-Helm: 4). *(3. Auflage/Errata: die pauschale Angabe „Kapazität 4 bzw. 6" wurde aus dem Fließtext gestrichen.)*
- **Schild**: Verteidigungswert wird ebenfalls **zum Verteidigungswert der getragenen Rüstung addiert**.
- **Schutzschild** (elektrisch): 10 Ladungen für elektrischen Angriff, lädt sich am Stromnetz mit 1 Ladung pro 10 Sekunden (WiFi-Vorteil: 1 Ladung/Stunde per Induktion).

---

### 8. Elektronik – Kommlinks, Cyberdecks, Riggerkonsolen (S. 268–269)

- **Kommlink-Slaves**: Ein Kommlink kann maximal so viele Slave-Geräte verwalten, wie seine **Gerätestufe** angibt.
- **Riggerkonsole – Drohnenanzahl**: `Maximale gleichzeitig verbundene Slave-Drohnen = Gerätestufe × 3`.
- **Riggerkonsole – geteilte Programme/Autosofts**: Anzahl der Programme/Autosofts, die eine Riggerkonsole mit ihren Slave-Drohnen teilen kann, entspricht ihrem **Datenverarbeitungsattribut**.
- **Riggerkonsole – Initiative**: Wird die Riggerkonsole in VR genutzt, wird ihr Datenverarbeitungsattribut zur Berechnung der Initiative herangezogen.
- **Riggerkonsole – Rauschunterdrückung**: Senkt sämtliche Rauschenmodifikatoren (für sich und ihre Slaves) um ihre eigene Gerätestufe.
- Cyberdecks enthalten stets Sim-Module für heißes Sim (kein Zukauf nötig).

---

### 9. Elektronikzubehör & Gegenmaßnahmen (S. 269–271)

- **Kompatibilität/PAN-Hintertür**: Sofern nicht anders angegeben, ist Elektronikzubehör kompatibel mit Kommlinks/Cyberdecks (und ggf. anderen Geräten). Alle Zubehörgeräte sind WiFi-fähig und stellen, wenn sie als Slave im PAN eines Users eingebunden sind, eine potenzielle Hacking-Hintertür dar; nicht eingebundene Zubehörteile haben „offene“ Verbindungen und können ohne Weiteres gehackt werden.
- **RFID-Löscher**: Reichweite max. 5 mm zum Chip; verursacht sofort **10 Kästchen Matrixschaden** (normal widerstanden). Lädt sich (mit WiFi-Vorteil) innerhalb einer Stunde am Stromnetz voll auf; 1 Ladung pro Anwendung.
- **Sensor-Chip**: Zeichnet 24 Stunden lang Sensordaten auf (max. Sensorstufe 2), danach werden alte Daten überschrieben (Ringpuffer).
- **Sicherheits-/Spionage-Chip**: Implantation unter der Haut erfordert eine Ausgedehnte Probe `Biotech + Logik (10, 1 Minute)`. Die Spionage-Variante läuft dauerhaft auf Schleichfahrt (S. 178) und würfelt bei einer Vergleichenden Probe gegen Matrixwahrnehmung mit **10 Würfeln**; sie sendet nur zu voreingestellten Zeiten in kurzen Sendeimpulsen.
- **Headkom-Blocker**: Entfernen durch Dritte erfordert eine Ausgedehnte Probe `Elektronik + Logik` **oder** `Mechanik + Geschicklichkeit (10, 1 Hauptmandlung)`. Selbstentfernung: Probe `Athletik + Geschicklichkeit (5)` + 1 Hauptmandlung.
- **Störsender (Jammer)**: Erzeugt Rauschen in Höhe seiner **Stufe** (1–6). Bereichsstörsender: kegelförmiger/kugelförmiger Bereich, Stufe sinkt `−1 pro 10 Meter` vom Zentrum. Zielgerichteter Störsender: 30°-Kegel, Stufe sinkt `−1 pro 30 Meter` vom Zentrum. Wände/Hindernisse können die Ausbreitung behindern (SL-Ermessen).
- **White-Noise-Generator**: Alle Wahrnehmungsproben, um eine Unterhaltung innerhalb von `[Stufe]` Metern mitzuhören, erhalten einen Würfelpoolmalus in Höhe der **Stufe** des Generators (1–6). Bei mehreren Generatoren zählt nur die höchste Stufe (nicht kumulativ). WiFi-Vorteil: effektive Reichweite verdreifacht.
- **Wanzenscanner**: Probe `Elektronik + Logik` als Vergleichende Probe gegen die Matrixwahrnehmungsprobe der Wanze. Der Benutzer erhält **2 automatische Erfolge** und muss bei der Vergleichenden Probe nur einen **Gleichstand** erzielen (keine Nettoerfolge nötig), um die Wanze zu finden.

---

### 10. Software (S. 271–272)

- **Lehrsoft**: Legt Unterrichtsproben mit einem Würfelpool in Höhe von `Stufe × 2` ab. Stufen 1–6.
- **Talentsoft**: Ersetzt bei einer Fertigkeitsprobe den Fertigkeitswert durch die **Talentsoftstufe**. Proben, die mit einer Talentsoft abgelegt werden, können **nicht durch Edge verbessert werden**. Nutzung erfordert eine Talentbuchse (S. 285/289).
- **Aktionssoft**: Ersetzt eine Aktionsfertigkeit (nicht magie-/resonanzverknüpft); Stufen 1–6. Anzahl gleichzeitig nutzbarer Aktionssofts = Stufe der Talentbuchse.
- **Linguasoft**: Stufe 1 entspricht Grundkenntnissen (Wortfetzen, nutzbar wie Wissensfertigkeit); Stufen 2–4 gewähren einen Würfelpoolbonus in Höhe der Stufe auf alle sprachbezogenen Proben. Maximalstufe 4. Anzahl gleichzeitig nutzbarer Linguasofts = Stufe der Talentbuchse.
- **Wissenssoft**: Repliziert eine Wissensfertigkeit direkt (überschreibt aktiv das eigene Wissen des Anwenders); keine eigene Stufe.
- **Datensoft**: Vergleichbar mit einer thematisch eingeschränkten Wissensfertigkeit (S. 100); wird genauso eingesetzt.
- **Kartensoft**: `+1 Würfelpoolbonus` auf Proben, den richtigen Weg zu finden.
- **Shopsoft**: `+1 Würfelpoolbonus` auf **Matrixsuche-Proben**, um passende Waren zu kaufen oder zu verkaufen (S. 272, 3. Auflage/Errata; früher: „Einflussproben").

#### Software-Preistabelle (S. 272)

| Software | Verfügbarkeit | Preis |
|---|---|---|
| Autosoft (Stufe 1–9) | Stufe | Stufe × 500 ¥ |
| Datensoft | 2 | 120 ¥ |
| Kartensoft | 2 | 100 ¥ |
| Lehrsoft (Stufe 1–6) | Stufe ÷ 3 | Stufe × 400 ¥ |
| Programm, Hacking | 4I | 250 ¥ |
| Programm, Standard | 1 | 60 ¥ |
| Shopsoft | 2 | 150 ¥ |
| Talentsoft – Aktionssoft (Stufe 1–6) | 4 | Stufe × 5.000 ¥ |
| Talentsoft – Linguasoft (Stufe 1–4) | 1 | Stufe × 1.500 ¥ |
| Talentsoft – Wissenssoft | – | 2.500 ¥ |

---

### 11. ID, Credsticks & Lizenzen (S. 273–274)

- **Beglaubigter Credstick**: Nicht auf eine Person registriert; das aufgedruckte Maximum ist der maximal speicherbare Betrag, nicht der tatsächliche Kontostand.

| Typ | Maximalbetrag | Verfügbarkeit | Preis |
|---|---|---|---|
| Standard | 5.000 ¥ | 1 | 5 ¥ |
| Silber | 20.000 ¥ | 1 | 20 ¥ |
| Gold | 100.000 ¥ | 2 | 100 ¥ |
| Platin | 500.000 ¥ | 3 | 500 ¥ |
| Ebenholz | 1.000.000 ¥ | 5 | 1.000 ¥ |

- **Gefälschte SIN – Verifizierungsprobe**: Das Verifizierungssystem legt eine Probe gegen den Schwellenwert `Stufe(SIN) × 2` ab. Mobile Verifizierungssysteme haben max. Stufe 3, stationäre max. Stufe 8.
- **Gefälschte Lizenz**: Gegen Verifizierungssysteme kommt die **Stufe der Lizenz** zum Einsatz. Eine gefälschte Lizenz kann keine höhere Stufe haben als die SIN, der sie zugewiesen ist.

| ID | Verfügbarkeit | Preis |
|---|---|---|
| Gefälschte SIN (Stufe 1–6) | 4I | Stufe × 2.500 ¥ |
| Gefälschte Lizenz (Stufe 1–6) | 4I | Stufe × 200 ¥ |

---

### 12. Werkzeuge (S. 274)

| Werkzeug | Bonus | Verfügbarkeit | Preis |
|---|---|---|---|
| Kiste | – (Mindestvoraussetzung für viele Proben) | 1 | 500 ¥ |
| Laden | `+1 Würfelpoolbonus` auf Bau-/Reparaturproben | 4 | 5.000 ¥ |
| Werkstatt | `+1 Würfelpoolbonus` + `1 Edge` auf Bau-/Reparaturproben | 7 | 50.000 ¥ |

---

### 13. Optische & Audio-Geräte – Kapazitätssystem (S. 274–277)

- **Kapazitätsprinzip**: Jedes optische/Audio-Gerät hat eine Kapazität, die das Hinzufügen von Sicht-/Audioverstärkungen begrenzt. Die Summe der Kapazitätskosten aller eingebauten Verstärkungen darf die Gerätekapazität nicht übersteigen.
- **Preisformel** (Gerätetabelle, S. 275/277): `Preis = Kapazität × Multiplikator ¥` (Multiplikator je nach Gerätetyp z. B. ×50, ×100, ×120).

#### Sichtverstärkungen – Kapazitätskosten (S. 276)

| Verstärkung | Kapazitätskosten | Verfügbarkeit | Preis |
|---|---|---|---|
| Bildverbindung | 1 | 1 | +25 ¥ |
| Blitzkompensation | 1 | 1 | +250 ¥ |
| Infrarotsicht | 1 | 2 | +500 ¥ |
| Restlichtverstärkung | 1 | 2 | +500 ¥ |
| Sichtverbesserung | 2 | 1 | +500 ¥ |
| Sichtvergrößerung | 1 | 1 | +250 ¥ |
| Smartlink | 2 | 2 | +2.000 ¥ |
| Ultraschallverbindung | 1 | 1 | +300 ¥ |

#### Audioverstärkungen – Kapazitätskosten (S. 277)

| Verstärkung | Kapazitätskosten | Verfügbarkeit | Preis |
|---|---|---|---|
| Audioverbesserung | 1 | 1 | +500 ¥ |
| Richtungsdetektor | 2 | 2 | +1.000 ¥ |
| Selektiver Geräuschfilter (Stufe 1–3) | Stufe | 3 | Stufe × 250 ¥ |

---

### 14. Sensoren (S. 277–278)

- **Sensorarray vs. Einzelsensor**: Ein Sensorarray (Stufe 2–8) kann so viele Funktionen enthalten, wie seiner Stufe entspricht; ein Einzelsensor (Stufe 1–8) kann nur eine Funktion enthalten.
- **Gehäuse-Kapazität**: Wie viele/welche Sensoren ein Gehäuse aufnehmen kann, hängt von dessen Kapazität (Tabelle *Sensoren*) und dem Gerätetyp (max. Sensorstufe nach Tabelle *Sensorpakete*) ab.

| Gerät | Kapazität | Preis |
|---|---|---|
| Tragbares Gehäuse | 1–3 | Kapazität × 100 ¥ |
| Stationäres Gehäuse | 1–6 | Kapazität × 250 ¥ |
| Sensorarray (Stufe 2–8) | [Stufe] | Stufe × 1.000 ¥ |
| Einzelsensor (Stufe 1–8) | [1] | Stufe × 100 ¥ |

#### Sensorpakete – maximale Sensorstufe nach Einbauort (S. 277)

| Paket | Maximale Sensorstufe |
|---|---|
| RFID, Audio- oder Sichtgerät, Headware | 2 |
| Tragbares Gerät, kleine (oder kleinere) Drohne | 3 |
| Stationäres Gerät, mittlere Drohne | 4 |
| Große Drohne, Cybergliedmaße | 5 |
| Motorrad | 6 |
| Fahrzeug (größer als ein Motorrad) | 7 |
| Gebäude, Gebäudekomplex | 8 |

- **Sensor als Wahrnehmungsersatz**: Wird ein Sensor aktiv für eine Wahrnehmungsprobe genutzt, ersetzt seine Stufe die Fertigkeit Wahrnehmung. Ein alleine agierender Sensor legt normalerweise eine Einfache Probe mit seiner Stufe gegen einen Schwellenwert ab (Tarnbarkeit des Ziels bzw. Nettoerfolge einer Zauberei-/Heimlichkeitsprobe).

#### Sensorfunktionen – maximale Reichweite (S. 278)

| Funktion | Maximale Reichweite |
|---|---|
| Bewegungsmelder | 25 m |
| Cyberwarescanner | 15 m |
| Kamera | Blickfeld |
| Laser-Entfernungsmesser | 1.000 m |
| Lasermikrofon | 100 m |
| MAD-Scanner | 5 m |
| Mikrofon | 100 m |
| Richtmikrofon | 100 m |
| Ultraschall | 50 m |

---

### 15. Sicherheitsgeräte, Schlösser & Einbruchswerkzeug (S. 278–279)

- **Magschloss**: Stufen 1–9.
- **Schloss (mechanisch)**: Stufen 1–6; zum Knacken ist eine erfolgreiche Probe `Mechanik + Geschicklichkeit` mit Schwellenwert = **Stufe des Schlosses** erforderlich.
- **Magnetkarten-Kopierer**: Kopieren einer Magnetkarte in Sekunden; Anfertigen der neuen Karte erfordert eine Ausgedehnte Probe `Elektronik + Logik (2, 10 Minuten)`.
- **Automatischer Dietrich**: Gewährt `+1 Würfelpoolbonus` auf die Probe zum Knacken eines mechanischen Schlosses.
- **Brecheisen**: Verdoppelt die effektive Stärke des Charakters beim Aufbrechen von Tür/Schloss/Behälter.
- **Magschlossknacker (WiFi-Vorteil)**: `+1` auf seine effektive Stufe.

| Gegenstand | Verfügbarkeit | Preis |
|---|---|---|
| Cyberwareblocker | 3 | 250 ¥ |
| Magschloss (Stufe 1–9) | 3 | Stufe × 100 ¥ |
| Metall-Handschellen | 1 | 20 ¥ |
| Plasstahl-Handschellen | 3 | 50 ¥ |
| Plastikstreifen (10 Stück) | 1 | 5 ¥ |
| Schloss (Stufe 1–6) | 2 | Stufe × 10 ¥ |

---

### Nicht erfasst

Bewusst ausgelassen wurden alle reinen Waffen-/Geräte-Statkataloge ohne verallgemeinerbare Formel, u. a.:

- Nahkampfwaffentabelle (S. 250), sämtliche Feuerwaffenkataloge (Taser, Holdout-, Leichte-, Schwere-, Automatik-, Maschinenpistolen, Schrotflinten, Jagdgewehre, Sturmgewehre, Scharfschützengewehre, Maschinengewehre/Sturmkanonen, Spezielle/Exotische Waffen, Granat-/Raketenwerfer; S. 251–258) mit ihren individuellen Schadens-/Angriffswerte-/Munitions-/Preiszeilen.
- Granaten- und Raketentabelle mit Einzelwerten (S. 263–264), Sprengstoffpakete-Einzelwerte wurden nur als Preis*skalierung* (Abschnitt 5) erfasst.
- Individuelle Kleidungs-/Panzerungs-Katalogeinträge (S. 265–266) – nur die Stacking-/Kapazitätsregeln (Abschnitte 6–7) wurden erfasst.
- Individuelle Kommlink-, Cyberdeck- und Riggerkonsolen-Modelltabellen (S. 268–269) – nur die Skalierungsformeln (Abschnitt 8) wurden erfasst.
- Individuelle Elektronikzubehör-, Software-, Credstick-, Werkzeug-, Optik-/Audio-/Sensor- und Sicherheitsgeräte-Preiszeilen einzelner Markenprodukte – jeweils nur die zugrunde liegenden Mechaniken/Kapazitäts- bzw. Stufenformeln wurden übernommen.
- Verweise auf Regeln außerhalb des Seitenbereichs (nicht im Detail nachvollzogen, nur zitiert): Sprengangriffe/Abweichung (S. 118), Gasangriffe (S. 120), Nicht genug Munition (S. 112), Matrixschaden reparieren (S. 175), Magschlösser (S. 240), Barrieren (S. 115), Wissensfertigkeiten (S. 100), Toxine und Drogen (S. 124), Talentbuchse/Talentleitungen (S. 285/289).

---

## Teil 8: Ausrüstung III: Bodytech, Magische Ausrüstung, Fahrzeuge (Buchseiten 280–305)

<sub>Quelle-Chunk: `docs/sr6/sr6_calc_p281-310.md` — Originaltitel: Shadowrun 6 – Regeln mit Berechnungen (Ausrüstung: Überlebensausrüstung, Biotech/Bodytech, Magische Ausrüstung, Fahrzeuge – Buchseiten 280–305)</sub>

Quelle: Sub-PDF `sr6_p281-310.pdf` (physische PDF-Seiten 1–30), deutsche Ausgabe. Die gedruckten Buchseiten in diesem Ausschnitt reichen von **S. 280 bis S. 305** (Kapitel AUSRÜSTUNG, Abschnitte Überlebensausrüstung/Industriechemikalien, Biotech/Bodytech, Toxine und Drogen, Magische Ausrüstung, Fahrzeuge und Drohnen). Ab Buchseite 306 beginnt ein neues Kapitel ("Deutschland in den Schatten") ohne Spielregeln – siehe *Nicht erfasst*.

---

### 1. Implantatkategorien – Essenz-, Preis- und Verfügbarkeits-Multiplikatoren (S. 283)

Cyberware- **und** Bioware-Implantate gibt es in fünf Kategorien: Standard, Gebraucht, Alphaware, Betaware, Deltaware. Die Grundpreise/-Essenzkosten in den Ausrüstungslisten gelten für **Standard**; andere Kategorien werden mit folgenden Faktoren umgerechnet:

| Kategorie | Essenzkosten | Preis | Verfügbarkeit |
|---|---|---|---|
| Standard | ×1 | ×1 | +0 |
| Gebraucht | ×1,1 | ×0,5 | −1 |
| Alphaware | ×0,8 | ×1,2 | +1 |
| Betaware | ×0,7 | ×1,5 | +2 |
| Deltaware | ×0,5 | ×2,5 | +3 |

- **Gebraucht** ist eine eigene, exklusive Kategorie – sie kombiniert sich mit keiner anderen (z. B. gibt es keine "gebrauchte Alphaware").
- Jegliches Zubehör und alle Erweiterungen eines Implantats müssen dieselbe Kategorie haben wie das Implantat, dem sie hinzugefügt werden.

### 2. Cyberware-/Bioware-Einbau: Operationsschaden (S. 283)

- Beim Implantieren von Cyberware **oder** Bioware erleidet der Charakter sowohl auf dem **Körperlichen** als auch auf dem **Betäubungs-Zustandsmonitor** je: `Schaden = Essenzkosten des Implantats × 3` (aufgerundet).
- Dieser Operationsschaden führt **niemals** zu Überzähligem Schaden.
- Der Preis für den chirurgischen Eingriff selbst ist **nicht** im Ausrüstungspreis enthalten und muss separat verhandelt/bezahlt werden.

### 3. Übersteuern von Bodytech (S. 284)

> **Errata 3. Auflage zur Tabelle *Cyberbuchsen* (S. 284):** Die Spalte „Matrixinitiative-Bonus" heißt jetzt „Matrixinitiative-Bonuswürfel (VR)" (zusätzliche Initiativewürfel in der VR, kein Zuschlag auf den Initiativewert); für Stufe 5 & 6 wurde der Wert von +3 auf **+2** korrigiert. Vollständige Cyberbuchsen-Tabelle siehe Teil 4, Abschnitt 17 (Matrix-Hardware).


- Ein attributssteigerndes Cyberwaresystem kann per Nebenhandlung "übersteuert" werden: Stufe des Systems `+2` für eine einzelne Handlung (das betroffene Attribut darf dadurch auch **über** den normalen Cap von `+4` gegenüber dem unmodifizierten Attribut hinaus gesteigert werden).
- Der zusätzliche Bonuswürfel muss ein **Schicksalswürfel** sein.
- **Patzer** beim Übersteuern: Das System schaltet für `[Stufe]` Kampfrunden ab.
- **Kritischer Patzer**: Der betroffene Muskel verkrampft, das Attribut fällt für `[Stufe]` Kampfrunden auf `0`.

### 4. Headware: Talentbuchse – Kapazität für gleichzeitig laufende Fertigkeiten (S. 285)

- Die **Talentbuchse** speichert Wissens-/Linguasofts (dauerhaft nutzbar wie eigene Fertigkeiten) und kann zusätzlich Aktionssofts über implantierte **Talentleitungen** (S. 289) laufen lassen.
- **Cap Summe**: `Σ (Stufen aller gleichzeitig laufenden Fertigkeiten) ≤ 2 × Stufe der Talentbuchse` (3. Auflage/Errata: ausdrücklich die *Summe der Stufen*, nicht die Zahl der Fertigkeiten).
- **Cap Einzelwert**: Die maximale Stufe einer einzelnen laufenden Fertigkeit = `Stufe der Talentbuchse` (3. Auflage/Errata; nicht die Stufe der Talentleitungen).
- Starten/Anhalten von Fertigkeiten erfordert keine Handlung; für über die Talentbuchse genutzte Fertigkeiten kann kein Edge eingesetzt werden.
- WiFi-Vorteil: Erhöht die Summen-Obergrenze auf das **Vierfache der Stufe der Talentbuchse**; Edge-Einsatz wird dann möglich.

### 5. Riggerkontrolle / Riggerinterface (S. 285, 297)

- **Riggerkontrolle** (Headware, 3. Auflage/Errata): Beim "Einspringen" in ein Fahrzeug/eine Drohne senkt sie den Schwellenwert **aller Proben zum Betrieb des Fahrzeugs** (Steuern-Proben, Abfeuern von Fahrzeugwaffen …) um ihre `Stufe`, gewährt einen Würfelpoolbonus in Höhe ihrer `Stufe` sowie **1 Edge je Probe**.
- **Riggerinterface** (Fahrzeugmodifikation): Ohne dieses kann ein Rigger ein Fahrzeug zwar vom Kommandositz aus steuern, aber sich nicht "als das Fahrzeug fühlen". Drohnen sind serienmäßig damit ausgestattet, Fahrzeuge benötigen den nachträglichen Einbau.

### 6. Cybergliedmaßen: Attribute, Zustandsmonitor, Attributserhöhung (S. 289–291)

- **Attributsbasis bei mehreren Gliedmaßen**: Bei Proben, die mehrere Cybergliedmaßen gemeinsam betreffen, gilt jeweils das **niedrigste** Attribut aller beteiligten Gliedmaßen – außer bei der Probe wird tatsächlich nur eine einzelne Gliedmaße eingesetzt, dann zählt nur deren Wert.
- **Standardwerte**: Standardcybergliedmaßen werden mit `Geschicklichkeit = 2` und `Stärke = 2` installiert.
- **Körperlicher Zustandsmonitor**: Jede ganze Cybergliedmaße vergrößert ihn um `+1 Kästchen`. Hände und Füße werden dabei ignoriert; partielle Cybergliedmaßen (Unterarm/-schenkel) zählen als **halbe** Gliedmaße.
- **Attributserhöhung (Zubehör)**: Erhöht Geschicklichkeit, Stärke oder Panzerung der Gliedmaße. Es gilt derselbe universelle Cap wie bei natürlichen Attributen: max. `+4` gegenüber dem natürlichen Attribut – ein Kauf über diesen Punkt hinaus ist Geldverschwendung.
- Panzerungserhöhung einer Cybergliedmaße erhöht **dauerhaft** den Verteidigungswert des Charakters.
- Eine Stärkeerhöhung wirkt sich nur auf Schaden/Angriffswert aus, wenn die Gliedmaße für die Handlung **tatsächlich** eingesetzt wird (z. B. Schlag mit dem Cyberarm ja, Tritt mit demselben Cyberarm nein).
- Stärke-/Geschicklichkeitserhöhungen sind **wirkungslos**, wenn sie in einem Cyberschädel eingebaut sind.

#### Sprunghydraulik (Cybergliedmaßen-Zubehör, S. 291)

- Beide Beine benötigen dieselbe Stufe.
- `Stufe` wird als Würfelpoolbonus zur Sprungprobe (S. 95) addiert.
- Jeder Erfolg verlängert einen vertikalen Sprung um `0,1 m` und einen horizontalen Sprung um `0,2 m`.
- Maximale Sprungweite bzw. -höhe erhöht sich um `20 %`.

### 7. Cyberimplantatwaffen: Tarnkeit und Einschränkungen (S. 291–292)

- Implantierte **Pistolen** (aller Art): Tarnkeit erhöht sich um `+2`.
- **Größere Waffen**: Tarnkeit bleibt unverändert, da sie auch implantiert auffällig bleiben.
- **Gewehre und Scharfschützengewehre** können nicht implantiert werden.
- Implantierte Feuerwaffen können per Nebenhandlung *Schnellziehen* bereit gemacht werden.
- Einzige zulässige Modifikationen für implantierte Feuerwaffen: **Lasermarkierer** und **Schalldämpfer**.

### 8. Kompositknochen & Knochenverstärkung – Kampfmodifikatoren (S. 288, 293)

Beide Implantate ändern Schadenswiderstand, Verteidigungswert sowie Schadens-/Angriffswert des waffenlosen Kampfs. Nur eine der drei Kompositknochen-Varianten kann gleichzeitig implantiert sein; Kompositknochen sind nicht mit anderer Bodytech für Knochen (z. B. Knochenverstärkung) kompatibel.

**Kompositknochen (Cyberware, S. 288):**

| Material | Schadenswiderstand | Verteidigungswert | Waffenloser Schadenswert | Waffenloser Angriffswert |
|---|---|---|---|---|
| Kunststoff | +1 | +1 | +1K | +1 |
| Aluminium | +2 | +1 | +2K | +2 |
| Titan | +2 | +2 | +2K | +3 |

**Knochenverstärkung (Bioware, S. 293):**

| Stufe | Schadenswiderstand | Waffenloser Schadenswert | Waffenloser Angriffswert |
|---|---|---|---|
| 1 | +1 | +1K | +1 |
| 2 | +2 | +1K | +2 |
| 3 | +3 | +2K | +2 |
| 4 | +4 | +2K | +3 |

### 9. Reaktions-/Initiative-Boosts: Stapel-Regeln (S. 288–289, 295)

Drei verschiedene Implantate erhöhen Reaktion und Initiativewürfel nach demselben Muster, sind aber **nicht** untereinander kombinierbar (Ausnahme: WiFi-Varianten koppeln sich paarweise und heben den Cap `+4` auf):

- **Reaktionsverbesserung** (Bodytech): `+Stufe` auf Reaktion (Initiativewert ändert sich entsprechend). Kompatibel mit kabellosem Reflexbooster (dann auch Erhöhung über `+4` hinaus möglich).
- **Reflexbooster** (Cyberware): pro Stufe `+1 Reaktion` (mit entsprechender Initiativewert-Erhöhung) und `+1 zusätzlicher Initiativewürfel` (mit zusätzlicher Nebenhandlung). Aktivieren/Deaktivieren = Nebenhandlung. Kompatibel mit kabelloser Reaktionsverbesserung (dann ebenfalls Erhöhung über `+4` möglich).
- **Synapsenbeschleuniger** (Kultivierte Bioware): pro Stufe `+1 Reaktion` (mit Initiativewert-Erhöhung) und `+1 zusätzlicher Initiativewürfel` (mit Nebenhandlung). Kann nicht deaktiviert werden – der Charakter nimmt die Welt dauerhaft in Zeitlupe wahr.

### 10. Standard-Bioware – ausgewählte Formeln (S. 292–294)

Grundprinzip: Bioware erzeugt **geringere Essenzkosten** als Cyberware mit vergleichbarem Effekt, ist aber wegen des Zeitaufwands für die Züchtung **teurer** in Nuyen.

- **Adrenalinpumpe**: Aktiv addiert sie `Stufe` zu Stärke, Geschicklichkeit, Reaktion **und** Willenskraft. Wirkdauer: `[Stufe × 1W6]` Kampfrunden, kann nicht vorzeitig deaktiviert werden. Nach Ablauf: Betäubungsschaden in Höhe der **halben Anzahl an Kampfrunden (aufgerundet)**, in denen die Pumpe aktiv war (Widerstand mit der **natürlichen** Konstitution). *(3. Auflage/Errata; früher: volle Rundenzahl.)* Danach 1 Stunde Regenerationszeit, in der sie nicht aktivierbar ist.
- **Hyperschilddrüse**: `+1` auf Konstitution, Geschicklichkeit, Reaktion und Stärke; der Charakter muss `25 %` mehr für seinen Lebensstil ausgeben (erhöhter Kalorienbedarf).
- **Maßgeschneiderte Pheromone**: `+Stufe` auf Charisma bei Überreden-/Einflussproben, nur wirksam in Riechweite/bequemer Unterhaltungsdistanz. Kein Effekt auf magische Fähigkeiten/Proben.
- **Muskelstraffung**: `+Stufe` auf Geschicklichkeit. Inkompatibel mit anderer geschicklichkeitssteigernder Bodytech (Cyberware Kunstmuskeln, Bioware Hochleistungsgelenke).
- **Muskelverstärkung**: `+Stufe` auf Stärke. Inkompatibel mit anderer stärkesteigernder Bodytech (z. B. Cyberware Kunstmuskeln).
- **Kunstmuskeln** (zum Vergleich, Cyberware): `+Stufe` auf **sowohl** Stärke **als auch** Geschicklichkeit; inkompatibel mit Muskelverstärkung/-straffung.
- **Synthcardium**: `+Stufe` Würfelpoolbonus auf Athletikproben beim Laufen, Schwimmen und Klettern.
- **Thrombozytenfabrik**: Immer wenn der Charakter `≥2` Kästchen Schaden auf dem Körperlichen Zustandsmonitor erleiden würde, wird der Schaden um `1 Kästchen` gesenkt.
- **Orthoskin**: `+Stufe` auf den Verteidigungswert. Inkompatibel mit anderer Bodytech für die Haut (z. B. Cyberware Dermalpanzerung).
- **Toxinextraktor**: Senkt den Schwellenwert einer Toxinwiderstandsprobe (S. 124 f.) um seine Stufe.
- **Lufttröhrenfilter**: `+Stufe` Würfelpoolbonus auf Toxinwiderstandsproben gegen Toxine mit Inhalationsvektor.
- **Symbionten**: `+Stufe` Würfelpoolbonus auf Heil-/Genesungsproben (Körperlich und Betäubung). Nahrungskosten: `Stufe × 200 ¥/Monat`, sofern nicht bereits ein besserer Lebensstil dies abdeckt; ohne Spezialnahrung sterben die Symbionten nach 1 Monat.

### 11. Kultivierte Bioware – ausgewählte Formeln (S. 295)

Kultivierte Bioware wird individuell für den Empfängerkörper gezüchtet; es gibt sie deshalb **nicht gebraucht** (keine "Gebraucht"-Kategorie).

- **Mnemoverstärker**: `+Stufe` Würfelpoolbonus auf Proben mit Wissensfertigkeiten sowie auf gedächtnisbezogene Proben.
- **Reflexrekorder**: Erhöht die Stufe **einer** mit einem Körperlichen Attribut verknüpften Fertigkeit um `1`. Mehrere Implantate für verschiedene Fertigkeiten möglich, aber nicht zwei für dieselbe Fertigkeit.
- **Schadenskompensator**: Der Charakter ignoriert eine Anzahl Schadenskästchen (wählbar Körperlich, Betäubung oder Kombination) in Höhe der Stufe des Kompensators, **bevor** Verletzungsmodifikatoren ermittelt werden.
- **Schlafregulator**: Charakter kommt mit `3 Stunden` Schlaf/Nacht aus; die Zeit bis zum Status *Erschöpft* (S. 54) verdoppelt sich. Heilzeiten werden dadurch nicht beeinflusst.
- **Schmerzeditor** (aktiv): Ignoriert alle Verletzungsmodifikatoren und bleibt bei Bewusstsein, selbst wenn der Betäubungszustandsmonitor voll ausgefüllt ist. Nachteil: Der Charakter spürt seinen tatsächlichen Schadenszustand nicht (nur durch Handlung *Genau beobachten* oder Vitalmonitor-Information).
- **Zerebralbooster**: `+Stufe` auf das Logikattribut.

### 12. Magische Ausrüstung: Foki – Bindungskosten, Preis, Verfügbarkeit (S. 296)

Alle Foki-Werte skalieren mit ihrer **Kraftstufe**:

| Fokus | Bindungskosten (Karma) | Verfügbarkeit | Preis |
|---|---|---|---|
| Geisterfokus | `Kraftstufe × 2` | `(Kraftstufe)L` | `Kraftstufe × 4.000 ¥` |
| Kraftfokus | `Kraftstufe × 6` | `(Kraftstufe + 3)L` | `Kraftstufe × 18.000 ¥` |
| Metamagiefokus | `Kraftstufe × 3` | `(Kraftstufe)L` | `Kraftstufe × 9.000 ¥` |
| Qi-Fokus | `Kraftstufe × 2` | `(Kraftstufe)L` | `Kraftstufe × 3.000 ¥` |
| Verzauberungsfokus | `Kraftstufe × 3` | `(Kraftstufe)L` | `Kraftstufe × 5.000 ¥` |
| Waffenfokus | `Kraftstufe × 3` | `(Kraftstufe + 3)L` | `Kraftstufe × 7.000 ¥` |
| Zauberfokus | `Kraftstufe × 2` | `(Kraftstufe)L` | `Kraftstufe × 4.000 ¥` |

- **Fokusformel** (zur Herstellung nötig): Preis = `Fokuspreis × 0,25`, Verfügbarkeit wie der Fokus selbst.
- **Zauberformeln** (auch für Rituale/alchemistische Zauber): feste Preise nach Kategorie – Heilung 500¥, Illusion 1.000¥, Kampf 2.000¥, Manipulation 1.500¥, Wahrnehmung 500¥.
- **Materialien für Magische Refugien**: Preis = `Kraftstufe × 500 ¥`, Verfügbarkeit = `(Kraftstufe)L`.
- **Reagenzien**: `50 ¥` pro Dram, Verfügbarkeit 2.

### 13. Fahrzeugmodifikationen: Waffenhalterungen (S. 297)

- **Anzahl der Waffenhalterungen** eines Fahrzeugs = `Rumpf ÷ 3` (abgerundet, bezogen auf den **unverstärkten** Rumpfwert).
- **Standard-Waffenhalterung**: max. eine sturmgewehrgroße Waffe + 250 Schuss Munition.
- **Schwere Waffenhalterung**: beansprucht den Platz von zwei Standard-Waffenhalterungen; nimmt jede Waffenart sowie bis zu 500 Schuss Gurtmunition **oder** `[Rumpf]` Lenkraketen auf.
- Alle Waffenhalterungen sind ferngesteuert und bestreichen einen Feuerbereich von `90°` sowohl vertikal als auch horizontal.
- **Manuelle Bedienung** ist als Aufpreis nur bei Fahrzeugen wählbar, nicht bei Drohnen.

### 14. Enterhakenkanone: Trefferschwellenwert (S. 280)

- Schwellenwert der Feuerwaffenprobe, um das gewünschte Ziel zu treffen: `Entfernung in Metern ÷ 20` (aufgerundet).

### 15. DocWagon-Verträge (S. 282) – Leistungsstufen

Strukturierte Rabatt-/Leistungsstufen ohne durchgehende Formel:

| Vertrag | Kostenlose Reanimationen/Jahr | HTR-Gebühr | Stationäre Behandlung |
|---|---|---|---|
| Standard | 0 (5.000 ¥ pro Reanimation/HTR-Einsatz) | voller Preis | voller Preis |
| Gold | 1 | −50 % | −10 % |
| Platin | 4 | kostenlos (Kompensationszahlungen für getötete Mitarbeiter weiterhin fällig) | kostenlos |
| Superplatin | 5 | kostenlos, keine Kompensationszahlungen | kostenlos |

Garantierte Ankunftszeit innerhalb vertraglich abgedeckter Großstadtregionen: unter 10 Minuten.

---

### Nicht erfasst

Folgende Inhalte im Bereich S. 280–310 wurden bewusst **nicht** übernommen, da sie reine Item-Kataloge ohne verallgemeinerbare Formel sind oder außerhalb des Regelbereichs liegen:

- Einzelbeschreibungen von Einbruchswerkzeug, Industriechemikalien, Überlebens- und Taucherausrüstung (S. 280–282) – nur Preis-/Verfügbarkeitstabellen, außer der bereits erfassten Enterhakenkanonen-Formel.
- Zahlreiche Headware-/Augen-/Ohren-Cyberware-Einträge, die nur "implantierte Version von [Basisgegenstand, S. 275–278]" ohne eigene neue Mechanik sind (Bildverbindung, Blitzkompensation, Infrarotsicht, Restlichtverstärkung, Retinaduplikat, Sichtverbesserung/-vergrößerung, Smartlink, Audioverbesserung, Audioverbindung, Balanceverstärker, Dämpfer, Richtungsdetektor, Selektiver Geräuschfilter).
- Die Kapazitätspool-Mechanik selbst (wie viel Kapazität ein Basissystem wie Cyberaugen, Cyberohren, Kopf oder Cybergliedmaße für Zubehör mit "Kapazitätskosten" bereitstellt) wird in diesem Seitenbereich vorausgesetzt, aber nicht hergeleitet – die Grundregel liegt vermutlich vor S. 280.
- Cyberimplantatwaffen-Werte-Tabelle (Schadens-/Angriffswerte je Einzelwaffe, S. 292) – reiner Waffenkatalog.
- Toxine/Drogen-Verfügbarkeits- und Preistabellen (S. 295 f.) – reiner Preiskatalog; die zugehörigen Widerstandsproben-Formeln stehen auf S. 124 f. (außerhalb dieses Bereichs).
- Sämtliche Einzelbeschreibungen von Fahrzeugen, Motorrädern, Booten, U-Booten, Flugzeugen, Rotormaschinen und Drohnen (S. 297–305) sowie die "Ähnliche Modelle"-Tabelle (S. 298) – reine Flavourtexte/Preiskataloge. *(Einzige Regel-Errata der 3. Auflage in diesem Bereich: Ares Dragon (S. 305) hat **Rumpf 22** statt 16.)*
- Die Bedeutung der einzelnen Fahrzeug-Statblock-Werte (Handling, Beschleunigung, Geschwindigkeitsintervall, Höchstgeschwindigkeit, Rumpf, Panzerung, Pilot, Sensor, Sitze) wird hier nur tabellarisch aufgelistet, aber nicht mit Berechnungsformeln (Fahren-Proben, Autopilot-Proben, Schadenswiderstand etc.) hergeleitet – diese Regeln sind offensichtlich auf späteren Seiten (jenseits S. 305) zu finden.
- Ab Buchseite 306 beginnt das Kapitel "Deutschland in den Schatten" (Metaplot/Setting-Beschreibung der ADL) – enthält keinerlei Spielregeln oder Berechnungen und wurde komplett ausgelassen.

---

## Teil 9: Tabellen-Anhang (Buchseiten 310–339)

<sub>Quelle-Chunk: `docs/sr6/sr6_calc_p311-340.md` — Originaltitel: Shadowrun 6 – Regeln mit Berechnungen (Grundregelwerk, Buchseiten 310–339)</sub>

Quelle: Sub-PDF `sr6_p311-340.pdf` (physische PDF-Seiten 311–340 der deutschen Ausgabe), entsprechend den im Fußtext gedruckten Buchseiten **310–339** (Buchseite = PDF-Seite − 1 in diesem Abschnitt). Der Bereich deckt das Ende des Settingkapitels **DEUTSCHLAND IN DEN SCHATTEN** (S. 310–322: ADL-Städte, Brennpunkt Hamburg/Wildost — reine Fluff-Beschreibung ohne Spielmechanik) sowie den kompletten Anhang **TABELLEN** (S. 323–335) ab. Ab S. 336 beginnt der alphabetische Index (kein Regelinhalt). Eine „Fahrzeuge und Drohnen"-Ausrüstungskapitel-Fortsetzung wie ursprünglich erwartet war in diesem Seitenbereich **nicht** mehr vorhanden — das Kapitel endet vor S. 310; die einschlägigen Rigger-/Drohnen-Formeln tauchen jedoch im Tabellen-Anhang (S. 197–201) wieder auf und sind unten vollständig erfasst.

Buchseitenzahlen sind in Klammern angegeben, z. B. (S. 235). Der Tabellen-Anhang fasst Regeln zusammen, die im Buch bereits an früherer Stelle (den in Klammern zitierten Seiten) eingeführt wurden; hier wird nur erfasst, was **nicht** bereits in den vorangehenden Teilen dieses Dokuments dokumentiert ist. Reine Duplikate werden am Ende unter „Nicht erfasst" aufgelistet.

---

### 1. Handlungen – vollständige Liste (S. 42, Tabellenanhang S. 323)

Vollständige Liste aller Neben- und Haupthandlungen (Grundregel „1 Nebenhandlung + 1 Haupthandlung pro Kampfrunde", Handlungstausch 1:4, s. bereits dokumentiert). Die Buchstaben in Klammern hinter jeder Handlung sind im vorliegenden Auszug nicht weiter legendiert (vermutlich auf S. 42 selbst erklärt, außerhalb dieses Seitenbereichs); sie werden hier unverändert wiedergegeben.

**Nebenhandlungen:** Abfangen (J), Aufstehen (I), Ausweichen (J), Bewegen (I), Blocken (I), Drohne befehligen (I), Fokus aktivieren/deaktivieren (I), Gegenstand fallen lassen (J), Geist befehligen (I), Geist entlassen (I), Gerätemodus ändern (J), In Deckung gehen (I), Mehrfachangriffe (I), Schnellziehen (I), Sich hinwerfen (J), Smartgun nachladen (I), Volle Deckung (J), Wahrnehmung verlagern (J), Weghechten (J), Ziel ansagen (I), Zielen (I), Zu Fall bringen (I).

**Haupthandlungen:** Angriff (I), Antimagie (J), Astrale Projektion (I), Einfaches Gerät verwenden* (I), Fertigkeit einsetzen (I), Gegenstand aufheben/ablegen (I), Geist herbeirufen (I), Geist verbannen (I), Genau beobachten (I), Hineinspringen (I), Manifestieren (I), Reinigen (I), Sprinten (I), Unterstützen (I), Volle Abwehr (I), Waffe bereit machen (I), Waffe nachladen (I), Zauber wirken (I).

*Mit DNI (Direktes Neuralinterface): nur Nebenhandlung.

---

### 2. Edge bei sozialen Proben (S. 50, Tabellenanhang S. 324)

Situative Edge-Vergabe bei sozialen Proben, aufgeschlüsselt nach Teilfertigkeit. Jeweils Bedingungen, unter denen **Sprecher** bzw. **Zuhörer** 1 Edge erhält.

**Allgemein**

| Edge für den Sprecher | Edge für den Zuhörer |
|---|---|
| Der Sprecher wird von einer Person vorgestellt, der der Zuhörer vertraut. | Der Zuhörer wurde vor dem Sprecher gewarnt. |
| Der Zuhörer schenkt Personen wie dem Sprecher generell Glauben. | Der Sprecher gehört einer Gruppe an, gegen die der Zuhörer starke Vorurteile hat. |
| Das Aussehen des Sprechers passt perfekt zu seiner Rolle. | Das Aussehen des Sprechers passt überhaupt nicht zu seiner Rolle. |
| Der Zuhörer hegt romantische Gefühle für den Sprecher. | Der Zuhörer hat eine starke persönliche Abneigung gegen den Sprecher. |
| Der Zuhörer kann eindeutig erkennen, wie er durch das Gesagte profitieren würde. | Der Zuhörer sieht ein hohes Risiko in dem, was der Sprecher sagt. |
| Die Gedanken und/oder Gefühle des Zuhörers stehen unter magischer Kontrolle. | — |

**Einschüchtern**

| Edge für den Sprecher | Edge für den Zuhörer |
|---|---|
| Der Sprecher ist dem Zuhörer eindeutig körperlich überlegen. | Der Zuhörer ist dem Sprecher eindeutig körperlich überlegen. |
| Der Zuhörer kann sich der Situation nicht einfach entziehen. | Der Zuhörer weiß, dass bereits Hilfe unterwegs ist. |

**Führen**

| Edge für den Sprecher | Edge für den Zuhörer |
|---|---|
| Die Personen, die der Sprecher führen will, vertrauen ihm. | Der Zuhörer hat einen Grund, dem Sprecher zu misstrauen. |
| Der Sprecher ist ranghöher als der Zuhörer. | Der Zuhörer ist ranghöher als der Sprecher. |

**Gebräuche**

| Edge für den Sprecher | Edge für den Zuhörer |
|---|---|
| Der Sprecher hat auf dem betreffenden Gebiet deutlich mehr Lebenserfahrung. | Der Zuhörer hat auf dem betreffenden Gebiet deutlich mehr Lebenserfahrung. |
| Der Sprecher wird von einer Person vorgestellt, der der Zuhörer vertraut. | Der Sprecher steht mit Personen in Verbindung, die der Zuhörer nicht mag oder denen er misstraut. |

**Überreden**

| Edge für den Sprecher | Edge für den Zuhörer |
|---|---|
| Der Zuhörer ist verzweifelt. | Der Zuhörer befindet sich in einer sicheren Position und scheut Risiken. |
| Der Sprecher hat überzeugende Beweise für seine Behauptungen. | Der Sprecher wurde bei einer offensichtlichen Lüge ertappt. |

**Verhandeln**

| Edge für den Sprecher | Edge für den Zuhörer |
|---|---|
| Der Sprecher ist verzweifelt. | Dem Sprecher mangelt es an Erfahrung oder Expertise für den Auftrag. |
| Der Sprecher teilt wichtige Informationen mit dem Zuhörer, die diesem zuvor unbekannt waren. | Der Sprecher teilt Informationen mit dem Zuhörer, die für diesen belanglos oder schädlich sind. |

---

### 3. Statusliste – Ergänzungen (S. 53, Tabellenanhang S. 325)

Der Tabellenanhang enthält die vollständige Statusliste; die meisten Einträge decken sich mit den bereits in Teil 1, Abschnitt 9 dokumentierten Werten. Drei Status fehlten dort noch:

- **Brennend #**: `(#)K Schaden`, dem jede Runde widerstanden werden muss, solange der Status aktiv ist. Status beenden z. B. mit Probe auf `Geschicklichkeit + Reaktion` (Schwellenwert 2). Die Status *Nass* und/oder *Unterkühlt* heben *Brennend* auf und umgekehrt.
- **Geräuschlos (Verbessert) #**: wie *Geräuschlos* (Zahl = Schwellenwert für Wahrnehmungsprobe, um den Charakter zu hören), aber zusätzlich auch wirksam gegen Mikrofone usw.
- **Verschleiert**: kein Wechsel zwischen Astral- und physischer Ebene möglich; nur astrale Wahrnehmung möglich.

---

### 4. Rassentypische Vorteile (S. 66, Tabellenanhang S. 326)

Ergänzung zur bereits dokumentierten Attribute-nach-Metatyp-Tabelle: kostenlose Vorteile, die jeder Metatyp automatisch erhält (zählen laut S. 68 nicht gegen das reguläre Vor-/Nachteile-Limit).

| Metatyp | Vorteile durch Metatyp |
|---|---|
| Mensch | Keine |
| Elf | Restlichtverstärkung |
| Ork | Restlichtverstärkung, Robust Gebaut 1 |
| Troll | Dermalablagerungen, Infrarotsicht, Robust Gebaut 2 |
| Zwerg | Infrarotsicht, Toxinresistenz |

---

### 5. Fertigkeitenliste – Fertigkeit-Attribut-Zuordnung (S. 94, Tabellenanhang S. 327)

Vollständige Zuordnung aller Fertigkeiten zu ihrem Primärattribut sowie ob die Fertigkeit ungeübt (ohne Fertigkeitswert, `Attribut − 1`, s. bereits dokumentiert) eingesetzt werden darf.

| Fertigkeit | Primärattribut | Ungeübt möglich? |
|---|---|---|
| Astral | Intuition | Nein |
| Athletik | Geschicklichkeit | Ja |
| Beschwören | Magie | Nein |
| Biotech | Logik | Nein |
| Cracken | Logik | Nein |
| Einfluss | Charisma | Ja |
| Elektronik | Logik | Ja |
| Exotische Waffen | Geschicklichkeit | Nein |
| Feuerwaffen | Geschicklichkeit | Ja |
| Heimlichkeit | Geschicklichkeit | Ja |
| Hexerei | Magie | Nein |
| Mechanik | Logik | Ja |
| Nahkampf | Geschicklichkeit | Ja |
| Natur | Intuition | Ja |
| Steuern | Reaktion | Ja |
| Tasken | Resonanz | Nein |
| Überreden | Charisma | Ja |
| Verzaubern | Magie | Nein |
| Wahrnehmung | Intuition | Ja |

---

### 6. Strukturstufen (S. 117, Tabellenanhang S. 328)

Materialstärke von Barrieren/Objekten als Widerstandsstufe (relevant für *Durchbrechen von Barrieren* u. Ä.).

| Stufe | Art |
|---|---|
| 1 | Papier (dünn) |
| 2 | Glas (dünn) |
| 3 | Papierstapel (1 cm) |
| 4 | Glas (1 cm) |
| 5 | Mörtel, hohle Holztür, Leichtbaumöbel |
| 6 | Gipskarton |
| 7 | Massive Holztür, Massivholzmöbel |
| 8 | Elektronische Ausrüstung, Absperrketten |
| 9 | Sicherheitsglas, Blech |
| 10 | Densiplast, dünner Baum |
| 11 | Holztür mit Metallkern oder -verkleidung, Panzerglas |
| 12 | Ziegel, dicker Baum |
| 13 | Kevlar-Wandplatte |
| 14 | Plasbeton |
| 15 | Beton |
| 16 | Sicherheitstür |
| 17 | Metallträger, dicke Metallplatte |
| 18 | Verkleidung aus abgereichertem Uran |
| 19 | Stahlbeton |
| 20 | Bunker |

---

### 7. Abweichung – geworfene/abgefeuerte Wurfwaffen (S. 118, Tabellenanhang S. 328)

Formel für die Abweichung von Granaten/Wurfwaffen und Werfer-Sprengköpfen bei Fehlwurf/-schuss, abhängig von der Reichweitenkategorie.

| Reichweite | Abweichung in Metern (geworfen)* | Abweichung in Metern (abgefeuert) |
|---|---|---|
| Sehr nah | `2W6 − 4 − Erfolge` | `2W6 + 2 − Erfolge`† |
| Nah | `2W6 − 2 − Erfolge` | `2W6 − Erfolge` |
| Mittel | `2W6 − Erfolge` | `2W6 + 2 − Erfolge` |
| Weit** | `2W6 + 2 − Erfolge` | `2W6 + 4 − Erfolge` |
| Sehr weit** | `2W6 + 4 − Erfolge` | `2W6 + 6 − Erfolge` |

\* Geworfene Granaten haben die Angriffswerte Waffenlos/Waffenlos−1/Waffenlos−6/−/− (je Reichweitenkategorie). Sinkt der Angriffswert auf 0, kann der Charakter die Granate auf diese Entfernung nicht werfen.
\*\* Die meisten Charaktere erreichen diese Reichweiten mit einer geworfenen Waffe nicht.
† Die meisten von Werfern abgefeuerten Sprengköpfe explodieren auf diese Entfernung nicht, weil die Sicherheitseinstellungen das verhindern.

---

### 8. Radius, Wirkung und Dauer von Gasangriffen (S. 120, Tabellenanhang S. 328)

Wie viele Kampfrunden ein Ziel nach dem Verlassen der Gaswolke noch (abgestuft) unter der Wirkung steht, gestaffelt nach Vielfachem des Basisradius.

| Radius | Runden mit voller Wirkung | Runden mit halber Wirkung | Runden mit einem Viertel der Wirkung | Runden ohne Wirkung |
|---|---|---|---|---|
| Radius | 1–5 | 6–8 | 9–10 | 11+ |
| Radius × 2 | — | 1–5 | 6–8 | 9+ |
| Radius × 3 | — | 1–4 | 5–6 | 7+ |
| Radius × 4 | — | — | 1–5 | 6+ |

---

### 9. Objektwiderstand (S. 132, Tabellenanhang S. 329)

Widerstandsstufe von Objekten gegen manipulative Zauber (z. B. Objekt verändern).

| Art des Objekts | Stufe |
|---|---|
| Natürliche Objekte (Bäume, Steine, Erde, Holz, unbehandeltes Wasser, von Hand kaltverformtes Metall) | 3 |
| Hergestellte einfache Objekte und Materialien (Ziegel, Glas, Leder, Papier, einfache Kunststoffe) | 6 |
| Hightech-Objekte und -Materialien (fortschrittliche Kunststoffe, Legierungen, Beton, elektronische Ausrüstung, Feuerwaffen, Sensoren) | 9 |
| Hochgradig verarbeitete Objekte (Kommlinks, Cyberdecks, Drohnen, Fahrzeuge, komplexer Giftmüll, Cheez-Bitz) | 15+ |

---

### 10. Ergebnisse von Wahrnehmungszaubern (S. 143, Tabellenanhang S. 329)

Informationsgehalt eines Wahrnehmungszaubers gestaffelt nach Nettoerfolgen.

| Nettoerfolge | Ergebnis |
|---|---|
| 1 | Allgemeine Informationen ohne Details (z. B. „zwei Lebensformen sind anwesend, es ist ein medizinisches Gerät, ein Zauber ist aktiv"). |
| 2 | Weitere Informationen über Form und Funktion ohne spezifische Details (z. B. „beide Lebensformen sind Tiere, das Gerät ist ein Diagnosegerät, der Zauber ist ein Illusionszauber"). |
| 3 | Spezifische Details (z. B. „die Tiere sind Hunde, das Gerät führt einen internen Scan durch, der Zauber ist Verwirrung"). |
| 4 | Entscheidende Details auch über Emotionen und Funktionen (z. B. „die Hunde sind wütend und hungrig, das Gerät funktioniert nur teilweise, der Zauber wurde von einem mächtigen Zauberer gewirkt"). |

---

### 11. Ergebnisse der Geistessonde (S. 144, Tabellenanhang S. 329)

| Nettoerfolge | Ergebnis |
|---|---|
| 1–2 | Der Beobachter kann nur die oberflächlichen Gedanken des Ziels lesen. |
| 3–4 | Der Beobachter kann alles herausfinden, was das Ziel bewusst weiß, und Erinnerungen aus den letzten 72 Stunden lesen. |
| 5+ | Der Beobachter kann ins Unterbewusstsein des Ziels eindringen und Informationen erhalten, die dem Ziel selbst nicht bewusst sind (z. B. psychologische Eigenheiten, tiefe Ängste, verschüttete Erinnerungen). |

---

### 12. Askennen / Astrale Wahrnehmung von Personen (S. 162, Tabellenanhang S. 329)

Informationsgehalt beim Askennen (astrales Wahrnehmen einer Aura), gestaffelt nach Anzahl der Erfolge.

| Erfolge | Informationen |
|---|---|
| 0 | Keine |
| 1 | Allgemeiner Gesundheitszustand des Ziels (gesund/krank); allgemeine Gefühlslage (glücklich, traurig, wütend usw.); ob das Ziel Erwacht oder mundan ist. |
| 2 | Vorhandensein und Lage von Standard-Cyberware; Vorhandensein und generelle Art aktiver Magie (Feuergeist, Manipulationszauber, Kraftfokus usw.); bereits einmal gesehene Auren können trotz Verbergung/Verkleidung mit einer Probe auf Erinnerungsvermögen (S. 37) wiedererkannt werden. |
| 3 | Vorhandensein und Lage von Alpha-Cyberware; ob Essenz und Magie des Ziels höher/niedriger/gleich der Magie des Wahrnehmenden sind; ob die Kraftstufe des Ziels höher/niedriger/gleich der Magie des Wahrnehmenden ist; allgemeine Diagnose gesundheitlicher Beeinträchtigungen (Krankheiten, Toxinwirkungen); astrale Signaturen auf dem Ziel. |
| 4 | Vorhandensein und Lage von Beta-Cyberware und Bioware; exakte Essenz-, Magie- und/oder Kraftstufe des Ziels; generelle Ursache einer bestehenden astralen Signatur (Kampfzauber, Luftgeist usw.). |
| 5+ | Vorhandensein und Lage von Delta-Cyberware, Gentech und Nanotech; genaue Diagnose von Krankheiten/Giften, die auf das Ziel wirken; ob das Ziel Technomancer oder [Text im Scan unscharf, vermutlich Adept] ist. |

---

### 13. Astralkampf (S. 163, Tabellenanhang S. 330)

Formeln für Kampf auf der Astralebene (Geister, astral projizierende Magier).

- **Angriffswert**: `Magie + Traditionsattribut`
- **Verteidigungswert**: `Intuition + natürliche Panzerung + Panzerungseffekte`
- **Initiative**: `Logik + Intuition + 2W6` ⚠️ **Fehler im Buch:** Die Errata der 3. Auflage korrigieren die astrale Initiative auf `Logik + Intuition + 3W6` (S. 163), doch diese Anhang-Tabelle auf S. 330 wurde bei der Korrektur übersehen und zeigt weiterhin `2W6`. **Für den NPC-Generator gilt `3W6`.**

**Würfelpools**

| Probe | Würfelpool |
|---|---|
| Waffenloser Kampf | Astral + Willenskraft |
| Waffenfoki | Nahkampf + Willenskraft |
| Spruchzauberei | Hexerei + Magie |
| Verteidigung | Logik + Intuition |
| Schadenswiderstand | Willenskraft |

**Schadenswerte**

| Angriffsart | Schaden |
|---|---|
| Waffenlos | `Traditionsattribut ÷ 2` (aufgerundet) |
| Waffenfokus | nach Waffe |

Der Angreifer wählt aus, ob er Körperlichen oder Betäubungsschaden verursacht.

---

### 14. Astrales Spurenlesen (S. 163, Tabellenanhang S. 330)

Schwellenwert-Modifikatoren für die Probe, eine astrale Spur zu verfolgen.

| Situation | Schwellenwert-Modifikator |
|---|---|
| Pro Stunde, seit die astrale Verbindung aktiv war | +1 |
| Ziel befindet sich hinter einer Manabarriere | `+ Kraftstufe der Barriere` |
| Auffinden des Beschwörers durch Geist | +2 |

---

### 15. Rauschen (S. 177, Tabellenanhang S. 330)

Rauschenwert (Matrix-Signalverschlechterung) nach physischer Entfernung bzw. Hindernissen; addiert sich zum Grundrauschen der Verbindung.

| Physische Entfernung zum Ziel/Hindernisse | Rauschenwert |
|---|---|
| Direktverbindung (jede Entfernung) | 0 |
| Bis 100 m | 0 |
| 101 – 1.000 m | 1 |
| 1.001 – 10.000 m | 3 |
| 10.001 – 100 km | 5 |
| Mehr als 100 km | 8 |
| Dichtes Laubwerk | 1 pro 5 m |
| Faradaykäfig | kein Signal, keine Handlung |
| Süßwasser | 1 pro 10 cm |
| Störsender | 1 pro Erfolg bei der Handlung *Signal stören* |
| Metallüberzogene Erde oder Mauer | 1 pro 0,5 m |
| Salzwasser | 1 pro cm |
| Spam-Zone oder Matrixloch | Stufe (des Effekts) |
| WiFi-Abschirmung (z. B. Tapete oder Farbe) | Stufe (des Effekts) |

---

### 16. Matrixhandlungen – vollständige Liste (S. 185, Tabellenanhang S. 330)

Analog zur physischen Handlungsliste (Abschnitt 1): alle Matrix-Neben- und -Haupthandlungen.

**Nebenhandlungen:** Host betreten/verlassen (J), Icon verändern (I), Interfacemodus wechseln (J), Matrixattribute austauschen (J), Matrixwahrnehmung* (J), Nachricht übermitteln (J).

**Haupthandlungen:** Ausstöpseln (J), Befehl vortäuschen (I), Brute Force (I), Datei cracken (I), Datei editieren (I), Datei verschlüsseln (J), Datenbombe entschärfen (I), Datenbombe legen (J), Datenspike (I), Gerät formatieren (I), Gerät neu starten (I), Gerät steuern (I), Hineinspringen (I), Hintertür benutzen (I), Icon aufspüren (I), Matrixsignatur löschen (I), Matrixsuche (I), Matrixwahrnehmung (J), Overwatch-Wert bestimmen (J), Programm abstürzen lassen (I), Prüfsummensuche (I), Signal stören (I), Sondieren (I), Teergrube (I), Übertragung abfangen (J), Verstecken (J), Volle Matrixabwehr (J).

\* In VR.

---

### 17. Matrixattribute und geistige Attribute (S. 189, Tabellenanhang S. 330)

Entsprechung zwischen Matrixattributen (von Geräten/Icons) und geistigen Attributen (von Personen/Personas) — zentral für alle Proben, bei denen ein Charakter mit seinen geistigen Attributen anstelle eines Geräts agiert (z. B. hineingesprungene Rigger, Technomancer).

| Matrixattribut | Geistiges Attribut |
|---|---|
| Gerätestufe | Resonanz |
| Angriff | Charisma |
| Schleicher | Intuition |
| Datenverarbeitung | Logik |
| Firewall | Willenskraft |

---

### 18. Riggerhandlungen – vollständige Liste (S. 199, Tabellenanhang S. 331)

| Handlung | Handlungsart | Wofür? |
|---|---|---|
| Angriff (S. 44) | Haupt (I) | Angriffe mit Fahrzeug oder Fahrzeugwaffe. |
| Drohne befehligen (S. 43) | Neben (I) | Senden eines Befehls an eine oder mehrere Drohnen. |
| Fertigkeit einsetzen (S. 44) | Haupt (I) | Handling-Proben u. Ä. |
| Gerät neu starten (S. 181) | Haupt (I) | Auswerfen eines Hackers. |
| Hineinspringen (S. 45/182) | Haupt (I) | Das, was nur ein Rigger kann. |
| Interfacemodus wechseln (S. 182) | Neben (I) | Wechsel zwischen Riggen in AR und VR. |
| Matrixattribute austauschen (S. 182) | Neben (J) | Austauschen von Datenverarbeitung und Firewall auf der Riggerkonsole. |
| Verstecken (S. 184) | Haupt (J) | Verstecken der eigenen Persona und/oder der Persona eines Fahrzeugs/einer Drohne. |
| Volle Matrixabwehr (S. 184) | Haupt (J) | Verteidigung gegen Hacker. |

---

### 19. Riggerkontrolle – Attributsubstitution beim Hineinspringen (S. 197, Tabellenanhang S. 330)

Beim Hineinspringen (Rigger übernimmt ein Fahrzeug/eine Drohne per VR) werden die eigenen körperlichen durch geistige Attribute ersetzt:

| Normales Attribut | Hineingesprungenes Attribut |
|---|---|
| Konstitution | Willenskraft |
| Geschicklichkeit | Logik |
| Reaktion | Intuition |
| Stärke | Charisma |

---

### 20. Würfelpools und Werte für Rigger und ihre Fahrzeuge (S. 200, Tabellenanhang S. 331)

Zentrale Formeltabelle für Fahrzeugkampf/-proben, je nach Steuerungsmodus.

*(Fassung 3. Auflage/Errata — die Anhang-Tabelle S. 331 wurde bei der Errata mit korrigiert und um *Heimlichkeit*/*Wahrnehmung* erweitert.)*

| Würfelpool/Wert | Manuelle/AR-Steuerung | Hineingesprungen (VR) † |
|---|---|---|
| Initiative | `Reaktion + Intuition + 1W6*` | `Intuition + Intuition + 2W6/3W6` (kaltes/heißes Sim) †† |
| Angriffswert | `Steuern + Sensor` | `Steuern + Sensor` |
| Verteidigungswert | `Steuern + Panzerung` | `Steuern + Panzerung` |
| Handlingprobe | `Steuern + Reaktion*` | `Steuern** + Intuition` |
| Angriffsprobe (Fahrzeug als Waffe) | `Steuern + Reaktion*` | `Steuern** + Intuition` |
| Angriffsprobe (Fahrzeugwaffe) | `Mechanik + Logik` | `Mechanik** + Logik` |
| Verteidigungsprobe | `Steuern + Reaktion*` | `Steuern** + Intuition` |
| Heimlichkeit | `Heimlichkeit + Geschicklichkeit` | `Heimlichkeit** + Logik` |
| Wahrnehmung | `Wahrnehmung + Intuition` | `Wahrnehmung** + Sensor` |
| Schadenswiderstandsprobe | `Rumpf` | `Rumpf` |
| Zustandsmonitor | `[Rumpf ÷ 2, aufgerundet] + 8` Kästchen | `[Rumpf ÷ 2, aufgerundet] + 8` Kästchen |

\* Bei manueller Steuerung gelten eventuelle Boni auf Reaktion und Initiative durch Bodytech.
\*\* `+ Stufe der Riggerkontrolle` (in der 3. Auflage nur noch in der VR-Spalte, nicht mehr bei Angriffs-/Verteidigungswert).
† *Steuern in VR ohne Riggerkontrolle*: gleiche Würfelpools wie „Hineingesprungen (VR)", aber ohne Riggerkontrolle-Boni.
†† Kabelverbindung angenommen; per WiFi hineingesprungen: Initiative = `Datenverarbeitung + Intuition + 2W6/3W6`.

---

### 21. Würfelpools von autonomen Drohnen (S. 201, Tabellenanhang S. 330)

Formeln für Drohnen, die ohne Rigger-Steuerung (Pilotprogramm) agieren.

| Wert | Berechnung |
|---|---|
| Angriffswert | Montierte Waffe bzw. `Manövrieren + Sensor` |
| Verteidigungswert | `Manövrieren + Panzerung` |
| Rigger-Initiative | `Datenverarbeitung + Intuition + 2W6/3W6*` |
| Drohnen-Initiative | `Pilot × 2 + 3W6` |
| Angriffs-Würfelpool | `[Waffe] Zielerfassung + Sensor` |
| Verteidigungs-Würfelpool | `Ausweichen + Pilot` |
| Heimlichkeit | `Stealth + Pilot` |
| Wahrnehmung | `Clearsight + Sensor` |

\* Für das Erteilen von Befehlen (kaltes/heißes Sim) bzw. für in Drohnen hineingesprungene Rigger.
*(3. Auflage/Errata: Angriffswert `+ Sensor` statt `+ Pilot`; Zeilen* Heimlichkeit */* Wahrnehmung *aus der Fließtext-Fassung S. 201 ergänzt.)*

---

### 22. Änderungen der Reputation (S. 235, Tabellenanhang S. 334)

Konkrete Reputationsdeltas für typische Handlungen (Reputation als laufender Charakterwert, relevant für Job-Angebote/NPC-Beziehungen).

| Aktion | Reputationsänderung |
|---|---|
| An gewaltsamer Auseinandersetzung in der Öffentlichkeit beteiligt, bei der ein Unbeteiligter zu Tode kommt | −1 |
| An gewaltsamer Auseinandersetzung in der Öffentlichkeit beteiligt, bei der mehrere Unbeteiligte zu Tode kommen | −3 |
| Tötet Polizisten und wird dabei gesehen | −2 |
| Hat Leuten in Not Schaden zugefügt oder gefoltert | −1 |
| Hat eine unschuldige Person entführt | −1 |
| Hat einen Deal mit Mr Johnson nicht eingehalten | −1 |
| Hat verletzten Passanten Erste Hilfe geleistet und wurde dabei gesehen | +1 |
| Hat einen Teil seines Geldes Unterprivilegierten überlassen | +1 |
| Hat bei der Arbeit für Leute, die nicht reich oder mächtig sind, Preisnachlass gewährt | +1 |
| Hat ein altes Versprechen eingelöst, ohne Geld dafür zu nehmen | +1 |
| Hat eine potenziell gewalttätige Situation entschärft | +1 |
| Hat eine beliebte berühmte Person aus der Not gerettet | +2 |

---

### 23. Fahndungsstufe (S. 236, Tabellenanhang S. 334)

#### Fahndungsstufen-Modifikatoren

Modifikatoren auf die (nicht näher spezifizierte, vermutlich an früherer Stelle im Buch definierte) Fahndungsstufenprobe.

| Steigernde Umstände | Modifikator |
|---|---|
| Spielsitzung beinhaltete exzessive Gewalt | +1 |
| Spielsitzung beinhaltete Mord | +1 |
| Spielsitzung beinhaltete feindseligen Kontakt mit reichen und/oder prominenten Individuen | +1 |
| Spielsitzung beinhaltete direkten Kontakt mit einem erwachsenen Drachen | +1 |
| Spielsitzung beinhaltete direkten Kontakt mit einem Großen Drachen | +2 |
| Spielsitzung beinhaltete Medienberichte (inkl. Matrixstream) über die Runneraktivitäten | +1 |
| Team hat einen oder mehrere Runner mit Reputation > +10 oder < −10 | +1 |

| Senkende Umstände | Modifikator |
|---|---|
| Die Runner sind illegalen Aktivitäten nachgegangen, ohne Aufmerksamkeit zu erregen | −1 |
| Mr Johnson hat seine Beziehungen spielen lassen, um Aspekte des Runs zu vertuschen | −1 |
| Die Runner haben ausreichend Bestechungsgelder gezahlt, um die Sache zu vertuschen | −1 |
| Die Runner haben eine Connection bei der Polizei gewonnen/genutzt, um ihre Spuren zu verwischen | −1 |
| Den Runnern wird genug Wohlwollen entgegengebracht, um Beteiligung an schlimmen Dingen unwahrscheinlich erscheinen zu lassen | −1 |
| Team hat einen oder mehrere Runner mit Reputation > −5 und keine Runner mit Reputation > +5 | −1 |

#### Auswirkungen der Fahndungsstufe

| Fahndungsstufe | Auswirkung |
|---|---|
| 0–3 | Keine Auswirkungen |
| 4–6 | Reaktionszeiten der Polizei um 25 % verringert |
| 7–9 | Reaktionszeiten der Polizei um 50 % verringert |
| 10 | Die SIN der Runner mit der niedrigsten Stufe gilt als verbrannt (kriminell im System erfasst); löst bei Verwendung einen Alarm aus. |
| 11–13 | Zwei zusätzliche Gesetzeshüter gehen in jeden Einsatz, der mit den Runnern zu tun hat. |
| 14–16 | Die Runner stehen auf der Liste der Meistgesuchten eines Polizeikonzerns, eines der Großen Zehn oder einer einflussreichen Nation; Verfolgung kann über nationale/Konzerngrenzen hinausgehen (je nach Abkommen). |
| 17+ | Fahndungsdruck wird intensiviert und an eine Eliteeinheit übertragen (z. B. Rote Samurai, Sioux Wildcats); Verfolgung erfolgt grenzenlos. |

---

### 24. Detektoren und Scanner (S. 243, Tabellenanhang S. 335)

#### Modifikatoren für chemische Detektoren

| Situation | Würfelpool-Modifikator |
|---|---|
| Pro 10 Schuss Munition | +1 |
| Pro Granate | +1 |
| Pro 2 Stufen Standard-(Nicht-Plastik-)Sprengstoff | +1 |
| Pro 4 Stufen Plastiksprengstoff | +1 |
| Sprengstoff/Munition in geschlossenem Plastikbehälter | −1 |

#### Cyberwarescanner

| Gegenstand | Schwellenwert |
|---|---|
| Standard-Cyberware, Waffen | 1 |
| Alphaware, andere Gegenstände | 2 |
| Betaware | 3 |
| Deltaware | 5 |

| Situation | Schwellenwert-Modifikator |
|---|---|
| 1 oder 2 Implantate/Gegenstände | +3 |
| 3 oder 4 Implantate/Gegenstände | +2 |
| 5 oder 6 Implantate/Gegenstände | +1 |
| 7+ Implantate/Gegenstände | − |

---

### 25. Verfügbarkeit – Stufenbedeutung (S. 245, Tabellenanhang S. 335)

Beschreibung, was die numerische Verfügbarkeitsstufe (Kaufschwellenwert für Ausrüstung) inhaltlich bedeutet.

| Stufe | Bedeutung |
|---|---|
| 1 | Praktisch überall erhältlich, notfalls ein paar Straßen weiter. |
| 2 | Braucht ein spezialisiertes Fachgeschäft (nicht im nächsten Stuffer Shack). |
| 3 | Braucht ein Fachgeschäft; relativ kleine Stückzahl, evtl. muss man im Sprawl suchen. |
| 4 | Nur bei Spezialhändlern; nicht für den Massenmarkt, spezialisierte Funktion. |
| 5 | Wirklich spezielle/Sammlerstücke für einen Nischenmarkt, aber auffindbar. |
| 6 | Recht seltene, oft handgefertigte Dinge; kleine Werkstätten/spezielle Hersteller, notfalls über Großhändler. |
| 7 | Nicht vom Stapel erhältlich, nur auf Bestellung spezialgefertigt. |
| 8 | Wie 7, zusätzlich Termin nötig und gründliche Hintergrundüberprüfung. |
| 9+ | Exklusivste Dinge; man muss jemanden finden, der eins besitzt und verkauft; Besitz kennzeichnet Elite-Status; bringt beim Verkauf zusätzliches Geld wegen Seltenheit. |

---

### 26. Tarnbarkeit (S. 247, Tabellenanhang S. 335)

Schwellenwert für Wahrnehmungsproben, um versteckte Gegenstände anhand ihrer Größe zu entdecken.

| Größe | Schwellenwert | Beispiel |
|---|---|---|
| Echt groß | 0 | Sturmkanone |
| Unhandlich | 1 | Sturmgewehr |
| Verstaubar | 2 | Schwere Pistole, Maschinenpistole |
| Taschengroß | 3 | Automatikpistole, Leichte Pistole |
| Handflächengroß | 4 | Kartenspiel, Holdout-Pistole |
| Kleine Handfläche | 5 | Einzelne Karte |
| Mit der Hand umschließbar | 6 | Feuerzeug |
| Klein | 7 | Sechsseitiger Würfel |
| Mini | 8 | Spionage-RFID-Chip |
| Fein | 9 | Pulverspuren |
| Mikroskopisch | 10 | Ein Floh auf der Schulter |

---

### Nicht erfasst

- **Buchseiten 310–322** (Settingkapitel *Deutschland in den Schatten*: München, Rhein-Ruhr-Megaplex, Hotspot Heidelberg/Düsseldorf, Berlin/Dresden/Leipzig-Halle/Sachsen, Hotspot Spreewald/Das Labyrinth, Norddeutscher Bund/Pomorya, Brennpunkt Hamburg mit allen Stadtteilen/Hotspots inkl. Wildost und der Wattburg) — durchgehend reine Fluff-/Lore-Beschreibung, **keine** Spielmechanik oder Zahlenwerte, daher komplett übersprungen.
- **Ideen für Patzer** (S. 233, Tabellenanhang S. 331–333) — dreiseitige Inspirationstabelle mit erzählerischen Vorschlägen für Patzer/kritische Patzer je Kategorie (Allgemein, Fernkampf, Nahkampf, Sozial, Zauberei, Herbeirufen, Matrix, Fahren). Enthält **keine** Zahlenwerte/Formeln (nur Erzähltext für Spielleitungsentscheidungen), daher nicht transkribiert.
- **Fertigkeitswerte-Bedeutungstabelle** (S. 101, Tabellenanhang S. 328) — rein deskriptiver Flavor-Text zu den Stufen 0–12+ (z. B. „Ungeübt", „Weltweite Elite"), keine Berechnung, übersprungen.
- **Vor- und Nachteile-Katalog** (S. 73, Tabellenanhang S. 327) — vollständige alphabetische Liste aller Vorteile (Karmakosten) und Nachteile (Karmabonus), insgesamt ca. 34 + 34 Einträge. Reiner Namen-/Kosten-Katalog ohne neue Formel (das allgemeine Kostenprinzip „Karmakosten bei Erschaffung × 2" beim Nachkauf ist bereits in Teil 1, Abschnitt 11 dokumentiert). Kostenspanne: Vorteile 3–14 Karma (teils gestuft, z. B. Robust Gebaut 4/Stufe, Erhöhte Konzentrationsfähigkeit 12/Stufe), Nachteile 2–20 Karmabonus (teils gestuft/als Bereich, z. B. Allergie 2–20, Abhängigkeit 2/Stufe, Glaskinn 4/Stufe). Nicht vollständig transkribiert, um Übertragungsfehler bei seltenen Qualitätsnamen zu vermeiden — bei Bedarf im Originalbuch auf S. 73 nachschlagen.
- **Index** (Buchseiten 336–339, im gelesenen Ausschnitt bis Buchstabe „G") — reines alphabetisches Stichwortregister mit Seitenzahlen, kein Regelinhalt.
- **Duplikate bereits dokumentierter Tabellen** im Tabellenanhang (identisch mit den Tabellen in Teil 1, dort mit vollem Kontext erfasst, hier nicht erneut wiedergegeben): Intervalle für Ausgedehnte Proben (S. 37), Ausweichenmalus/Weghechten (S. 44), Edge-Boosts im Kampf (S. 47), Edge-Handlungen nach Kosten (S. 48), Beinarbeit-Tabelle (S. 53), Statusliste-Kerneinträge (S. 53, bis auf die drei in Abschnitt 3 oben ergänzten neuen Status), Lebensstilkosten (S. 59), Prioritätentabelle (S. 65), Attribute-nach-Metatyp-Grundbereiche (S. 66, Rassenvorteile s. Abschnitt 4 oben), Entwicklungskosten-Tabelle (S. 72), Schwellenwerte für Wahrnehmungsproben (S. 99).
- **Askennen-Tabelle, letzte Zeile** (S. 162): ein Textfragment war im Scan nicht zweifelsfrei lesbar (vermutlich „…ob das Ziel Technomancer oder Adept ist"); im Original auf S. 162 zur Sicherheit gegenprüfen.

---

## Teil 10: Buchende: Index & Charakterbogen (Buchseiten 340–352)

<sub>Quelle-Chunk: `docs/sr6/sr6_calc_p341-352.md` — Originaltitel: Shadowrun 6 – Regeln mit Berechnungen (Grundregelwerk, Buchseiten 340–352 / Ende des Buchs)</sub>

Quelle: Sub-PDF `sr6_p341-352.pdf` (physische PDF-Seiten 341–352 der deutschen Ausgabe). Die im Fußtext gedruckten Buchseiten sind **340–347** (Index, Fortsetzung ab Buchstabe „G", der bereits in Teil 9 bis zum Buchstaben „G" erfasst wurde); danach folgen der zweiseitige **Charakterbogen** (unpaginiert) sowie zwei unpaginierte Werbe-/Verlagsseiten am Buchende.

Dieser Chunk enthält **keine neuen Spielmechanik-Formeln oder Tabellen**. Er wird der Vollständigkeit halber dokumentiert, damit klar ist, dass das Buchende vollständig gesichtet wurde.

---

### 1. Index (Buchseiten 340–347)

Fortsetzung des alphabetischen Stichwortregisters aus dem vorherigen Abschnitt (dort bis „G" gesichtet). Dieser Chunk deckt die Buchstaben **G (Rest) bis Z** ab, verteilt auf die PDF-Seiten 1–8 der Sub-PDF:

- PDF-Seite 1 → Buchseite 340: G(esamt)–H
- PDF-Seite 2 → Buchseite 341: I–J–K–L
- PDF-Seite 3 → Buchseite 342: L–M–N
- PDF-Seite 4 → Buchseite 343: N–O–P–Q–R
- PDF-Seite 5 → Buchseite 344: R–S
- PDF-Seite 6 → Buchseite 345: S–T
- PDF-Seite 7 → Buchseite 346: T–U–V–W
- PDF-Seite 8 → Buchseite 347: W–Y–Z (Ende des Index)

Reines Stichwort-/Seitenzahlregister ohne Regeltext oder Formeln. Nicht transkribiert.

---

### 2. Charakterbogen (unpaginiert, PDF-Seiten 9–10 der Sub-PDF, ≈ Buchseiten 348–349)

Zweiseitiges ausfüllbares Formular („Charakterbogen") zum Ausdrucken:

- **Seite 1**: Persönliche Daten, Attribute (Felder für Konstitution, Geschicklichkeit, Reaktion, Stärke, Willenskraft, Logik, Intuition, Charisma, Edge, Edgepunkte, Angriffswert waffenlos / Essenz, Magie/Resonanz, Initiative, Matrix-Initiative, Astrale Initiative, Selbstbeherrschung, Menschenkenntnis, Erinnerungsvermögen, Heben/Tragen, Bewegung, Verteidigungswert), Wichtige Kampf-Infos, Zustandsmonitor (Körperlicher Schaden / Betäubungsschaden, je mit den bereits an anderer Stelle dokumentierten Formeln `(Konstitution ÷ 2, aufgerundet) + 8` bzw. `(Willenskraft ÷ 2, aufgerundet) + 8` Kästchen — hier nur als Vordruck abgebildet, keine neue Information), Fertigkeiten, Vor- und Nachteile, IDs/Lebensstile/Währung, Connections.
- **Seite 2**: Fernkampfwaffen, Nahkampfwaffen, Panzerung, Matrixwerte, Bodytech, Fahrzeug, Zauber/Erzeugnisse/Rituale/Komplexe Formen, Adeptenkräfte & andere Fähigkeiten.

Reines Ausfüllformular ohne zusätzlichen Regeltext; alle darauf referenzierten Formeln sind bereits an früherer Stelle in diesem Dokument dokumentiert. Nicht transkribiert.

---

### 3. Verlagsseiten (unpaginiert, PDF-Seiten 11–12 der Sub-PDF)

- PDF-Seite 11: Werbeanzeige „Shadowrun Datenupload" (Hinweis auf PDF-Käufe bei Pegasus Digital).
- PDF-Seite 12: Rückseite des Buchs mit Marketingtext „Riskiere alles!" (Kurzbeschreibung des Spiels) sowie Verlags-/Lizenzangaben (Topps, Catalyst Game Labs, Pegasus Spiele, Art.-Nr. 46100P).

Kein Regelinhalt. Nicht transkribiert.

---

### Fazit

Dies ist das Ende des Buchs. Es wurden **keine** neuen Berechnungen, Formeln oder Tabellen gefunden, die nicht bereits in den vorangehenden Teilen dieses Dokuments erfasst sind.
