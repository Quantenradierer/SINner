# Data-Regeln vs. `sr6_rules_complete.md` — Abgleich

Stand: 2026-08-29. Verglichen: alle Dateien in `backend/data/sr6/core/rules/` (und die davon
referenzierten Waffen-/Fertigkeitsdaten in `backend/data/sr6/core/gear/`) gegen
`docs/sr6/sr6_rules_complete.md` sowie das deutsche Grundregelwerk (3. Auflage /
`Shadowrun_6_Downloadversion_2024.pdf`) und die Errata 3. Auflage.

Das Regel-Engine ist überwiegend korrekt und bereits errata-bewusst: astrale Initiative = 3 Würfel,
Cyberbuchsen-VR-Bonuswürfel, direkte/indirekte Zauberabwehr, Reflexbooster Stufe 1–4. Die folgenden
Punkte weichen ab.

---

## Umsetzungsstand (2026-08-29)

| Punkt | Status |
|---|---|
| A1 waffenloser Grundschaden 0 → 2B | ✅ `weapon.json` (`damage: 2`), Seite `114 → 112` |
| A2 waffenloser Angriffswert = REA+STÄ | ✅ neue BASE-Regel `sr6core/unarmed attack rating` in `data/sr6/core/rules/weapon.json`; `weapon.json`-Katalogwert auf `0` gesetzt (Regel ist Quelle) |
| A3 Nahkampfwaffen += Stärke auf Angriffswert | ✅ neue Regel `sr6core/melee weapon strength to attack rating` + `wear_rules` an allen 14 `blades`/`clubs`-Waffen. Peitschen (REA) entfallen — im Kern-GRW nicht enthalten. Schlagringe/Schockhandschuhe folgen der waffenlosen Regel und bleiben außen vor. |
| A4 Überlebensmesser 4K → 3K | ✅ `weapon.json` (`damage: 3`) |
| A5 Cyberglied setzt KON/REA auf 2 | ✅ 24 `REPLACEMENT …/body` + `…/reaction`-Regeln entfernt (49 → 25); stale `wear_rules`-Verweise in `data/sr6/core/gear/cyberware/cyberlimbs.json` mitentfernt (−48); Seiten `285`/`288 → 289` |
| B electronics += `complex_forms` | ✅ `character.py` `Electronics` + `character.json`; Seite `93 → 96` |
| B firearms → 10er-Liste (GRW S. 97) | ✅ `character.py` `Firearms` (`holdout_pistols … tasers`) + `character.json`; Seite `93 → 97` |
| B stealth `disguise` → `camouflage` | ✅ `character.py` `Stealth` + `character.json`; Seite `93 → 97` |
| B conjuring/outdoors/athletics | ⏸️ nicht angefasst — im konsolidierten Doc stehen keine Spezialisierungslisten, gegen das GRW nicht zweitverifizierbar |
| C Seitenverweis-Drift | ✅ `character.json`: `39 → 41`, `161 → 163`, `123 → 124` |
| Zusatz: `foundry.py` waffenloser Schaden | ✅ SR5-Formel `ceil(STÄ/2)` → fester Wert `2` (`foundry.py`), `import math` entfernt |

Alle 154 Tests (`npc_creator.tests`) grün; Regel-Engine-Funktionsprüfung: waffenloser AW = REA+STÄ,
Katana-AW = 10+STÄ, Feuerwaffen-AW unverändert.

---

## Nachtrag (2026-08-29): fehlende Grund-Regeln ergänzt

Vier abgeleitete Charakterwerte hatten ein Feld im Modell, aber **keine BASE-Regel** — sie blieben
still auf `0`. Beim `physical_condition_monitor` war das ein echter Bug: die Cyberware-`+1`-Regeln
addierten auf eine Basis von 0.

| Neue Regel (`character.json`) | Formel | Quelle |
|---|---|---|
| `sr6core/base physical condition monitor` | `ceil(Konstitution / 2) + 8` | S. 40 |
| `sr6core/base stun condition monitor` | `ceil(Willenskraft / 2) + 8` | S. 40 |
| `sr6core/base resist physical damage` | `Konstitution` (Schadenswiderstand, Schritt 4) | S. 108 |
| `sr6core/base resist astral damage` | `Willenskraft` (Astralkampf) | S. 163 |

