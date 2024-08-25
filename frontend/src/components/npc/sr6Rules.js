
function physicalCondition(entity) {
    return 8 + Math.ceil(entity.values['constitution'] / 2);
}

function stunCondition(entity) {
    return 8 + Math.ceil(entity.values['willpower'] / 2);
}

function initiativeBase(entity) {
    return entity.values['intuition'] + entity.values['reaction'];
}

export {physicalCondition, stunCondition};