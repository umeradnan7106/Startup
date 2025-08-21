# backend/main.py
from flask import Flask, render_template, request
from backend.models import db
from backend.auth import auth_bp
from backend.routes.chat import chat_bp
from backend.routes.bots import bots_bp
from backend.routes.chatbot import chatbot_bp
from backend.config import Config
from backend.extensions import jwt


app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(Config)
# Initialize database
db.init_app(app)
jwt.init_app(app)
# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(chat_bp)
app.register_blueprint(bots_bp)
app.register_blueprint(chatbot_bp)


@app.route("/")
def home():
    return {"message": "Chatbot backend is running 🚀"}


@app.route("/widget")
def widget():
    bot_id = request.args.get("bot_id")
    if not bot_id:
        return "⚠️ bot_id is required", 400
    return render_template("widget.html", bot_id=bot_id)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Tables create ho jayein
    app.run(debug=True)

