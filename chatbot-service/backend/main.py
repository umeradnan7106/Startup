# chatbot-service/backend/main.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Flask app config
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is missing in your .env file")

genai.configure(api_key=GEMINI_API_KEY)

# Choose model (2.0-pro is stable, 2.5-pro is in preview)
try:
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    raise RuntimeError(f"❌ Error initializing Gemini model: {e}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/widget")
def widget():
    return render_template("widget.html")


@app.route("/chatbot", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"response": "⚠️ Message is required"}), 400

        user_message = data["message"].strip()
        if not user_message:
            return jsonify({"response": "⚠️ Message cannot be empty"}), 400

        # Generate response from Gemini
        response = model.generate_content(user_message)

        text_response = ""
        if hasattr(response, "text") and response.text:
            text_response = response.text.strip()
        elif hasattr(response, "parts") and response.parts:
            text_response = response.parts[0].text.strip()
        else:
            text_response = "⚠️ Sorry, I didn't get that."

        return jsonify({"response": text_response})

    except Exception as e:
        return jsonify({"response": f"❌ Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
