The rules are defined in this format:

```
[
  {
    "name": "rulebook/type/name",
    "source": { "page": 39, "book": "SR6Core" },
    "modifies": "character.physical_initiative_dices",
    "modifier_type": "BASE",
    "modification": "1",
  }
]
```

- Name is used as lookup for translations, or directly shown to the user.

- Source defines the book and page site.

- modifies defines what is being modified, in this example the amount of physical initiative dices from a character.

- modifier type can be BASE, REPLACEMENT, ADD, LIMIT and will be called in this order.

  - BASE is the e.g. the base damage of close combat.
  - REPLACEMENT is in case something modifies the BASE rules, like cyberware which results in a different calculation of the BASE rule. Therefore, if a replacement exists, the base is being ignored.
  - ADD adds or subtracts values, due to modifications
  - LIMIT limits the value range, e.g. the lowest attribute value is always 0. The highest modified value can't exceed the points + 4.

- modification can be python code. character, weapon or similar objects will be given if it makes sense (a vehicle modification will get character and vehicle but no weapon. A weapon modification may get a vehicle if it is placed onto a vehicle)

It can be simple (like 1) but also complex like (character.attributes.reaction * character.attribute.logic / 2).

mathematical operations and min, max, floor, ceil are all available.
The current value, calculated from previous modifications, is also available under the var name `value` The current value, calculated from previous modifications, is also available under the var name `value`, which usually shouldn't be used, except for LIMIT

One example:

BODY, the user invested 2 Points into it.
- BASE:  takes the points, the strength value is 2 therefore.
- REPLACEMENT: due to a cyberarm, the strength is being replaced by 4
- ADD: The cyberarm itself has mods, giving it +4
- LIMIT: max(0, min(points + 4, value))

- BASE 2
- REPLACEMENT 3
- ADD +4
- LIMIT max(0, min(3 + 4, 6))
- = 6