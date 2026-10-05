import React, {useEffect, useRef, useState} from "react";
import i18next from "../../i18n";
import FloorOverlay, {LAYERS, pretty, roomInfo} from "./overlay";
import "./floorplan.css";

const MIN_ZOOM = 2;
const MAX_ZOOM = 200;
const LAYERS_KEY = "floorplan.layers";

function recall(key) {
    try {
        return JSON.parse(localStorage.getItem(key));
    } catch {
        return null;
    }
}

function store(key, value) {
    try {
        localStorage.setItem(key, JSON.stringify(value));
    } catch {
        // Per-viewer convenience only.
    }
}

const defaultLayers = () => {
    const saved = recall(LAYERS_KEY) || {};
    return Object.fromEntries(LAYERS.map(([key, on]) => [key, key in saved ? saved[key] : on]));
};

function Tip({tip}) {
    if (!tip) return null;
    const {info, x, y} = tip;
    return (
        <div className="floorplan-tip" style={{left: Math.min(x + 14, window.innerWidth - 300), top: y + 14}}>
            <b>{info.type}</b> <span style={{opacity: .6}}>{info.id}</span><br/>
            {info.summary}
            {info.unit && <><br/>{i18next.t("floorplan_unit")} {info.unit}</>}
            {info.furniture.length > 0 && <><br/>{info.furniture.join(", ")}</>}
            {info.devices.length > 0 && <><br/><span style={{color: "#ff8a3d"}}>{info.devices.join(", ")}</span></>}
        </div>
    );
}

/**
 * The whole workspace: `sidebar` (the parameters) and the layer toggles on the left, floor tabs,
 * zoom and downloads above the map. `floorplan` is the detail from the API and `building` its
 * stored JSON; both are null until there is a finished floorplan, then `placeholder` fills the
 * map area. `actions` go into the toolbar.
 */
export default function FloorplanViewer({floorplan, building, sidebar, actions, placeholder}) {
    const [level, setLevel] = useState(0);
    const [layers, setLayers] = useState(defaultLayers);
    const [gridStep, setGridStep] = useState(3);
    const [zoom, setZoom] = useState(null);
    const [tip, setTip] = useState(null);
    const viewport = useRef(null);

    const padding = floorplan ? floorplan.padding : 0;
    const fit = () => {
        const el = viewport.current;
        if (!el || !building) return MIN_ZOOM * 4;
        const zx = (el.clientWidth - 32) / (building.width + 2 * padding);
        const zy = (el.clientHeight - 32) / (building.height + 2 * padding);
        return Math.max(MIN_ZOOM, Math.min(zx, zy));
    };
    useEffect(() => {
        if (!building) return;
        const levels = building.floors.map((f) => f.level);
        setLevel((current) => (levels.includes(current) ? current : levels.includes(0) ? 0 : levels[0]));
        setZoom(fit());
    }, [building]);

    const floor = building && building.floors.find((f) => f.level === level);
    const files = (floorplan && floorplan.floors.find((f) => f.level === level)) || {};
    const zoomBy = (factor) => setZoom((z) => Math.max(MIN_ZOOM, Math.min(MAX_ZOOM, z * factor)));
    const toggle = (key) => {
        const next = {...layers, [key]: !layers[key]};
        setLayers(next);
        store(LAYERS_KEY, next);
    };
    const stem = building ? `${building.params.building_type}_${building.seed}` : "";
    const tag = level >= 0 ? `F${level}` : `B${-level}`;

    return (
        <div className="floorplan-viewer">
            <aside>
                {sidebar}
                <h4>{i18next.t("floorplan_layers")}</h4>
                {LAYERS.map(([key, , swatch]) => (
                    <label key={key}>
                        <input type="checkbox" checked={!!layers[key]} onChange={() => toggle(key)}/>
                        <span className="swatch" style={{background: swatch}}/>
                        {i18next.t(`floorplan_layer_${key}`)}
                    </label>
                ))}
                <label className="grid-step">
                    {i18next.t("floorplan_grid_every")}
                    <input type="number" min="1" value={gridStep} style={{width: 60}}
                           onChange={(e) => setGridStep(+e.target.value || 1)}/>
                </label>
            </aside>
            <main>
                <div className="bar">
                    {building && [...building.floors].sort((a, b) => b.level - a.level).map((f) => (
                        <button key={f.level} className={f.level === level ? "active" : ""}
                                title={f.role ? `${i18next.t("floorplan_role")}: ${f.role}` : ""}
                                onClick={() => setLevel(f.level)}>{f.name}</button>
                    ))}
                    <span className="spacer"/>
                    {building && <span style={{opacity: .7}}>
                        {pretty(building.params.building_type)} · {building.width}×{building.height}{" "}
                        ({building.width * .5}×{building.height * .5} m) · {i18next.t("floorplan_seed")} {building.seed}
                    </span>}
                    <button onClick={() => zoomBy(1 / 1.25)} title={i18next.t("floorplan_zoom_out")}>−</button>
                    <button onClick={() => setZoom(fit())}>{i18next.t("floorplan_zoom_fit")}</button>
                    <button onClick={() => zoomBy(1.25)} title={i18next.t("floorplan_zoom_in")}>+</button>
                </div>
                <div className="bar">
                    {building && <>
                        <a className="fp-button" href={files.image_url} download={`${stem}_${tag}.webp`}>WebP</a>
                        {files.dd2vtt_url &&
                            <a className="fp-button" href={files.dd2vtt_url} download={`${stem}_${tag}.dd2vtt`}
                               title={i18next.t("floorplan_dd2vtt_hint")}>dd2vtt</a>}
                        <a className="fp-button" href={floorplan.building_url} download={`${stem}.json`}>JSON</a>
                    </>}
                    <span className="spacer"/>
                    {actions}
                </div>
                <div className="floorplan-viewport" ref={viewport}
                     onWheel={(e) => {
                         if (!e.ctrlKey) return;
                         zoomBy(e.deltaY < 0 ? 1.15 : 1 / 1.15);
                     }}>
                    {!building && <div className="floorplan-placeholder">{placeholder}</div>}
                    {building && zoom !== null && floor && (
                        <div className="floorplan-stage"
                             style={{
                                 width: (building.width + 2 * padding) * zoom,
                                 height: (building.height + 2 * padding) * zoom,
                             }}>
                            {layers.image && files.image_url && <img src={files.image_url} alt=""/>}
                            <FloorOverlay building={building} floor={floor} padding={padding} zoom={zoom}
                                          layers={layers} gridStep={gridStep}
                                          onRoomHover={(e, room) => setTip({
                                              info: roomInfo(room, floor), x: e.clientX, y: e.clientY,
                                          })}
                                          onRoomLeave={() => setTip(null)}/>
                        </div>
                    )}
                </div>
                <Tip tip={tip}/>
                {building && building.warnings.length > 0 && (
                    <ul className="floorplan-warnings">
                        {building.warnings.map((w, i) => <li key={i}>{w}</li>)}
                    </ul>
                )}
            </main>
        </div>
    );
}
