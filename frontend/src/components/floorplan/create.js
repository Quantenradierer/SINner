import React from "react";
import i18next from "../../i18n";
import {TabsHeader} from "../cyberpunk/tabsHeader";
import {optionLabel} from "./names";
import "./floorplan.css";

const FORM_KEY = "floorplan.form";
const SEED_MAX = 2 ** 31;

export const DEFAULT_FORM = {
    building_type: "office", width: 48, depth: 30, floors_above: 1, floors_below: 0,
    shape: "rectangle", wealth: "middle", condition: "maintained", security: "low",
    street_side: "S", service_side: "", seed: "", rooms_seed: "", furniture_seed: "",
    security_seed: "", theme: "neon2",
};

export function recallForm() {
    try {
        return {...DEFAULT_FORM, ...JSON.parse(localStorage.getItem(FORM_KEY))};
    } catch {
        return DEFAULT_FORM;
    }
}

export function rememberForm(values) {
    try {
        localStorage.setItem(FORM_KEY, JSON.stringify(values));
    } catch {
        // Per-viewer convenience only.
    }
}

/** The form values that reproduce a stored floorplan (its attributes), for "new variation". */
export function formFromAttributes(attributes) {
    const p = attributes.params;
    return {
        ...DEFAULT_FORM,
        building_type: p.building_type, width: p.width, depth: p.depth,
        floors_above: p.floors_above, floors_below: p.floors_below, shape: p.shape,
        wealth: p.wealth, condition: p.condition, security: p.security, street_side: p.street_side,
        service_side: p.service_side || "", seed: p.seed ?? "", rooms_seed: p.rooms_seed ?? "",
        furniture_seed: p.furniture_seed ?? "", security_seed: p.security_seed ?? "", theme: attributes.theme,
    };
}

const seedValue = (v) => (v === "" || v == null ? null : +v);

const SEEDS = [
    ["seed", "floorplan_seed_layout"], ["rooms_seed", "floorplan_seed_rooms"],
    ["furniture_seed", "floorplan_seed_furniture"], ["security_seed", "floorplan_seed_security"],
];

const requestFromForm = (v) => ({
    params: {
        building_type: v.building_type, width: +v.width, depth: +v.depth,
        floors_above: +v.floors_above, floors_below: +v.floors_below, shape: v.shape,
        wealth: v.wealth, condition: v.condition, security: v.security,
        street_side: v.street_side, service_side: v.service_side || null,
        seed: seedValue(v.seed), rooms_seed: seedValue(v.rooms_seed),
        furniture_seed: seedValue(v.furniture_seed), security_seed: seedValue(v.security_seed),
    },
    theme: v.theme,
    language: i18next.language,  // of the room names baked into the images
});

function Select({name, values, form, set, blank}) {
    return (
        <select value={form[name]} onChange={(e) => set(name, e.target.value)}>
            {blank !== undefined && <option value="">{blank}</option>}
            {values.map((v) => <option key={v} value={v}>{optionLabel(v)}</option>)}
        </select>
    );
}

function Field({label, children}) {
    return <label className="field">{label}{children}</label>;
}

function NumberInput({name, form, set, min, max}) {
    return <input type="number" value={form[name]} min={min} max={max}
                  onChange={(e) => set(name, e.target.value)}/>;
}

export const FloorplanTabs = () => (
    <TabsHeader tabs={{
        npcs: {url: "/npcs/create", name: i18next.t("tab_header_npc_create")},
        locations: {url: "/locations/create", name: i18next.t("tab_header_locations_create")},
        floorplans: {url: "/floorplans/create", name: i18next.t("tab_header_floorplans_create")},
    }}/>
);

/** The request body for the API from the form values. */
export const requestFromFormValues = requestFromForm;

/** Every generation parameter; `set(name, value)` updates one, Enter calls `onSubmit`, a dice button calls `onReroll(name, seed)`. */
export default function ParamsForm({options, form, set, onSubmit, onReroll}) {
    const limits = options.limits;

    return (
        <form className="floorplan-form" onSubmit={(e) => { e.preventDefault(); onSubmit(); }}>
            <h4>{i18next.t("floorplan_building")}</h4>
            <Field label={i18next.t("floorplan_type")}>
                <Select name="building_type" values={options.building_types} form={form} set={set}/>
            </Field>
            <div className="pair">
                <Field label={i18next.t("floorplan_width")}>
                    <NumberInput name="width" form={form} set={set} min={limits.side_cells[0]}
                                 max={limits.side_cells[1]}/>
                </Field>
                <Field label={i18next.t("floorplan_depth")}>
                    <NumberInput name="depth" form={form} set={set} min={limits.side_cells[0]}
                                 max={limits.side_cells[1]}/>
                </Field>
            </div>
            <div className="pair">
                <Field label={i18next.t("floorplan_floors_above")}>
                    <input type="number" value={form.floors_above}
                           min={limits.floors_above[0]} max={limits.floors_above[1]}
                           onChange={(e) => set("floors_above", e.target.value)}/>
                </Field>
                <Field label={i18next.t("floorplan_floors_below")}>
                    <input type="number" value={form.floors_below}
                           min={limits.floors_below[0]} max={limits.floors_below[1]}
                           onChange={(e) => set("floors_below", e.target.value)}/>
                </Field>
            </div>
            <Field label={i18next.t("floorplan_shape")}>
                <select value={form.shape} onChange={(e) => set("shape", e.target.value)}>
                    {options.shape.map((v) => <option key={v} value={v}>{optionLabel(v)}</option>)}
                </select>
            </Field>
            {form.shape === "osm" && (
                <p className="osm-credit">
                    {i18next.t("floorplan_osm_credit")}{" "}
                    <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">
                        © OpenStreetMap contributors (ODbL)
                    </a>
                </p>
            )}
            <Field label={i18next.t("floorplan_wealth")}>
                <Select name="wealth" values={options.wealth} form={form} set={set}/>
            </Field>
            <Field label={i18next.t("floorplan_condition")}>
                <Select name="condition" values={options.condition} form={form} set={set}/>
            </Field>
            <Field label={i18next.t("floorplan_security")}>
                <Select name="security" values={options.security} form={form} set={set}/>
            </Field>

            <h4>{i18next.t("floorplan_site")}</h4>
            <Field label={i18next.t("floorplan_street_side")}>
                <Select name="street_side" values={options.sides} form={form} set={set}/>
            </Field>
            <Field label={i18next.t("floorplan_service_side")}>
                <Select name="service_side" values={options.sides} form={form} set={set}
                        blank={i18next.t("floorplan_opposite_of_street")}/>
            </Field>

            <h4>{i18next.t("floorplan_seed")}</h4>
            {SEEDS.map(([name, label]) => (
                <Field key={name} label={i18next.t(label)}>
                    <div className="row">
                        <input type="number" min={limits.seed[0]} max={limits.seed[1]} value={form[name]}
                               placeholder={i18next.t(name === "seed" ? "floorplan_random" : "floorplan_follows_layout")}
                               onChange={(e) => set(name, e.target.value)}/>
                        <button type="button" className="fp-button" title={i18next.t("floorplan_reroll")}
                                aria-label={i18next.t("floorplan_reroll")}
                                onClick={() => onReroll(name, Math.floor(Math.random() * SEED_MAX))}>🎲</button>
                    </div>
                </Field>
            ))}

            <h4>{i18next.t("floorplan_image")}</h4>
            <Field label={i18next.t("floorplan_theme")}>
                <Select name="theme" values={options.themes} form={form} set={set}/>
            </Field>
        </form>
    );
}
