# Shadowrun 6 – Regelreferenz

**[`sr6_rules_complete.md`](sr6_rules_complete.md)** enthält die vollständige, konsolidierte Extraktion
aller Berechnungen, Formeln, Schwellenwerte und Kostentabellen aus dem deutschen
**Shadowrun 6 – Grundregelwerk** (352 Buchseiten). Es ist die einzige Referenzdatei für die
regelkonforme NPC-Generierung in diesem Projekt.

Früher war der Inhalt auf zehn Chunk-Dateien (`sr6_rules_calculations.md`, `sr6_calc_p*.md`)
verteilt; diese wurden zu der einen Datei zusammengeführt. Die zehn ursprünglichen Abschnitte
sind darin als **Teil 1 – 10** wiederzufinden (jeweils mit einem `<sub>Quelle-Chunk: …</sub>`-Vermerk).

## Stand / Errata

Gegengeprüft (Stand 2026-08) gegen **`Shadowrun_6_Downloadversion_2024.pdf`** (354 PDF-Seiten) und die
[**Errata zum Grundregelwerk, 3. Auflage**](https://shadowrun6.de/downloads/errata/errata_sr6_grundregelwerk_aufl3.pdf).
Die Downloadversion 2024 ist bereits die **3. Auflage** — die regelrelevanten Errata (2. → 3. Auflage)
sind darin überwiegend eingearbeitet. Korrigierte bzw. ergänzte Stellen sind mit *„3. Auflage/Errata"*
markiert. Die vollständige Änderungsübersicht steht im Abschnitt *Stand / Errata* am Anfang von
`sr6_rules_complete.md`; die wichtigsten Punkte:

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
- **Bekannter Buchfehler:** Der Tabellen-Anhang **S. 330** (Teil 9) zeigt die astrale Initiative weiterhin
  als `+ 2W6`; korrekt ist laut Errata (S. 163) `+ 3W6`.

## Hinweise

- Buchseiten-Nummerierung folgt den gedruckten Fußzeilen im PDF, **nicht** dem internen PDF-Seitenindex.
- Item-Kataloge (einzelne Waffen-/Rüstungs-/Cyberware-Statblöcke ohne verallgemeinerbare Formel) sind
  bewusst **nicht** vollständig transkribiert — jeder Teil dokumentiert am Ende unter „Nicht erfasst", was
  ausgelassen wurde.
- Einige Tabellen tauchen doppelt auf (Fließtext + Tabellen-Anhang in Teil 9). Im Zweifel gilt die
  frühere/detailliertere Fassung; der Anhang verweist per Kommentar darauf.
- Die erratarelevanten Formeln wurden 2026-08 gegen `Shadowrun_6_Downloadversion_2024.pdf` zweitverifiziert;
  bei verbleibenden Unstimmigkeiten mit dem PDF hat das Original Vorrang.
