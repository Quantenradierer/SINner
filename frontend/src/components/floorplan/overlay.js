import React from "react";
import i18next from "../../i18n";
import {matrixSpec, objectName, pretty, roomName, term} from "./names";

// Port of the overlay layers of the Floorplaner page (roomplanner/ui/index.html).
// Coordinates are cells; the SVG's viewBox maps them onto the themed image.

export const M2_PER_CELL = 0.25;
const ROOM_LABEL_PX = 12;

export const LAYERS = [
    ["image", true, "#888"],
    ["labels", true, "#ffffff"],
    ["objects", false, "#9be37a"],
    ["matrix", false, "#3dd6ff"],
    ["grid", false, "#7a8190"],
];

export {pretty};

const DEVICE_CONTROLS = {camera: ["camera", "audio"], motion_sensor: ["motion"], alarm_panel: ["alarm"]};

/** The Matrix nodes of a floor: hackable objects, security devices, lights and every door. */
function matrixNodes(floor) {
    const nodes = [];
    const add = (x, y, w, h, name, controls, round) => nodes.push({x, y, w, h, name, controls, round});
    for (const obj of floor.objects) {
        const spec = matrixSpec(obj.kind);
        if (spec) add(obj.x, obj.y, obj.w, obj.h, spec.as ? term("word", spec.as) : objectName(obj.kind), spec.controls, false);
    }
    for (const d of floor.devices) {
        if (DEVICE_CONTROLS[d.kind]) add(d.x, d.y, 1, 1, pretty(d.kind), DEVICE_CONTROLS[d.kind], true);
    }
    for (const light of floor.lights) {
        add(light.x - .5, light.y - .5, 1, 1, `${pretty(light.kind)} ${i18next.t("floorplan_light_word")}`, ["power"], true);
    }
    for (const o of floor.openings) {
        if (o.kind !== "door") continue;  // every door has a controller, visible or not
        const [x0, y0, x1, y1] = runCoords(o.edges);
        const lock = o.lock ? ` (${pretty(o.lock)}${o.rating ? " " + o.rating : ""})` : "";
        add((x0 + x1) / 2 - .5, (y0 + y1) / 2 - .5, 1, 1, `${term("word", "door")}${lock}`, ["lock"], true);
    }
    return nodes;
}

const cellsPath = (cells) => cells.map(([x, y]) => `M${x} ${y}h1v1h-1z`).join("");

const edgeCoords = ([x, y, axis]) => (axis === "h" ? [x, y, x + 1, y] : [x, y, x, y + 1]);

const edgesPath = (edges) => edges.map((e) => {
    const [a, b, c, d] = edgeCoords(e);
    return `M${a} ${b}L${c} ${d}`;
}).join("");

function runCoords(edges) {
    const first = edgeCoords(edges[0]), last = edgeCoords(edges[edges.length - 1]);
    return [first[0], first[1], last[2], last[3]];
}

function centre(cells) {
    const cx = cells.reduce((s, c) => s + c[0], 0) / cells.length;
    const cy = cells.reduce((s, c) => s + c[1], 0) / cells.length;
    let best = cells[0], dist = Infinity;
    for (const c of cells) {
        const d = (c[0] + .5 - cx) ** 2 + (c[1] + .5 - cy) ** 2;
        if (d < dist) {
            dist = d;
            best = c;
        }
    }
    return [best[0] + .5, best[1] + .5];
}

export function bounds(cells) {
    const xs = cells.map((c) => c[0]), ys = cells.map((c) => c[1]);
    return [Math.min(...xs), Math.min(...ys), Math.max(...xs) + 1, Math.max(...ys) + 1];
}

const CHAR_PX = ROOM_LABEL_PX * 0.55;  // average glyph width on screen

/**
 * The label lines that fit into the room at this zoom: the name if it fits at all, the id
 * and area if there is height for a second line, the unit for a third. Null: no label.
 */