Engine: `ceil` / `floor` / `round` waren laut `rules/readme.md` in `modification`-Ausdrücken
verfügbar, wurden aber nie an `simple_eval` übergeben. Jetzt zentral als `RULE_FUNCTIONS`
in `rule.py` (`min`, `max`, `ceil`, `floor`, `round`).

**Weiterhin offen — blockiert, nicht vergessen:** Bioware (Muskeltoner/-augmentation, Knochendichte,
Zerebralbooster, Synaptik-Beschleuniger, Schadenskompensator, Thrombozytenfabrik, Orthoskin …),
Cyberohren, Adeptenkräfte, Vor-/Nachteile, Zauber/Foki sind im `data/`-Katalog **gar nicht
vorhanden** — dafür müssen erst Gear-Einträge (und teils neue Modellfelder: Skillwires,
Wundmodifikator-Unterdrückung, Bewegungsrate, Steuer-Rig) angelegt werden. Reine Regel-Ergänzungen
reichen dort nicht.

---

## A. Wert- / Mechanik-Abweichungen

### A1 — Waffenloser Grundschaden

- **Datei:** `data/sr6/core/gear/weapon.json` → `sr6core/weapon/unarmed`
- **Daten:** `damage: 0`, `damage_type: "S"`
- **Buch/Docs:** **2 Betäubung** — Errata S. 98: *„Der Grundschaden im waffenlosen Kampf beträgt 2B"*
  (Teil 2 §6/§8 in `sr6_rules_complete.md`).
- **Bewertung:** Sieht nach dem Vor-Errata-Stand aus. Fix: `damage: 2`.

### A2 — Waffenloser Angriffswert ist fest statt REA+STÄ

- **Datei:** `data/sr6/core/gear/weapon.json` → `sr6core/weapon/unarmed`
- **Daten:** `attack_rating_0: 2` (fester Wert), keine Regel addiert REA+STÄ.
- **Buch/Docs:** Waffenloser Angriffswert = **Reaktion + Stärke** (Teil 1 §4).
- **Bewertung:** Der Foundry-Exporter berechnet `str + rea` separat (`foundry.py:133`), d. h. der
  Pipeline-Wert aus der Waffe wird dort nicht genutzt / ist inkonsistent. Entweder eine Regel
  ergänzen, die `unarmed.attack_rating_0` auf `reaction.mod + strength.mod` setzt, oder klarstellen,
  dass der Katalogwert bewusst roh bleibt.

### A3 — Stärke wird nicht auf Nahkampf-Angriffswerte addiert

- **Ort:** kein Eintrag in `rules/`, keine Engine-Logik.
- **Buch/Docs:** Errata S. 245: *„Nahkampfwaffen addieren die Stärke des Charakters zu ihrem
  Angriffswert"* (Peitschen: Reaktion) — Teil 6 §14 / Teil 7 §14.
- **Bewertung:** Die Katalog-Angriffswerte (Messer 6, Katana 10, …) sind die blanken Waffenwerte
  und bleiben blank. Es gibt keinen `rules/`-Eintrag und keinen Code, der STÄ (bzw. REA bei
  Peitschen) draufrechnet.

### A4 — Überlebensmesser Schaden

- **Datei:** `data/sr6/core/gear/weapon.json` → `sr6core/weapon/survival knife`
- **Daten:** `damage: 4`, `damage_type: "P"`
- **Buch/Docs:** **Überlebensmesser = 3K / AW 8** (Buch S. 249, Teil 6 §14).
  `sr6core/weapon/combat/survival knife` ist bereits korrekt bei 3P/8.
- **Bewertung:** Fix: `damage: 3`.

### A5 — Cyberglied setzt Konstitution & Reaktion auf 2

