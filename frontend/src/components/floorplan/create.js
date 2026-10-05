import React, {useEffect, useState} from "react";
import {Button, FrameLines, FramePentagon, Text} from "@arwes/core";
import {Helmet} from "react-helmet";
import {useNavigate} from "react-router-dom";
import api from "../../axios";
import i18next from "../../i18n";
import {TabsHeader} from "../cyberpunk/tabsHeader";
import Warning from "../warning";
import {pretty} from "./overlay";
import "./floorplan.css";

const FORM_KEY = "floorplan.form";
const SEED_MAX = 2 ** 31;

export const DEFAULT_FORM = {
    building_type: "office", room: "", width: 48, depth: 30, floors_above: 1, floors_below: 0,
    shape: "rectangle", chamfer: 0, wealth: "middle", condition: "maintained", security: "low",
    street_side: "S", service_side: "", entrances_override: false, entrances: ["main"],
    seed: "", theme: "neon2", cell_px: 25, supersample: 1,
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
        building_type: p.building_type, room: p.room || "", width: p.width, depth: p.depth,
        floors_above: p.floors_above, floors_below: p.floors_below, shape: p.shape, chamfer: p.chamfer,
        wealth: p.wealth, condition: p.condition, security: p.security, street_side: p.street_side,
        service_side: p.service_side || "", entrances_override: !!p.entrances,
        entrances: p.entrances || DEFAULT_FORM.entrances, seed: p.seed ?? "",
        theme: attributes.theme, cell_px: attributes.cell_px, supersample: attributes.supersample,
    };
}

const requestFromForm = (v) => ({
    params: {
        building_type: v.building_type, width: +v.width, depth: +v.depth,
        floors_above: +v.floors_above, floors_below: +v.floors_below, shape: v.shape,
        chamfer: +v.chamfer, wealth: v.wealth, condition: v.condition, security: v.security,
        street_side: v.street_side, service_side: v.service_side || null, room: v.room || null,
        seed: v.seed === "" ? null : +v.seed,
        ...(v.entrances_override ? {entrances: v.entrances} : {}),
    },
    theme: v.theme, cell_px: +v.cell_px, supersample: +v.supersample,
});

// Options are translated where a `floorplan_opt_<value>` key exists, else shown as roomplanner names them.
const optionLabel = (value) => {
    const key = `floorplan_opt_${value}`;
    return i18next.exists(key) ? i18next.t(key) : pretty(value);
};

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

