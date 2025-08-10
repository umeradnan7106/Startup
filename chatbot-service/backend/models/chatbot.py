# backend/models/chatbot.py
from pydantic import BaseModel
import uuid

class ChatbotBase(BaseModel):
    name: str
    welcome_message: str

class Chatbot(ChatbotBase):
    id: str

    @classmethod
    def create(cls, data: ChatbotBase):
        return cls(id=str(uuid.uuid4()), **data.dict())
