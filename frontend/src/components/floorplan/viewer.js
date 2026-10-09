import React, {useEffect, useRef, useState} from "react";
import i18next from "../../i18n";
import FloorOverlay, {LAYERS, roomInfo} from "./overlay";
import {optionLabel} from "./names";
import "./floorplan.css";

const MIN_ZOOM = 2;
const MAX_ZOOM = 200;
const LAYERS_KEY = "floorplan.layers";
const TIP_WIDTH = 300;
const TIP_HEIGHT = 150;

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

/** "Erdgeschoss", "2. OG", "UG 1" instead of roomplanner's English floor names. */
export const floorName = (level) => {
    if (level === 0) return i18next.t("floorplan_floor_ground");
    return level > 0
        ? i18next.t("floorplan_floor_upper", {level})
        : i18next.t("floorplan_floor_basement", {level: -level});
};

function Tip({tip}) {
    if (!tip) return null;
    const {info, x, y} = tip;
    // Stay on screen: flip to the other side of the cursor near the right and bottom edges.
    const left = x + 14 + TIP_WIDTH > window.innerWidth ? x - 14 - TIP_WIDTH : x + 14;
    const top = y + 14 + TIP_HEIGHT > window.innerHeight ? y - 14 - TIP_HEIGHT : y + 14;
    return (
        <div className="floorplan-tip" style={{left: Math.max(4, left), top: Math.max(4, top)}}>
            <b>{info.type}</b> <span style={{opacity: .6}}>{info.id}</span><br/>
            {info.summary}
            {info.unit && <><br/>{i18next.t("floorplan_unit")} {info.unit}</>}
            {info.furniture.length > 0 && <><br/>{info.furniture.join(", ")}</>}
            {info.devices.length > 0 && <><br/><span style={{color: "#ff8a3d"}}>{info.devices.join(", ")}</span></>}
        </div>
    );
}

/**
 * The workspace: `sidebar` (the parameters, scrolls) with `sidebarFooter` (always visible) on
 * the left; layer toggles, floor tabs, zoom and downloads around the map. `floorplan` is the
 * detail from the API and `building` its stored JSON; both are null until there is a finished
 * floorplan, then `placeholder` fills the map area. `actions` go into the download row.
 */
// Grid lines every this many cells.
const GRID_STEP = 2;

