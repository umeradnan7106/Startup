# backend/auth.py

from flask import Blueprint, request, jsonify
from backend.extensions import db
from backend.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
from backend.config import Config

auth_bp = Blueprint("auth", __name__)

# ----------------------
# Signup Route
# ----------------------
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    # Check if user exists
    existing_user = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()

    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    # Hash password
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # JWT token generate
    token = jwt.encode(
        {
            "user_id": new_user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        },
        Config.JWT_SECRET_KEY,
        algorithm="HS256",
    )

    return jsonify({
        "message": "User created successfully",
        "token": token,
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
        },
    }), 201


# ----------------------
# Login Route
# ----------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # JWT token generate
    token = jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        },
        Config.JWT_SECRET_KEY,
        algorithm="HS256",
    )

    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        },
    }), 200
