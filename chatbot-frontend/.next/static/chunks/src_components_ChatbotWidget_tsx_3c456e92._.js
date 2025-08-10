(globalThis.TURBOPACK = globalThis.TURBOPACK || []).push([typeof document === "object" ? document.currentScript : undefined, {

"[project]/src/components/ChatbotWidget.tsx [app-client] (ecmascript)": ((__turbopack_context__) => {
"use strict";

var { k: __turbopack_refresh__, m: module } = __turbopack_context__;
{
__turbopack_context__.s({
    "default": ()=>__TURBOPACK__default__export__
});
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/compiled/react/index.js [app-client] (ecmascript)");
var _s = __turbopack_context__.k.signature();
"use client";
;
const ChatbotWidget = ()=>{
    _s();
    (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$compiled$2f$react$2f$index$2e$js__$5b$app$2d$client$5d$__$28$ecmascript$29$__["useEffect"])({
        "ChatbotWidget.useEffect": ()=>{
            const script = document.createElement("script");
            script.src = "http://localhost:8000/static/widget.js"; // 👈 API service ka URL
            script.async = true;
            script.setAttribute("data-bot-id", "ec97e16b-1826-41a3-b242-675913dbc5e0");
            document.body.appendChild(script);
            return ({
                "ChatbotWidget.useEffect": ()=>{
                    document.body.removeChild(script);
                }
            })["ChatbotWidget.useEffect"];
        }
    }["ChatbotWidget.useEffect"], []);
    return null; // Widget khud hi DOM me inject hoga
};
_s(ChatbotWidget, "OD7bBpZva5O2jO+Puf00hKivP7c=");
_c = ChatbotWidget;
const __TURBOPACK__default__export__ = ChatbotWidget;
var _c;
__turbopack_context__.k.register(_c, "ChatbotWidget");
if (typeof globalThis.$RefreshHelpers$ === 'object' && globalThis.$RefreshHelpers !== null) {
    __turbopack_context__.k.registerExports(module, globalThis.$RefreshHelpers$);
}
}}),
}]);

//# sourceMappingURL=src_components_ChatbotWidget_tsx_3c456e92._.js.map