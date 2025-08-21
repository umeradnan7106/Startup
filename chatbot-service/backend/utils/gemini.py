import google.generativeai as genai
from backend.config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

def get_gemini_response(message: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(message)
    return getattr(response, "text", "").strip() or "⚠️ No response."
