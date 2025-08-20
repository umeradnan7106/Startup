import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    # Security keys
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_DIRECT_URI = os.getenv("DIRECT_URL", SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # Gemini AI config
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL")

    # Debug mode
    DEBUG = os.getenv("FLASK_DEBUG", "False").lower() in ["true", "1", "yes"]