export default function FloorplanViewer({floorplan, building, sidebar, sidebarFooter, actions, placeholder}) {
    const [level, setLevel] = useState(0);
    const [layers, setLayers] = useState(defaultLayers);
    const [zoom, setZoom] = useState(null);
    const [pan, setPan] = useState({x: 0, y: 0});  // px offset of the map from the centre
    const [tip, setTip] = useState(null);
    const viewport = useRef(null);
    const side = useRef(null);

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
        setPan({x: 0, y: 0});
    }, [building]);
    // A newly opened floorplan shows its parameters from the top (type, size).
    useEffect(() => {
        if (side.current) side.current.scrollTop = 0;
    }, [floorplan && floorplan.id]);

    // Drag the map with the mouse (or a finger); a short press is still a click or hover.
    const drag = useRef(null);
    const dragStart = (e) => {
        if (e.button !== 0) return;
        drag.current = {x: e.clientX, y: e.clientY, from: pan, moved: false};
    };
    const dragMove = (e) => {
        const d = drag.current, el = viewport.current;
        if (!d) return;
        const dx = e.clientX - d.x, dy = e.clientY - d.y;
        if (!d.moved && Math.hypot(dx, dy) < 4) return;
        if (!d.moved) {
            d.moved = true;
            el.setPointerCapture(e.pointerId);
            setTip(null);
            el.classList.add("dragging");
        }
        setPan({x: d.from.x + dx, y: d.from.y + dy});
    };
    const dragEnd = (e) => {
        const el = viewport.current;
        if (drag.current && drag.current.moved && el.hasPointerCapture(e.pointerId)) el.releasePointerCapture(e.pointerId);
        el.classList.remove("dragging");
        drag.current = null;
    };

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
                <div className="scroll" ref={side}>{sidebar}</div>
                <div className="footer">{sidebarFooter}</div>
            </aside>
            <main>
                <div className="layers" role="group" aria-label={i18next.t("floorplan_layers")}>
                    {LAYERS.map(([key, , swatch]) => (
                        <label key={key} className="chip">
                            <input type="checkbox" checked={!!layers[key]} onChange={() => toggle(key)}/>
                            <span className="swatch" style={{background: swatch}}/>
                            {i18next.t(`floorplan_layer_${key}`)}
                        </label>
                    ))}
                </div>
                <div className="bar">
                    <span className="spacer"/>
                    {building && <>
                        <button onClick={() => zoomBy(1 / 1.25)} title={i18next.t("floorplan_zoom_out")}
                                aria-label={i18next.t("floorplan_zoom_out")}>−</button>
                        <button onClick={() => { setZoom(fit()); setPan({x: 0, y: 0}); }}>{i18next.t("floorplan_zoom_fit")}</button>
                        <button onClick={() => zoomBy(1.25)} title={i18next.t("floorplan_zoom_in")}
                                aria-label={i18next.t("floorplan_zoom_in")}>+</button>
                    </>}
                </div>
                <div className="floorplan-map">
                {building && (
                    <div className="floors" role="group" aria-label={i18next.t("floorplan_floor_list")}>
                        {[...building.floors].sort((a, b) => b.level - a.level).map((f) => (
                            <button key={f.level} className={f.level === level ? "active" : ""}
                                    aria-pressed={f.level === level}
                                    title={f.role ? `${i18next.t("floorplan_role")}: ${f.role}` : ""}
                                    onClick={() => setLevel(f.level)}>{floorName(f.level)}</button>
                        ))}
                    </div>
                )}
                <div className="floorplan-viewport" ref={viewport}
                     onPointerDown={dragStart} onPointerMove={dragMove} onPointerUp={dragEnd}
                     onPointerCancel={dragEnd}
                     onWheel={(e) => {
                         if (!e.ctrlKey) return;
                         zoomBy(e.deltaY < 0 ? 1.15 : 1 / 1.15);
                     }}>
                    {!building && <div className="floorplan-placeholder">{placeholder}</div>}
                    {building && zoom !== null && floor && (
                        <div className="floorplan-stage"
                             style={{
                                 transform: `translate(calc(-50% + ${pan.x}px), calc(-50% + ${pan.y}px))`,
                                 width: (building.width + 2 * padding) * zoom,
                                 height: (building.height + 2 * padding) * zoom,
                             }}>
                            {layers.image && files.image_url && <img src={files.image_url} alt=""/>}
                            <FloorOverlay building={building} floor={floor} padding={padding} zoom={zoom}
                                          layers={layers} gridStep={GRID_STEP}
                                          onRoomHover={(e, room) => setTip({
                                              info: roomInfo(room, floor), x: e.clientX, y: e.clientY,
                                          })}
                                          onRoomLeave={() => setTip(null)}/>
                        </div>
                    )}
                </div>
                </div>
                <Tip tip={tip}/>
                {building && (
                    <div className="bar downloads">
                        <span className="caption">
                            {optionLabel(building.params.building_type)} · {building.width}×{building.height}{" "}
                            ({building.width * .5}×{building.height * .5} m) · {i18next.t("floorplan_seed")} {building.seed}
                        </span>
                        <span className="spacer"/>
                        <span className="group-label">{i18next.t("floorplan_download")}</span>
                        <a className="fp-button" href={files.image_url} download={`${stem}_${tag}.webp`}>WebP</a>
                        {files.dd2vtt_url &&
                            <a className="fp-button" href={files.dd2vtt_url} download={`${stem}_${tag}.dd2vtt`}
                               title={i18next.t("floorplan_dd2vtt_hint")}>dd2vtt</a>}
                        <a className="fp-button" href={floorplan.building_url} download={`${stem}.json`}>JSON</a>
                        {actions}
                    </div>
                )}
            </main>
        </div>
    );
}
