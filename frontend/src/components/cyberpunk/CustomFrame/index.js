"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CustomFrame = void 0;
var animation_1 = require("@arwes/animation");
var CustomFrame_component_1 = require("./CustomFrame.component");
// TODO: withAnimator does not support a functional React component declared
// in "function Component () {}" notation with "defaultProps".
var CustomFrame = animation_1.withAnimator()(CustomFrame_component_1.CustomFrame);
exports.CustomFrame = CustomFrame;