function labelLines(room, zoom) {
    const [x0, y0, x1, y1] = bounds(room.cells);
    const width = (x1 - x0) * zoom, height = (y1 - y0) * zoom;
    const name = roomName(room.type);
    if (width < name.length * CHAR_PX || height < ROOM_LABEL_PX * 1.6) return null;
    const lines = [[name, 1, "600"]];
    const detail = `${room.id} · ${room.cells.length * M2_PER_CELL} m²`;
    if (height >= ROOM_LABEL_PX * 3 && width >= detail.length * CHAR_PX * .8) lines.push([detail, .8]);
    if (room.unit && height >= ROOM_LABEL_PX * 4.2) lines.push([`${i18next.t("floorplan_unit")} ${room.unit}`, .8]);
    return lines;
}

// Text with a dark outline, lines = [[content, scale, weight], ...].
function Label({x, y, lines, size, colour = "#fff"}) {
    return (
        <text x={x} y={y} fontSize={size} textAnchor="middle" fill={colour}
              stroke="rgba(0,0,0,.75)" strokeWidth={size * .18} paintOrder="stroke">
            {lines.map(([content, scale, weight], i) => (
                <tspan key={i} x={x} dy={i === 0 ? `${-(lines.length - 1) * .55}em` : "1.1em"}
                       fontSize={size * scale} fontWeight={weight || "normal"}>{content}</tspan>
            ))}
        </text>
    );
}

/** What the tooltip shows for a room: area, box size, furniture and security devices. */
export function roomInfo(room, floor) {
    const counts = {};
    for (const obj of floor.objects) {
        if (obj.room === room.id) counts[obj.kind] = (counts[obj.kind] || 0) + 1;
    }
    const devices = floor.devices.filter((d) => d.room === room.id).map((d) => d.kind);
    const [x0, y0, x1, y1] = bounds(room.cells);
    return {
        type: roomName(room.type),
        id: room.id,
        summary: `${room.cells.length} ${i18next.t("floorplan_cells")} · ${room.cells.length * M2_PER_CELL} m² · ` +
            `${(x1 - x0) * .5}×${(y1 - y0) * .5} m`,
        unit: room.unit,
        furniture: Object.entries(counts).map(([k, n]) => (n > 1 ? `${n}× ` : "") + objectName(k)),
        devices: devices.map(pretty),
    };
}

/**
 * The SVG drawn over the floor image. `building` gives the size, `floor` the content;
 * `layers` is {key: bool}; `onRoomHover(event, room)` / `onRoomLeave()` drive the tooltip.
 */
