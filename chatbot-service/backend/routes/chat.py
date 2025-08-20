# backend/routes/chat.py
import os
import google.generativeai as genai
from flask import Blueprint, request, jsonify, render_template
from ..models import Chatbot, Message, UsageLog
from ..extensions import db
from ..config import Config

chat_bp = Blueprint("chat", __name__)

# configure Gemini once
genai.configure(api_key=Config.GEMINI_API_KEY)

def estimate_tokens(text: str) -> int:
    # very rough estimate ~4 chars per token
    return max(1, int(len(text) / 4))

@chat_bp.get("/")
def health():
    return "OK", 200

@chat_bp.get("/widget")
def widget():
    # support ?bot_id=... so each site can load specific bot
    # If missing, widget will still render but chat POST will fail
    return render_template("widget.html")

@chat_bp.post("/chatbot")
def chatbot():
    data = request.get_json() or {}
    user_message = (data.get("message") or "").strip()
    bot_id = (data.get("bot_id") or "").strip()  # required for multi-tenant

    if not user_message:
        return jsonify({"response": "⚠️ Message cannot be empty"}), 400
    if not bot_id:
        return jsonify({"response": "⚠️ bot_id is required"}), 400

    bot = Chatbot.query.get(bot_id)
    if not bot:
        return jsonify({"response": "⚠️ Invalid bot_id"}), 404

    model_name = bot.model or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    model = genai.GenerativeModel(model_name)

    try:
        # store user message
        db.session.add(Message(bot_id=bot.id, role="user", content=user_message))
        db.session.commit()

        resp = model.generate_content(user_message)
        text = getattr(resp, "text", None) or (getattr(resp, "parts", [None])[0].text if getattr(resp, "parts", None) else "")
        text = (text or "Sorry, I didn't get that.").strip()

        # store bot message
        db.session.add(Message(bot_id=bot.id, role="bot", content=text))

        # naive token accounting
        p = estimate_tokens(user_message)
        c = estimate_tokens(text)
        u = UsageLog(bot_id=bot.id, prompt_tokens=p, completion_tokens=c, total_tokens=p+c)
        db.session.add(u)
        db.session.commit()

        return jsonify({"response": text})
    except Exception as e:
        db.session.rollback()
        return jsonify({"response": f"❌ Error: {str(e)}"}), 500
