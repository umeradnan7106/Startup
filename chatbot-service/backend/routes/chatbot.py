# 📂 File: backend/routes/chatbot.py


from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models import Chatbot

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/my-bots", methods=["GET"])
@jwt_required()
def get_user_bots():
    uid = get_jwt_identity()
    bots = Chatbot.query.filter_by(user_id=uid).all()
    return jsonify([{
        "id": b.id,
        "name": b.name,
        "model": b.model,
        "welcome_message": b.welcome_message
    } for b in bots])