export default function FloorOverlay({building, floor, padding, zoom, layers: L, gridStep, onRoomHover, onRoomLeave}) {
    const cols = building.width + 2 * padding, rows = building.height + 2 * padding;
    const size = ROOM_LABEL_PX / zoom;  // the same on screen for every room and zoom

    return (
        <svg xmlns="http://www.w3.org/2000/svg" viewBox={`${-padding} ${-padding} ${cols} ${rows}`}
             style={{position: "absolute", inset: 0, width: "100%", height: "100%"}}>
            {!L.image && <rect x={-padding} y={-padding} width={cols} height={rows} fill="#101217"/>}

            {L.grid && <path fill="none" stroke="rgba(200,210,230,.35)" strokeWidth={.05} d={gridPath(building, gridStep)}/>}

            {L.lights && <g>
                {floor.lights.map((light, i) => {
                    const id = `fp-light-${floor.level}-${i}`;
                    const alpha = light.state === "off" ? 0 : .45 * light.intensity;
                    return (
                        <React.Fragment key={id}>
                            <radialGradient id={id}>
                                <stop offset={0} stopColor={light.colour} stopOpacity={alpha}/>
                                <stop offset={1} stopColor={light.colour} stopOpacity={0}/>
                            </radialGradient>
                            <circle cx={light.x} cy={light.y} r={light.radius} fill={`url(#${id})`}/>
                            <circle cx={light.x} cy={light.y} r={.25} fill={light.colour}
                                    stroke={light.state === "on" ? "#000" : "#f00"} strokeWidth={.08}
                                    strokeDasharray={light.state === "flicker" ? ".1 .1" : "none"}>
                                <title>{i18next.t("floorplan_light_title", {kind: light.kind, state: light.state, radius: light.radius})}</title>
                            </circle>
                        </React.Fragment>
                    );
                })}
            </g>}

            {L.objects && <g>
                {floor.objects.map((obj, i) => {
                    const [fx, fy] = {
                        N: [obj.x + obj.w / 2, obj.y], S: [obj.x + obj.w / 2, obj.y + obj.h],
                        E: [obj.x + obj.w, obj.y + obj.h / 2], W: [obj.x, obj.y + obj.h / 2],
                    }[obj.facing];
                    const labelSize = Math.min(.55, (obj.w * 1.6) / Math.max(4, obj.kind.length));
                    return (
                        <React.Fragment key={i}>
                            <rect x={obj.x + .05} y={obj.y + .05} width={obj.w - .1} height={obj.h - .1}
                                  fill={obj.blocking === false ? "rgba(155,227,122,.08)" : "rgba(155,227,122,.22)"}
                                  stroke="#9be37a" strokeWidth={.06} rx={.1}>
                                <title>{`${objectName(obj.kind)} (${obj.w}×${obj.h}, ${i18next.t("floorplan_faces")} ${obj.facing})`}</title>
                            </rect>
                            {/* Front marker: a dot on the side the object faces. */}
                            <circle cx={fx} cy={fy} r={.12} fill="#9be37a"/>
                            {labelSize >= .22 && <Label x={obj.x + obj.w / 2} y={obj.y + obj.h / 2 + labelSize * .35}
                                                        lines={[[objectName(obj.kind), 1]]} size={labelSize}
                                                        colour="#d8f7c6"/>}
                        </React.Fragment>
                    );
                })}
            </g>}

            {L.locks && <g>
                {floor.openings.filter((o) => o.kind === "door" && (o.lock || o.entrance)).map((o, i) => {
                    const [x0, y0, x1, y1] = runCoords(o.edges);
                    const mx = (x0 + x1) / 2, my = (y0 + y1) / 2;
                    const text = [o.entrance ? o.entrance.toUpperCase() : null,
                        o.lock ? `${o.lock}${o.rating ? " " + o.rating : ""}` : null].filter(Boolean).join(" · ");
                    return (
                        <React.Fragment key={i}>
                            <circle cx={mx} cy={my} r={.2} fill={o.lock ? "#ff6b6b" : "#f5c35b"}/>
                            <Label x={mx} y={my - .45} lines={[[text, 1, "bold"]]} size={.5}
                                   colour={o.entrance ? "#ffe08a" : "#ffb0b0"}/>
                        </React.Fragment>
                    );
                })}
            </g>}

            {L.matrix && <g>
                {matrixNodes(floor).map((n, i) => {
                    const cx = n.x + n.w / 2, cy = n.y + n.h / 2;
                    const attrs = {fill: "rgba(61,214,255,.22)", stroke: "#3dd6ff", strokeWidth: .08};
                    return (
                        <React.Fragment key={i}>
                            {n.round
                                ? <circle cx={cx} cy={cy} r={.4} {...attrs}/>
                                : <rect x={n.x + .05} y={n.y + .05} width={n.w - .1} height={n.h - .1} rx={.1} {...attrs}/>}
                            <Label x={cx} y={cy + .15} lines={[["◈", 1, "bold"]]} size={.6} colour="#a8f0ff"/>
                            <title>{`${n.name}: ${n.controls.map((c) => term("control", c)).join(", ")}`}</title>
                        </React.Fragment>
                    );
                })}
            </g>}

            {L.labels && <g>
                {floor.rooms.map((room) => {
                    const lines = labelLines(room, zoom);
                    if (!lines) return null;
                    const [cx, cy] = centre(room.cells);
                    return <Label key={room.id} x={cx} y={cy} lines={lines} size={size}/>;
                })}
            </g>}

            {/* Hover targets for the room tooltip, on top of everything. */}
            <g>
                {floor.rooms.map((room) => (
                    <path key={room.id} d={cellsPath(room.cells)} className="floorplan-room-hit"
                          onMouseMove={(e) => onRoomHover(e, room)} onMouseLeave={onRoomLeave}/>
                ))}
            </g>
        </svg>
    );
}

function gridPath(building, step) {
    const s = Math.max(1, step || 1);
    let d = "";
    for (let x = 0; x <= building.width; x += s) d += `M${x} 0V${building.height}`;
    for (let y = 0; y <= building.height; y += s) d += `M0 ${y}H${building.width}`;
    return d;
}
