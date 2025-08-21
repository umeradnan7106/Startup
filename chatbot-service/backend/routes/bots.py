# backend/routes/bots.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models import Chatbot
from backend.extensions import db
import uuid

bots_bp = Blueprint("bots", __name__)

@bots_bp.route("/bots", methods=["POST"])
@jwt_required()
def create_bot():
    uid = get_jwt_identity()
    data = request.get_json()
    bot = Chatbot(
        id=str(uuid.uuid4()),
        user_id=uid,
        name=data.get("name") or "New Bot",
        welcome_message=data.get("welcome_message") or "Hello!",
        model=data.get("model") or "gemini-2.5-flash",
    )
    db.session.add(bot)
    db.session.commit()
    return jsonify({"id": bot.id}), 201