- **Datei:** `data/sr6/core/rules/cyberware/cyberlimbs.json`
- **Daten:** REPLACEMENT setzt für jedes Gliedmaßen-Teil **body, agility, reaction, strength**
  auf `2`.
- **Buch/Docs:** Buch S. 289: *„Standardcybergliedmaßen werden mit Geschicklichkeit und Stärke
  auf 2 installiert"* (Teil 8 §6). Konstitution und Reaktion eines Cyberglieds werden **nicht**
  neu definiert.
- **Bewertung:** Body/Reaction auf fest 2 zu setzen senkt sie für die meisten Charaktere. Nur
  `agility` + `strength` sollten REPLACEMENT auf 2 sein; body/reaction sollten durch die
  natürliche BASE aus `character_limbs.json` fallen.

---

## B. Errata nicht abgebildet — Fertigkeits-Spezialisierungslisten

- **Datei:** `data/sr6/core/rules/character.json`, Regeln `"specialisation of X"` (zitieren `page 93`)

Die Sub-Fertigkeitslisten weichen vom Buch 3. Auflage (S. 96–97) ab:

| Fertigkeit | Daten | Buch / Errata |
|---|---|---|
| **electronics** | `computer, hardware, software` | + **Komplexe Formen** (Errata S. 96) |
| **firearms** | `automatics, longarms, pistols, rifles, shotguns` (engl. Core-Set) | `Automatikpistolen, Gewehre, Holdout-Pistolen, Leichte Pistolen, Maschinengewehre, Maschinenpistolen, Schrotflinten, Schwere Pistolen, Sturmkanonen, Taser` (Errata S. 97) |
| **stealth** | `disguise, palming, sneaking` | `Fingerfertigkeit, Schleichen, Tarnung` — `disguise` gehört zu Con, nicht Stealth; korrekt wäre `camouflage` |
| conjuring | + `binding` | Buch nur `Herbeirufen, Verbannen` |
| outdoors | fehlt `animal_handling` (Tierführung) | |
| athletics | fehlt `escape_artist` / `free_fall` | |

**Bewertung:** Angleichung ändert Sub-Fertigkeitsfelder am Charaktermodell — Designentscheidung,
daher hier nur markiert. Zitat sollte außerdem auf S. 96–97 (Fertigkeitseinträge) statt S. 93
(Fertigkeiten-Einleitung) zeigen.

---

## C. Seitenverweis-Drift (niedrige Priorität; dt. Grundregelwerk-Paginierung)

- `character.json` Initiative-Regeln (Würfel BASE/LIMIT, `..._base`): zitieren **S. 39** → die
  Fakten (Würfel starten bei 1, max. 5W6, Wert = REA+INT) stehen auf **S. 40–41**.
- `defense_rating` / `defense_pool_physical` BASE: zitieren **S. 39** → **S. 41**.
- `defense_astral` & `astral_initiative_base`: zitieren **S. 161** (Askennen) → Astralkampf-Kasten
  ist **S. 163**.
- `resist_toxin`: zitiert **S. 123** → Toxinregeln beginnen **S. 124**.
- `cyberware/cyberlimbs.json` Konditionsmonitor-Regel: zitiert **S. 285**, Glied-Attribut-Regeln
  **S. 288** → Cyberglied-Abschnitt ist **S. 289**; der allgemeine „+4"-Cap auf modifizierte
  Attribute ist **S. 39**.
- `cyberware/bodyware.json` Reflexbooster-Regeln: zitieren **S. 288** → Item-Tabelle + Aktivierungs-
  text sind **S. 289**.

---

## D. Bekannt offen (bereits in Commit `b37ded8` dokumentiert, keine Regression)

- Rüstungs-Nichtstapelung.
- Reflexbooster ↔ Reaktionsverbesserung / Dermalpanzer ↔ Orthoskin gegenseitiger Ausschluss —
  dem Engine fehlt ein „Bestes-der-Kategorie"-Primitiv.
- Cyberglied-Konditionsmonitor „+1 pro vollem Glied, Teilglied = halb, Hände/Füße ignoriert" ist
  ebenfalls nicht als flaches `+1` ausdrückbar.
