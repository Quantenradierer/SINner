import i18next from "../../i18n";

// Room and object names come from roomplanner in the page's language, loaded with the options.
let catalogue = {rooms: {}, objects: {}};

export const setNames = (names) => { catalogue = {rooms: {}, objects: {}, ...names}; };

export const pretty = (text) => String(text).replace(/_/g, " ");
export const roomName = (id) => catalogue.rooms[id] || pretty(id);
export const objectName = (id) => catalogue.objects[id] || pretty(id);

/** A parameter value in the page's language where there is a `floorplan_opt_<value>` text. */
export const optionLabel = (value) => {
    const key = `floorplan_opt_${value}`;
    return i18next.exists(key) ? i18next.t(key) : pretty(value);
};

/** "Büro 48×30" for a floorplan's stored parameters. */
export const floorplanTitle = (params) =>
    params ? `${optionLabel(params.building_type)} ${params.width}×${params.depth}` : "";
