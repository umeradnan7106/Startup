// // src/components/ChatbotWidget.tsx
// "use client";
// import { useEffect } from "react";

// const ChatbotWidget = () => {
//   useEffect(() => {
//     const script = document.createElement("script");
//     script.src = "https://chatbot-backend-production-f970.up.railway.app/static/widget.js"; // 👈 API service ka URL
//     script.async = true;
//     script.setAttribute("data-bot-id", "ec97e16b-1826-41a3-b242-675913dbc5e0");
//     document.body.appendChild(script);

//     return () => {
//       document.body.removeChild(script);
//     };
//   }, []);

//   return null; // Widget khud hi DOM me inject hoga
// };

// export default ChatbotWidget;




// src/components/ChatbotWidget.tsx
"use client";
import { useEffect } from "react";

export default function ChatbotWidget() {
  useEffect(() => {
    const script = document.createElement("script");
    script.src = "https://chatbot-backend-production-f970.up.railway.app/static/widget.js";
    script.async = true;
    script.setAttribute("data-widget", "https://chatbot-backend-production-f970.up.railway.app/widget");
    script.setAttribute("data-bot-id", "<BOT_ID_FROM_DB>");
    document.body.appendChild(script);
    return () => { document.body.removeChild(script); };
  }, []);
  return null;
}
