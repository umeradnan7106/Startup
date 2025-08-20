# # backend/main.py

# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from config import Config
# from flask_cors import CORS
# from auth import auth_bp

# # Flask App Setup
# app = Flask(__name__)
# CORS(app) 
# app.config.from_object(Config)
# app.register_blueprint(auth_bp, url_prefix="/auth")


# # Database Setup
# db = SQLAlchemy(app)

# # User Model
# class User(db.Model):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = generate_password_hash(password)  # password hash

# # Signup Route
# @app.route("/signup", methods=["POST"])
# def signup():
#     data = request.json
#     username = data.get("username")
#     email = data.get("email")
#     password = data.get("password")

#     if not username or not email or not password:
#         return jsonify({"error": "All fields are required"}), 400

#     # Check existing user
#     existing_user = User.query.filter(
#         (User.username == username) | (User.email == email)
#     ).first()

#     if existing_user:
#         return jsonify({"error": "User already exists"}), 400

#     new_user = User(username=username, email=email, password=password)
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({"message": "User created successfully"}), 201

# # Login Route
# @app.route("/login", methods=["POST"])
# def login():
#     data = request.json
#     email = data.get("email")
#     password = data.get("password")

#     if not email or not password:
#         return jsonify({"error": "Email and password required"}), 400

#     user = User.query.filter_by(email=email).first()

#     if not user or not check_password_hash(user.password, password):
#         return jsonify({"error": "Invalid credentials"}), 401

#     return jsonify({
#         "message": "Login successful",
#         "user": {
#             "id": user.id,
#             "username": user.username,
#             "email": user.email
#         }
#     }), 200

# # Run Flask App
# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()  # users table ban jayegi agar na ho
#     app.run(debug=True)


# backend/main.py
from flask import Flask
from backend.models import db
from backend.auth import auth_bp
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)
# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")

@app.route("/")
def home():
    return {"message": "Chatbot backend is running 🚀"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Tables create ho jayein
    app.run(debug=True)





# acha mujhe aik cheez or kerni hai ye login kerne per access_token deraha hai lekin mai chah raha hoon aik access_token ka button ho jo login ya signup ke baad dashboard mai aye phir usko dabayen to woh access_token de or woh supabase mai jis id mai access_token generate hua hai usme ajaye 
