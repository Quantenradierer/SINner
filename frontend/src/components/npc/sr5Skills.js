// Active skills of the Shadowrun 5 core rulebook; keys mirror backend game_mechanics/sr5/skills.py.
const skillKey = (name) => 'sr5_skill_' + name.toLowerCase().replace(/-/g, '_').replace(/ /g, '_');

const categories = {
    combat: [
        'Archery', 'Automatics', 'Blades', 'Clubs', 'Exotic Melee Weapon', 'Exotic Ranged Weapon',
        'Heavy Weapons', 'Longarms', 'Pistols', 'Throwing Weapons', 'Unarmed Combat', 'Gunnery'
    ],
    physical: [
        'Disguise', 'Diving', 'Escape Artist', 'Free-Fall', 'Gymnastics', 'Locksmith', 'Palming',
        'Perception', 'Running', 'Sneaking', 'Survival', 'Swimming', 'Tracking'
    ],
    social: [
        'Animal Handling', 'Con', 'Etiquette', 'Impersonation', 'Instruction', 'Intimidation',
        'Leadership', 'Negotiation', 'Performance'
    ],
    magical: [
        'Alchemy', 'Arcana', 'Artificing', 'Assensing', 'Astral Combat', 'Banishing', 'Binding',
        'Counterspelling', 'Disenchanting', 'Ritual Spellcasting', 'Spellcasting', 'Summoning'
    ],
    resonance: ['Compiling', 'Decompiling', 'Registering'],
    technical: [
        'Aeronautics Mechanic', 'Armorer', 'Artisan', 'Automotive Mechanic', 'Biotechnology', 'Chemistry',
        'Computer', 'Cybercombat', 'Cybertechnology', 'Demolitions', 'Electronic Warfare', 'First Aid',
        'Forgery', 'Hacking', 'Hardware', 'Industrial Mechanic', 'Medicine', 'Nautical Mechanic',
        'Navigation', 'Software'
    ],
    vehicle: [
        'Pilot Aerospace', 'Pilot Aircraft', 'Pilot Exotic Vehicle', 'Pilot Ground Craft', 'Pilot Walker',
        'Pilot Watercraft'
    ]
};

export {skillKey, categories};
