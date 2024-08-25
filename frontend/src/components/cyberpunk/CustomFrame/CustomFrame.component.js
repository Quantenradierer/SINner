"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
var __spreadArrays = (this && this.__spreadArrays) || function () {
    for (var s = 0, i = 0, il = arguments.length; i < il; i++) s += arguments[i].length;
    for (var r = Array(s), k = 0, i = 0; i < il; i++)
        for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++)
            r[k] = a[j];
    return r;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.CustomFrame = void 0;
var css_1 = require("@emotion/css");
var react_1 = require("@emotion/react");
var useBleepsOnAnimator_1 = require("@arwes/core/lib/utils/useBleepsOnAnimator");
var Frame_1 = require("@arwes/core/lib/utils/Frame");
function CustomFrame(props) {
    var animator = props.animator, className = props.className, lineWidth = props.lineWidth, squareSize = props.squareSize, otherProps = __rest(props, ["animator", "className", "lineWidth", "squareSize"]);
    useBleepsOnAnimator_1.useBleepsOnAnimator({
        entering: 'assemble',
        exiting: 'assemble'
    });
    var _a = react_1.useTheme(), space = _a.space, outline = _a.outline;
    var ss = squareSize;
    var polyline1 = [];
    var polyline2 = [];

    polyline1 = [
        ['100%', '100%'],
        ['100%', '0'],

        ['100% - ' + ss, 0],
        [ss, 0],
        [0, ss],
        [0, '100%'],
    ];

    return (react_1.jsx(Frame_1.Frame, __assign({}, otherProps, { className: css_1.cx('arwes-frame-pentagon', className), css: {
            padding: space(2) + "px " + space(4) + "px"
        }, shapes: [
            polyline1.concat(polyline2)
        ], polylines: [
            polyline1,
            __spreadArrays([
                polyline1[polyline1.length - 1]
            ])
        ], lineWidth: outline(lineWidth) })));
}
exports.CustomFrame = CustomFrame;
CustomFrame.defaultProps = {
    lineWidth: 1,
    squareSize: 15
};
