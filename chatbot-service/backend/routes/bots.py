import uuid
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models import Chatbot

bots_bp = Blueprint("bots", __name__, url_prefix="/bots")

@bots_bp.get("/")
@jwt_required()
def list_bots():
    uid = get_jwt_identity()
    bots = Chatbot.query.filter_by(user_id=uid).all()
    return jsonify([{
        "id": b.id, "name": b.name, "welcome_message": b.welcome_message, "model": b.model
    } for b in bots])

@bots_bp.post("/")
@jwt_required()
def create_bot():
    uid = get_jwt_identity()
    data = request.get_json() or {}
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
