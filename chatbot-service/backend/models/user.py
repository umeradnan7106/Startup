# backend/models/user.py

from datetime import datetime
import uuid
from ..extensions import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # ✅ updated field name
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # ✅ added for Supabase sync

    def __repr__(self):
        return f"<User {self.username}>"

    # Relationship: One user can have many chatbots
    chatbots = db.relationship("Chatbot", backref="owner", lazy=True)


class Chatbot(db.Model):
    __tablename__ = "chatbots"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  # ✅ UUID
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    welcome_message = db.Column(db.String(500), default="Hi! How can I help?")
    model = db.Column(db.String(120), default="gemini-2.5-flash")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    messages = db.relationship("Message", backref="bot", lazy=True)
    usages = db.relationship("UsageLog", backref="bot", lazy=True)


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bot_id = db.Column(db.String(36), db.ForeignKey("chatbots.id"), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'user' or 'bot'
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class UsageLog(db.Model):
    __tablename__ = "usage_logs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bot_id = db.Column(db.String(36), db.ForeignKey("chatbots.id"), nullable=False)
    prompt_tokens = db.Column(db.Integer, default=0)
    completion_tokens = db.Column(db.Integer, default=0)
    total_tokens = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
