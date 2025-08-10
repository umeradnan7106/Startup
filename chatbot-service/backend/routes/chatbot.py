# 📂 File: backend/routes/chatbot.py

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()

class Message(BaseModel):
    message: str

@router.post("/chatbot")
async def chatbot_endpoint(payload: Message):
    user_message = payload.message
    print("User message:", user_message)

    # Dummy bot response
    bot_response = f"You said: {user_message}"

    return JSONResponse(content={"response": bot_response})
