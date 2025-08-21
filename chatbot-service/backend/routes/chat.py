# backend/routes/chat.py
from flask import Blueprint, request, jsonify
from backend.models import Chatbot, Message, UsageLog
from backend.extensions import db
from backend.utils.gemini import get_gemini_response

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_message = (data.get("message") or "").strip()
    bot_id = (data.get("bot_id") or "").strip()

    if not user_message:
        return jsonify({"response": "⚠️ Message cannot be empty"}), 400
    if not bot_id:
        return jsonify({"response": "⚠️ bot_id is required"}), 400

    bot = Chatbot.query.get(bot_id)
    if not bot:
        return jsonify({"response": "⚠️ Invalid bot_id"}), 404

    reply = get_gemini_response(user_message)

    db.session.add(Message(bot_id=bot.id, role="user", content=user_message))
    db.session.add(Message(bot_id=bot.id, role="bot", content=reply))
    db.session.add(UsageLog(bot_id=bot.id, prompt_tokens=len(user_message)//4, completion_tokens=len(reply)//4, total_tokens=(len(user_message)+len(reply))//4))
    db.session.commit()

    return jsonify({"response": reply})
