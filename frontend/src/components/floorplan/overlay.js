import React from "react";

// Port of the overlay layers of the Floorplaner page (roomplanner/ui/index.html).
// Coordinates are cells; the SVG's viewBox maps them onto the themed image.

export const M2_PER_CELL = 0.25;
const ROOM_LABEL_PX = 12;

export const LAYERS = [
    ["image", true, "#888"],
    ["rooms", false, "#6aa9ff"],
    ["walls", false, "#e8e8e8"],
    ["labels", true, "#ffffff"],
    ["units", false, "#c792ea"],
    ["openings", false, "#f5c35b"],
    ["locks", false, "#ff6b6b"],
    ["objects", false, "#9be37a"],
    ["devices", false, "#ff8a3d"],
    ["lights", false, "#fff3a0"],
    ["grid", false, "#7a8190"],
];

const FACING = {N: [0, -1], S: [0, 1], E: [1, 0], W: [-1, 0]};

export const pretty = (text) => String(text).replace(/_/g, " ");

function hue(text) {
    let h = 0;
    for (const ch of text) h = (h * 31 + ch.charCodeAt(0)) % 360;
    return h;
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

function describeOpening(o) {
    const parts = [`${o.kind} (${o.edges.length} cells)`];
    if (o.state) parts.push(o.state);
    if (o.material) parts.push(o.material);
    if (o.lock) parts.push(`lock: ${o.lock}${o.rating ? " " + o.rating : ""}`);
    if (o.entrance) parts.push(`${o.entrance} entrance`);
    return parts.join(" · ");
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
        type: pretty(room.type),
        id: room.id,
        summary: `${room.cells.length} cells · ${room.cells.length * M2_PER_CELL} m² · ` +
            `${(x1 - x0) * .5}×${(y1 - y0) * .5} m`,
        unit: room.unit,
        furniture: Object.entries(counts).map(([k, n]) => (n > 1 ? `${n}× ` : "") + pretty(k)),
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

            {L.rooms && <g fillOpacity={L.image ? .35 : .55}>
                {floor.rooms.map((room) => (
                    <path key={room.id} d={cellsPath(room.cells)} fill={`hsl(${hue(room.type)} 55% 50%)`}/>
                ))}
            </g>}

            {L.units && <g>
                {floor.rooms.filter((room) => room.unit).map((room) => (
                    <path key={room.id} d={cellsPath(room.cells)} fill={`hsl(${hue(room.unit)} 70% 60%)`}
                          fillOpacity={.3}/>
                ))}
            </g>}

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
                                <title>{`${light.kind} light · ${light.state} · r ${light.radius}`}</title>
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
                                <title>{`${obj.kind} (${obj.w}×${obj.h}, faces ${obj.facing})`}</title>
                            </rect>
                            {/* Front marker: a dot on the side the object faces. */}
                            <circle cx={fx} cy={fy} r={.12} fill="#9be37a"/>
                            {labelSize >= .22 && <Label x={obj.x + obj.w / 2} y={obj.y + obj.h / 2 + labelSize * .35}
                                                        lines={[[pretty(obj.kind), 1]]} size={labelSize}
                                                        colour="#d8f7c6"/>}
                        </React.Fragment>
                    );
                })}
            </g>}

            {L.walls && <path d={edgesPath(floor.walls)} stroke="#e8e8e8" strokeWidth={.18}
                              strokeLinecap="square" fill="none"/>}

            {L.openings && <g fill="none" strokeLinecap="butt">
                {floor.openings.map((o, i) => {
                    const colour = {door: "#f5c35b", window: "#5ec8ff", breach: "#c08a5b"}[o.kind];
                    const [x0, y0, x1, y1] = runCoords(o.edges);
                    return (
                        <React.Fragment key={i}>
                            <path d={edgesPath(o.edges)} stroke={colour} strokeWidth={.32}
                                  strokeDasharray={o.kind === "breach" || o.state === "missing" ? ".2 .15" : "none"}
                                  opacity={o.state === "blocked" ? .5 : 1}>
                                <title>{describeOpening(o)}</title>
                            </path>
                            {o.kind === "door" && o.state === "blocked" &&
                                <path d={`M${x0} ${y0}L${x1} ${y1}`} stroke="#ff3b3b" strokeWidth={.1}/>}
                        </React.Fragment>
                    );
                })}
            </g>}

            {L.devices && <g>
                {floor.devices.map((d, i) => {
                    const cx = d.x + .5, cy = d.y + .5;
                    const [dx, dy] = FACING[d.facing];
                    return (
                        <React.Fragment key={i}>
                            <path d={`M${cx} ${cy}L${cx + dx * .7} ${cy + dy * .7}`} stroke="#ff8a3d" strokeWidth={.1}/>
                            <circle cx={cx} cy={cy} r={.38} fill="#2a1508" stroke="#ff8a3d" strokeWidth={.08}>
                                <title>{`${pretty(d.kind)} · rating ${d.rating} · faces ${d.facing}`}</title>
                            </circle>
                            <Label x={cx} y={cy + .16} lines={[[d.kind[0].toUpperCase(), 1, "bold"]]} size={.45}
                                   colour="#ffb27a"/>
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

            {L.labels && <g>
                {floor.rooms.map((room) => {
                    const [cx, cy] = centre(room.cells);
                    const lines = [[pretty(room.type), 1, "600"],
                        [`${room.id} · ${room.cells.length * M2_PER_CELL} m²`, .8]];
                    if (room.unit) lines.push([`unit ${room.unit}`, .8]);
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
