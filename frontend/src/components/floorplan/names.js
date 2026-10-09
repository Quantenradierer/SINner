import i18next from "../../i18n";

// Room and object names come from roomplanner in the page's language, loaded with the options.
let catalogue = {rooms: {}, objects: {}, terms: {}};

let matrixObjects = {};

export const setNames = (names, matrix = {}) => {
    catalogue = {rooms: {}, objects: {}, terms: {}, ...names};
    matrixObjects = matrix;
};

/** The objects the Matrix layer shows: {kind: {controls: [...], as: word or null}}. */
export const matrixSpec = (kind) => matrixObjects[kind];

export const pretty = (text) => String(text).replace(/_/g, " ");
export const roomName = (id) => catalogue.rooms[id] || pretty(id);
export const objectName = (id) => catalogue.objects[id] || pretty(id);

/** A word of a group (`control`, `word`) of roomplanner's terms in the page's language. */
export const term = (group, id) => (catalogue.terms[group] || {})[id] || pretty(id);

/** A parameter value in the page's language where there is a `floorplan_opt_<value>` text. */
export const optionLabel = (value) => {
    const key = `floorplan_opt_${value}`;
    return i18next.exists(key) ? i18next.t(key) : pretty(value);
};

/** "Büro 48×30" for a floorplan's stored parameters. */
export const floorplanTitle = (params) =>
    params ? `${optionLabel(params.building_type)} ${params.width}×${params.depth}` : "";