export default function FloorplanCreate() {
    const navigate = useNavigate();
    const [options, setOptions] = useState(null);
    const [form, setForm] = useState(recallForm);
    const [error, setError] = useState(null);
    const [busy, setBusy] = useState(false);

    useEffect(() => {
        api.get("/api/npc_creator/floorplans/options/")
            .then((response) => setOptions(response.data))
            .catch(() => setError(i18next.t("floorplan_options_failed")));
    }, []);

    const set = (name, value) => setForm((f) => {
        const next = {...f, [name]: value};
        if (name === "building_type" && options && !options.rooms[value].includes(next.room)) next.room = "";
        return next;
    });
    const lone = form.room !== "";
    const limits = options?.limits;

    const submit = async (event) => {
        event.preventDefault();
        setBusy(true);
        setError(null);
        rememberForm(form);
        try {
            const response = await api.post("/api/npc_creator/floorplans/", requestFromForm(form));
            navigate(`/floorplans/${response.data.id}`);
        } catch (e) {
            setError(e.response?.data?.error || i18next.t("prompt_failed_connection"));
            setBusy(false);
        }
    };

    return (
        <div style={{width: "100%", position: "relative"}}>
            <Helmet><title>{i18next.t("page_floorplan_create_title")}</title></Helmet>
            <FloorplanTabs/>
            <FrameLines style={{width: "100%"}}>
                <Text>{i18next.t("create_explanation_floorplan")}</Text>
                {options && (
                    <form className="floorplan-form" onSubmit={submit}>
                        <div className="grid">
                            <div>
                                <h4>{i18next.t("floorplan_building")}</h4>
                                <Field label={i18next.t("floorplan_type")}>
                                    <Select name="building_type" values={options.building_types} form={form} set={set}/>
                                </Field>
                                <Field label={i18next.t("floorplan_room")}>
                                    <Select name="room" values={options.rooms[form.building_type]} form={form}
                                            set={set} blank={i18next.t("floorplan_whole_building")}/>
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
                                <div className="pair" style={{opacity: lone ? .45 : 1}}>
                                    <Field label={i18next.t("floorplan_floors_above")}>
                                        <input type="number" disabled={lone} value={form.floors_above}
                                               min={limits.floors_above[0]} max={limits.floors_above[1]}
                                               onChange={(e) => set("floors_above", e.target.value)}/>
                                    </Field>
                                    <Field label={i18next.t("floorplan_floors_below")}>
                                        <input type="number" disabled={lone} value={form.floors_below}
                                               min={limits.floors_below[0]} max={limits.floors_below[1]}
                                               onChange={(e) => set("floors_below", e.target.value)}/>
                                    </Field>
                                </div>
                            </div>
                            <div>
                                <h4>{i18next.t("floorplan_character")}</h4>
                                <Field label={i18next.t("floorplan_shape")}>
                                    <select disabled={lone} value={form.shape} onChange={(e) => set("shape", e.target.value)}>
                                        {options.shape.map((v) => <option key={v} value={v}>{optionLabel(v)}</option>)}
                                    </select>
                                </Field>
                                <Field label={i18next.t("floorplan_chamfer")}>
                                    <input type="number" min="0" disabled={lone} value={form.chamfer}
                                           onChange={(e) => set("chamfer", e.target.value)}/>
                                </Field>
                                <Field label={i18next.t("floorplan_wealth")}>
                                    <Select name="wealth" values={options.wealth} form={form} set={set}/>
                                </Field>
                                <Field label={i18next.t("floorplan_condition")}>
                                    <Select name="condition" values={options.condition} form={form} set={set}/>
                                </Field>
                                <Field label={i18next.t("floorplan_security")}>
                                    <Select name="security" values={options.security} form={form} set={set}/>
                                </Field>
                            </div>
                            <div>
                                <h4>{i18next.t("floorplan_site")}</h4>
                                <Field label={i18next.t("floorplan_street_side")}>
                                    <Select name="street_side" values={options.sides} form={form} set={set}/>
                                </Field>
                                <Field label={i18next.t("floorplan_service_side")}>
                                    <Select name="service_side" values={options.sides} form={form} set={set}
                                            blank={i18next.t("floorplan_opposite_of_street")}/>
                                </Field>
                                <div className="checks">
                                    <label>
                                        <input type="checkbox" checked={form.entrances_override}
                                               onChange={(e) => set("entrances_override", e.target.checked)}/>
                                        {i18next.t("floorplan_override_entrances")}
                                    </label>
                                </div>
                                <div className="checks" style={{opacity: form.entrances_override ? 1 : .45}}>
                                    {options.entrances.map((kind) => (
                                        <label key={kind}>
                                            <input type="checkbox" disabled={!form.entrances_override}
                                                   checked={form.entrances.includes(kind)}
                                                   onChange={(e) => set("entrances", e.target.checked
                                                       ? [...form.entrances, kind]
                                                       : form.entrances.filter((k) => k !== kind))}/>
                                            {optionLabel(kind)}
                                        </label>
                                    ))}
                                </div>
                            </div>
                            <div>
                                <h4>{i18next.t("floorplan_seed")}</h4>
                                <div className="row">
                                    <input type="number" min={limits.seed[0]} max={limits.seed[1]} value={form.seed}
                                           placeholder={i18next.t("floorplan_random")}
                                           onChange={(e) => set("seed", e.target.value)}/>
                                    <Button FrameComponent={FramePentagon} type="button" style={{margin: 0}}
                                            title={i18next.t("floorplan_reroll")}
                                            onClick={() => set("seed", Math.floor(Math.random() * SEED_MAX))}>
                                        <Text>🎲</Text>
                                    </Button>
                                </div>
                                <h4>{i18next.t("floorplan_image")}</h4>
                                <Field label={i18next.t("floorplan_theme")}>
                                    <Select name="theme" values={options.themes} form={form} set={set}/>
                                </Field>
                                <div className="pair">
                                    <Field label={i18next.t("floorplan_cell_px")}>
                                        <NumberInput name="cell_px" form={form} set={set} min={limits.cell_px[0]}
                                                max={limits.cell_px[1]}/>
                                    </Field>
                                    <Field label={i18next.t("floorplan_supersample")}>
                                        <NumberInput name="supersample" form={form} set={set} min={limits.supersample[0]}
                                                max={limits.supersample[1]}/>
                                    </Field>
                                </div>
                            </div>
                        </div>
                        <div style={{display: "flex", justifyContent: "flex-end", marginTop: 10}}>
                            <Button FrameComponent={FramePentagon} style={{margin: 3, width: 150}}
                                    onClick={submit} disabled={busy}>
                                <Text>{i18next.t("floorplan_generate")}</Text>
                            </Button>
                        </div>
                    </form>
                )}
            </FrameLines>
            {error && <div style={{marginTop: 15}}><Warning text={error}/></div>}
        </div>
    );
}
