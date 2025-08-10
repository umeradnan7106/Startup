"use client";
import { useEffect } from "react";

const ChatbotWidget = () => {
  useEffect(() => {
    const script = document.createElement("script");
    script.src = "http://localhost:8000/static/widget.js"; // 👈 API service ka URL
    script.async = true;
    script.setAttribute("data-bot-id", "ec97e16b-1826-41a3-b242-675913dbc5e0");
    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    };
  }, []);

  return null; // Widget khud hi DOM me inject hoga
};

export default ChatbotWidget;
